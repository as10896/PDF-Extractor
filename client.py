import requests

def pdf_extract(filename):
    url ='http://127.0.0.1:9998/pdf'
    files = {'file': open(filename, "rb")}
    r = requests.post(url, files=files)
    return r.text

if __name__ == "__main__":
    print(pdf_extract("國立清華大學106學年度行事曆.pdf"))
