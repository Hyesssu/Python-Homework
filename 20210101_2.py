#201102 윤혜수님 Python

#예제 1
'''
import turtle

def square() :
    for _ in range(4) :
        turtle.forward(70)
        turtle.left(90)

turtle.shape("turtle")

for i in range(1,4) :
    turtle.up()
    turtle.goto(100*i,0)
    turtle.down()
    square()

turtle.done()
'''

#예제1
'''
def sum(first,second) :
    print("정수 "+str(first)+"+"+str(second)+"의 합은? "+str(first+second))

first = int(input("첫 번째 정수 : "))
second = int(input("두 번째 정수 : "))
sum(first,second)
'''

#예제2
'''
def circleArea(radius) :
    global pi
    circleArea = pi*radius**2
    return circleArea

def circleCircumference(radius) :
    global pi
    circleCircumference = pi*radius*2
    return circleCircumference

pi = 3.1415926

radius = int(input("반지름의 값을 입력하세요 : "))
print("반지름이 "+str(radius)+"인 원의 면적 : "+str(circleArea(radius)))
print("반지름이 "+str(radius)+"인 원의 둘레 : "+str(circleCircumference(radius)))
'''

#예제3
'''
import turtle
turtle.shape("turtle")

def function(x) :
    return (x**2+1)*0.01

turtle.forward(100)
turtle.home()
turtle.left(90)
turtle.forward(100)
turtle.home()

for x in range(100) :
    turtle.goto(x,function(x))

turtle.done()
'''

#과제
'''
import turtle
turtle.shape("arrow")

def repeat(i) :
        turtle.left(90)
        turtle.forward(slist[i])
        turtle.left(90)

slist=[120,56,309,220,156,23,98]

turtle.color("blue","red")
turtle.begin_fill()

for i in range(7) :
    turtle.forward(50)
    repeat(i)
    turtle.forward(50)
    turtle.write(slist[i])
    repeat(i)
    turtle.goto(50*(i+1),0)

turtle.end_fill()
turtle.done()
'''





