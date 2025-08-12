from fpdf import FPDF

userName = input("Name: ")

pdf = FPDF()
pdf.add_page()

pdf.set_font('helvetica',"B", size=45)
pdf.cell(0,60,"CS50 Shirtificate",align="C")
pdf.image("shirtificate.png", x=0, y=80)

pdf.set_font_size(25)
pdf.set_text_color(255,255,255)


pdf.text(x=60, y=170, text=f"{userName} took CS50")
pdf.output("shirtificate.pdf")






