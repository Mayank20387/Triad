import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="system28")
 con2=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="system23")
 con4=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="system23");
 con5=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="system23");
import tkinter
from tkinter import messagebox
from tkinter import *
def detail():
      m=tkinter.Tk()
      m.configure(background="green")
      m.geometry("600x500")
      m.title("FIND YOUR IDEAL HOTEL")
      r=tkinter.Label(m,text="DETAILS",font=("Calibri",30,"bold"),bg='yellow')
      L=tkinter.Label(m,text="(FORM TO BE FILLED IN CAPITAL LETTERS)",font=("Calibri",15,"bold"),bg="green")
      r.place(x=220,y=0)
      na=StringVar()
      ea=StringVar()
      pw=StringVar()
      ph=StringVar()
      perma=IntVar()
      t1=tkinter.Label(m,text="ENTER YOUR NAME:",font=("Calibri",16,"bold"),bg='pink')
      t2=tkinter.Label(m,text="ENTER YOUR EMAIL ADDESS:",font=("Calibri",16,"bold"),bg='pink')
      t3=tkinter.Label(m,text="ENTERYOUR PASSWORD:",font=("Calibri",16,"bold"),bg='pink')
      t4=tkinter.Label(m,text="PHONE NO.:",font=("Calibri",16,"bold"),bg='pink')
      e=tkinter.Button(m,text="GO AHEAD",command=lambda:triv(),font=("Lucida Sans",16),bg='pink')
      e2=Checkbutton(m,text="PERMANENT",variable=perma,width=15)
      L.place(x=130,y=50)
      t1.place(x=50,y=100)
      t2.place(x=50,y=145)
      t3.place(x=50,y=190)
      t4.place(x=50,y=230)
      e.place(x=210,y=310)
      e2.place(x=210,y=270)
      l1=tkinter.Entry(m,textvariable=na,font=("Calibri",16,"bold"))
      l3=tkinter.Entry(m,textvariable=pw,font=("Calibri",16,"bold"))
      l2=tkinter.Entry(m,textvariable=ea,font=("Calibri",16,"bold"))
      l4=tkinter.Entry(m,textvariable=ph,font=("Calibri",16,"bold"))
      l1.place(x=320,y=100)
      l2.place(x=320,y=145)
      l3.place(x=320,y=190)
      l4.place(x=320,y=230)
      def get1():
            cursor1=con.cursor()
            g1=t1.get()
            g2=t2.get()
            g3=t3.get()
            g4=t4.get()
            print("\t\t\tDETAILS OF CUTSOMER")
            print("\t\t      (Form to be filled in capital letter)")
            sql="insert into customer values(' "+g1+" ',' "+g2+" ',' "+g3+" ',' "+str(g4)+" ')"
            cursor1.execute(sql)
            con.commit()
            cursor1.execute("select * from customer")
            record=cursor1.fetchall()
            print("\t  CUSTOMERNAME","\t  EMAIL","\t   PASSWORD","\t  PHONENO")
            for i in record:
                 print("\t  ",i[0],"\t         ",         i[1],"\t    ",i[2],"\t  ",i[3])
            z=perma.get()
            if z>=1:
                  messagebox.showinfo("CUSTOMER DATA","SORRY!PLEASE TRY AGAIN ")
            else:
                  messagebox.showinfo("CUSTOMER DATA","DATA ENTERED SUCCESSFULLY")
            cursor1.close()
            button5=tkinter.Button(r,text="SUBMIT",bg="orange", command=get1,font=("arial black",20,"bold"))
            button5.place(x=175,y=300)
