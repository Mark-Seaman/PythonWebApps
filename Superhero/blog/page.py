from requests import get


def get_web_page(url):
    response = get(url)
    p = f"URL: {url},"
    s = f"Status Code: {response.status_code},"
    t = response.text
    c = f"Text: {len(t)} characters"
    # print(p, s, c)
    return t
