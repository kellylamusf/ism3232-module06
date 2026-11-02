# my_main.py
#Author: Kelly Lam

from my_assistant import CafeAssistant
from my_tool import CafeOrders

ORDERS = {
    "1": "received",
    "2": "being made",
    "3": "ready for pickup",
    "4": "picked up",
}

order_tool = CafeOrders(ORDERS)
assistant = CafeAssistant(
    "Chuoi",
    "You are a friendly order-status assistant. You can check the status for the Green and Bean Cafe.",
    order_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message.lower() != "quit":
    reply = assistant.respond(user_message)
    print(f"{assistant.name}: {reply}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")