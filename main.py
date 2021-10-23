class Bill:
    """
    Object that contains data about the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate by name with how much days they stay in the flat
    and how much of the bill they pay.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass

class PdfReport:
    """Pdf report generator given the filename and the flatmates"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatemate1, flatemate2, bill):
        pass