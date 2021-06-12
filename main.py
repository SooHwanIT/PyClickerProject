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
gold_text = StringVar()  # 골드를 표시할 골드_텍스트를 텍스트 형식으로 지정
gold_text.set(gold)  # 골드 텍스트를 골드로 지정 (초기값 = 0)
gold_Labal = Label(window, textvariable=gold_text).pack(
    side=TOP)  # 골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per click 선언
gold_per_click_text = StringVar()  # 골드 per 클릭을 표시할 골드 per 클릭_텍스트를 텍스트 형식으로 지정
# 골드 per 클릭 텍스트를 골드 per 클릭로 지정 (초기값 = 0)
gold_per_click_text.set(gold_per_click)
gold_per_click_Labal = Label(window, textvariable=gold_per_click_text).pack(
    side=TOP)  # 골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per sec 선언
gold_per_sec_text = StringVar()  # 골드perSec를 표시할 골드perSec_텍스트를 텍스트 형식으로 지정
gold_per_sec_text.set(gold_per_sec)  # 골드perSec 텍스트를 골드perSec로 지정 (초기값 = 0)
gold_per_sec_Labal = Label(window, textvariable=gold_per_sec_text).pack(
    side=TOP)  # 골드perSec를 표시할 tk.labal을 생성 후 골드 택스트를 연결


def Button_OnClick():  # 버튼을 누를때마다 실행되는 함수
    global gold  # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
    global gold_per_click
    gold += gold_per_click  # 골드를 1 늘려줌 (GPC로 변경 예정 )
    gold_text.set(gold)  # 골드를 표시해주는 골드 텍스트를 업데이트 해줌
    Save()

gold_Button = Button(window, text='Button', command=Button_OnClick).pack(
    side=BOTTOM, anchor=CENTER)  # 골드 버튼을 만들고 누를때마다 함수를 실행시킴

def Upgrade_Cost(startCost,level,pow): #밸런스
    print ((startCost,level,pow))
    return int((level*pow)**2+(level*(pow+startCost)))+startCost

class Click_Upgrade_button():
    def __init__(self, name, startCost, cost_pow, upgrade_pow):  # 이름, 비용, 비용 증가량, 업그레이드 수치
        self.name = name #이름
        self.level = 0 #레벨
        self.startCost = startCost #초기업그레이드비용  
        self.cost = startCost #업그레이드 비용
        self.cost_pow = cost_pow #업그레이드 비용 증가량
        self.upgrade_pow = upgrade_pow #업그레이드 수치
        self.text =  StringVar() # 버튼 text 
        self.text.set('loding') #text 초기화
        self.button = Button(  #버튼 생성
            window, textvariable=self.text, command=self.Buy_Click_Upgrade).pack(side=TOP, anchor=S)
        self.UI_Update() #UI 업데이트
            
    def Buy_Click_Upgrade(self):
        global gold  # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
        global gold_per_click
        if gold >= self.cost:  # 돈이 충분한가 확인
            gold -= self.cost  # 돈 차감
            self.level += 1  # 레벨 1 증가
            self.cost = Upgrade_Cost(self.startCost,self.level,self.cost_pow) # 비용 증가 
            gold_per_click += self.upgrade_pow  # 업그레이드 수치만큼 골드 퍼 클릭 증가
            self.UI_Update()
            
    def GetLevel(self):
        return self.level
    def UI_Update(self):
        self.text.set(str(self.name) +".Lv"+ str(self.level) + "\n 비용 : " + str(int(self.cost)) + "\ngold/click증가량: " + str(self.upgrade_pow))
        gold_per_click_text.set(gold_per_click)  # 라벨 업데이트
        gold_text.set(gold)  # 라벨 업데이트


class Auto_Upgrade_button():
    def __init__(self, name, startCost, cost_pow, upgrade_pow):  # 이름, 비용, 비용 증가량, 업그레이드 수치
        self.name = name    #이름 
        self.level = 0   #레벨 
        self.startCost = startCost#초기업그레이드 비용 
        self.cost = startCost    #업그레이드 비용 
        self.cost_pow = cost_pow    #업그레이드 비용 증가량 
        self.upgrade_pow = upgrade_pow  #업그레이드 수치
        self.text = StringVar()     #버튼 text 선언
        self.text.set("loding")     #버튼 text 초기화
        self.button = Button( #버튼 생성
            window, textvariable=self.text, command=self.Buy_Auto_Gold).pack(
            side=TOP, anchor=S)
        self.UI_Update()

    def Buy_Auto_Gold(self): #버튼을 누를때 실행
        global gold  # 골드를로벌 함수로 지정해서 참조할수 있게 만듬
        global gold_per_sec # ''
        if gold >= self.cost:#골드 >= 비용
            gold -= self.cost  # 비용만큼 골드 차감
            self.level += 1  # 레벨 1 증가
            self.cost =  Upgrade_Cost(self.startCost,self.level,self.cost_pow)  # 비용 증가
            gold_per_sec += self.upgrade_pow #GPS 를 업그레이드 수치만큼 증가
            self.UI_Update() #UI 업데이트
        
    def UI_Update(self):
        self.text.set(str(self.name) +".Lv"+ str(self.level) + "\n 비용 : " + str(int(self.cost)) + "\ngold/sec 증가량: " + str(self.upgrade_pow))
        gold_per_sec_text.set(gold_per_sec)# 라벨 업데이트
        gold_text.set(gold)# 라벨 업데이트


Cbt = [0,0,0]
Cbt[0] = Click_Upgrade_button("test1", 10, 1.2, 1)
Cbt[1] = Click_Upgrade_button("test2", 200, 1.2, 10)
Cbt[2] = Click_Upgrade_button("test3", 3000, 1.2, 20)

Abt1 = Auto_Upgrade_button("test1", 10, 1.2, 1)
Abt2 = Auto_Upgrade_button("test2", 200, 1.2, 5)
Abt3 = Auto_Upgrade_button("test3", 3000, 1.2, 10)


def Auto_Gold():  # 1초마다 실행되는 함수
    global gold #글로벌로 골드 선언 
    global gold_per_sec #글로벌로 GPS 선언 
    gold += gold_per_sec #골드를 GPS만큼 증가
    gold_text.set(gold) #라벨 업데이트
    threading.Timer(1, Auto_Gold).start()  # 1초마다 재귀실행
    #함수 마지막에 1초 후에 다시 동일 함수를 실행함으로써 1초마다 재귀실행되는 함수 생성
def Save():
    f = open("info.txt", 'w')
    f.write(str(gold))
    for i in range(1,len(Cbt)):
        f.write(str(Cbt[i].GetLevel()))
    f.close()
Auto_Gold() #함수 실행

window.mainloop()
