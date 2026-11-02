# stock_tool.py
# Author: Kelly Lam


class StockLookup:
    """A tool that shows the amount of stock we have for each product."""

    def __init__(self, stock):
        """Store the stock counts this tool can look up."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product mentioned in text, or None."""
        for product in self.stock:
            if product in text.lower():
                return product
            return None

    def count_for(self, product):
        """Return the stock count for a product, or None if unknown."""
        if product in self.stock:
            return self.stock[product]
        return None
