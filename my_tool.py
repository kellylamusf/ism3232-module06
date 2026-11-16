# my_tool.py
# Author: Kelly Lam

TOOLS = {
    "look_up_order": ["order_id"],
    "add_order": ["item", "customer"],
}


class Toolbox:
    """The one door every model request passes through."""

    def __init__(self, order_tool):
        self.order_tool = order_tool
        self.queue = []

    def tools(self):
        """The tool methods the model may ask for."""
        return [self.order_tool.look_up_order, self.place_order]

    def place_order(self, item: str, customer: str):
        """Ask the front desk to make a new order. Staff must approve it first.

        Args:
            item: What the customer wants, like latte.
            customer: The customer's name, like Dana.
        """
        request = {
            "id": len(self.queue) + 1,
            "item": item,
            "customer": customer,
            "state": "waiting",
        }
        self.queue.append(request)
        return "Your order has been sent to the front desk for approval."

    def run(self, name, arguments, said):
        """Check a tool request, then run it or queue it."""
        if name not in TOOLS:
            return f"Refused: there is no tool called {name}."
        if set(arguments) != set(TOOLS[name]):
            return "Refused: that request had the wrong details."
        for key, value in arguments.items():
            if not str(value).strip():
                return f"Refused: {key} was empty."
            if str(value).lower() not in said.lower():
                return f"Refused: the customer never typed {key}."
        if name == "look_up_order":
            return self.order_tool.look_up_order(**arguments)
        return self.place_order(**arguments)

    def approve(self, request_id):
        """The only code that makes the order. A second approval does nothing."""
        for request in self.queue:
            if request["id"] == request_id and request["state"] == "waiting":
                request["state"] = "approved"
                self.order_tool.add_order(request["item"], request["customer"])
                return True
        return False

    def reject(self, request_id):
        """Reject a waiting request. Nothing is made."""
        for request in self.queue:
            if request["id"] == request_id and request["state"] == "waiting":
                request["state"] = "rejected"
                return True
        return False


class CafeOrders:
    """A tool that knows about the status of your cafe orders. It knows nothing about chatting."""

    def __init__(self, orders):
        """Store the orders this tool can look up."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order mentioned in text, or None."""
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None

    def find_status(self, order_id):
        """Return the status of one order, or None if there is no such order."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None

    def look_up_order(self, order_id):
        """Look up the status of one cafe order.

        Args:
            order_id: The order number the customer typed, like 2.
        """
        status = self.find_status(str(order_id))
        if status is None:
            return f"I don't know about order {order_id}. Please check your receipt number."
        return f"Order {order_id} is {status}."

    def add_order(self, item, customer):
        """Create a new order. Only the toolbox's approve may call this."""
        order_id = str(len(self.orders) + 1)
        self.orders[order_id] = "received"
        return order_id
