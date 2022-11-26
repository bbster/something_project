import random

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NewResolution(BaseModel):
    message = str
    email = str


@app.get("/app/extract_lotto")
async def get_lotto():
        req = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1')

        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        last_number = soup.select_one('div.win_result > h4 > strong').text.replace("회", "")
        last_number = int(last_number)
        win_number_list = []

        for index in range(last_number, last_number-100, -1):
            url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}"
            url = url.format(index)
            request_result = requests.get(url)
            format_json = request_result.json()

            if format_json.get('returnValue') == "fail":
                break

            print(f"{index}회차 data 받아오는 중", end='\r')
            if last_number-10 <= index:  # 큰값에서부터 줄어드는데 index는 계속 줄어든단말이지
                win_number_dict = _number_dict(format_json, index)
                win_number_list.append(win_number_dict)

            random_lotto_number = _line_numbers(format_json)

        result = {
            '1등 당첨 번호': win_number_list,
            '번호 추출': random_lotto_number
        }
        return result


def _number_dict(format_json, index):
    win_price = format_json.get('firstWinamnt', None)
    win_price = str(win_price)
    win_price = f'{win_price[:-8]}억'

    numbers_dict = {
        f"{index}회차": [
            win_price,
            format_json.get('drwtNo1', None),
            format_json.get('drwtNo2', None),
            format_json.get('drwtNo3', None),
            format_json.get('drwtNo4', None),
            format_json.get('drwtNo5', None),
            format_json.get('drwtNo6', None),
            format_json.get('bnusNo', None)],
    }
    return numbers_dict


def _line_numbers(format_json):
    numbers = set()
    numbers.add(format_json.get('drwtNo1', None)),
    numbers.add(format_json.get('drwtNo2', None)),
    numbers.add(format_json.get('drwtNo3', None)),
    numbers.add(format_json.get('drwtNo4', None)),
    numbers.add(format_json.get('drwtNo5', None)),
    numbers.add(format_json.get('drwtNo6', None)),
    numbers.add(format_json.get('bnusNo', None))

    for i in range(5):
        random_numbers1 = random.sample(numbers, 6)
        random_numbers2 = random.sample(numbers, 6)
        random_numbers3 = random.sample(numbers, 6)
        random_numbers4 = random.sample(numbers, 6)
        random_numbers5 = random.sample(numbers, 6)
        random_numbers1.sort()
        random_numbers2.sort()
        random_numbers3.sort()
        random_numbers4.sort()
        random_numbers5.sort()
        lotto_data = {
            'line1': random_numbers1,
            'line2': random_numbers2,
            'line3': random_numbers3,
            'line4': random_numbers4,
            'line5': random_numbers5,

        }

    return lotto_data


@app.get("/app/resolution")
async def get_resolution():
    result = []

    pass


@app.post("/app/resolution")
async def post_resolution():
    pass
