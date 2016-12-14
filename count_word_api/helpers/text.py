from bs4 import BeautifulSoup


def html_to_text(html_text):
    """Receive pure html and convert to text without tags"""
    soup = BeautifulSoup(html_text, "html.parser")
    clean_html = ' '.join(soup.find_all(text=True))
    return clean_html
