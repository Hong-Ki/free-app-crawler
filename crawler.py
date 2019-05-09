import requests
from bs4 import BeautifulSoup


def getPlatforms():
    req = requests.get(
        'http://bbs.ruliweb.com/market/board/1020/list?search_type=member_srl&search_key=5046042')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(
        'tr.table_body:not(.notice)'
    )[:2]
    results = []
    for element in elements:
        platform = {
            'title': element.select('.subject a ')[0].text,
            'link': element.select('.subject a ')[0].get('href'),
            'time': element.select('.time')[0].text.strip(),
        }
        results.append(platform)

    return results


def getAppInfo(link):
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    links = list(filter(
        lambda link: ('play.google.com' in link.get('href'))
        | ('itunes.apple.com' in link.get('href')), soup.select('div.board_main_view a')
    ))
    links = list(map(
        lambda link: link.get('href'), links
    ))

    titles = soup.select('div.board_main_view h3')
    titles = list(map(lambda title: title.text.replace('\xa0', ''), titles))

    return {'links': links, 'titles': titles, 'length': len(links)}