N=tkinter.Tk()
N.geometry("500x500")
N.configure(background="cyan")
m1=tkinter.Label(N,text="!!!!!!!SMARTTRAVEL!!!!!!",bg="cyan",font=("arial black",20,"bold","underline")  )
a=tkinter.Label(N,text ="FIND YOUR IDEAL HOTEL",bg="pink",font=("algerian",17,"bold"))
b=tkinter.Label(N,text ="WITH",bg="pink",font=("algerian",17,"bold"))
c=tkinter.Label (N,text="*THE SUITABLE PRICES* ",bg="pink" ,font =("algerian",17,"bold")) 
d=tkinter.Label(N,text="BOOKNOW.....",bg="cyan",font=("algerian",17,"bold"))
e=tkinter.Label(N,text="BOOKTOMORROW.....",bg="cyan",font=("algerian",17,"bold"))
f=tkinter.Label(N,text="BOOKTODAY.....",bg="cyan",font=("algerian",17,"bold"))
but=tkinter.Button(N,text="EXPLORE",bg="pink",command=lambda:detail(),font=("arial black",15,"bold","underline"))
m1.place(x=100,y=0)
a.place(x=105,y=55)
b.place(x=205,y=88)
c.place(x=105,y=123)
d.place(x=125,y=165)
e.place(x=125,y=200)
f.place(x=125,y=234)
but.place(x=180,y=300)

def triv():
      co="y"
      while co=="y" or co=="Y":
            print("\t","*"*60)
            print("\t\t\t            SMART TRAVEL")
            print("\t\t         SOURCE","\t \t DESTINATION")
            print("\t\t         1.DELHI","\t\t(a)DUBAI")
            print("\t\t         2.MUMBAI","\t\t(b)SWITZERLAND")
            print("\t","-"*60)
            p=input("\t\t      ARE YOU A PREVIOUS USER(Y/N)   :")
            sc=input("\t\t      SOURCE CHOICE                  :")
            dc=input("\t\t      DESTINATION CHOICE             :")
            if sc=="DELHI"  and dc=='DUBAI' or dc=='dubai' and sc=="delhi":
                  deldub()
            elif sc=="DELHI"  and dc=='SWITZERLAND'  or sc=="delhi" and dc=="switzerland":
                  delswit1()
            elif sc=="MUMBAI" and  dc=='DUBAI' or dc=='dubai' and sc=="mumbai":
                  mumdub()
            elif sc=="MUMBAI" and  dc=='SWITZERLAND' or dc=='switzerland' and sc=="mumbai":
                  mumswit()
            co=input("DO YOU WANT TO TRY MORE :")
#Delhi toh dubai
def deldub():
      print("\t","*"*60)
      print("\t\t\t      **DELHI TO DUBAI**")
      print("\t","*"*60)
      print("\t\t             ACCOMODATION (TYPES)")
      print("\t\t\t\t(A) 5 STAR")
      print("\t\t\t\t(B) 4 STAR")
      st=input("\t\t\tENTER YOUR CHOICE (A/B)       :")
      if st=='A' or st=="a":
            fivestar()
      if st=='B' or st=="b":
            fourstar()
#5-star
def fivestar():
      d="y"
      while d=="y" or d=="Y":
            print("\t","*"*60)
            print("\t\t\t\t!5-STAR HOTELS!")
            print("\t\t\t1. MANDARIN ORIENTAL JUMEIRA")
            print("\t\t\t2. CORAL BOUTIQUE VILLAS")
            print("\t\t\t3. NOVOTEL ")
            fiv=int(input("\t\t\tENTER YOUR CHOICE (1/2/3)     :"))
            print("\t","*"*60)
            if fiv==1:
                  mandarin()
            elif fiv==2:
                  coral()
            elif fiv==3:
                  novotel()
            d=input("\t\t\t  DO YOU WANT TO CONTINUE (Y/N) :")
            print("\t","*"*60)
