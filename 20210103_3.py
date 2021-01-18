#201123 윤혜수님 Python 
# 예제1
'''
from tkinter import * 

window = Tk()

label1 = Label(window, text="화씨")
label2 = Label(window, text="섭씨")
entry1 = Entry(window)
entry2 = Entry(window)
button1 = Button(window, text="화씨->섭씨")
button2 = Button(window, text="섭씨->화씨")
label1.pack()
label2.pack()
entry1.pack()
entry2.pack()
button1.pack()
button2.pack()

window.mainloop()
'''
#예제1
'''
from tkinter import *

def process() :
    inch = int(entry.get())
    cm = inch*2.54
    label4["text"]=str(cm)+"센티미터"
    
window = Tk()

label1 = Label(window, text="인치를 센티미터로 변환하는 프로그램")
label2 = Label(window, text="인치를 입력하시오 : ")
label3 = Label(window, text="변환결과:")
label4 = Label(window, text="결과값이 출력됩니다.")
entry = Entry(window)
button1 = Button(window, text="변환", command=process) 

label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=1, column=0)
entry.grid(row=1, column=1)
label3.grid(row=2, column=0)
label4.grid(row=2, column=1)
button1.grid(row=3, column=1)
window.mainloop()
'''
#실습1
'''
from tkinter import *

def plus () :
    global total # tkinter에서는 항상 global을 사용.
    sum1 = int(entry.get())
    total += sum1
    label2["text"] = total # 왜 55번 줄을 여기에 적으면 실행이 되지 않는 것일까? 된다
                        # 함수가 호출되었을 때 또 그 값이 계산이 되는 등 필요한 경우에만.. 그렇지 않으면 그냥 반환을 자동으로 하고 냅둠

def minus () :
    global total
    minus1 = int(entry.get())
    total -= minus1
    label2["text"] = total


def reset () :
    global total # 밖에 있는 인자.. 얘는 retrun을 해야지만 바뀜. total는 모든 함수가 공유하고 변화해야하니까
    reset = int(entry.get())
    total = 0
    label2["text"] = 0
    entry.delete(0,END)


window=Tk()
total = 0
label1 = Label(window, text="현재 합계")
label2 = Label(window, text="0")
entry = Entry(window)
button1 = Button(window, text="더하기(+)", command = plus) #plus()
button2 = Button(window, text="빼기(-)", command = minus)
button3 = Button(window, text="초기화", command = reset)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, columnspan=2)
entry.grid(row=1, column=0, columnspan=3)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

window.mainloop()

'''
