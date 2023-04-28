import requests
from bs4 import BeautifulSoup

url = requests.get("https://jtexpress.vn/vi/tracking?type=track&billcode=841195468192")
htmltext = url.text
soup = BeautifulSoup(htmltext)
result = soup.find('div',{'class':'result_vandon'}).text
result = ' '.join(result.split())
print(result)