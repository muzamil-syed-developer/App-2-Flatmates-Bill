from fpdf import FPDF

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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight

        return to_pay

class PdfReport:
    """Pdf report generator given the filename and the flatmates"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount = 120, period = "April 2021")
john = Flatmate(name = "John", days_in_house = 20)
marry = Flatmate(name = "Marry", days_in_house = 25)

print("John pays: ", john.pays(the_bill,flatmate2=marry))
print("Marry pays: ", marry.pays(the_bill,flatmate2=marry))