from bs4 import BeautifulSoup
import requests

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

films = [
    (' '.join(n.get_text().split()).replace('.', ''))
    for n in soup.select('.lister-list tr td.titleColumn')
]
images = [
    img.attrs.get('src')
    for img in soup.select('.lister-list tr td.posterColumn a img')
]
urls = [
    a.attrs.get('href')
    for a in soup.select('.lister-list tr td.posterColumn a')
]
ratings = [
    strong.get_text()
    for strong in soup.select('.lister-list tr td.ratingColumn.imdbRating')
]

for index in range(0, len(films)):
    pos_len = len(str(index))

    result = {
        'name': films[index][pos_len+1:-7],
        'pos': films[index][0:pos_len],
        'year': films[index][-6:].replace('(', '').replace(')', ''),
        'url': urls[index],
        'image': images[index],
    }
    print(result)
