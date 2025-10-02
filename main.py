from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from agents import Agent, Runner,Session, function_tool, ModelSettings
from agents.run import RunConfig
from configure.config import gemini_model

app = FastAPI()

# CORS: allow Next.js dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bashars-portfolio.vercel.app"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@function_tool
def bashar_info():

  return {
      "about": "I am a dedicated creative professional specializing in front-end web development and UI/UX design, with expertise in HTML, CSS, JavaScript, TypeScript, Next.js, Tailwind CSS, ShadCN UI, and Radix UI. I also have strong skills in Figma and video editing.",

        "services": {
            "frontend": "Responsive front-end development using Next.js, React, Tailwind, ShadCN UI, and Radix UI.",
            "uiux": "User-centered UI/UX design using Figma, focusing on intuitive and aesthetic interfaces.",
            "video_editing": "High-quality video editing to deliver engaging visual content."
        },

        "skills": [
            "HTML", "CSS", "JavaScript", "TypeScript",
            "Next.js", "Tailwind CSS", "ShadCN UI",
            "Radix UI", "Figma", "Video Editing"
        ],

        "projects": [
            {
                "title": "E-Commerce Website",
                "description": "A full stack e-commerce site built with Next.js, Sanity, Tailwind CSS.",
               # "link": "https://marketplace-by-bashar.vercel.app/"
            },
            {
                "title": "Blogs Website",
                "description": "A blog platform with interactive commenting features.",
               # "link": "https://bashar-blogs.vercel.app/"
            },
            {
                "title": "Bashar Motors",
                "description": "Car purchase website built with Next.js, React, CSS, and TypeScript.",
               # "link": "https://bashar-motors.vercel.app/"
            },
            {
                "title": "Hangman Game",
                "description": "Interactive Hangman game built with JavaScript.",
                #"link": "https://e-commerce-website-amber-eight.vercel.app/"
            },
            {
                "title": "AI Image Generator",
                "description": "AI-powered image generation app built with JavaScript.",
               # "link": "https://ai-image-developer-by-bashar.netlify.app/"
            }
        ]
    }

agent = Agent(
    name="Assistant",
    instructions="""

    You are an expert assistant that provides information about M. Bashar Sheikh.
    
    Rules:
    - Always call the 'bashar_info' tool.
    - If the user asks generally about "projects", return a short summary list 
      (just project names with one-line descriptions).
    - If the user asks about a specific project (like 'Bashar Motors' or 'E-Commerce Website'),
      show ONLY that projects details and link.
    - Do not list every project unless explicitly asked ("show all projects").
    - Keep responses concise, professional, and easy to read.
    - Extract and present only the relevant information (about, services, skills) depending on the users query.
    - Do not dump all information at once.
    - Use a clean, professional, and conversational tone.
    - If user asks about projects, include project links.
    - If user asks about services or skills, list them in bullet points.

    
    """,
    model=gemini_model,
    tools=[bashar_info],
    model_settings= ModelSettings(tool_choice="required")
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

# FastAPI will take whatever the function returns and validate/convert it into a ChatResponse object through response_model = ChatResponse
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message is required.")

    if not os.getenv("GEMINI_API_KEY"):
        raise HTTPException(status_code=500, detail="Missing GEMINI_API_KEY.")

    try:
        result = await Runner.run(
            agent,
            req.message.strip(),
            run_config=RunConfig(model=gemini_model),
        )
        reply = (result.final_output or "").strip()
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

