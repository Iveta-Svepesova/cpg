import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Chyba: server vratil kod {response.status_code}")
        return hrefs

    html = response.text

    # vyhledá všechny href odkazy
    matches = re.findall(r'<a\s+href=["\'](.*?)["\']', html)

    # přidá jen absolutní odkazy
    for m in matches:
        if m.startswith("http"):
            hrefs.append(m)

    return hrefs


if __name__ == "__main__":
    try:
        # URL ze zadání
        url = "https://www.jcu.cz"
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)  # vypíše seznam odkazů, např.:
        # ["https://www.jcu.cz/cz/prijimaci-zkousky/studijni-programy",
        #  "https://www.jcu.cz/cz/prijimaci-zkousky/prijimaci-rizeni", ...]
    except Exception as e:
        print(f"Program skoncil chybou: {e}")