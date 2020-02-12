from withhtml_p2.random_promises import gen_prophecies
from datetime import datetime as dt


def generate_body(header, paragraphs):
    """генерирует код body"""
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"\n<p>{p}</p>"
    return f"<body>{body}\n</body>"


def generate_page(head, body):
    """оборачивает переданные аргументы в тег"""
    page = f"<html>{head}{body}</html>"
    return page


def generate_head(title):
    head = f"""<head>
        <meta charset='UTF-8'>"
        <title>{title}</title>
        </head>
        """
    return head


def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w")
    # today = dt.now().date()
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()


#####################

today = dt.now().date()
save_page(
    title='Гороскоп на сегодня',
    header=f"Что день {str(today)} нам готовит",
    paragraphs=gen_prophecies()
)
