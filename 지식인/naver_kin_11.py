from bs4 import BeautifulSoup
import requests

url = "https://post.naver.com/viewer/postView.nhn?volumeNo=30361119&memberNo=34059480&navigationType=push"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# print(res.text)
a = soup.find_all('div')[1]
a = a.find_all('div')[1]
print(a)

