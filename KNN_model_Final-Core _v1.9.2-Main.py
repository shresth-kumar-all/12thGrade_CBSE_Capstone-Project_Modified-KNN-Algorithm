#IMPORTING NECESSARY LIBRARIES:

import pandas as pd
import numpy as np
import tkinter as tk
import customtkinter as  ctk
from PIL import Image,ImageTk

########################################################################################################################################################################################################################################

#NOTES FOR NON-NERDS (IN CAPS):

#TO RUN ON A NEW SYSTEM REPLACE THE FILE PATHS IN THE LIST
#"D" FROM THE SYSTEM THIS ALGORITHM IS RUNNING ON.

#CONVERT ALL THE "\" USED FOR FILE NAVIGATION TO "\\" TO
#PREVENT "FileNotFound Error" FROM ARISING UPON RUNNING THE
#CODE.

#THE NUMBER OF FILE PATHS ENTERED WILL BE THE NUMBER OF
#GENRES.

#THE SOFTWARE WILL BE MADE AN APP USING INSTALLATION WIZARDS.
#WHILE DESIGNING THE UI, ALLOW THE USER TO CHOOSE THE GENRE
#BY MAKING SPCIFIC BUTTONS, OR MORE REALISTICALLY A DROPDOWN
#SHOWING ALL OPTIONS TO THE USER.

########################################################################################################################################################################################################################################

#Input Values:
global V
V=[0,0,0,0,0,0,0,0,0,0,0]

global c
c=0

#UI SEGMENT:
root=tk.Tk()
root.geometry("1200x675")
root.title("53544655")

bg=tk.PhotoImage(file="UI_Assets\\UIBG_F.png")

C1=tk.Canvas(root,width="1200",height="675")
C1.pack()
C1.create_image(0,0,image=bg,anchor="nw")

global inL
inL=0

#A slider is by default 200 pixels long and 15 pixels tall.
def slider(r,X,Y,name):
    Label_num=tk.Label(root,text="0")
    Label_num.place(x=235+X,y=Y-5)

    Label_name=tk.Label(root,text=name,fg="White",bg="#474747")
    Label_name.pack()
    Label_name.place(x=X-25,y=Y-25)

    def slide(value):
        V[r]=int(value)
        Label_num.config(text=f"{int(value)}")
    Slider=ctk.CTkSlider(root,
                     from_=0,
                     to=100,
                     width=235,
                     command=slide)
    Slider.set(0)
    Slider.place(x=X,y=Y)

slider(0,100,100,"Action")
slider(1,100,150,"Fictional")
slider(2,100,200,"Superhero")
slider(3,100,250,"Tragedy")
slider(4,100,300,"Drama")
slider(5,100,350,"Crime")
slider(6,100,400,"Thriller")
slider(7,100,450,"Horror")
slider(8,100,500,"Romance")
slider(9,100,550,"Comedy")
slider(10,100,600,"Sports")

#SELECTING DATASETS:
global G
G=[]
D=["Data\\csvMovies.csv",
   "Data\\csvTVShows.csv",
   "Data\\csvBooks.csv",
   "Data\\csvAnime.csv",
   "Data\\csvComics.csv"]

#BUTTONS ON THE SIDE:
def g0():
    G.clear()
    G.append(0)
    c=0
B_g0=tk.Button(root,
               text="Movies",
               bg="#B8162C",
               fg="White",
               activebackground="#B8162C",
               activeforeground="#11FF00",
               border=0,
               height=3,
               width=8,
               command=g0)
B_g0.pack()
B_g0.place(x=4,y=240)

def g1():
    G.clear()
    G.append(1)
    c=0
B_g1=tk.Button(root,
               text="TV Shows",
               bg="#BA7215",
               fg="White",
               activebackground="#BA7215",
               activeforeground="#0066FF",
               border=0,
               height=3,
               width=8,
               command=g1)
B_g1.pack()
B_g1.place(x=4,y=298)

def g2():
    G.clear()
    G.append(2)
    c=0
B_g2=tk.Button(root,
               text="Books",
               bg="#20B916",
               fg="White",
               activebackground="#20B916",
               activeforeground="#FF0012",
               border=0,
               height=3,
               width=8,
               command=g2)
B_g2.pack()
B_g2.place(x=4,y=355)

def g3():
    G.clear()
    G.append(3)
    c=0
