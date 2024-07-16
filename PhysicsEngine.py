#2D Physics Engine goo hyun goose
from tkinter import *
tk=Tk()

tk.title('Physics 2D CHANGP')
tk.geometry("900x600+0+0")
tk.resizable(False,False)

userInterface = Frame(tk, relief = "solid", width = 300, height = 600)
userInterface.place(x=0, y=0)

display = Frame(tk, relief = "solid", bd = 2, width = 600, height = 600)
display.place(x = 300, y = 0)

canvas  = Canvas(display, relief="solid", bd=0, width = 600, height = 600, bg='white')
canvas.pack()

objectList = []


def mouse_position(event):                    #마우스 위치 받아오기
    global objectList
    mousex, mousey = event.x, event.y
    place_circle(mousex, mousey)

def place_circle(x, y):                       #원 그리기
    global objectList
    objectList.append([x, y, radius_value, 0, 0])   #[x location, y location, radius, x velocity, y velocity]
    canvas.create_oval(x-radius_value, y-radius_value, x+radius_value, y+radius_value)

canvas.bind('<Button-1>', mouse_position)

def falling(k):                                #중력 구현
    global objectList
    objectList[k][4] += 9.8
    print(objectList, 'falling')

def collisionCheck(k):
    global xgap, ygap, objectList
    for j in range(len(objectList)-1, k-1, -1):
        xgap = objectList[k][0] - objectList[j][0]
        ygap = objectList[k][1] - objectList[j][1]

        if xgap**2 + ygap**2 <= (objectList[k][2] + objectList[j][2])**2 :
            collision(k, j)

def collision(a, b):
    global objectList
    objectList[a][3] = xgap*10
    objectList[a][4] = ygap*(-10)
    objectList[b][3] = xgap*(-10)
    objectList[b][4] = ygap*10

def animate():
    global objectList
    for i in range(len(objectList)):
        falling(i)
        collisionCheck(i)

    for i in range(len(objectList)):
        print(objectList)
        canvas.move(i+1, objectList[i][3], objectList[i][4])
        canvas.update()

#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
#왜안돼?
        

def azzui():
    ...

def clear():           # clear the window (기능 추가 필요함)
    global huhu
    huhu = 0
    print(huhu)
    

def close():           # close the window
    tk.quit()
    tk.destroy()


def temp():            # clear()와 경고 창 삭제를 동시에
    global areyouokaytoclear
    clear()
    # deselectall()
    areyouokaytoclear.destroy()

def tempwarn():        # clear, clear경고 창. 비정의 커맨드 경고 창 코드 참고.
    global areyouokaytoclear
    AYOC = "Are You Okay To Clear This Work?"
    areyouokaytoclear = Toplevel(tk)
    areyouokaytoclear.geometry("320x200+820+100")
    areyouokaytoclear.resizable(False, False)
    areyouokaytoclear.title("Are You Okay To Clear This Work?")
    entlabel = Label(areyouokaytoclear, text = AYOC, width = 200, height = 50, fg = "red", relief = "solid", bitmap = "info", compound = "top")
    entlabel.pack()
    yentbutton = Button(areyouokaytoclear, width = 10, text = "yes", overrelief = "solid", command = temp)  #  yes 누르면 경고 창 삭제, clear실행
    noentbutton = Button(areyouokaytoclear, width = 10, text = "no", overrelief = "solid", command = areyouokaytoclear.destroy)  #  no 누르면 경고 창만 삭제
    yentbutton.pack()
    noentbutton.pack()

def closewarn():       # close the window with warnning window \ tempwarn 참고
    AYOE = "Are You Okay To Exit This Program?"
    areyouokaytoexit = Toplevel(tk)
    areyouokaytoexit.geometry("320x200+820+100")
    areyouokaytoexit.resizable(False, False)
    areyouokaytoexit.title("Are You Okay To Exit This Program?")
    esclabel = Label(areyouokaytoexit, text = AYOE, width = 200, height = 50, fg = "red", relief = "solid", bitmap = "info", compound = "top")
    esclabel.pack()
    yescbutton = Button(areyouokaytoexit, width = 10, text = "yes", overrelief = "solid", command = close)
    noescbutton = Button(areyouokaytoexit, width = 10, text = "no", overrelief = "solid", command = areyouokaytoexit.destroy)
    yescbutton.pack()
    noescbutton.pack()