def mandarin():
      k,x,y,z,r=0,0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=9800"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
                 print("\t\t\t ",i[0])
                 print("\t\t\t\t   ",i[1])
                 print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
                     print("\t\t\tTRASNPORT FEE                  :",k[2])
                     print("\t\t\tVISA FEE                       :",k[3])
                      print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
       f=a+b
       if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
        else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)

      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = KHUSHI TYAGI")
      print("\t\t\t    SOURCE CHOSEN     = MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-10-2019")
      print("\t\t\t    CHECK-OUT         = 07-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def coral():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=12460"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
       else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = ROHAN SHARMA")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-05-2019")
      print("\t\t\t    CHECK-OUT         = 07-05-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
 def novotel():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=10400"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
     days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
       else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = ABHAY TOMAR")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-10-2019")
      print("\t\t\t    CHECK-OUT         = 07-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
#4-star
def fourstar():
      print("\t","-"*80) 
      d="y"
      while d=="y" or d=="Y": 
            print("\t\t\t         !4-STAR HOTELS!")
            print("\t\t\t      1. FRASER SUITES ")
            print("\t\t\t      2. LANDMARK GRAND ")
            print("\t\t\t      3. GOLDEN TULIP AL BARSHA  ")
            fou=int(input("\t\t\t    ENTER YOUR CHOICE (1/2/3) :"))
            if fou==1:
                  fraser()
            elif fou==2:
                  landmark()
            elif fou==3:
                  tulip()
            d=input("\t\tDO YOU WANT TO CONTINUE (Y/N) :")
            print("*"*60)      
            
def fraser():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=7500"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
     else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = ROHAN TYAGI")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-10-2019")
      print("\t\t\t    CHECK-OUT         = 07-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)


def landmark():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=6800"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
       else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = KHUSHI TYAGI")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-01-2019")
      print("\t\t\t    CHECK-OUT         = 07-01-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def tulip():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=5900"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
       else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = MAYANK KAIM")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 04-10-2019")
      print("\t\t\t    CHECK-OUT         = 10-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
#delhi to switzerland      
def delswit1():
      print("\t","*"*60)
      print("\t\t\t      **DELHI TO SWITZERLAND**")
      print("\t","*"*60)
      print("\t\t             ACCOMODATION (TYPES)")
      print("\t\t\t\t(A) 5 STAR")
      print("\t\t\t\t(B) 4 STAR")
      st1=input("\t\t\tENTER YOUR CHOICE (A/B)       :")
      if st1=='A' or st1=="a":
            fivestar1()
      if st1=='B' or st1=="b":
            fourstar1()
      print("\t","*"*60)

#5-star
def fivestar1():
      d="y"
      while d=="y" or d=="Y":
            print("\t\t!5-STAR HOTELS!")
            print("*"*60)
            print("\t\t1. INTERCONTINENTAL DAVOS")
            print("\t\t2. THE CHEDI ANDERMATT")
            print("\t\t3. ROYAL SAVOY LAUSANNE ")
            print("*"*60)
            fiv1=int(input("\t\tENTER YOUR CHOICE (1/2/3):"))
            if fiv1==1:
                  davos()
            elif fiv1==2:
                  chedi()
            elif fiv1==3:
                  savoy()
            d=input("\t\tDO YOU WANT TO CONTINUE (Y/N) :")
            print("*"*60)      
  def davos():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=9250"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='SWITZERLAND'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
     else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = RAHUL RATORI")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-10-2019")
      print("\t\t\t    CHECK-OUT         = 07-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def chedi():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=10250"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
      else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = KARTIK PANDEY")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 20-10-2019")
      print("\t\t\t    CHECK-OUT         = 27-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def savoy():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=9600"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='SWITZERLAND'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
        else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = SHARVI KHANNA")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-02-2019")
      print("\t\t\t    CHECK-OUT         = 07-02-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
#4-star
def fourstar1():
      print("\t","-"*65)
       d="y"
       while d=="y" or d=="Y":
            print("\t\t\t         !4-STAR HOTELS!")
            print("\t\t\t      1. NOVOTEL LAUSANNE")
            print("\t\t\t      2. EUROTEL MOUTREUX ")
            print("\t\t\t      3. HOTEL CENTURY ")
            fou1=int(input("\t\t\tENTER YOUR CHOICE (1/2/3)     :"))
            if fou1==1:
                  lausanne()
            elif fou1==2:
                  moutreux()
            elif fou1==3:
                  century()
            d=input("\t\t\t DO YOU WANT TO CONTINUE (Y/N) :")
            print("\t","*"*60)
 def lausanne():
      print("\t\t\t     NOVOTEL LAUSANNE")
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=7800"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='SWITZERLAND'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
        else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)

      print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = TANVI RAWAT")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 12-10-2019")
      print("\t\t\t    CHECK-OUT         = 20-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def moutreux():
      print("\t","-"*65)
      print("\t\t\t       EUROTEL MOUTREUX ")
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=6400"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
            print("\t\t",i[0])
            print("\t\t\t",i[1])
            print("\t\t\tPER DAY PRICE        :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='SWITZERLAND'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE        :",k[2])
            print("\t\t\tVISA FEE             :",k[3])
            print("\t\t\tCAB FEE              :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS     :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN   :"))
      r=int(input("\t\t\tROOMS REQUIRED       :"))
      days=int(input("\t\t\tNUMBER OF DAYS      :"))
      print("\t","*"*60) 
      print("\t\t\t    FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t  DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.20
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =ROHAN SHARMA")
      print("\t\t\t    SOURCE CHOSEN     =DELHI")
      print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =15-06-2019")
      print("\t\t\t    CHECK-OUT         =25-06-2019")
      print("\t\t\t    GST               =0.20")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
def century():
      k,x,y,z=0,0,0,0
      cursor1=con.cursor()
      sql="select * from deldub where PER_DAY_PRICE=7000"
      cursor1.execute(sql)
      a=cursor1.fetchall()
      for i in a:
           print("\t\t\t ",i[0])
           print("\t\t\t\t   ",i[1])
           print("\t\t\tPER DAY PRICE                  :",i[2])
      cursor2=con2.cursor()
      sql2="select * from hotel where SOURCE='DELHI'and DESTINATION='SWITZERLAND'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
           print("\t\t\tTRASNPORT FEE                  :",k[2])
           print("\t\t\tVISA FEE                       :",k[3])
           print("\t\t\tCAB FEE                        :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS               :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN             :"))
      days=int(input("\t\t\tENTER THE NUMBER OF DAYS       :"))
      f=a+b
      if f<=2:
            print(" ")
            print("\t\t\t\tYOUR ROOM IS READY")
      else:
            print(" ")
            print("\t\t\tYOU WILL REQUIRE MORE THAN ONE ROOM")
            r=2
            print("\t\t\t\t NUMBER OF ROOM :",r)
     print("\t","*"*60)
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)
      print("\t\t\t         FREE WIFI")
      print("\t\t\t         FREE BREAKFAST ")
      print("\t\t\t         24X ROOM SERVICE")
      print("\t\t\t         SWIMMING POOL & THEATRE")
      print("\t","-"*60)
      ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)    :")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*i[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.18
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     = AYUSHI TYAGI")
      print("\t\t\t    SOURCE CHOSEN     = DELHI")
      print("\t\t\t    DESTINATION CHOSEN= SWITZERLAND")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          = 02-10-2019")
      print("\t\t\t    CHECK-OUT         = 07-10-2019")
      print("\t\t\t    GST               = 0.18")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","-"*60)
