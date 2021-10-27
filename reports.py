import os
import webbrowser
from fpdf import FPDF


class PdfReport:
    """Pdf report generator given the filename and the flatmates"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # create pdf and page
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add image to the pdf
        pdf.image("house.png", w=30, h=30)

        # add title with appropriate font
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # change font for text body
        pdf.set_font(family="Times", size=12)

        # add body text
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt=str("{:.2f}".format(flatmate1.pays(bill, flatmate2))), border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=100, h=40, txt=str("{:.2f}".format(flatmate2.pays(bill, flatmate1))), border=1, ln=1)

        # output file
        pdf.output(self.filename)

        # open pdf
        webbrowser.open("file://" + os.path.realpath(self.filename))
