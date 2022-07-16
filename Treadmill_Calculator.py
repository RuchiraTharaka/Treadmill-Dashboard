from tkinter import*
from tkinter.ttk import Combobox
root=Tk()
'''root.geometry("991x366")'''
root.title("TREADMILL CALCULATOR")
import time
from datetime import datetime

counter = 66600
running = False

def counter_label(label,ent1,label1,ent2,label2,ent3,label3,label4,label5):
    def count():
        if running:
            global counter,distance,calories,steps,losti
            try:
                label5['text']=''
                weight=float(ent1.get())
                height=float(ent2.get())
                speed=float(ent3.get())
                aw = c1.get()
                al = c2.get()
                av = c3.get()
                ass = c5.get()
                if aw=="g":  weight=weight/1000
                elif aw=="lb":   weight=weight/2.20462262185

                if al == "cm":  height = height / 100
                elif al == "in":    height = height / 39.37007874
                elif al == "ft":    height = height / 3.28084

                if av == "km/h":     speed=speed*5/18

                if height<=0 or weight<=0 or speed<=0:
                    a=float("For error handling purpose.")

                slops = {"-5%":[0.0251,0.2157,0.7888,1.2957],"-4%":[0.0244,0.2079,0.8053,1.3281],"-3%":[0.0237,0.2000,0.8217,1.3605],
                         "-2%":[0.0230,0.1922,0.8382,1.3929],"-1%":[0.0222,0.1844,0.8526,1.4253],"0%":[0.0215,0.1765,0.8710,1.4577],
                         "1%":[0.0171,0.1062,0.6080,1.8600],"2%":[0.0184,0.1134,0.6566,1.9200],"3%":[0.0196,0.1205,0.7053,1.9800],
                         "4%":[0.0208,0.1277,0.7539,2.0400],"5%":[0.0221,0.1349,0.8025,2.1000]}

                if counter == 66600:
                    display = " Starting... "
                    distance='0000'
                    distance1='0000'
                    steps='0000'
                    steps1='0000'
                    calories1='0000'
                    calories='0000'
                    losti1='0000'
                    losti='0000'
                else:
                    tt = datetime.fromtimestamp(counter)
                    string = tt.strftime("%H : %M : %S")
                    list1=string.split(" : ")
                    distance=float(distance)+(speed/4)
                    steps=float(steps)+((speed/4)/(height*0.414))
                    s=speed/5*18
                    xx=(((slops[ass][0])*(s**3))-((slops[ass][1])*(s**2))+((slops[ass][2])*s)+(slops[ass][3]))*weight*1/14400
                    calories=float(calories)+xx
                    losti=float(losti)+(xx/ (3500 / 0.453592) * 1000)
                    distance1=round(distance,1)
                    steps1=int(steps)
                    calories1='%.2f'%(round(calories,2))
                    losti1=round(losti,2)
                    display = string
                label1['text']=str(distance1)+" m"
                label2['text'] = str(steps1)
                label3['text'] = str(calories1) + " cal"
                label4['text'] = str(losti1) + " g"
                label['text'] = display
                label.after(250, count)
                counter += 0.25
            except:
                try:
                    tt = datetime.fromtimestamp(counter)
                    string = tt.strftime("%H : %M : %S")
                    display = string
                    if display=="00 : 00 : 00" :
                        label['text'],label1['text'],label2['text'],label3['text'],label4['text'],label5['text']="00 : 00 : 00","0000 m","0000","0000 cal","0000 g","Unable to start. Errors are detecting in inputs."
                    else:
                        label5['text'] = "Errors are detecting in inputs."
                        label1['text'],label2['text']=str(round(distance,1))+" m",str(int(steps))
                        label3['text'],label4['text']=str('%.2f'%round(calories,2))+" cal",str(round(losti,2))+" g"
                        label['text']=display
                        label.after(250, count)
                        counter += 0.25
                except:
                    label5['text'] = "Unable to start. Errors are detecting in inputs."


    count()

