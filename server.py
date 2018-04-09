from flask import Flask, request
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

app = Flask(__name__)

def convert(binary, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(binary, pagenums):
        interpreter.process_page(page)
    converter.close()
    text = output.getvalue()
    output.close
    return text

@app.route("/pdf", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            return convert(file)
        else:
            return "Please add something to your request body."
    else:
        return "Please use POST."

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()