#mumbai to dubai

def mumdub():
    cont="Y"
    while cont=="Y"or cont=="y":
        print("\t","*"*60)
        print("\t\t\t       MUMBAI TO DUBAI")
        print("\t","*"*60)
        print("\t\t\t   ACCOMMODATION(All Types)")
        print("\t\t\t         1. 5-STAR HOTEL")
        print("\t\t\t         2. 4-STAR HOTEL")
        ab=int(input("\t\t\t  ENTER YOUR CHOICE(1/2):"))
        if ab==1:
            fistar()
        elif ab==2:
            fostar()
        cont=input("\t\t\t  EXPLORE IT (Y/N):")
        print("\t\t","-"*55)
#5-star
def fistar():
    co="Y"
    while co=="Y" or co=="y":
        print("\t","*"*60)
        print("\t\t\t       5 5-STAR HOTELS")
        print("\t\t\t   (According to your requirement)")
        print("\t","*"*60)    
        print("\t\t\t     1. HOTEL PRIDE PLAZA")
        print("\t\t\t     2. EROS HOTEL")
        print("\t\t\t     3. RADDISON HOTEL")
        print("\t\t                                           ")
        ac=int(input("\t\t\t   HOTEL  TO  CHOOSE(1/2/3):"))
        if ac==1:
            pride()
        elif ac==2:
            eros()
        elif ac==3:
            raddison()
        co=input("\t\t\t        DO YOU WANT TO CONTINUE(Y/N):")