def calculate(ent,label,ent1,label1,ent2,label2,ent3,label3,label4,label5):
    try:
        label5['text']=''
        t=float(ent.get())
        weight = float(ent1.get())
        height = float(ent2.get())
        speed = float(ent3.get())
        aw = c1.get()
        al = c2.get()
        av = c3.get()
        at = c4.get()
        ass = c5.get()
        if aw == "g":
            weight = weight / 1000
        elif aw == "lb":
            weight = weight / 2.20462262185

        if al == "cm":
            height = height / 100
        elif al == "in":
            height = height / 39.37007874
        elif al == "ft":
            height = height / 3.28084

        if av == "km/h":     speed = speed * 5 / 18

        if at == "min":     t=t*60
        elif at == "h":     t=t*3600

        if height <= 0 or weight <= 0 or speed <= 0 or t<=0:
            a = float("For error handling purpose.")

        slops = {"-5%":[0.0251,0.2157,0.7888,1.2957],"-4%":[0.0244,0.2079,0.8053,1.3281],"-3%": [0.0237, 0.2000, 0.8217, 1.3605],
                 "-2%":[0.0230,0.1922,0.8382,1.3929],"-1%":[0.0222,0.1844,0.8526,1.4253],"0%":[0.0215,0.1765,0.8710,1.4577],
                 "1%":[0.0171,0.1062,0.6080,1.8600],"2%":[0.0184,0.1134,0.6566,1.9200],"3%":[0.0196,0.1205,0.7053,1.9800],
                 "4%":[0.0208,0.1277,0.7539,2.0400],"5%":[0.0221,0.1349,0.8025,2.1000]}

        dis=t*speed
        step=dis/(height*0.414)
        s=speed*18/5
        calo=((((slops[ass][0])*(s**3))-((slops[ass][1])*(s**2))+((slops[ass][2])*s)+(slops[ass][3]))*weight*(t/3600))
        min = t // 60
        sec = t % 60
        hours = min // 60
        min = min % 60
        lost=calo / (3500 / 0.453592) * 1000
        label['text'] = ("00"+str(int(hours)))[-2:]+' : '+("00"+str(int(min)))[-2:]+' : '+("00"+str(int(sec)))[-2:]
        label1['text'] = str(round(dis,1)) + " m"
        label2['text'] = str(int(step))
        label3['text'] = str('%.2f'%(round(calo,2))) + " cal"
        label4['text'] = str(round(lost,2))+ " g"
    except:
        label['text'],label1['text'],label2['text'],label3['text'],label4['text'],label5['text']="00 : 00 : 00","0000 m","0000","0000 cal","0000 g","Errors are detecting in inputs."

def start(label,ent1,label1,ent2,label2,ent3,label3,label4,label5):
    global running
    running=True
    counter_label(label,ent1,label1,ent2,label2,ent3,label3,label4,label5)
    b1['state']='disabled'
    b2['state']='normal'
    b3['state']='normal'
    b4['state'] = 'disabled'

def stop():
    global running
    b1['state']='normal'
    b2['state']='disabled'
    b3['state']='normal'
    running = False

def reset(label,label1,label2,label3,label4,label5):
    global counter
    counter = 66600
    if running == False:
        b3['state'] = 'disabled'
        label['text'] = '00 : 00 : 00'
        label1['text'] = '0000 m'
        label2['text'] = '0000'
        label3['text'] = '0000 cal'
        label4['text'] = '0000 g'
        b4['state'] = 'normal'
        label5['text'] = ''
    else:
        label['text'] = ' Starting... '
        label5['text'] = ''

def selected(event):
    l22['text']=c5.get()

def cleardata(ent1,ent2,ent3,ent4,label1):
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    label1['text']=''
    c1.set(u1[0])
    c2.set(u2[0])
    c3.set(u2[1])
    c4.set(u4[1])
    c5.set(u5[5])


f1=LabelFrame(root,bg='aquamarine3',pady=20)
f1.grid(row=1,column=0,columnspan=2)
f2=LabelFrame(root,bg='aquamarine3',pady=20)
f2.grid(row=1,column=2)
f3=LabelFrame(root,bg='aquamarine3',pady=20)
f3.grid(row=1,column=3)
f6=LabelFrame(root,bg='aquamarine3',pady=20)
f6.grid(row=1,column=4)
f4=LabelFrame(root,bg='aquamarine3',pady=15)
f4.grid(row=2,column=1,columnspan=4)
f5=LabelFrame(root,bg='midnight blue',padx=10,pady=0)
f5.grid(row=0,column=0,columnspan=5)
f7=LabelFrame(root,bg='aquamarine3',pady=0)
f7.grid(row=2,column=0)

