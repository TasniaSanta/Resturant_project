from tkinter import *
import random
import time;
import datetime
import tkinter.messagebox

root=Tk()
root.geometry("1550x750+0+0")
root.title("Resturant Management Systems")
root.configure(background="Cadet Blue")

Tops=Frame(root,bg="Cadet Blue",bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=("arial",50,"bold"),text="Resturant Management Systems",bd=21,bg="Cadet Blue",
               fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F=Frame(root,bg="Powder Blue",bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F,bg="Powder Blue",bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F,bg="Powder Blue",bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F,bg="Powder Blue",bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame=Frame(root,bg="Cadet Blue",bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg="powder Blue",bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg="Cadet Blue",bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame,bg="powder Blue",bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame,bg="powder Blue",bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)
#--------------------------Variable-----------------------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

Dateoforder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

text_Input=StringVar()
operator=""

E_Latta=StringVar()
E_Espresso=StringVar()
E_Iced_Latta=StringVar()
E_Vale_Coffee=StringVar()
E_Cappuccino=StringVar()
E_African_Coffee=StringVar()
E_American_Coffee=StringVar()
E_Iced_Cappuccino=StringVar()

E_SchoolCake=StringVar()
E_Sunny_AO_Cake=StringVar()
E_Jonathan_YO_Cake=StringVar()
E_West_African_Cake=StringVar()
E_Lagos_Choclate_Cake=StringVar()
E_Kilburn_Choclate_Cake=StringVar()
E_Carlton_Hill_Cake=StringVar()
E_Queen_Park_Cake=StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

E_SchoolCake.set("0")
E_Sunny_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Lagos_Choclate_Cake.set("0")
E_Kilburn_Choclate_Cake.set("0")
E_Carlton_Hill_Cake.set("0")
E_Queen_Park_Cake.set("0")

Dateoforder.set(time.strftime("%d/%m/%Y"))
#-----------------------------exit confirmation-------------------------
def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Resturant System","Confirm if u want to exit")
    if iExit>0:
        root.destroy()
        return
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_SchoolCake.set("0")
    E_Sunny_AO_Cake.set("0")
    E_Jonathan_YO_Cake.set("0")
    E_West_African_Cake.set("0")
    E_Lagos_Choclate_Cake.set("0")
    E_Kilburn_Choclate_Cake.set("0")
    E_Carlton_Hill_Cake.set("0")
    E_Queen_Park_Cake.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    txtLatta.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latta.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtSchoolCake.configure(state=DISABLED)
    txtSunny_AO_Cake.configure(state=DISABLED)
    txtJonathan_YO_Cake.configure(state=DISABLED)
    txtWest_African_Cake.configure(state=DISABLED)
    txtLagos_Choclate_Cake.configure(state=DISABLED)
    txtKilburn_Choclate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Cake.configure(state=DISABLED)
    txtQueen_Park_Cake.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())

    Item9=float(E_SchoolCake.get())
    Item10=float(E_Sunny_AO_Cake.get())
    Item11=float(E_Jonathan_YO_Cake.get())
    Item12=float(E_West_African_Cake.get())
    Item13=float(E_Lagos_Choclate_Cake.get())
    Item14=float(E_Kilburn_Choclate_Cake.get())
    Item15=float(E_Carlton_Hill_Cake.get())
    Item16=float(E_Queen_Park_Cake.get())

    PriceofDrinks=(Item1*1.2)+(Item2*1.99)+(Item3*2.05)+(Item4*1.89)+(Item5*1.99)\
        +(Item6*2.99)+(Item7*2.39)+(Item8*1.29)
    
    PriceofCakes=(Item9*1.35)+(Item10*2.2)+(Item11*1.99)+(Item12*1.49)+(Item13*1.8)\
        +(Item14*1.67)+(Item15*1.6)+(Item16*1.99)
    DrinksPrice="€",str("%.2f"%(PriceofDrinks))
    CakesPrice="€",str("%.2f"%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="€",str("%.2f"%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS="€",str("%.2f"%(PriceofDrinks+PriceofCakes+1.59))
    SubTotal.set(SubTotalofITEMS)

    #Tax="£",str("%.2f"%(PriceofDrinks+PriceofCakes+1.59)*0.15)
    Tax = "€" + str("%.2f" % ((PriceofDrinks + PriceofCakes + 1.59) * 0.15))

    PaidTax.set(Tax)
    TT=((PriceofDrinks+PriceofCakes+1.59)*0.15)
    TC="€",str("%.2f"%(PriceofDrinks+PriceofCakes+1.59+TT))
    TotalCost.set(TC)
    

def chkLatta():
    if (var1.get()==1):
        txtLatta.configure(state=NORMAL)
        txtLatta.focus()
        txtLatta.delete("0",END)
        E_Latta.set("")
    elif(var1.get()==0):
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")

def chkEspresso():
    if (var2.get()==1):
        txtEspresso.configure(state=NORMAL)
        txtEspresso.focus()
        E_Espresso.set("")
    elif(var2.get()==0):
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
def chkIced_Latta():
    if (var3.get()==1):
        txtIced_Latta.configure(state=NORMAL)
        txtIced_Latta.delete("0",END)
        txtIced_Latta.focus()
    elif(var3.get()==0):
        txtIced_Latta.configure(state=DISABLED)
        E_Iced_Latta.set("0")        
def chkVale_coffee():
    if (var4.get()==1):
        txtVale_Coffee.configure(state=NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete(0,END)
    elif(var4.get()==0):
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
def chkCappucino():
    if (var5.get()==1):
        txtCappuccino.configure(state=NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete("0",END)
    elif(var5.get()==0):
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")  

def chkAfrican_coffee():
    if (var6.get()==1):
        txtAfrican_Coffee.configure(state=NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete("0",END)
    elif(var6.get()==0):
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
def chkAmerican_coffee():
    if (var7.get()==1):
        txtAmerican_Coffee.configure(state=NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete("0",END)
    elif(var7.get()==0):
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")
def chkIced_Cappucino():
    if (var8.get()==1):
        txtIced_Cappuccino.configure(state=NORMAL)
        txtIced_Cappuccino.focus()
        txtIced_Cappuccino.delete("0",END)
    elif(var8.get()==0):
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")
def chkSchool_cake():
    if (var9.get()==1):
        txtSchoolCake.configure(state=NORMAL)
        txtSchoolCake.focus()
        txtSchoolCake.delete("0",END)
    elif(var9.get()==0):
        txtSchoolCake.configure(state=DISABLED)
        E_SchoolCake.set("0")
def chkSunny_AO_Cake():
    if (var10.get()==1):
        txtSunny_AO_Cake.configure(state=NORMAL)
        txtSunny_AO_Cake.focus()
        txtSunny_AO_Cake.delete("0",END)
    elif(var10.get()==0):
        txtSunny_AO_Cake.configure(state=DISABLED)
        E_Sunny_AO_Cake.set("0")
def chkJonathan_YO_Cake():
    if (var11.get()==1):
        txtJonathan_YO_Cake.configure(state=NORMAL)
        txtJonathan_YO_Cake.focus()
        txtJonathan_YO_Cake.delete("0",END)
    elif(var11.get()==0):
        txtJonathan_YO_Cake.configure(state=DISABLED)
        E_Jonathan_YO_Cake.set("0")
def chkWest_Africa_Cake():
    if (var12.get()==1):
        txtWest_African_Cake.configure(state=NORMAL)
        txtWest_African_Cake.focus()
        txtWest_African_Cake.delete("0",END)
    elif(var12.get()==0):
        txtWest_African_Cake.configure(state=DISABLED)
        E_West_African_Cake.set("0")
def chkLagos_choclte_Cake():
    if (var13.get()==1):
        txtLagos_Choclate_Cake.configure(state=NORMAL)
        txtLagos_Choclate_Cake.focus()
        txtLagos_Choclate_Cake.delete("0",END)
    elif(var13.get()==0):
        txtLagos_Choclate_Cake.configure(state=DISABLED)
        E_Lagos_Choclate_Cake.set("0")
def chkKilburn_chocolate_Cake():
    if (var14.get()==1):
        txtKilburn_Choclate_Cake.configure(state=NORMAL)
        txtKilburn_Choclate_Cake.focus()
        txtKilburn_Choclate_Cake.delete("0",END)
    elif(var14.get()==0):
        txtKilburn_Choclate_Cake.configure(state=DISABLED)
        E_Kilburn_Choclate_Cake.set("0")

def chkCarlton_Hill_Cake():
    if (var15.get()==1):
        txtCarlton_Hill_Cake.configure(state=NORMAL)
        txtCarlton_Hill_Cake.focus()
        txtCarlton_Hill_Cake.delete("0",END)
    elif(var15.get()==0):
        txtCarlton_Hill_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Cake.set("0")


def chkQueen_park_Cake():
    if (var16.get()==1):
        txtQueen_Park_Cake.configure(state=NORMAL)
        txtQueen_Park_Cake.focus()
        txtQueen_Park_Cake.delete("0",END)
    elif(var16.get()==0):
        txtQueen_Park_Cake.configure(state=DISABLED)
        E_Queen_Park_Cake.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    X=random.randint(10903,609235)
    randomRef=str(X)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t" + Receipt_Ref.get()+"\t"+Dateoforder.get()+"\n")
    txtReceipt.insert(END,"Item:\t\t" + "Cost of Items\n")
    txtReceipt.insert(END,"Latta:\t\t" + E_Latta.get()+"\n")
    txtReceipt.insert(END,"Espresso:\t\t" + E_Espresso.get()+"\n")
    txtReceipt.insert(END,"Iced Latta:\t\t" + E_Iced_Latta.get()+"\n")
    txtReceipt.insert(END,"Vale Coffee:\t\t" + E_Vale_Coffee.get()+"\n")
    txtReceipt.insert(END,"Cappuccino:\t\t" + E_Cappuccino.get()+"\n")
    txtReceipt.insert(END,"African Coffee:\t\t" + E_African_Coffee.get()+"\n")
    txtReceipt.insert(END,"American Coffee:\t\t" + E_American_Coffee.get()+"\n")
    txtReceipt.insert(END,"Iced Cappuccino :\t\t" + E_Iced_Cappuccino.get()+"\n")
    txtReceipt.insert(END,"School Cake:\t\t" + E_SchoolCake.get()+"\n")
    txtReceipt.insert(END,"Sunny AO Cake:\t\t" + E_Sunny_AO_Cake.get()+"\n")
    txtReceipt.insert(END,"Jonathan YO Cake:\t\t" + E_Jonathan_YO_Cake.get()+"\n")
    txtReceipt.insert(END,"West African Cak:\t\t" + E_West_African_Cake.get()+"\n")
    txtReceipt.insert(END,"Lagos Choclate Cake:\t\t" + E_Lagos_Choclate_Cake.get()+"\n")
    txtReceipt.insert(END,"Kilburn Choclate Cake:\t\t" + E_Kilburn_Choclate_Cake.get()+"\n")
    txtReceipt.insert(END,"Carlton Hill Cake:\t\t" + E_Carlton_Hill_Cake.get()+"\n")
    txtReceipt.insert(END,"Queen Park Cake:\t\t" + E_Queen_Park_Cake.get()+"\n")
    txtReceipt.insert(END,"Cost of Drinks:\t\t" + CostofDrinks.get()+"\nTax paid:\t\t"+PaidTax.get()+"\n")
    txtReceipt.insert(END,"Cost of Cakes:\t\t" + CostofCakes.get()+"\nSubTotal:\t\t"+str(SubTotal.get()+"\n"))
    txtReceipt.insert(END,"Service Charge:\t\t" + ServiceCharge.get()+"\nTotal Cost:\t\t"+str(TotalCost.get()+"\n"))

#------------------------------------------------Drinks------------------#
Latta=Checkbutton(Drinks_F,text="Latta",variable=var1,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkLatta).grid(row=0,sticky=W)
Espresso=Checkbutton(Drinks_F,text="Espresso",variable=var2,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkEspresso).grid(row=1,sticky=W)
Iced_Latta=Checkbutton(Drinks_F,text="Iced_Latta",variable=var3,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkIced_Latta).grid(row=2,sticky=W)
Vale_Coffee=Checkbutton(Drinks_F,text="Vale Coffee",variable=var4,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkVale_coffee).grid(row=3,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text="Cappuccino",variable=var5,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkCappucino).grid(row=4,sticky=W)
African_Coffee=Checkbutton(Drinks_F,text="African Coffee",variable=var6,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkAfrican_coffee).grid(row=5,sticky=W)
American_Coffee=Checkbutton(Drinks_F,text="American Coffee",variable=var7,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkAmerican_coffee).grid(row=6,sticky=W)
Iced_Cappuccino=Checkbutton(Drinks_F,text="Iced Cappuccino",variable=var8,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="powder Blue",command=chkIced_Cappucino).grid(row=7,sticky=W)
#------------------------------------------------Entry box for drinks------------------#
txtLatta=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Latta,bd=8,width=6,justify=LEFT,state=DISABLED)
txtLatta.grid(row=0,column=1)

txtEspresso=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Espresso,bd=8,width=6,justify=LEFT,state=DISABLED)
txtEspresso.grid(row=1,column=1)

txtIced_Latta=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Iced_Latta,bd=8,width=6,justify=LEFT,state=DISABLED)
txtIced_Latta.grid(row=2,column=1)

txtVale_Coffee=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Vale_Coffee,bd=8,width=6,justify=LEFT,state=DISABLED)
txtVale_Coffee.grid(row=3,column=1)

txtCappuccino=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Cappuccino,bd=8,width=6,justify=LEFT,state=DISABLED)
txtCappuccino.grid(row=4,column=1)

txtAfrican_Coffee=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_African_Coffee,bd=8,width=6,justify=LEFT,state=DISABLED)
txtAfrican_Coffee.grid(row=5,column=1)

txtAmerican_Coffee=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_American_Coffee,bd=8,width=6,justify=LEFT,state=DISABLED)
txtAmerican_Coffee.grid(row=6,column=1)

