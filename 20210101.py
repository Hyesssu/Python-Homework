#201026 윤혜수님 Python

#예제 1
'''
temp = int(input("현재 온도를 입력하시오 : "))

    if temp >= 25 :
        print("반 바지를 입으세요.")
    else :
        print("긴 바지를 입으세요.")

'''
#예제 2
'''
score = int(input("성적을 입력하시오. "))

while score <0 or 100 < score : 
    print("잘못 입력하셨습니다.")
    score = int(input("성적을 입력하시오. "))

if score >= 90 :
    print("A학점 입니다.")
elif score >= 80 :
    print("B학점 입니다.")
elif score >= 70 :
    print("C학점 입니다.")
elif score >= 60 :
    print("D학점 입니다.")
else :
    print("F학점 입니다.")
'''

#예제3
'''
import random
a = random.randint(1,100)
b = random.randint(1,100)
c = int(input(str(a)+"-"+str(b)+"=")) # 왜 , 면 안 되는거지?.. input도 문자열 1개만 가능. write 처럼

if c==a-b :
    print("맞았습니다.")
else :
    print("틀렸습니다.")
'''

#예제1
'''
num = int(input("원하는 단은? "))

for i in range(1,10) :
    print(str(num),"*",str(i),"=",str(num*i))
'''

#예제1
'''
for i in range(1,51) :
    print(str(2*i), end=" ")
'''

#예제2
'''
import random

a = random.randint(1,10)
b = random.randint(1,10)
answer = int(input(str(a)+"*"+str(b)+"는 "))

while answer != a*b :
    a = random.randint(1,10)
    b = random.randint(1,10)
    answer = int(input(str(a)+"*"+str(b)+"는 "))

print("맞았습니다.")
'''

#예제3
'''
total = 0
a = int(input("정수를 입력하시오 : "))

while a != 0 :
    total += a
    a = int(input("정수를 입력하시오 : "))

print("합은",str(total),"입니다.")
'''

#예제4
'''
import random
import turtle

turtle.shape("turtle")

for _ in range(10) :
    radius = random.randint(10,150)
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(radius)

turtle.done()
'''
    


    