def aboutPE():
    AYOE = "About Physics Engine \n Visualizing Physics Engine And Experience It \n \n \n Editors: JunSeok.S HyunJune.J \n email: rkddkdus05@gmail.com"
    aboutLC = Toplevel(tk)
    aboutLC.geometry("320x200+820+100")
    aboutLC.resizable(False, False)
    aboutLC.title("About Physic Engine")
    lclabel = Label(aboutLC, text = AYOE, width = 300, height = 150, fg = "medium purple", relief = "solid", bitmap = "info", compound = "top")
    lclabel.pack()
    lcbutton = Button(aboutLC, width = 10, text = "close", overrelief = "solid", command = aboutLC.destroy)
    lcbutton.pack()

def PEhelp():
    AYOE = "DirectCurrent Circuit Help \n Commands \n \n \n [m(ㅡ)] > [fill 'ㅡ'wire] \n [l(ㅣ)] > [fill 'ㅣ'wire] \n \n derived from 'ㅡ' is fill Current Distribution wire \n [n(ㅜ)] > [fill 'ㅜ'wire] \n [h(ㅗ)] > [fill 'ㅗ'wire] \n \n derived from 'ㅣ' is fill Current Collecting wire \n [j(ㅓ)] > [fill 'ㅓ'wire] \n [k(ㅏ)] > [fill 'ㅏ'wire] \n \n [s(ㄴ)] > [fill 'ㄴ'wire] \n [b] > [set battery]  \n [r] > [set resistance]  \n [space] > [rotate wire] \n [Esc] > [Exit] \n [Enter] > [Clear] \n [e] > [Erase] \n [o] > [Operate] \n [1] > [Resistance1] \n [2] > [Resistance2] \n [3] > [Resistance3] \n [4] > [Resistance4] \n [5] > [Resistance5] \n [6] > [Resistance6] "
    LCHelp = Toplevel(tk)
    LCHelp.geometry("320x520+820+100")
    LCHelp.resizable(False, False)
    LCHelp.title("DirectCurrent Circuit Help")
    lclabel = Label(LCHelp, text = AYOE, width = 300, height = 470, fg = "gold4", relief = "solid", bitmap = "info", compound = "top")
    lclabel.pack()
    lcbutton = Button(LCHelp, width = 10, text = "close", overrelief = "solid", command = LCHelp.destroy)
    lcbutton.pack()

def nihahaha():  #  NiHaHaHa!!!!
    Nihahaha = Toplevel(tk)
    Nihahaha.geometry("400x400")
    Nihahaha.resizable(False, False)
    Nihahaha.title("NiHaHaHa!")
    imagenihaha = PhotoImage(file = "nihahaha.PNG")
    Label.image = imagenihaha # because of Python gabagecollector works reference counting, so i have to 수동으로 참고 횟수 늘려주기.
    nilabel = Label(Nihahaha, image = imagenihaha, compound = "top")
    nilabel.pack(expand = 1, anchor = CENTER)
    print("Nihahaha!")

texts = Text(userInterface, width=15, height=2)
texts.insert(INSERT, "")
texts.pack(padx=4)


menubar = Menu(tk) # menubar is Menu

menu1 = Menu(menubar, tearoff = 0) # menu1은 첫 번째 Menu, tearoff = 0: 하위 메뉴 분리 기능 사용 유무 판단

menu1.add_command(label = "Clear", command = tempwarn)
menu1.add_separator()
menu1.add_command(label = "Exit", command = closewarn)
menubar.add_cascade(label = "File", menu = menu1)

menu2 = Menu(menubar, tearoff = 0, selectcolor = "green")

menu2.add_radiobutton(label = "Undo", state = "disabled") # 미안한데 작동 안돼
menu2.add_radiobutton(label = "Redo") # 미안한데 작동 안돼
menu2.add_radiobutton(label = "Cut") # 미안한데 작동 안돼(, command = fuction 없으면 작동 안 된다 보면 됨)
menubar.add_cascade(label = "Edit", menu = menu2)

menu3 = Menu(menubar, tearoff = 0)

menu3.add_checkbutton(label = "NA")
menu3.add_checkbutton(label = "mapl")
menu3.add_checkbutton(label = "nihahaha", command = nihahaha)
menubar.add_cascade(label = "Run", menu = menu3)

menu4 = Menu(menubar, tearoff = 0)

menu4.add_command(label = "About DirectCurrentCircuit", command = aboutPE)
menu4.add_separator()
menu4.add_command(label = "D.C. Help", command = PEhelp)
menubar.add_cascade(label = "Help", menu = menu4)

tk.config(menu = menubar)


# def Atsui()

def kuhuhuhu(): # Kufufu 💢💢💢
    mousex = tk.winfo_pointerx(); mousey = tk.winfo_pointery()
    print(mousex, mousey)
    

