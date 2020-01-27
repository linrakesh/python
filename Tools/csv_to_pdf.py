#   program to convert CSV file into PDF file
from fpdf import FPDF
import csv

with open("e:/python/tools/SampleData.csv", "r") as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        print(row)


pdf = FPDF(orientation='P', unit='mm', format='A4')  # P -potrait  L-Landscape
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=str(d), ln=1, align="C")
pdf.output("simple_demo.pdf")
