import os
import webbrowser

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

        #create pdf and page
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add image to the pdf
        pdf.image("house.png", w=30, h=30)

        #add title with appropriate font
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #change font for text body
        pdf.set_font(family="Times", size=12)

        #add body text
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt=str("{:.2f}".format(flatmate1.pays(the_bill,flatmate2))), border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=100, h=40, txt=str("{:.2f}".format(flatmate2.pays(the_bill, flatmate1))), border=1, ln=1)

        #output file
        pdf.output(self.filename)

        #open pdf
        webbrowser.open("file://"+os.path.realpath(self.filename))


#test code
the_bill = Bill(amount = 120, period = "April 2021")
john = Flatmate(name = "John", days_in_house = 20)
marry = Flatmate(name = "Marry", days_in_house = 25)

print("John pays: ", john.pays(the_bill,flatmate2=marry))
print("Marry pays: ", marry.pays(the_bill,flatmate2=marry))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john,flatmate2=marry, bill=the_bill)