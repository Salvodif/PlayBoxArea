from docx2python import docx2python


biblio = {}


class book:
    def __init__(self, title: str, edition: str, year):
        self.title = title
        self.edition = edition
        self.year = year


# biblio.setdefault("J.K. Rowling", []).append(book("Harry Potter", 1, 1997))
# biblio.setdefault("J.K. Rowling", []).append(book("Animali fantastici", 1, 2001))

i = 0

with docx2python("salvatore di fazio.docx") as docx_content:
    for footnote in docx_content.footnotes_runs:
        i += 1
        print(i)
