import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

load_dotenv()
model_name = os.getenv("MODEL", "gpt-3.5-turbo")
llm = init_chat_model(model_name, temperature=0)

# Placeholder scheduling tool
def schedule_appointment(request: str) -> str:
    return f"Scheduling placeholder: would try to schedule {request} and return available slots (mock)"

tools = [
    {"name": "Scheduler", "func": schedule_appointment, "description": "Schedule appointments and return available slots"}
]

agent = create_agent(llm, tools=tools, name="AgenticAppointments")

if __name__ == '__main__':
    while True:
        q = input('You: ')
        if q.lower() in ['exit','quit']:
            break
        print('Bot:', agent.run(q))
