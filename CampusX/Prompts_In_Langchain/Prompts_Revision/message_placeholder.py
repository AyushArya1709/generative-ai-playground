from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# ============================================================
# 1. CREATE CHAT PROMPT TEMPLATE
# ============================================================

chat_template = ChatPromptTemplate([
    
    # System instruction
    ("system", "You are a helpful customer support agent."),

    # Previous conversation will be inserted here
    MessagesPlaceholder(variable_name="chat_history"),

    # Current user message
    ("human", "{query}")
])


# ============================================================
# 2. CREATE EMPTY CHAT HISTORY
# ============================================================

chat_history = []


# ============================================================
# 3. LOCATE CHAT HISTORY FILE
# ============================================================

file_path = Path(__file__).parent / "chat_history.txt"


# ============================================================
# 4. LOAD PREVIOUS CHAT HISTORY
# ============================================================

with open(file_path) as file:
    chat_history.extend(file.readlines())


# ============================================================
# 5. CHECK LOADED CHAT HISTORY
# ============================================================

print("Chat History:")
print(chat_history)


# ============================================================
# 6. CREATE FINAL PROMPT
# ============================================================

prompt = chat_template.invoke({
    
    # Insert previous conversation
    "chat_history": chat_history,

    # Insert current user message
    "query": HumanMessage(
        content="I want to return my product."
    )
})


# ============================================================
# 7. CHECK FINAL PROMPT
# ============================================================

print("\nFinal Prompt:")
print(prompt)