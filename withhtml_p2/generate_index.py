from withhtml_p2.random_promises import gen_prophecies
from datetime import datetime as dt


def generate_body(header, paragraphs):
    """генерирует код body"""
    body = '<h1>' + header + '</h1>'
    for p in paragraphs:
        body += '<p>' + p + '</p>'
    return '<body>' + body + '</body>'


def generate_page(head, body):
    """оборачивает переданные аргументы в тег"""
    page = "<html>" + head + body + '</html>'
    return page


def generate_head(title):
    head = "<meta charset='UTF-8'>" + "<title>" + title + "</title>"
    return "<head>" + head + "</head>"


def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
save_page(
    title='гороскоп на сегодня',
    header='что день ' + str(today) + ' нам готовит',
    paragraphs=gen_prophecies()
)