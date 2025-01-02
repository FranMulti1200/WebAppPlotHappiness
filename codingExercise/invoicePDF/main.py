from fpdf import FPDF
import pandas as pd

factura = {
    "description":"",
    "quantity":"",
    "unit Price":"",
}

list_desciption = []
list_quantity = []
list_unitPrice = []

user_name = input("Introduzca su nombre: ")
user_address = input("Introduzca su dirección: ")
while True:
    print("Introduzca los datos para la factura")
    description = input("Descripción: ")
    list_desciption.append(description)
    factura["description"] = list_desciption
    quantity = int(input("Cantidad: "))
    list_quantity.append(quantity)
    factura["quantity"] = list_quantity
    unitPrice = float(input("Precio Unitario "))
    list_unitPrice.append(unitPrice)
    factura["unit Price"] = list_unitPrice
    #linea = (description, quantity, unitPrice)
    #factura_linea.append(linea)

    nuevaLinea = input("Añadir nueva linea? (S/N)")
    if nuevaLinea == "N":
        break

df = pd.DataFrame(factura)
#print(df)
df.to_csv("factura.csv", index=False)

#df = pd.read_csv("factura.csv")

print(df)

for item in df:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    title = "Invoice"
    company = "Tech Solutions Inc."
    address = "123 Innovation Drive, Tech City, TX 75001"

    pdf.set_font(family="Arial", size=21, style="B")
    pdf.cell(w=210, h=8, txt=title, align="C", ln=1)

    # Company data
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=210, h=8, txt=company, ln=1)
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)
    pdf.set_font(family="Arial", size=14)
    pdf.cell(w=50, h=8, txt=address, ln=1)
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)

    # Client data
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=210, h=8, txt=f"Bill to: {user_name}", ln=1)
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)
    pdf.set_font(family="Arial", size=14)
    pdf.cell(w=210, h=8, txt=user_address, ln=1)

    # Add a header
    header = list(df.columns)
    header = [item.title() for item in header]
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)
    #pdf.set_text_color(80, 80, 80)
    pdf.cell(w=75, h=8, txt=header[0], border=1)
    pdf.cell(w=40, h=8, txt=header[1], align="C", border=1)
    pdf.cell(w=40, h=8, txt=header[2], align="C", border=1)
    pdf.cell(w=40, h=8, txt="Total", align="C", border=1, ln=1)

    # Add rows to the table
    subtotal = 0
    for index, row in df.iterrows():
        total = row["quantity"] * row["unit Price"]
        total = round(total, 2)
        pdf.set_font(family="Arial", size=10)
        #pdf.set_text_color(80, 80, 80)
        pdf.cell(w=75, h=8, txt=str(row["description"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["quantity"]), align="C", border=1)
        pdf.cell(w=40, h=8, txt=str(f"${row["unit Price"]}"), align="C", border=1)
        pdf.cell(w=40, h=8, txt=str(f"${total}"), align="C", border=1, ln=1)
        subtotal = subtotal + total
        subtotal = round(subtotal, 2)

    # Subtotal line
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.cell(w=210, h=8, txt="", align="C", ln=1)
    pdf.cell(w=155, h=8, txt="Subtotal", align="R", border=1)
    pdf.cell(w=40, h=8, txt=str(f"${subtotal}"), align="C", border=1, ln=1)

    tax = round(subtotal*0.07, 2)
    pdf.cell(w=155, h=8, txt="Tax", align="R", border=1)
    pdf.cell(w=40, h=8, txt=str(f"${tax}"), align="C", border=1, ln=1)

    # Add total plus tax
    total_tax = round(subtotal+tax, 2)
    pdf.cell(w=155, h=8, txt="Total", align="R", border=1)
    pdf.cell(w=40, h=8, txt=str(f"${total_tax}"), align="C", border=1, ln=1)

    pdf.output("invoice_pdf/invoice.pdf")