txtIced_Cappuccino=Entry(Drinks_F,font=("arial",16,"bold"),textvariable=E_Iced_Cappuccino,bd=8,width=6,justify=LEFT,state=DISABLED)
txtIced_Cappuccino.grid(row=7,column=1)

#-------------------------------cakes--------------------------------------------------#
SchoolCake=Checkbutton(Cake_F,text="School Cake",variable=var9,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkSchool_cake).grid(row=0,sticky=W)
Sunny_AO_Cake=Checkbutton(Cake_F,text="Sunny O Cake",variable=var10,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkSunny_AO_Cake).grid(row=1,sticky=W)
Jonathan_YO_Cake=Checkbutton(Cake_F,text="Jonathan O Cake",variable=var11,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkJonathan_YO_Cake).grid(row=2,sticky=W)
West_African_Cake=Checkbutton(Cake_F,text="West African Cake",variable=var12,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkWest_Africa_Cake).grid(row=3,sticky=W)
Lagos_Choclate_Cake=Checkbutton(Cake_F,text="Lagos Choclate Cake",variable=var13,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkLagos_choclte_Cake).grid(row=4,sticky=W)
Kilburn_Choclate_Cake=Checkbutton(Cake_F,text="Kilburn Choclate Cake",variable=var14,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkKilburn_chocolate_Cake).grid(row=5,sticky=W)
Carlton_Hill_Cake=Checkbutton(Cake_F,text="Carlton Hill Cake",variable=var15,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkCarlton_Hill_Cake).grid(row=6,sticky=W)
Queen_Park_Cake=Checkbutton(Cake_F,text="Queen Park Cake",variable=var16,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="powder Blue",command=chkQueen_park_Cake).grid(row=7,sticky=W)

