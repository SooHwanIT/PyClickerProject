from tkinter import *
import tkinter 
from tkinter.ttk import *
from pathlib import Path
from tkinter import messagebox
import time
import threading

window = Tk()

window.geometry('360x730')

frameInfo = tkinter.Frame(window,relief="solid", bd=2)
frameInfo.pack(side=TOP,fill='x')


notebook = Notebook(window, takefocus=True)
notebook.pack(side=BOTTOM,fill='x')

frame1 = Frame(window)
notebook.add(frame1, text="GoldPerClickUpgrade")
frame2 = Frame(window)
notebook.add(frame2, text="GoldPerTimeUpgrade")
frame3 = Frame(window)
notebook.add(frame3, text="CrystalUpgrade")

#변수 선언


#gold 선언
gold = 0
gold_text = StringVar()  # 골드를 표시할 골드_텍스트를 텍스트 형식으로 지정
gold_text.set(gold)  # 골드 텍스트를 골드로 지정 (초기값 = 0)
gold_Labal = Label(frameInfo, textvariable=gold_text).pack(side=LEFT,anchor='s')  # 골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per click 선언
gold_per_click = 1
gold_per_click_text = StringVar()  # 골드 per 클릭을 표시할 골드 per 클릭_텍스트를 텍스트 형식으로 지정
# 골드 per 클릭 텍스트를 골드 per 클릭로 지정 (초기값 = 0)
gold_per_click_text.set(gold_per_click)
gold_per_click_Labal = Label(frameInfo, textvariable=gold_per_click_text).pack(side=LEFT,anchor='center')  # 골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

#gold per sec 선언
# gold_per_sec = 0
# gold_per_sec_text = StringVar()  # 골드perSec를 표시할 골드perSec_텍스트를 텍스트 형식으로 지정
# gold_per_sec_text.set(gold_per_sec)  # 골드perSec 텍스트를 골드perSec로 지정 (초기값 = 0)
# gold_per_sec_Labal = Label(frameInfo, textvariable=gold_per_sec_text).grid(row=0, column=2)  # 골드perSec를 표시할 tk.labal을 생성 후 골드 택스트를 연결

crystal = 0
crystal_text = StringVar()  # 골드를 표시할 골드_텍스트를 텍스트 형식으로 지정
crystal_text.set(crystal)  # 골드 텍스트를 골드로 지정 (초기값 = 0)
crystal_Labal = Label(frameInfo, textvariable=crystal_text).pack(side=RIGHT,anchor='n')  # 골드를 표시할 tk.labal을 생성 후 골드 택스트를 연결

def Button_OnClick():  # 버튼을 누를때마다 실행되는 함수
    global gold  # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
    global gold_per_click
    gold += gold_per_click  # 골드를 1 늘려줌 (GPC로 변경 예정 )
    gold_text.set(gold)  # 골드를 표시해주는 골드 텍스트를 업데이트 해줌


gold_Button = tkinter.Button(window, text='Button', command=Button_OnClick,height=400).pack(
   side=TOP,fill='both')  # 골드 버튼을 만들고 누를때마다 함수를 실행시킴



def GoldToCrystal():
    MsgBox = messagebox.askyesno("Ask Yes/No", "10000gold => 1crystal\n다른 모든 업그레이드가 초기화 됩니다\n크리스탈을 사용한 업그레이드 제외")
    if (MsgBox == True):
        global gold
        global gold_per_click
        global crystal
        print(int(gold/10000))
        crystal += int(gold/10000)
        crystal_text.set(crystal)
        gold = 0
        gold_per_click = 1
        Cbtindex = len(Cbt)
        for i in range(0, Cbtindex):
            Cbt[i].SetLevel(0)

        Abtindex = len(Abt)
        for i in range(0, Abtindex):
            Abt[i].SetLevel(0)

toCrystal_Button = Button(frame3, text='toCrystal', command=GoldToCrystal).grid(
    row=0, column=5)

def Upgrade_Cost(startCost, level, pow):  # 밸런스
    return int((level*pow)**2+(level*(pow+startCost)))+startCost