def pride():
    d,e=0,0
    print("\t\t","_"*55)
    print("\t\t\t        !!!!!!HOTEL PRIDE PLAZA!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=10599"
    cursor1.execute(sql)
    records=cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =BVYA SINGH RAWAT")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =20-05-2019")
      print("\t\t\t    CHECK-OUT         =25-05-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()
    
def eros():
    d,e=0,0
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!!EROS  HOTEL  !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=13950"
    cursor1.execute(sql)
    records=cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =PRIYANSHU PATWAAL")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =10-09-2019")
      print("\t\t\t    CHECK-OUT         =20-09-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()

def raddison():
      d,e=0,0
      print("\t","*"*60)
      print("\t\t\t!!!!!!!! HOTEL RADDISON !!!!!!!!")
      print("\t","*"*55)
      cursor1=con4.cursor()
      cursor2=con4.cursor()
      sql="select  * from  MTOD where per_day_price=9700"
      cursor1.execute(sql)
      records= cursor1.fetchall()
      for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =HIMANI KHERWAL")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =01-11-2019")
      print("\t\t\t    CHECK-OUT         =07-11-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()
#4-star            
def fostar():
    co="Y"
    while co=="Y" or co=="y":
        print("\t\t","-"*82)
        print("\t\t\t    4 4-STAR HOTELS")
        print("\t\t\t (According to your requirement)")
        print("\t\t\t         1. HOTEL PALZA ")
        print("\t\t\t         2. IN N OUT HOTEL")
        print("\t\t\t         3. ENCLAVE HOTEL")
        print("\t\t                      ")
        ac=int(input("\t\t\t  HOTEL   TO CHOOSE(1/2/3):"))
        if ac==1:
            plaza()
        elif ac==2:
            innout()
        elif ac==3:
            enclave()
        co=input("\t\t\t  WANT TO EXPLORE MORE HOTELS(Y/N):")
        print("\t\t","*"*55)
def plaza():
    d,e=0,0
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!!HOTEL PLAZA!!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    cursor2=con2.cursor()
    sql="select  * from  MTOD where per_day_price=7800"
    cursor1.execute(sql)
    records= cursor1.fetchall()
     for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =MAHESH SHARMA")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =06-06-2019")
      print("\t\t\t    CHECK-OUT         =07-07-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()
def innout():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! IN N OUT HOTEL !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=9800"
    cursor1.execute(sql)
    records= cursor1.fetchall()
     for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =GEORGE SWEDEN")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =01-03-2019")
      print("\t\t\t    CHECK-OUT         =07-03-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()
def enclave():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! HOTEL ENCLAVE !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=4500"
    cursor1.execute(sql)
    records= cursor1.fetchall()
     for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
      cursor2=con4.cursor()
      sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='DUBAI'"
      cursor2.execute(sql2)
      a2=cursor2.fetchall()
      for k in a2:
            print("\t\t\tTRASNPORT FEE            :",k[2])
            print("\t\t\tVISA FEE                 :",k[3])
            print("\t\t\tCAB FEE                  :",k[4])
      a=int(input("\t\t\tNUMBER OF ADULTS         :"))
      b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
      r=int(input("\t\t\tROOMS REQUIRED           :"))
      days=int(input("\t\t\tNUMBER OF DAYS           :"))
      print("\t","*"*60) 
      print("\t\t\t   FACILITIES TO BE PROVIDED")
      print("\t","-"*60)      
      print("\t\t\t      24X ROOM SERVICE")
      print("\t\t\t      OCEAN VIEW")
      print("\t\t\t      BOAT RENTAL")
      print("\t\t\t      FREE WIFI")
      print("\t\t\t      NIGHT CLUB & BAR")
      print("\t","-"*60)
      ch=input("\t\t\t   DO YOU WANT TO PROCEED(Y/N)")
      if ch=="N" or ch=="n":
            triv()
      else:
            print("\t\t\t\t\t BILL")
            ab=r*days*k[2]
            ab12=(k[2]+k[3]+k[4])*0.05*0.17
            c=ab+ab12
      print("\t\t\t    CUSTOMER NAME     =MANOJ TYAGI")
      print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
      print("\t\t\t    DESTINATION CHOSEN=DUBAI")
      print("\t\t\t    NUMBER OF ADULT   =",a)
      print("\t\t\t    NUMBER OF CHILDREN=",b)
      print("\t\t\t    NUMBER OF DAYS    =",days)
      print("\t\t\t    CHECK-IN          =10-11-2019")
      print("\t\t\t    CHECK-OUT         =27-11-2019")
      print("\t\t\t    GST               =0.17")
      print("\t\t\t    TOTAL AMOUNT      =",c)
      print("\t","*"*60)
      cursor1.close()
      cursor2.close()
#mumbai to switzerland         
def mumswit():
      cont="Y"
      while cont=="Y"or cont=="y":
            print("\t","*"*60)
            print("\t\t\t       MUMBAI TO SWITZERLAND")
            print("\t","*"*60)
            print("\t\t\t   ACCOMMODATION(All Types)")
            print("\t\t\t         1. 5-STAR HOTEL")
            print("\t\t\t         2. 4-STAR HOTEL")
            b=int(input("\t\t\t  ENTER YOUR CHOICE(1/2):"))
            if b==1:
                  fi_ve()
            elif b==2:
                  fo_ur()
      a=input("\t\t\t\t  EXPLORE HOTELS (Y/N):")
      print("\t\t","-"*55)
#5-star
def fi_ve():
    co="Y"
    while co== "Y" or co=="y":
        print("\t\t","-"*82)
        print("\t\t\t         5 5-STAR HOTELS")
        print("\t\t\t   (According to your requirement)")
        print("\t\t\t         1. HOTEL GLORIA")
        print("\t\t\t         2. ARGO HOTEL")
        print("\t\t\t         3. HOTEL EDISSON")
        ac=int(input("\t\t\t   HOTEL  TO CHOOSE(1/2/3):"))
        if ac==1:
            gloria()
        elif ac==2:
            argo()
        elif ac==3:
            ddison()
        co=input("\t\t\t                  DO YOU WANT TO CONTINUE(Y/N)")
def gloria():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! HOTEL GLORIA !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=13000"
    cursor1.execute(sql)
    records= cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    print("\t","-"*60)
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =ISHIKA ARORA")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =21-10-2019")
    print("\t\t\t    CHECK-OUT         =30-10-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","-"*65)
    cursor1.close()
    cursor2.close()
