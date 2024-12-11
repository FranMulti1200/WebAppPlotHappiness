import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def sold(self):
        stock = int(df.loc[df["id"] == self.article_id, "in stock"].squeeze())
        currentStock = stock - 1
        df.loc[df["id"] == self.article_id, "in stock"] = currentStock
        df.to_csv("articles.csv", index=False)


    def inStock(self):
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        return in_stock
        """
        if int(available) > 0:
            return True
        else:
            return False"""

class Receipt:
    def __init__(self, id, name, price ):
        self.id = id
        self.name = name
        self.price = price

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
article_id = input("Choose an article to buy: ")
article = Article(article_id=article_id)

if article.inStock():
    article.sold()
    receipt = Receipt(id=article.article_id, name=article.name, price=article.price)
    receipt.generate()
else:
    print("No such article in stock")