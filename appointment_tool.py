# appointment_tool.py
# Author: Kelly Lam


class AppointmentBook:
    """A tool that shows open appointment times and answers questions about them."""

    def __init__(self, open_times):
        """Store the open times this tool can look up."""
        self.open_times = open_times

    def find_day(self, text):
        """Return the first known day mentioned in text, or None."""
        for day in self.open_times:
            if day in text.lower():
                return day
        return None

    def times_for(self, day):
        """Return the open times for one day, or None if there is no such day."""
        if day in self.open_times:
            return self.open_times[day]
        return None