def argo():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! ARGO HOTEL !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=12500"
    cursor1.execute(sql)
    records= cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    print("\t","-"*60)
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =ARTI SINGH")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =02-10-2019")
    print("\t\t\t    CHECK-OUT         =09-10-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","-"*65)
    cursor1.close()
    cursor2.close()
def eddison():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! HOTEL EDDISON !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=10000"
    cursor1.execute(sql)
    records= cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    print("\t","-"*60)
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =TANVI RAWAT")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =19-09-2019")
    print("\t\t\t    CHECK-OUT         =20-09-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","-"*65)
    cursor1.close()
    cursor2.close()
#4-star
def fo_ur():
      print("\t","*"*60)
      co="Y"
      while co=="Y" or co=="y":
            print("\t\t\t     4 4-STAR HOTELS")
            print("\t\t\t (According to your requirement)")
            print("\t\t\t    1.HOTEL PALOMAR")
            print("\t\t\t    2.HOTEL CASINO")
            print("\t\t\t    3.ONE STAR HOTEL")
            ac=int(input("\t\t\t  HOTEL TO CHOOSE(1/2):"))
            if ac==1:
                  palomar()
            elif ac==2:
                  casino()
            elif ac==3:
                  onestar()
      co=input("\t\t\t WANT TO EXPLORE MORE HOTELS(Y/N):")