B_g3=tk.Button(root,
               text="Anime",
               bg="#168BB9",
               fg="White",
               activebackground="#168BB9",
               activeforeground="#FF8700",
               border=0,
               height=3,
               width=8,
               command=g3)
B_g3.pack()
B_g3.place(x=4,y=408)

def g4():
    G.clear()
    G.append(4)
    c=0
B_g4=tk.Button(root,
               text="Comics",
               bg="#152FBB",
               fg="White",
               activebackground="#152FBB",
               activeforeground="#FFC900",
               border=0,
               height=3,
               width=8,
               command=g4)
B_g4.pack()
B_g4.place(x=4,y=463)

#counting started from 0 not 1.

########################################################################################################################################################################################################################################

#EXTRACTING NECESSARY FEATURES AND THE TARGET VARIABLE FROM
#SELECTED DATASET AND CONVERTING THEM INTO USEABLE LISTS:

out=""
def showvals():
    print(V)
#Recieving Values:
    in1=V[0]
    in2=V[1]
    in3=V[2]
    in4=V[3]
    in5=V[4]
    in6=V[5]
    in7=V[6]
    in8=V[7]
    in9=V[8]
    in10=V[9]
    in11=V[10]

    data=pd.read_csv(D[G[0]],encoding="latin-1")
    #print(data)

    Action=data["Action"]
    Fictional=data["Fictional"]
    Superhero=data["Superhero"]
    Tragedy=data["Tragedy"]
    Drama=data["Drama"]
    Crime=data["Crime"]
    Thriller=data["Thriller"]
    Horror=data["Horror"]
    Romance=data["Romance"]
    Comedy=data["Comedy"]
    Sports=data["Sports"]
    global Name
    Name=data["Name"]
    #print(Name)

    #print(Action[0]-in1)
    print(V)
    k=len(Name)

############################################################################################################################################################################################################################################

#BACKUP LISTS FOR ALL COMPUTATIONAL WORK:

    DistList=[]
    DLBackup=[]

#CONVERTING TABLE FORMAT TO LIST FORMAT FOR USING LIST
#OPERATIONS ON IT LIKE THE DISTANCE LIST:
    NBackup=list(data["Name"])
    #print(NBackup,len(NBackup))

#USING EUCLIDIAN DISTANCE TO FIND THE DISTANCE BETWEEN THE
#SET OF FEATURES ENTERED BY THE USER TO COMPARE LATER.
#UPDATE DISTANCE FORMULA ACCORDING TO NUMBER OF FEATURES
#IN THE DATA SET:
    for i in range(0,len(Name)):
        Dist=(((Action[i]-in1)**2)+((Fictional[i]-in2)**2)+((Superhero[i]-in3)**2)+((Tragedy[i]-in4)**2)+((Drama[i]-in5)**2)+((Crime[i]-in6)**2)+((Thriller[i]-in7)**2)+((Horror[i]-in8)**2)+((Romance[i]-in9)**2)+((Comedy[i]-in10)**2)+((Sports[i]-in11)**2))**(1/2)
        DistEnter=Dist
        DistList.append(DistEnter)
        DLBackup.append(DistEnter)

    #print(DLBackup,len(DLBackup))

############################################################################################################################################################################################################################################

#FINDING OUT THE "k" CLOSEST VALUES FORM THE DISTANCES
#CALCULATED FROM THE ENTERED DATA POINT:

    Kneighbours_Dist=[]

    for j in range(0,k):
        kn_min=min(DistList, key=lambda l:np.float16(l))
        Kneighbours_Dist.append(kn_min)
        DistList.remove(kn_min)
        #print(Kneighbours_Dist)

############################################################################################################################################################################################################################################

