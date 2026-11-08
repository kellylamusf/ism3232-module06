from my_assistant import CafeAssistant
from my_tool import CafeOrders


def make_assistant():
    """Build a CafeAssistant with its own tools for each tests."""
    orders = {
        "1": "received",
        "2": "being made",
        "3": "ready for pickup",
        "4": "picked up",
    }
    return CafeAssistant(
        "Chuoi",
        "Be friendly and helpful. You can check the status for the Green and Bean Cafe.",
        CafeOrders(orders),
    )


def test_order_tools():
    assistant = make_assistant()
    assert assistant.respond("Where is my order 2?") == "Order 2 is being made."


def find_order_number(self, message):
    for word in message.split():
        cleaned = word.strip("?.,!#")
        if cleaned.isdigit():
            return int(cleaned)
    return None


def test_changing_an_order_goes_to_a_barista():
    assistant = make_assistant()
    assert "barista" in assistant.respond("Please change my order to a latte.")


def test_unknown_request_gets_a_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("Do you have almond milk?")