def palomar():
    print("\t","*"*60)
    print("\t\t\t    !!!!!!!!HOTEL PALOMAR!!!!!!!!")
    print("\t","_"*60)
    cursor1=con4.cursor()
    sql="select  * from  MTOD where per_day_price=7800"
    cursor1.execute(sql)
    records= cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    print("\t","-"*60)
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =ISHAAN AVASTHI")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =21-07-2019")
    print("\t\t\t    CHECK-OUT         =30-07-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","-"*65)
    cursor1.close()
    cursor2.close()
def casino():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!!! HOTEL CASINO !!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=6500"
    cursor1.execute(sql)
    records= cursor1.fetchall
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    print("\t","-"*60)
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =MAHIRA AVASTHI")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =21-07-2019")
    print("\t\t\t    CHECK-OUT         =30-07-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","-"*65)
    cursor1.close()
    cursor2.close()
        
def onestar():
    print("\t\t","_"*55)
    print("\t\t\t\t!!!!!!! ONE-STAR HOTEL!!!!!!!!")
    print("\t\t","_"*55)
    cursor1=con.cursor()
    sql="select  * from  MTOD where per_day_price=8000"
    cursor1.execute(sql)
    records= cursor1.fetchall()
    for i in records:
            print("\t\t\t ",i[0])
            print("\t\t\t\t   ",i[1])
            print("\t\t\tPER DAY PRICE            :",i[2])
    cursor2=con4.cursor()
    sql2="select * from hotel where SOURCE='MUMBAI'and DESTINATION='SWITZERLAND'"
    cursor2.execute(sql2)
    a2=cursor2.fetchall()
    for k in a2:
          print("\t\t\tTRASNPORT FEE            :",k[2])
          print("\t\t\tVISA FEE                 :",k[3])
          print("\t\t\tCAB FEE                  :",k[4])
    a=int(input("\t\t\tNUMBER OF ADULTS         :"))
    b=int(input("\t\t\tNUMBER OF CHILDREN       :"))
    r=int(input("\t\t\tNUMBER OF ROOMS REQUIRED :"))
    days=int(input("\t\t\tENTER THE NUMBER OF DAYS :"))
    print("\t","*"*60) 
    print("\t\t\t   FACILITIES TO BE PROVIDED")
    print("\t","-"*60)      
    print("\t\t\t    24X ROOM SERVICE")
    print("\t\t\t    OCEAN VIEW")
    print("\t\t\t    BOAT RENTAL")
    print("\t\t\t    FREE WIFI")
    print("\t\t\t    NIGHT CLUB & BAR")
    ch=input("\t\t\tDO YOU WANT TO PROCEED(Y/N)")
    if ch=="N" or ch=="n":
          triv()
    else:
          print("\t\t\t\t\t BILL")
          ab=r*days*k[2]
          ab12=(k[2]+k[3]+k[4])*0.05*0.18
          c=ab+ab12
    print("\t\t\t    CUSTOMER NAME     =HINA KHAN")
    print("\t\t\t    SOURCE CHOSEN     =MUMBAI")
    print("\t\t\t    DESTINATION CHOSEN=SWITZERLAND")
    print("\t\t\t    NUMBER OF ADULT   =",a)
    print("\t\t\t    NUMBER OF CHILDREN=",b)
    print("\t\t\t    NUMBER OF DAYS    =",days)
    print("\t\t\t    CHECK-IN          =10-02-2019")
    print("\t\t\t    CHECK-OUT         =20-03-2019")
    print("\t\t\t    GST               =0.18")
    print("\t\t\t    TOTAL AMOUNT      =",c)
    print("\t","*"*60)
    cursor1.close()
    cursor2.close()
