# my_main.py
# Author: Kelly Lam

from my_assistant import CafeAssistant
from my_tool import CafeOrders, Toolbox
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

ORDERS = {
    "1": "received",
    "2": "being made",
    "3": "ready for pickup",
    "4": "picked up",
}

INSTRUCTIONS = (
    "You are Chuoi, a friendly order-status assistant for the Green and Bean Cafe. "
    "Answer in one short sentence"
    "If the customers says hello, reply: Hello! How can I help you today?"
    "Use look_up_order to check the status of an order. "
    "Use place_order only when the customer has given an item and their name. "
    "If you don't have their name, ask for it."
)

toolbox = Toolbox(CafeOrders(ORDERS))
assistant = CafeAssistant("Chuoi", INSTRUCTIONS, toolbox, OllamaModel(MODEL_NAME))


print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message.lower() != "quit":
    reply = assistant.respond(user_message)
    print(f"{assistant.name}: {reply}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
print("Front desk review")
for request in toolbox.queue:
    print(f"Request {request['id']}: {request['customer']}, {request['item']}")
    if input("Approve? yes or no: ").lower() == "yes":
        toolbox.approve(request["id"])
        print(f"Request {request['id']} approved.")
    else:
        toolbox.reject(request["id"])
        print(f"Request {request['id']} rejected.")
print(f"Orders: {len(toolbox.order_tool.orders)}")
