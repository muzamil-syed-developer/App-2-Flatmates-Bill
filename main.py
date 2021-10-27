from flat import Bill, Flatmate
from reports import PdfReport

#test code
the_bill = Bill(amount = 120, period ="April 2021")
john = Flatmate(name ="John", days_in_house = 20)
marry = Flatmate(name ="Marry", days_in_house = 25)

print("John pays: ", john.pays(the_bill,flatmate2=marry))
print("Marry pays: ", marry.pays(the_bill,flatmate2=marry))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john,flatmate2=marry, bill=the_bill)