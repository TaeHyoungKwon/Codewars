import requests
from bs4 import BeautifulSoup


def show_bus_arrival_time():
    url = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?serviceKey=7jHs%2Bx3TFCBGi9X0WFnQeUXUpCC7KJLJ1aA%2BmM3j8cJau%2B67c22LhWy%2FmkWvLG7m%2BieC4iQay%2FgroMRytDrmzQ%3D%3D&stId=110000234&busRouteId=100100043&ord=8"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    first_bus_arrival_time = soup.find("arrmsg1").text
    second_bus_arrival_time = soup.find("arrmsg2").text

    message = "261번 버스 도착 정보입니다."
    first_bus_message = f"첫번째 버스 : {first_bus_arrival_time}"
    second_bus_message = f"두번째 버스 : {second_bus_arrival_time}"

    return message + "\n" + first_bus_message + "\n" + second_bus_message


print(show_bus_arrival_time())