#COMPARING THE MIN. DISTANCES WITH THEIR CORRESPONDING NAMES
#IN THE LIST OF NAMES AND STORING THEM IN A SINGLE LIST, THE
#THE LIST HAS DECENDING ORDER OF SIMILARITY TO THE GIVEN DATA
#POINT BY THE USER:
    global Kneighbours_Names
    Kneighbours_Names=[]
    key1=0
    n=len(DLBackup)-1
    minus=2

    while key1 < k:
        C1=Kneighbours_Dist[key1]
        #print(C1)
        C2=DLBackup[n]
        #print(C2)
        if C1 == C2:
            Kneighbours_Names.append(NBackup[n])
            DLBackup.pop(n)
            NBackup.pop(n)
            #print(n)
            n=len(Name)-minus
            minus+=1
            key1+=1

        else:
            n-=1
    
    global control_0, control_1, control_2, control_3
    control_0=c
    control_1=c+1
    control_2=c+2
    control_3=c+3
    #print(control_0,control_1,control_2,control_3)

    global current_image00, L1
    img00 = Image.open(f"UI_Assets\\{G[0]}\\{Kneighbours_Names[control_0]}.PNG")
    current_image00 = ImageTk.PhotoImage(img00)
    L1.config(image=current_image00)
    L2.config(text=f"{Kneighbours_Names[control_0]}")

    global current_image01, L3
    img01 = Image.open(f"UI_Assets\\{G[0]}\\{Kneighbours_Names[control_1]}.PNG")
    current_image01 = ImageTk.PhotoImage(img01)
    L3.config(image=current_image01)
    L4.config(text=f"{Kneighbours_Names[control_1]}")

    global current_image10, L5
    img10 = Image.open(f"UI_Assets\\{G[0]}\\{Kneighbours_Names[control_2]}.PNG")
    current_image10 = ImageTk.PhotoImage(img10)
    L5.config(image=current_image10)
    L6.config(text=f"{Kneighbours_Names[control_2]}")

    global current_image11, L7
    img11 = Image.open(f"UI_Assets\\{G[0]}\\{Kneighbours_Names[control_3]}.PNG")
    current_image11 = ImageTk.PhotoImage(img11)
    L7.config(image=current_image11)
    L8.config(text=f"{Kneighbours_Names[control_3]}")

    B_prev["state"]=tk.NORMAL
    B_next["state"]=tk.NORMAL

####################################################################################################################################################################################################################################################

def prev_():
    global c
    if c-4<0:
        c=0
        showvals()

    else:
        c-=4
        showvals()
    #print(c)
        
B_prev=tk.Button(root,text="Prev",bg="red",command=prev_)
B_prev.pack()
B_prev.place(x=400,y=500)
B_prev["state"]=tk.DISABLED

def next_():
    global c
    if c+8>len(Name):
        c=len(Name)-5
        showvals()

    else:
        c+=4
        showvals()
    #print(c)
        
B_next=tk.Button(root,text="Next",bg="Blue",command=next_)
B_next.pack()
B_next.place(x=400,y=300)
B_next["state"]=tk.DISABLED

####################################################################################################################################################################################################################################################

current_image00 = None
current_image01 = None
current_image10 = None
current_image11= None

img1 = Image.open("UI_Assets\\Inactive.PNG")
img_out1 = ImageTk.PhotoImage(img1)
L1 = tk.Label(root, image=img_out1)
L1.pack()
L1.place(x=506,y=91)

L2 = tk.Label(root, text="")
L2.pack()
L2.place(x=506,y=345)

img2 = Image.open("UI_Assets\\Inactive.PNG")
img_out2 = ImageTk.PhotoImage(img2)
L3 = tk.Label(root, image=img_out2)
L3.pack()
L3.place(x=846,y=91)

L4 = tk.Label(root, text="")
L4.pack()
L4.place(x=846,y=345)

img3 = Image.open("UI_Assets\\Inactive.PNG")
img_out3 = ImageTk.PhotoImage(img3)
L5 = tk.Label(root, image=img_out3)
L5.pack()
L5.place(x=506,y=379)

L6 = tk.Label(root, text="")
L6.pack()
L6.place(x=506,y=633)

img4 = Image.open("UI_Assets\\Inactive.PNG")
img_out4 = ImageTk.PhotoImage(img4)
L7 = tk.Label(root, image=img_out4)
L7.pack()
L7.place(x=846,y=379)

L8 = tk.Label(root, text="")
L8.pack()
L8.place(x=846,y=633)

########################################################################################################################################################################################################################################

runKNN=tk.Button(root,text="Search",command=showvals)
runKNN.place(x=190,y=640)

########################################################################################################################################################################################################################################

#SUGGESTING THE OUTCOMES TO THE USER:

print(out)
print("v1.9.2")
#print("Model STFU")

#SUSTAINING THE WINDOW:

root.resizable(width="False",height="False")
root.mainloop()