l1=Label(f1,text="WEIGHT",padx=75,pady=10,bg='aquamarine3',fg='DarkSlateGray1',font='Mangal 20').grid(row=0,column=0,columnspan=2)
l2=Label(f2,text="HEIGHT",padx=80,pady=10,bg='aquamarine3',fg='DarkSlateGray1',font='Mangal 20').grid(row=0,column=0,columnspan=2)
l3=Label(f3,text="SPEED",padx=80,pady=10,bg='aquamarine3',fg='DarkSlateGray1',font='Mangal 20').grid(row=0,column=0,columnspan=2)
l21=Label(f6,text="SLOP",padx=58,pady=10,bg='aquamarine3',fg='DarkSlateGray1',font='Mangal 20').grid(row=0,column=0)
l4=Label(f4,text="      TIME",padx=35,pady=10,bg='aquamarine3',fg='DarkSlateGray1',font='Mangal 20').grid(row=0,column=0,rowspan=2)
l5=Label(f5,text="STOPWATCH",bg='midnight blue',fg='cornflower blue',padx=45,font='AIGDT 12 bold')
l5.grid(row=0,column=0)
l6=Label(f4,text='or',padx=45,pady=10,bg='aquamarine3',fg='aquamarine',font='Mangal 15').grid(row=0,column=4,rowspan=2)
l7=Label(f5,text="   DISTANCE   ",bg='midnight blue',fg='cornflower blue',font='AIGDT 12 bold').grid(row=0,column=2)
l8=Label(f5,text="  STEPS  ",bg='midnight blue',fg='cornflower blue',font='AIGDT 12 bold').grid(row=0,column=4)
l9=Label(f5,text=' CALORIES LOST ',bg='midnight blue',fg='cornflower blue',font='AIGDT 12 bold').grid(row=0,column=6)
l18=Label(f5,text=" WEIGHT LOST ",bg='midnight blue',fg='cornflower blue',font='AIGDT 12 bold').grid(row=0,column=8)
l10=Label(f5,text="|",font='AMGDT 60',bg='midnight blue',fg='cornflower blue').grid(row=0,column=1,rowspan=2)
l11=Label(f5,text="|",font='AMGDT 60',bg='midnight blue',fg='cornflower blue').grid(row=0,column=3,rowspan=2)
l12=Label(f5,text="|",font='AMGDT 60',bg='midnight blue',fg='cornflower blue').grid(row=0,column=5,rowspan=2)
l19=Label(f5,text="|",font='AMGDT 60',bg='midnight blue',fg='cornflower blue').grid(row=0,column=7,rowspan=2)
l13=Label(f5,text="00 : 00 : 00",bg='midnight blue',fg='white',font='Leelawadee 30')
l13.grid(row=1,column=0)
l14=Label(f5,text="0000 m",bg='midnight blue',fg='white',font='Leelawadee 25')
l14.grid(row=1,column=2)
l15=Label(f5,text="0000",bg='midnight blue',fg='white',font='Leelawadee 25')
l15.grid(row=1,column=4)
l16=Label(f5,text="0000 cal",bg='midnight blue',fg='white',font='Leelawadee 25')
l16.grid(row=1,column=6)
l20=Label(f5,text="0000 g",bg='midnight blue',fg='white',font='Leelawadee 25')
l20.grid(row=1,column=8)
l22=Label(f4,text='',padx=75,bg='aquamarine3').grid(row=1,column=6)
l23=Label(f4,text='',pady=0,bg='aquamarine3',fg='red',font='Arial 10')
l23.grid(row=2,column=0,columnspan=7)

e1=Entry(f1,bg='aquamarine4',fg='white')
e1.grid(row=1,column=0)
e2=Entry(f2,bg='aquamarine4',fg='white')
e2.grid(row=1,column=0)
e3=Entry(f3,bg='aquamarine4',fg='white')
e3.grid(row=1,column=0)
e4=Entry(f4,bg='aquamarine4',fg='white')
e4.grid(row=0,column=5)

u1=["kg","g","lb"]
u2=["m","cm","in","ft"]
u3=["km/h","m/s"]
u4=["s","min","h"]
u5=["5%","4%","3%","2%","1%","0%","-1%","-2%","-3%","-4%","-5%"]

c1=StringVar()
c1.set(u1[0])
c2=StringVar()
c2.set(u2[0])
c3=StringVar()
c3.set(u3[1])
c4=StringVar()
c4.set(u4[1])
c5=StringVar()
c5.set(u5[5])

cl1=OptionMenu(f1,c1,*u1)
cl1.grid(row=1,column=1)
cl2=OptionMenu(f2,c2,*u2)
cl2.grid(row=1,column=1)
cl3=OptionMenu(f3,c3,*u3)
cl3.grid(row=1,column=1)
cl5=OptionMenu(f6,c5,*u5)
cl5.grid(row=1,column=0)
cl4=OptionMenu(f4,c4,*u4)
cl4.grid(row=0,column=6)

b1=Button(f4,text="START",bg='medium blue',fg='deep sky blue',padx=10,pady=0,font='Leelawadee 15 bold',command=lambda :start(l13,e1,l14,e2,l15,e3,l16,l20,l23))
b1.grid(row=0,column=1,rowspan=2)
b2=Button(f4,text="STOP",bg='medium blue',fg='deep sky blue',padx=10,pady=0,font='Leelawadee 15 bold',state='disabled',command=stop)
b2.grid(row=0,column=2,rowspan=2)
b3=Button(f4,text="RESET",bg='medium blue',fg='deep sky blue',padx=10,pady=0,font='Leelawadee 15 bold',state='disabled',command=lambda :reset(l13,l14,l15,l16,l20,l23))
b3.grid(row=0,column=3,rowspan=2)
b4=Button(f4,text="CALCULATE",bg='medium blue',fg='deep sky blue',padx=10,pady=0,font='Leelawadee 15 bold',command=lambda :calculate(e4,l13,e1,l14,e2,l15,e3,l16,l20,l23))
b4.grid(row=1,column=5)
b5=Button(f7,text='''CLEAR
DATA''',bg='midnight blue',fg='deep sky blue',padx=0,pady=28,font='Leelawadee 15 bold',command=lambda :cleardata(e1,e2,e3,e4,l23))
b5.grid(row=0,column=0,rowspan=2)

root.mainloop()
