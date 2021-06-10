from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import time 
import threading
window = Tk() 

window.geometry('400x400')
#변수 선언
gold = 0
gold_per_click = 1
gold_per_sec = 0

#gold 선언
gold_text = StringVar() #골드를 표시할 골드_텍스트를 텍스트 형식으로 지정
gold_text.set(gold) #골드 텍스트를 골드로 지정 (초기값 = 0)
gold_Labal = Label(window,textvariable=gold_text).pack(side=TOP) #골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per click 선언
gold_per_click_text = StringVar() #골드 per 클릭을 표시할 골드 per 클릭_텍스트를 텍스트 형식으로 지정
gold_per_click_text.set(gold_per_click) #골드 per 클릭 텍스트를 골드 per 클릭로 지정 (초기값 = 0)
gold_per_click_Labal = Label(window,textvariable=gold_per_click_text).pack(side=TOP) #골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per sec 선언
gold_per_sec_text = StringVar() #골드perSec를 표시할 골드perSec_텍스트를 텍스트 형식으로 지정
gold_per_sec_text.set(gold_per_sec) #골드perSec 텍스트를 골드perSec로 지정 (초기값 = 0)
gold_per_sec_Labal = Label(window,textvariable=gold_per_sec_text).pack(side=TOP) #골드perSec를 표시할 tk.labal을 생성 후 골드 택스트를 연결
 



def Button_OnClick():  #버튼을 누를때마다 실행되는 함수
    global gold # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
    global gold_per_click 
    gold += gold_per_click  #골드를 1 늘려줌 (GPC로 변경 예정 )
    gold_text.set(gold) #골드를 표시해주는 골드 텍스트를 업데이트 해줌

gold_Button = Button(window,text= 'Button',command = Button_OnClick ).pack(side=BOTTOM,anchor=CENTER) #골드 버튼을 만들고 누를때마다 함수를 실행시킴

def Auto_Gold(): # 1초마다
    global gold
    global gold_per_sec
    gold += gold_per_sec
    gold_text.set(gold)
    threading.Timer(1,Auto_Gold).start() # 1초마다 재귀실행

def Buy_Auto_Gold(cost):
    global gold # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
    global gold_per_sec 
    if gold>= cost:
        gold -= cost
        gold_per_sec+=1
        gold_per_sec_text.set(gold_per_sec)
        gold_text.set(gold)

buy_auto_gold_1 = Button(window,text= ' upgade \n gold/sec \n price : 10  \n goldPerSec += 1',command = lambda: Buy_Auto_Gold(10)).pack(side=RIGHT) #초당 n골드를 생성하는 기계를 사는 버튼

def Buy_Click_Gold(cost):
    global gold # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
    global gold_per_click 
    if gold>= cost:
        gold -= cost
        gold_per_click +=1
        gold_per_click_text.set(gold_per_click)
        gold_text.set(gold)

buy_click_gold = Button(window,text= ' upgade \n gold/click \n price : 10  \n goldPerClick += 1',command = lambda: Buy_Click_Gold(10)).pack(side=LEFT) #초당 n골드를 생성하는 기계를 사는 버튼


Auto_Gold()

window.mainloop()