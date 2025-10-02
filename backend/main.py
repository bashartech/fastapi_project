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
#     return """

# ## Give Information, Services, Portfolio, Skills, Projects About M.Bashar Sheikh

# ### ABOUT :

# - I am a dedicated creative professional specializing in front end web development and UI/UX design, with expertise in HTML, CSS, JavaScript, TypeScript, Next.js, Tailwind CSS, ShadCN UI, and Radix UI. I focus on creating visually appealing, user friendly websites that seamlessly blend aesthetics with functionality. Additionally, I possess skills in Figma for UI design and video editing, allowing me to craft engaging visual narratives. My unique blend of technical and creative abilities enables me to deliver innovative digital solutions that captivate and inspire.

# ### SERVICES :

# - Introduction:
# As a committed imaginative expert spend significant time in front end web advancement and UI/UX plan, I influence a different range of abilities that incorporates HTML, CSS, JavaScript, TypeScript, Next.js, Tailwind CSS, ShadCN UI, and Radix UI. My attention is on making outwardly engaging and easy to understand sites that consistently incorporate style with usefulness. Moreover, I use Figma for natural UI plan and have skill in video altering to make connecting with visual stories. This special blend of specialized and inventive capacities empowers me to convey creative computerized arrangements that enrapture crowds and hoist brand encounters.

# - Front-end Web Development:

# We specialize in front-end improvement, conveying client driven sites that upgrade your internet based presence and surpass assumptions. Our obligation to client fulfillment drives us to use the most recent advances, including HTML, CSS, JavaScript, and TypeScript, guaranteeing powerful and responsive plans custom fitted to your requirements. By utilizing systems like Next.js and libraries, for example, Respond, we make dynamic web applications that give an outstanding client experience. Our mastery in Tailwind CSS, ShadCN UI, and Radix UI empowers us to create outwardly staggering and natural connection points. With an emphasis on responsiveness and authority, we guarantee that each task meets as well as surpasses industry principles, making drawing in computerized arrangements that reverberate with your crowd and raise your image. Join forces with us to change your vision into the real world and make enduring progress in the computerized scene.

# - UI/UX Design:

# Our UI/UX configuration administrations are devoted to making instinctive and connecting with client encounters that enthrall and hold your crowd. We utilize a client focused plan approach, using instruments like Figma to foster outwardly engaging and utilitarian points of interaction that line up with your image character. By joining stylish plan with consistent ease of use, we guarantee that each cooperation feels normal and fulfilling for clients. Our obligation to responsiveness ensures that plans perform faultlessly across all gadgets, upgrading client commitment and fulfillment. With an emphasis on exploration and approval, we focus on grasping your crowds requirements, empowering us to convey custom-made arrangements that meet as well as surpass assumptions. Trust us to raise your computerized presence through imaginative UI/UX plan that resounds with clients and encourages faithfulness, making your image hang out in a serious scene.

# - Video Editing:

# Our video altering administrations are intended to change your crude film into dazzling visual stories that draw in and resound with your crowd. Using industry driving programming, we carefully make top notch recordings that mirror your extraordinary vision and brand personality. From special clasps to artistic stories, our altering cycle underlines clearness, cognizance, and inventiveness, guaranteeing that each undertaking really conveys your message. We focus on tender loving care, utilizing strategies, for example, variety evaluating, sound plan, and consistent advances to improve the general creation quality. Focused on responsiveness and client fulfillment, we team up intimately with you all through the altering venture, making changes in view of your criticism to surpass assumptions. Whether you really want content for online entertainment, advertising efforts, or exceptional occasions, our video altering administrations are custom-made to raise your narrating and charm your crowd, at last driving commitment and brand steadfastness.

# ### PROJECTS :

# 1. E-Commerce Website

# - A Full Stack E-Commerce Website built with Next.js, React, Sanity and Tailwind CSS. This website allows customers to purchase products based on their needs..

# - Link = [E-Commerce Website](https://marketplace-by-bashar.vercel.app/)

# 2. Blogs Website

# - The blog website allows users to easily browse and read various blog posts. Additionally, it provides an interactive commenting feature.

# - Link = [Blogs Website](https://bashar-blogs.vercel.app/)

# 3. Bashar Motors

# - A professional car purchase website featuring top-tier vehicles, expertly crafted using Next.js, React, CSS, and TypeScript for a seamless browsing and buying experience

# - Link = [Bashar Motors](https://bashar-motors.vercel.app/)

# 4. Hangman Game

# - An interactive Hangman Game built with JavaScript, offering an engaging word-guessing experience through intuitive gameplay and dynamic features.

# - Link = [Hangman Game](https://e-commerce-website-amber-eight.vercel.app/)

# 5. Ai Image Generator

# - An advanced AI image generator website, meticulously crafted with JavaScript, delivering high-quality, dynamic visuals through seamless and intuitive user interactions.

# - Link = [Ai Image Generator](https://ai-image-developer-by-bashar.netlify.app/)


# """

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
