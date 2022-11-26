import requests
import random


numbers = set()
for i in range(950, 9999):
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}"
    url = url.format(i)
    request_result = requests.get(url)
    format_json = request_result.json()

    if format_json.get('returnValue') == "fail":
        print("회차 없음")
        break

    print(f"{i}회차 data 받아오는 중")

    success_result = format_json.get('returnValue', None)
    numbers.add(format_json.get('drwtNo1', None))
    numbers.add(format_json.get('drwtNo2', None))
    numbers.add(format_json.get('drwtNo3', None))
    numbers.add(format_json.get('drwtNo4', None))
    numbers.add(format_json.get('drwtNo5', None))
    numbers.add(format_json.get('drwtNo6', None))
    numbers.add(format_json.get('bnusNo', None))

for i in range(5):
    random_numbers1 = random.sample(numbers, 6)
    random_numbers1.sort()
    print(random_numbers1)