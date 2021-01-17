#201102 윤혜수님 Python

#과제 1-1)
'''
z = int(input("정수를 입력하시오 >> "))

for i in range(z) :
    print("*"*(i+1))
'''
#과제 1-2)
'''
z = int(input("정수를 입력하시오 >> "))

for i in range(z) :
    print("*"*(z-i))
'''
#과제 1-3)
'''
z = int(input("정수를 입력하시오 >> "))

for i in range(z) :
    print(" "*(z-i+1)+"*"*(i+1))
'''
#과제 1-4)
'''
z = int(input("정수를 입력하시오 >> "))

for i in range(z) :
    print(" "*i+"*"*(z-i))
'''
#과제 2
'''
z = int(input("정수를 입력하시오 >> "))

for i in range(z) :
    print(" "*(z-i)+"*"*(2*i+1))

for i in range(z) :
    print(" "*(i+1)+"*"*(2*(z-i)-1))
'''

#과제 3
'''
start = int(input("시작 수 : "))
last = int(input("끝 수 : "))
distance = int(input("증가 값 : "))

print("="*40)

print("합 : ", end="")
sum_total = 0
for num in range(start, last, distance) :
    sum_total += num
    print(num, end=" + ")
print("\b\b=", sum_total)

print("곱 : ", end="")
multiple_total = 1
for num in range(start, last, distance) :
    multiple_total *= num
    print(num, end=" * ")
print("\b\b=", multiple_total)

print("="*40)
'''
#과제 4
'''
slist=[]
for i in range(1,11) :
    a = int(input(str(i)+"번째 숫자를 입력하시오 >> "))
    slist.append(a)

max = slist[0]
min = slist[0]

for a in range(10) :
    if max < slist[a] :
        max = slist[a]
    if min > slist[a] :
        min = slist[a]

print("입력된 값은",str(slist)+"이며, 제일 큰 값은 ",str(max)+"이고,")
print("제일 작은 값은 "+str(min)+"이다.")
'''
#과제 5
print("="*40)
print("1. 전원 끄기")
print("2. 전원 켜기")
print("3. 볼륨 조절")
print("4. 채널 조절")
print("5. 현재의 상태 출력")
print("6. 프로그램 종료")
print("="*40)

POWER = False
Volumn = 0
Channel = 0

def power() : 
    global POWER
    if POWER :
        POWER = False
    else :
        POWER = True

def setVolumnUp(size) :
    global Volumn
    Volumn += size

    if Volumn > 20 : 
        Volumn = 20

    return Volumn

def setVolumnDonw(size) :
    global Volumn
    Volumn += size

    if Volumn < 0 : 
        Volumn = 1
    return Volumn

def setChannelUp(size) :
    global Channel
    Channel += size
    if Channel < 1 : 
        Channel = 1
    return Channel

def setChannelDown(size) :
    global Channel
    Channel += size
    if Channel > 10 :
        Channel = 10
    return Channel
        
def getNow() :

    print("현재의 TV의 전원 상태는",str(POWER),"볼륨은",str(Volumn),"채널은",str(Channel),"입니다.")

want = int(input("원하는 기능의 번호를 입력하세요 >> "))

while want != 6 :
    if want == 1 :
        if POWER :
            power()
        else :
            print("이미 꺼져있습니다.")

    elif want == 2 :
        if POWER :
            print("이미 켜져있습니다.")
        else :
            power()
    
    elif want == 3 :

        if POWER : 
            size = int(input("변경할 볼륨을 입력하세요 "))

            if size > 0 : 
                setVolumnUp(size)
            elif size < 0 :
                setVolumnDonw(size)            

        else :
            print ("TV가 꺼져있습니다.")
            break

    elif want == 4 :

        if POWER :
            size = int(input("변경할 채널을 입력하세요 "))

            if size > 0 :
                setChannelUp(size)
            elif size < 0 :
                setChannelDown(size)
        
        else :
            print("TV가 꺼져있습니다.")
            break

    elif want == 5 :
        getNow()

    want = int(input("원하는 기능의 번호를 입력하세요 >> "))
    


