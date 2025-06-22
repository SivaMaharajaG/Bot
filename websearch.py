# websearch.py

import requests
from bs4 import BeautifulSoup

def search_web(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}+site:.in"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = []
        for div in soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
            text = div.get_text()
            if len(text.strip()) > 50:
                results.append(text.strip())
        return results[:3]  # Return top 3 snippets
    except Exception as e:
        return [f"Error fetching web results: {e}"]
