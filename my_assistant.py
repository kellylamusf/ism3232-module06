# my_assitant.py
# Author: Kelly Lam

HANDOFF_WORDS = ["change", "cancel", "swap", "modify"]


class CafeAssistant:
    """A mock cafe assistant. Its replies comes from simple rules, not from AI."""

    def __init__(self, name, instructions, order_tool):
        """Set up on assitant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.history = []

    def respond(self, user_message):
        """ "Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """ "Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't change an order. I'm passing you to a barista."
        if "order" in text or "status" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check your order status."
        return "I'm not sure how to respond to that. I can check your order status."

    def needs_human(self, text):
        """Return True if the message asks to change an order."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer a question about the order."""
        order_number = self.order_tool.find_order_id(user_message)
        if order_number is None:
            return "I don't see an order number in your message. Please send your order number, like 2."
        status = self.order_tool.find_status(order_number)
        if status is None:
            return f"I don't know about order {order_number}. Please check your receipt number."
        return f"Order {order_number} is {status}."