# ㅎㅇ

# 키 입력 저장하는 변수
keypressed = 0

# 키 입력 출력하는 함수: MikoMikoNyanNyan()
def MikoMikoNyanNyan(event): # 미코미코 냥냥♪
    global keypressed
    keypressed = event.keysym
    print(keypressed)
        # test()
    if event.keysym == 'a' :
        kuhuhuhu()
        print("Kufufu~") 
    elif event.keysym == 'Escape' :
        closewarn()
    elif event.keysym == 'Return' : # 대충 Return=엔터키라는 뜻
        tempwarn()
    elif event.keysym == 'g' :
        print(radius_value)

tk.bind("<KeyPress>", MikoMikoNyanNyan)




def setradius(self):
    explanationresistance.config(text = '반지름 크기를 선택')
    if self == '':
        return True
    
    valid = False
    
    if self.isdigit():
        if (int(self) >= 0 and int(self) <= 100): # 0~100 값만 사용 가능함ㅋ
            valid = True
    return valid

def errorsetradius(self):
        unknowntext = str(self) + ' is invalid value \n try valid value: 0~100'  #  위쪽에 정의되지 않은 키 입력들을 unknowntext로 간주, <입력된 키값, 'is not a valid key'>로써 나타냄 (나중에 화면 크기에 맞춰서 최대/최소 설정 크기 지정해 주면 정말 좋겠어요)
        toplevel = Toplevel(tk)
        toplevel.geometry("320x200+820+100")
        toplevel.resizable(False, False)
        toplevel.title("ERROR: not a valid key")  # 창 이름
        label = Label(toplevel, text = unknowntext, width = 200, height = 50, fg = "red", relief = "solid", bitmap = "error", compound = "top")  #  unknowntext출력, i마크 표시(붉은색) 할 창 생성
        label.pack()

        button = Button(toplevel, width = 10, text = "ok", overrelief = "solid", command = toplevel.destroy)  #  ok버튼 누르면 경고 창 삭제
        button.pack()

# display.bind_all('<KeyPress>', keypressed)

validate_command = (userInterface.register(setradius), '%P')
invalid_command = (userInterface.register(errorsetradius), '%P')
explanationresistance = Label(userInterface, text = "▼반지름의를크기를 선택▼", height = 3) 
explanationresistance.pack(padx=4) 



def update_variable(*args):
    global radius_value # global로 선언했으니 다른 곳에서 global radius어쩌고 안 써도 작동 됨 앙기모찌ㅋ
    radius_value = radius_spinbox_var.get()

radius_spinbox_var = IntVar() # 너희 때문에 추가근무하게 됐잖아 ㅡㅡ

# 해결함 해보셈 textvariable로 radius_spinbox_var라고 말 해줬어야 했는데 안함 ㅋㅋ
Circlespinbox = Spinbox(userInterface, width=10, from_=1, to=100, validate = 'all', validatecommand=validate_command, invalidcommand=invalid_command, textvariable=radius_spinbox_var)
Circlespinbox.pack(padx=4) 

radius_spinbox_var.trace('w', update_variable) # 이거 저번에도 떳는데 그냥 되던데 Spinbox 변화 감지/계속 업데이트 해줌(update_variable)
radius_value = radius_spinbox_var.get() # 실행 화면에서 g키 누르면 이거 값 알 수 있음ㅋㅋ(터미널에 뜸) good NihahahaKufufuToriyaShubabababa

# 김창섭,,네가 만든 Worlds, 네가 만든 Characters,Maplestory,
#  Players'cheers,너의 가장 큰 Gloria Haters의 noise, 넌 mute,
#  네 의지는 so strong, 로기견's Just Shadow , 더쿠's Just a spark,
#  너의 fight,Always right Maplestory, 우리 의 인생, Passion, Dream ,
#  네가 만든 Heart We're with you, in every battle, every war,
#  Together we fight,together we renew.




# 앞으로 spinbox 만들 때 각 spinbox의 값 여러 개 받으려면 아래 형식을 이용하시오.. (그런데 이것도 내가 할 것 같은 느낌..)
# spinbox_values = [1spinbox.get(),
#            2spinbox.get(),
#            3spinbox.get(),
#            4spinbox.get(),
#            5spinbox.get()]
# 리스트로 나타냈으니 ^하드코딩^ DlWlFkf말고 잘 해보셈 ㅋㅋ 

# def                                      야심준석코딩하라고



def whileTrue():
    animate()
    tk.after(100, whileTrue)

whileTrue()

tk.mainloop()