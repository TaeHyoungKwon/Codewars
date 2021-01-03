import requests


def main():
    response = requests.get("sample.com")

    if response.content['status'] == '013':
        print(response.content['message'])  # 조회된 데이타가 없습니다. 출력
    else:
        """
        else문에 써서, 오류가 발생시에는 건너 뛰도록 함
        df = pd.DataFrame XXXX
        XXXX
        XXXXXXXX
        XXXXXXXX
        for i in XXXXXXX: 
        """

    # 그 밑에 있는 코드들 실행