from docx2python import docx2python


biblio = {}


class book:
    def __init__(self, title: str, edition: str, year):
        self.title = title
        self.edition = edition
        self.year = year


with docx2python("salvatore di fazio.docx") as docx_content:
    print(docx_content.footnotes_runs)
