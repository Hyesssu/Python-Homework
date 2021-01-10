#201019 윤혜수님 Python
#연습문제 1
'''
print("환영합니다.\n파이썬의 세계에 오신 것을 환영합니다.\n 파이썬은 강력합니다.")
print("환영합니다.")
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")
'''

#연습문제 2
'''
import turtle
turtle.shape("turtle")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.done()
'''

#연습문제 3
'''
import turtle
turtle.shape("turtle")
turtle.forward(100)
turtle.up()
turtle.goto(0,100)
turtle.down()
turtle.forward(100)
turtle.done()
'''

#연습문제 4
'''
ground = str(input("경기장은 어디입니까? "))
winner = str(input("이긴 팀은 어디입니까? "))
looser = str(input("진 팀은 어디입니까? "))
VIP = str(input("우수선수는 누구입니까? "))
score = str(input("스코어는 몇대몇입니까? "))
print("="*40)
print("오늘",ground,"에서 야구 경기가 열렸습니다.")
print(winner,"과",looser,"은 치열한 공방전을 펼쳤습니다.")
print(VIP,"이 맹활약을 하였습니다.")
print("결국",winner,"이(가)",looser,"을(를)",score,"로 이겼습니다.")
print("="*40)
'''

#연습문제 5
'''
a = int(input("첫 번째 숫자를 입력하시오 : "))
b = int(input("두 번째 숫자를 입력하시오 : "))
c = int(input("세 번째 숫자를 입력하시오 : "))
print(str(a),str(b),str(c),"의 평균은",str((a+b+c)/3),"입니다.")
'''


#과제
'''
import turtle
turtle.shape("turtle")
radius = 50
turtle.circle(radius)
turtle.up()
turtle.goto(100,0)
turtle.down()
radius+=20
turtle.circle(radius)
turtle.up()
turtle.goto(200,0)
turtle.down()
radius+=20
turtle.circle(radius)
turtle.done()
'''

#연습문제 1. 매출 계산하기
'''
아메리카노 = 2000
카페라떼 = 3000
카푸치노 = 3500
ameEA = int(input("아메리카노 판매 개수 : "))
cafeEA = int(input("카페라떼 판매 개수 : "))
cafuEA = int(input("카푸치노 판매 개수 : "))
total = 아메리카노*ameEA + 카페라떼*cafeEA + 카푸치노*cafuEA
print("총 매출은",str(total),"입니다.")
'''

#연습문제 2.
'''
a=int(input("a : ")) 
b=int(input("y : "))
print("두 수의 합 : ",a+b)
print("두 수의 차 : ", a-b)
print("두 수의 곱 : ", a*b)
print("두 수의 평균 : ", (a+b)/2)
print("큰 수 : ", max(a,b))
print("작은 수 : ", min(a,b))
'''

#연습문제 3.
'''
z = int(input("네 자리 정수를 입력하시오 : "))
total=z//10**3
z=z%10**3
total+=z//10**2
z=z%10**2
total+=z//10
z=z%10
total+=z
print("자리 수의 합 : ", str(total))
'''

#연습문제
'''
import turtle
name = str(turtle.textinput("TITLE", "당신의 이름은 무엇입니까?"))
turtle.shape("turtle")
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.write("안녕하세요?"+name+"씨, 터틀 인사드립니다.")
        # :: 궁금증 :: 왜 ,를 사용하면 되지 않는 것인지?
turtle.done()
'''

#연습문제 1
'''
print("안녕하세요?")
name = input("이름이 어떻게 되세요?")
print("만나서 반갑습니다.", str(name), "씨")
print("이름의 길이는 다음과 같군요.",str(len(name)))
age = int(input("나이가 어떻게 되나요?"))
print("내년이면",str(age+1),"이 되시는군요.")
'''

#연습문제 2
'''
a = str(input("기호를 입력하시오 : "))
b = str(input("중간에 삽입할 문자열을 입력하시오 : "))
print(a[0]+b+a[1])
'''

#연습문제 3
'''
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
x3 = int(input("x3 : "))
y3 = int(input("y3 : "))

import turtle
turtle.shape("turtle")
turtle.up()
turtle.goto(x1,y1)
turtle.down()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.done()
'''

#과제
'''
import turtle
color=[]
color.append(str(input("첫 번째 색을 입력하세요 : ")))
color.append(str(input("두 번째 색을 입력하세요 : ")))
color.append(str(input("세 번째 색을 입력하세요 : ")))
color.append(str(input("네 번째 색을 입력하세요 : ")))

turtle.shape("turtle")
turtle.fillcolor(color[0])
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.goto(50,0)
turtle.fillcolor(color[1])
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.goto(100,0)
turtle.fillcolor(color[2])
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.goto(150,0)
turtle.fillcolor(color[3])
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.done()
'''