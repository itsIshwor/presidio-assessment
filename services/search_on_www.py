from bs4 import BeautifulSoup
import requests
from googlesearch import search
from flask import jsonify
import unicodedata


def search_on_web(query_param: str):
    links = [each_link for each_link in search(
        query_param, stop=10, verify_ssl=False)]
    return jsonify({"top links": (links), "most popular answer": f'{fetch_answer_from_links(links)}'})


def fetch_answer_from_links(links: list):
    for link in links:
        response = requests.get(link)
        html_content = response.text
        soup = (BeautifulSoup(html_content, 'html.parser'))
        try:
            paragraphs = soup.find_all('p')
        except IndexError as err:
            print(err)
            continue
    paragraph = paragraphs[0]
    clean_text = unicodedata.normalize("NFKD", paragraph.get_text())
    clean_text = clean_text if clean_text.count(
        " ") > 5 else "There is no appropraite anser found found please follow top links"
    return clean_text
