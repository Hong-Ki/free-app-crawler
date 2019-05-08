import requests
from bs4 import BeautifulSoup

req = requests.get('http://bbs.ruliweb.com/market/board/1020/list?search_type=member_srl&search_key=5046042')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
elements = soup.select(
  'tr.table_body:not(.notice)'
)[:2]

arr = []

for element in elements:
  obj = {
    'title' : element.select('.subject a ')[0].text,
    'link': element.select('.subject a ')[0].get('href'),
    'time': element.select('.time')[0].text.strip(),
  }
  arr.append(obj)
                                            
#print(arr)
for obj in arr:
  req = requests.get(obj['link'])
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')

  links = soup.select('div.board_main_view a')
  links = list(filter(lambda link: ('play.google.com' in link.get('href')) | ('itunes.apple.com' in link.get('href')) , links))

  print('---LINKS')
  print(links)
  print('---LINKS END')

  arr2= []
  for i in range( len(links) ):
    app = {
      'link': links[i].get('href')
    }

    arr2.append(app)
  print(arr2)