#------------------------------------------------Entry box for Cakes------------------#
txtSchoolCake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                    state=DISABLED,textvariable=E_SchoolCake)
txtSchoolCake.grid(row=0,column=1)

txtSunny_AO_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                       state=DISABLED,textvariable=E_Sunny_AO_Cake)
txtSunny_AO_Cake.grid(row=1,column=1)

txtJonathan_YO_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                          state=DISABLED,textvariable=E_Jonathan_YO_Cake)
txtJonathan_YO_Cake.grid(row=2,column=1)

txtWest_African_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                           state=DISABLED,textvariable=E_West_African_Cake)
txtWest_African_Cake.grid(row=3,column=1)

txtLagos_Choclate_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                             state=DISABLED,textvariable=E_Lagos_Choclate_Cake)
txtLagos_Choclate_Cake.grid(row=4,column=1)

txtKilburn_Choclate_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                               state=DISABLED,textvariable=E_Kilburn_Choclate_Cake)
txtKilburn_Choclate_Cake.grid(row=5,column=1)

txtCarlton_Hill_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                           state=DISABLED,textvariable=E_Carlton_Hill_Cake)
txtCarlton_Hill_Cake.grid(row=6,column=1)

txtQueen_Park_Cake=Entry(Cake_F,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,
                         state=DISABLED,textvariable=E_Queen_Park_Cake)
