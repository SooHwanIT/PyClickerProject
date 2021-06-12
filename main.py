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

class Auto_Upgade_button():
    def __init__(self,name,cost,cost_pow,upgade_pow): #이름, 비용, 비용 증가량, 업그레이드 수치
            self.cost = cost
            self.power = cost_pow
            self.upgade_pow = upgade_pow
            self.name = name +"\n 비용 : " + str(cost) + "gold/sec 증가량: " + str(upgade_pow)
            self.button = Button(window,text = self.name, command = self.Buy_Auto_Gold).pack(side=TOP,anchor=S)
    def Buy_Auto_Gold(self):
        global gold # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
        global gold_per_sec 
        if gold>= self.cost:
            gold -= self.cost
            gold_per_sec+= self.upgade_pow
            gold_per_sec_text.set(gold_per_sec)
            gold_text.set(gold)

class Click_Upgade_button():
    def __init__(self,name,cost,cost_pow,upgade_pow): #이름, 비용, 비용 증가량, 업그레이드 수치
        self.cost = cost
        self.power = cost_pow
        self.upgade_pow = upgade_pow
        self.name = name +"\n 비용 : " + str(cost) + "gold/click 증가량: " + str(upgade_pow)
        self.button = Button(window,text = self.name, command = self.Buy_Click_Upgade).pack(side=TOP,anchor=S)
    def Buy_Click_Upgade(self):
        global gold # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
        global gold_per_click 
        if gold>= self.cost: #돈이 충분한가 확인
            gold -= self.cost #돈 차감
            gold_per_click += self.upgade_pow #업그레이드 수치만큼 골드 퍼 클릭 증가
            gold_per_click_text.set(gold_per_click) #라벨 업데이트
            gold_text.set(gold) #라벨 업데이트

Cbt1 = Click_Upgade_button("test1",10,15,1)
Cbt2 = Click_Upgade_button("test2",20,15,2)
Cbt3 = Click_Upgade_button("test3",30,15,3)

Abt1 = Auto_Upgade_button("test1",10,15,1)
Abt2 = Auto_Upgade_button("test2",20,15,2)
Abt3 = Auto_Upgade_button("test3",30,15,3)


Auto_Gold()

window.mainloop()