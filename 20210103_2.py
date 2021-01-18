#201109 윤혜수님 Python 

#예제 1
'''
import random
slist=[0,0,0,0,0,0]
for _ in range(1000) :
    a = random.randint(1,7)
    if a == 1 :
        slist[0]=slist[0]+1
    elif a == 2 :
        slist[1]=slist[1]+1
    elif a == 3 :
        slist[2]=slist[2]+1
    elif a == 4 :
        slist[3]=slist[3]+1
    elif a==5 :
        slist[4]=slist[4]+1
    else :
        slist[5]=slist[5]+1

for i in range(6) :
    print("주사위가",str(i+1),"인 경우는",str(slist[i]))
'''

#예제 1
'''
book={"파이썬" : "최근에 가장 떠오르는 프로그래밍 언어","변수" : "데이터를 저장하는 메모리 공간","함수" : "작업을 수행하는 문장들의 집합에 이름을 붙인 것","리스트" : "서로 관련이 없는 항목들의 모임"}

print("다음은 어떤 단어에 대한 설명일까요?")
print("="*40)
#.. 어떻게 끌어오는지 다시 여쭤봐야겠다.
for answer, quiz in book.items() :
    a = input(quiz+" : ")
    if a == answer : 
        print("정답입니다.")
    else :
        print("틀렸습니다.")
    #1. keys values items중에서 무엇이 적합한지를 판단 할 것
    #2. items에는 한 쌍을 통으로 반환하기 때문에 values를 가지고 keys를 판단 할 수 있고, 그래서 items를 제일 많이 쓰고, keys -> values 순으로 사용 함
    #3. values를 가지고는 keys를 유추 할 수는 없음.
    #4. 헷갈리면 그냥 items..

'''
#과제1
'''
import random
import turtle

def draw_shape(color,length,sides,x,y) :
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(sides) :
            turtle.forward(length)
            turtle.left(360/sides)
        turtle.end_fill()


slist=["yellow","white","green","blue","red","orange","purple"]
turtle.shape("turtle")
for i in range(7) : 
    color=slist[i]
    length=random.randint(30,100)
    sides=random.randint(3,7)
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    draw_shape(color,length,sides,x,y)

turtle.done()
'''