class Click_Upgrade_button():
    def __init__(self, name, startCost, cost_pow, upgrade_pow, index):  # 이름, 비용, 비용 증가량, 업그레이드 수치
        self.name = name  # 이름
        self.level = 0  # 레벨
        self.startCost = startCost  # 초기업그레이드비용
        self.cost = startCost  # 업그레이드 비용
        self.cost_pow = cost_pow  # 업그레이드 비용 증가량
        self.upgrade_pow = upgrade_pow  # 업그레이드 수치
        self.text = StringVar()  # 버튼 text
        self.text.set('loding')  # text 초기화
        self.button = Button(  # 버튼 생성
            frame1, textvariable=self.text, command=self.Buy_Click_Upgrade, width=20).pack(side=TOP,fill='x')
        self.UI_Update()  # UI 업데이트

    def Buy_Click_Upgrade(self):
        global gold  # 골드를 글로벌 함수로 지정해서 참조할수 있게 만듬
        global gold_per_click
        if gold >= self.cost:  # 돈이 충분한가 확인
            gold -= self.cost  # 돈 차감
            self.level += 1  # 레벨 1 증가
            self.cost = Upgrade_Cost(
                self.startCost, self.level, self.cost_pow)  # 비용 증가
            gold_per_click += self.upgrade_pow  # 업그레이드 수치만큼 골드 퍼 클릭 증가
            self.UI_Update()

    def GetLevel(self):
        return self.level

    def SetLevel(self, level):
        global gold_per_click
        self.level = level
        self.cost = Upgrade_Cost(self.startCost, self.level, self.cost_pow)
        for _ in range(0,level):
            gold_per_click += self.upgrade_pow 
        self.UI_Update()  # UI 업데이트

    def UI_Update(self):
        self.text.set(str(self.name) + ".Lv" + str(self.level) + "\n 비용 : " +
                      str(int(self.cost)) + "\ngold/click증가량: " + str(self.upgrade_pow))
        gold_per_click_text.set(gold_per_click)  # 라벨 업데이트
        gold_text.set(gold)  # 라벨 업데이트


class Auto_Upgrade_button():
    def __init__(self, name, startCost, cost_pow, upgrade_pow, index, time):  # 이름, 비용, 비용 증가량, 업그레이드 수치
        self.name = name  # 이름
        self.level = 0  # 레벨
        self.time = time  # 시간
        self.startCost = startCost  # 초기업그레이드 비용
        self.cost = startCost  # 업그레이드 비용
        self.cost_pow = cost_pow  # 업그레이드 비용 증가량
        self.upgrade_pow = upgrade_pow  # 업그레이드 수치
        self.text = StringVar()  # 버튼 text 선언
        self.text.set("loding")  # 버튼 text 초기화
        self.index= index
        self.V_PB = DoubleVar()
        self.button = Button(  # 버튼 생성
            frame2, textvariable=self.text, command=self.Buy_Auto_Gold, width=20).pack(side=TOP,fill='x')
        self.progressbar = Progressbar(
            frame2, maximum=100*self.time, variable=self.V_PB, length=100, mode="determinate")
        self.progressbar.pack(side=TOP,fill='x')
        self.UI_Update()

    def Buy_Auto_Gold(self):  # 버튼을 누를때 실행
        global gold  # 골드를로벌 함수로 지정해서 참조할수 있게 만듬
        if gold >= self.cost:  # 골드 >= 비용
            gold -= self.cost  # 비용만큼 골드 차감
            self.level += 1  # 레벨 1 증가
            self.cost = Upgrade_Cost(
                self.startCost, self.level, self.cost_pow)  # 비용 증가
            # gold_per_sec += self.upgrade_pow  # GPS 를 업그레이드 수치만큼 증가
            if(self.level == 1):
                self.fristUpgrade()
            self.UI_Update()  # UI 업데이트

    def GetLevel(self):
        return self.level

    def SetLevel(self, level):
        self.level = level
        self.cost = Upgrade_Cost(self.startCost, self.level, self.cost_pow)
        if(level !=0) :
            self.fristUpgrade()
        else: 
            self.progressbar.grid_remove()
            self.t.cancel()
        self.UI_Update()  # UI 업데이트

    def fristUpgrade(self):
        global gold 
        gold -= self.upgrade_pow*self.level
        self.V_PB = DoubleVar()
        self.progressbar.start(6)
        self.Auto_Gold_Play()  # 함수 실행

    def UI_Update(self):
        self.text.set(self.name+".Lv"+str(self.level)+"("+str(self.time) + "초)\nLv"+str(self.level) + " : 골드 증가량" + str(int(self.level *
                      self.upgrade_pow))+"\n 업그레이드 비용 "+str(self.cost)+"\nLv"+str(self.level+1) + " : 골드 증가량"+str(int((self.level+1)*self.upgrade_pow)))
        # gold_per_sec_text.set(gold_per_sec)  # 라벨 업데이트
        gold_text.set(gold)  # 라벨 업데이트

    def Auto_Gold_Play(self):  # 1초마다 실행되는 함수
        global gold  # 글로벌로 골드 선언
        gold += self.upgrade_pow*self.level  # 골드를 GPS만큼 증가
        gold_text.set(gold)  # 라벨 업데이트
        self.V_PB.set(0)
        # for i in [1,1,1,1,1,1,1,1,1,1,1,1]:
        #     time.sleep(0.1)
        #     self.progressbar.step(10)
        #     if self.V_PB.get() >= self.time*10 : break
        # self.Auto_Gold_Play()
        self.t = threading.Timer(self.time, self.Auto_Gold_Play)
        self.t.start()

