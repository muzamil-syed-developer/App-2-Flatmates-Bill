from flat import Bill, Flatmate
from reports import PdfReport

period = input("Enter the period for the bill: e.g January 2021 ")
amount = float(input("Enter the bill amount: "))

f1 = input("Enter the name of the first flatmate: ")
d1 = int(input(f"Enter the amount of days {f1} stayed in the house: "))

f2 = input("Enter the name of the second flatmate: ")
d2 = int(input(f"Enter the amount of days {f2} stayed in the house: "))

the_bill = Bill(amount=amount, period=period)
mate1 = Flatmate(name=f1, days_in_house=d1)
mate2 = Flatmate(name=f2, days_in_house=d2)

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=mate1, flatmate2=mate2, bill=the_bill)