txtQueen_Park_Cake.grid(row=7,column=1)
#-------------------------Total cost--------------------------------#
lblCostofDrinks=Label(Cost_F,font=("arial",14,"bold"),text="Cost of Drinks",bg="powder Blue",fg="black")
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,font=("arial",14,"bold"),textvariable=CostofDrinks,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes=Label(Cost_F,font=("arial",14,"bold"),text="Cost of Cakes",bg="powder Blue",fg="black")
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes=Entry(Cost_F,font=("arial",14,"bold"),textvariable=CostofCakes,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=("arial",14,"bold"),text="Service Charge",bg="powder Blue",fg="black")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,font=("arial",14,"bold"),textvariable=ServiceCharge,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

#----------------------------------Payment Information---------------------------#
lblPaidTax=Label(Cost_F,font=("arial",14,"bold"),text="Paid Tax",bd=7,bg="powder Blue",fg="black")
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,font=("arial",14,"bold"),textvariable=PaidTax,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=("arial",14,"bold"),text="Sub Total",bd=7,bg="powder Blue",fg="black")
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,font=("arial",14,"bold"),textvariable=SubTotal,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=("arial",14,"bold"),text="Total Cost",bd=7,bg="powder Blue",fg="black")
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,font=("arial",14,"bold"),textvariable=TotalCost,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)
#---------------------------------------------Receipt-------------------------------------------#
txtReceipt=Text(Receipt_F,width=46,height=12,bg="white",bd=4,font=("arial",12,"bold"))
txtReceipt.grid(row=0,column=0)
#-----------------------------------Buttons----------------------#
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Total",
                bg="powder blue",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Receipt",
                bg="powder blue",command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Reset",
                bg="powder blue",command=Reset)#.grid(row=0,column=2)
btnReset.grid(row=0, column=2)

btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Exit",
                bg="powder blue",command=iExit ).grid(row=0,column=3)
#-------------------------------Calculator Display-----------------------------
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    Sumup=str(eval(operator))
    text_Input.set(Sumup)
    operator=""
    
txtDisplay=Entry(Cal_F,width=45,bg="white",bd=4,font=("arial",12,"bold"),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#----------------------------------- calculator Buttons----------------------#
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="7",
                bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="8",
                bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="9",
                bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="+",
                bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)
#----------------------------------- calculator Buttons----------------------#
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="4"
               ,command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="5"
                ,command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="6"
                ,command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="-",
                bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)
#----------------------------------- calculator Buttons----------------------#
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="1"
                ,command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="2"
                ,command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="3"
                ,command=lambda:btnClick(3)).grid(row=4,column=2)
btnMul=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="*",
                bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)
#----------------------------------- calculator Buttons----------------------#
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="0",
                bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="C",
                bg="powder blue",command=btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="=",
                bg="powder blue",command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="/",
                bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)
root.mainloop()