from requests import get
from bs4 import BeautifulSoup
url = 'https://trak.in/india-startup-funding-investment-2015/'
response = get(url)
print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('table', class_='tablepress-46')
print(movie_containers)