#함수 마지막에 1초 후에 다시 동일 함수를 실행함으로써 1초마다 재귀실행되는 함수 생성

def Save():
    f = open("info.txt", 'w')
    SaveUpdate = ''
    SaveUpdate += str(gold)+'\n' + str(gold_per_click) + '\n'
    # '\n'+str(gold_per_sec)
    SaveUpdate += str(crystal)+'\n'
    SaveUpdate += str(len(Cbt))+'\n'
    for i in range(0, len(Cbt)):
        SaveUpdate += str(Cbt[i].GetLevel()) + '\n'
    SaveUpdate += str(len(Abt))+'\n'
    for i in range(0, len(Abt)):
        SaveUpdate += str(Abt[i].GetLevel()) + '\n'


    f.write(str(SaveUpdate))
    f.close()


def Load():
    global gold
    global gold_per_click
    # global gold_per_sec
    global crystal
    f = open("info.txt", 'r')

    gold = int(f.readline())
    gold_per_click = int(f.readline())
    # gold_per_sec = int(f.readline())
    crystal = int(f.readline())
    crystal_text.set(crystal)

    Cbtindex = 3
    Cbtindex = int(f.readline())
    for i in range(0, int(Cbtindex)):
        Cbt[i].SetLevel(int(f.readline()))

    Abtindex = 3
    Abtindex = int(f.readline())
    for i in range(0, int(Abtindex)):
        Abt[i].SetLevel(int(f.readline()))

    f.close()

Cbt = {}
Cbt[0] = Click_Upgrade_button("test1", 10, 1.2, 1, 0)
Cbt[1] = Click_Upgrade_button("test2", 200, 1.2, 10, 1)
Cbt[2] = Click_Upgrade_button("test3", 3000, 1.2, 20, 2)

Abt = {}
Abt[0] = Auto_Upgrade_button("test1", 1, 1.2, 1, 0, 1)
Abt[1] = Auto_Upgrade_button("test2", 1, 1.2, 1000, 1, 10)
Abt[2] = Auto_Upgrade_button("test3", 3000, 1.2, 10, 2, 3)



#저장 불러오기 옵션
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Load", command=Load)

window.config(menu=menubar)
# Button(  # 버튼 생성
#     window, text="L", command=Load).pack(
#     side=TOP, anchor=S)
# Button(  # 버튼 생성
#     window, text="S", command=Save).pack(
#     side=TOP, anchor=S)

window.mainloop()
