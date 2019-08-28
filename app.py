from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의


@app.route('/name')
def name():
    return '강동주'

@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'


#### /squre/숫자
#### -> 입력된 숫자를 제곱한 결과를 보여줌
@app.route('/square/<int:number>')
def square(number):
    # number를 ㄹ제곱하여 반환
    return str(number ** 2)

#### /menu/
#### -> 점심메뉴 추천
@app.route('/menu')
def menu():
    foods = ['바스버거','대우식당','진가와','고갯마루']
    return random.choice(foods)

#### /lotto/
#### -> 로또번호 추천
@app.route('/lotto')
def lotto():
    winner = [3, 5, 12, 13, 33, 39]
    num = random.sample(range(1,46),6)
    #num.sort()

    # 만약 6개가 모두 일치하면 -> 1등
    # 만약 5개가 일치하면 -> 3등
    # 만약 4개가 일치하면 -> 4등
    # 만약 3개가 일치하면 -> 5등

    #cnt = 0
    cnt = len(set(winner) & set(num))
    rank = '꽝'

    # for i in num:
    #     if i in winner:
    #         cnt += 1

    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'

    return str(sorted(num)) + rank

