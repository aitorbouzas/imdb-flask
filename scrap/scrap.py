from bs4 import BeautifulSoup
import requests
import os
import json

BASE_URL = 'http://'
BASE_URL += os.getenv("APPLICATION_HOST", "0.0.0.0")
BASE_URL += ':' + os.getenv("APPLICATION_PORT", "5000")
API_GET = BASE_URL + '/api/top/'
API_POST = BASE_URL + '/api/film/'

# First, delete all records
response = requests.get(API_GET)
films = json.loads(response.text)

for film in films.get('films'):
    requests.delete(API_POST + str(film.get('id')))

# Get IMDB films

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

# Select from soup all data
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

# Run through data
for index in range(0, len(films)):
    pos_len = len(str(index))

    result = {
        'name': films[index][pos_len+1:-7],
        'pos': films[index][0:pos_len+1],
        'year': films[index][-6:].replace('(', '').replace(')', ''),
        'url': urls[index],
        'image': images[index],
        'rating': ratings[index],
    }

    r = requests.post(
        API_POST,
        data=json.dumps(result),
        headers={'content-type': 'application/json'}
    )
    if r.status_code != 200:
        print('ERROR: ' + r.status_code)
        print(r.text)
