# how to read document:

# - First read the first page of document and note those points which we are not able to understand completely in first time. then research on those points and understand it.

# - Follow same steps for other pages and note the points and concepts . then learn these

# - Must implement it in a practicle way 

# long term and short term memory present in context

# GENERIC CLASS = context: RunContextWrapper[UserContext]

# default tool_choice = ("auto") to llm  but in agent passed None in default

# parallel_tool_calls=False --> due to this tools will not run parallely but still run individually one by one 

# 1 turn is equal to llm call like if we have 2 tools and question is related to both of them so 2 turns used because both tools run parallely and llm call only 2 times but if we false parallel tool call it will run separately and turns will be 3

# instructions = MaybeAwaitable

# In dynamic instructions:  def get_sys_prompt(context: RunContextWrapper ,agent: Agent) ----> must first argument is context otherwise if we will give other value like agent so still context information will give to the agent by default because it is on first number . if we try to print context like (context.context) so it will return an error

# in dynamic instruction both agent and context are important 

# context will not given to llm but it will be passed to all the properties of agent like tools etc

# if we will transfer the agent of (refund_agent) so its function call become transfer_to_refund_agent but if we will override this name (tool_name_override="refund order") so the name remains the same , no transfer add. tool override name only change in tracing not in the terminal.

#   input_filter=handoff_filters.remove_all_tools --> this will remove all the tools and also all the function call from the tracing
  

# AgentBase defines the structure.
# Agent defines the specific behavior

# Agent[TContext] give structured output and also take input as well






## IMPORTING

# from agents.exceptions import InputGuardrailTripwireTriggered
