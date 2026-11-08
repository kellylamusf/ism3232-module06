# echo_model.py
# Author: Kelly Lam


class EchoModel:
    """A model that just repeats what the user said. It stands in for a real AI model."""

    def reply(self, instructions, history):
        """Return the last message in the history."""
        last_message = history[-1]["content"]
        return f"You said: {last_message}"
