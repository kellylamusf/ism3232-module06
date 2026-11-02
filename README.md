# ISM3232 Lab 10

- **Name:** Kelly Lam
- **Date:** 11/1/2026

## What This Program Does
- Chuoi is a mock support assistant for the Green and Bean Cafe that tells the customer the order status by looking up the number in the CafeOrders tool. It replies comes from simple keyword rules and not from AI or a real ordering system. Any requests to change, cancel, swap, or modifying the order will go straight to a barista. If Chuoi cannot find the order number it will ask the customer to check their reciept again instead of guessing. 
## Business Rules
- The assistant checks each message against. If the message contains change, cnacel, swap, or modify, Chuoi will automatically pass the customer to a barista.
- If the message contains order or status, Chuoi will look for an order number. 
- If the message contains hello, Chuoi will greet the customer and state that it can check an order status for them
- If it goes outside of any of those boundaries, Chuoi will reply with not being able to help and only being able to check an order status. 
## How to Run 
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- python3 my_main.py
- If you want to stop the chat with the bot, type quit to stop. 
## How to Test
- ruff format . && ruff check . && pytest -v
## Files in this Repository
- my_assistant.py
- my main.py
- tests/test_my_assistant.py
- my_tool.py
## AI Use Statement 
- I used Claude to help me plan and identify my coding errors. 
