from my_assistant import CafeAssistant
from my_tool import CafeOrders, Toolbox
from fake_model import FakeModel

def make_assistant(model):
    """Build a CafeAssistant with its own tools for each tests."""
    orders = {
        "1": "received",
        "2": "being made",
        "3": "ready for pickup",
        "4": "picked up",
    }
    toolbox = Toolbox(CafeOrders(orders))
    return CafeAssistant(
        "Chuoi",
        "Be friendly and helpful. You can check the status for the Green and Bean Cafe.",
        toolbox,
        model,
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

def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}

def test_unknown_request_gets_a_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("Do you have almond milk?")

def test_model_can_look_up_an_order():
    model = FakeModel(
        [
            ask_for_tool("look_up_order", {"order_id": "2"}),
            {"text": "Order 2 is being made."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Where is my order 2?")
    assert assistant.history[1]["content"] == "Order 2 is being made."


def test_made_up_detail_is_refused():
    model = FakeModel(
        [
            ask_for_tool("place_order", {"item": "latte", "customer": "Dana"}),
            {"text": "What is your name?"},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Can I get a latte?")
    assert "Refused" in assistant.history[1]["content"]
    assert assistant.toolbox.queue == []


def test_unknown_tool_is_refused():
    model = FakeModel(
        [ask_for_tool("delete_order", {"order_id": "2"}), {"text": "Sorry."}]
    )
    assistant = make_assistant(model)
    assistant.respond("Delete order 2")
    assert "Refused" in assistant.history[1]["content"]


def test_request_waits_and_changes_nothing():
    model = FakeModel(
        [
            ask_for_tool("place_order", {"item": "latte", "customer": "Dana"}),
            {"text": "Sent to the front desk."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Please order a latte, my name is Dana")
    assert len(assistant.toolbox.queue) == 1
    assert assistant.toolbox.queue[0]["state"] == "waiting"
    assert len(assistant.toolbox.order_tool.orders) == 4


def test_approve_makes_the_order_once():
    model = FakeModel(
        [
            ask_for_tool("place_order", {"item": "latte", "customer": "Dana"}),
            {"text": "Sent to the front desk."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Please order a latte, my name is Dana")
    assert assistant.toolbox.approve(1) is True
    assert assistant.toolbox.approve(1) is False
    assert len(assistant.toolbox.order_tool.orders) == 5


def test_changing_an_order_goes_to_a_barista():
    model = FakeModel([])
    assistant = make_assistant(model)
    reply = assistant.respond("Please cancel my order")
    assert "barista" in reply
    assert model.calls == 0


def test_loop_stops_after_three_tool_rounds():
    request = ask_for_tool("look_up_order", {"order_id": "2"})
    model = FakeModel([request, request, request, {"text": "never reached"}])
    assistant = make_assistant(model)
    reply = assistant.respond("Where is my order 2?")
    assert "couldn't finish" in reply
    assert model.calls == 3