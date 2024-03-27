import secrets
from tkinter import Tk, Frame, Label, Entry, Checkbutton, Button, Text, StringVar, IntVar, END, DISABLED, NORMAL,RIDGE,CENTER,TOP,BOTTOM,RIGHT,LEFT,W
import random
import time;
import datetime
import tkinter.messagebox
# Initialize Tkinter
root=Tk()
root.geometry("1550x750+0+0")
root.title("Resturant Management Systems")
root.configure(background="#5F9EA0")

Tops=Frame(root,bg="#5F9EA0",bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=("arial",50,"bold"),text="Resturant Management Systems",bd=21,bg="#5F9EA0",
               fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F=Frame(root,bg="#B0E0E6",bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F,bg="#B0E0E6",bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F,bg="#B0E0E6",bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F,bg="#B0E0E6",bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame=Frame(root,bg="#5F9EA0",bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg="#B0E0E6",bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg="#5F9EA0",bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame,bg="#B0E0E6",bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame,bg="#B0E0E6",bd=10,relief=RIDGE)
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
  
def exit_application():
    exit_confirmation = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if exit_confirmation:
        root.destroy()
# Define a function to reset all the fields
def reset_values():
    # Reset all variables and entry fields
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    # Reset other variables here...
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

# Define a function to calculate the cost of items
def calculate_costs():
    # Calculate cost of drinks and cakes here...
    item_latta=float(E_Latta.get())
    item_espresso=float(E_Espresso.get())
    item_iced_latta=float(E_Iced_Latta.get())
    item_vale_coffee=float(E_Vale_Coffee.get())
    item_cappuccino=float(E_Cappuccino.get())
    item_african_coffee=float(E_African_Coffee.get())
    item_american_coffee=float(E_American_Coffee.get())
    item_iced_cappuccino=float(E_Iced_Cappuccino.get())

    item_school_cake=float(E_SchoolCake.get())
    item_sunny_ao_cake=float(E_Sunny_AO_Cake.get())
    item_jonathan_yo_cake=float(E_Jonathan_YO_Cake.get())
    item_west_african_cake=float(E_West_African_Cake.get())
    item_lagos_chocolate_cake=float(E_Lagos_Choclate_Cake.get())
    item_kilburn_chocolate_cake=float(E_Kilburn_Choclate_Cake.get())
    item_carlton_hill_cake=float(E_Carlton_Hill_Cake.get())
    item_queen_park_cake=float(E_Queen_Park_Cake.get())

    price_of_drinks=(item_latta*1.2)+(item_espresso*1.99)+(item_iced_latta*2.05)+(item_vale_coffee*1.89)+(item_cappuccino*1.99)\
        +(item_african_coffee*2.99)+(item_american_coffee*2.39)+(item_iced_cappuccino*1.29)
    
    price_of_cakes=(item_school_cake*1.35)+(item_sunny_ao_cake*2.2)+(item_jonathan_yo_cake*1.99)+(item_west_african_cake*1.49)+(item_lagos_chocolate_cake*1.8)\
        +(item_kilburn_chocolate_cake*1.67)+(item_carlton_hill_cake*1.6)+(item_queen_park_cake*1.99)
    drinks_price="€",str("%.2f"%(price_of_drinks))
    cakes_price="€",str("%.2f"%(price_of_cakes))
    CostofCakes.set(cakes_price)
    CostofDrinks.set(drinks_price)
    SC="€",str("%.2f"%(1.59))
    ServiceCharge.set(SC)

    subtotal_items="€",str("%.2f"%(price_of_drinks+price_of_cakes+1.59))
    SubTotal.set(subtotal_items)
    tax = "€" + str("%.2f" % ((price_of_drinks + price_of_cakes + 1.59) * 0.15))
    PaidTax.set(tax)
    TT=((price_of_drinks+price_of_cakes+1.59)*0.15)
    TC="€",str("%.2f"%(price_of_drinks+price_of_cakes+1.59+TT))
    TotalCost.set(TC)
    

def check_latta():
    if var1.get()==1:
        txtLatta.configure(state=NORMAL)
        txtLatta.focus()
        txtLatta.delete("0",END)
        E_Latta.set("")
    elif var1.get()==0:
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")

def check_espresso():
    if var2.get()==1:
        txtEspresso.configure(state=NORMAL)
        txtEspresso.focus()
        E_Espresso.set("")
    elif var2.get()==0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
def check_iced_latta():
    if var3.get()==1:
        txtIced_Latta.configure(state=NORMAL)
        txtIced_Latta.delete("0",END)
        txtIced_Latta.focus()
    elif var3.get()==0:
        txtIced_Latta.configure(state=DISABLED)
        E_Iced_Latta.set("0")        
def check_vale_coffee():
    if var4.get()==1:
        txtVale_Coffee.configure(state=NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete(0,END)
    elif var4.get()==0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
def check_cappucino():
    if var5.get()==1:
        txtCappuccino.configure(state=NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete("0",END)
    elif var5.get()==0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")  

def check_african_coffee():
    if var6.get()==1:
        txtAfrican_Coffee.configure(state=NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete("0",END)
    elif var6.get()==0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
def check_american_coffee():
    if var7.get()==1:
        txtAmerican_Coffee.configure(state=NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete("0",END)
    elif var7.get()==0:
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")
def check_iced_cappucino():
    if var8.get()==1:
        txtIced_Cappuccino.configure(state=NORMAL)
        txtIced_Cappuccino.focus()
        txtIced_Cappuccino.delete("0",END)
    elif var8.get()==0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")
def check_school_cake():
    if var9.get()==1:
        txtSchoolCake.configure(state=NORMAL)
        txtSchoolCake.focus()
        txtSchoolCake.delete("0",END)
    elif var9.get()==0:
        txtSchoolCake.configure(state=DISABLED)
        E_SchoolCake.set("0")
def check_sunny_ao_cake():
    if var10.get()==1:
        txtSunny_AO_Cake.configure(state=NORMAL)
        txtSunny_AO_Cake.focus()
        txtSunny_AO_Cake.delete("0",END)
    elif var10.get()==0:
        txtSunny_AO_Cake.configure(state=DISABLED)
        E_Sunny_AO_Cake.set("0")
def check_jonathan_yo_cake():
    if var11.get()==1:
        txtJonathan_YO_Cake.configure(state=NORMAL)
        txtJonathan_YO_Cake.focus()
        txtJonathan_YO_Cake.delete("0",END)
    elif var11.get()==0:
        txtJonathan_YO_Cake.configure(state=DISABLED)
        E_Jonathan_YO_Cake.set("0")
def check_west_africa_cake():
    if var12.get()==1:
        txtWest_African_Cake.configure(state=NORMAL)
        txtWest_African_Cake.focus()
        txtWest_African_Cake.delete("0",END)
    elif var12.get()==0:
        txtWest_African_Cake.configure(state=DISABLED)
        E_West_African_Cake.set("0")
def check_lagos_choclte_cake():
    if var13.get()==1:
        txtLagos_Choclate_Cake.configure(state=NORMAL)
        txtLagos_Choclate_Cake.focus()
        txtLagos_Choclate_Cake.delete("0",END)
    elif var13.get()==0:
        txtLagos_Choclate_Cake.configure(state=DISABLED)
        E_Lagos_Choclate_Cake.set("0")
def check_kilburn_chocolate_cake():
    if var14.get()==1:
        txtKilburn_Choclate_Cake.configure(state=NORMAL)
        txtKilburn_Choclate_Cake.focus()
        txtKilburn_Choclate_Cake.delete("0",END)
    elif var14.get()==0:
        txtKilburn_Choclate_Cake.configure(state=DISABLED)
        E_Kilburn_Choclate_Cake.set("0")

def check_carlton_hill_cake():
    if var15.get()==1:
        txtCarlton_Hill_Cake.configure(state=NORMAL)
        txtCarlton_Hill_Cake.focus()
        txtCarlton_Hill_Cake.delete("0",END)
    elif var15.get()==0:
        txtCarlton_Hill_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Cake.set("0")

def check_queen_park_cake():
    if var16.get()==1:
        txtQueen_Park_Cake.configure(state=NORMAL)
        txtQueen_Park_Cake.focus()
        txtQueen_Park_Cake.delete("0",END)
    elif var16.get()==0:
        txtQueen_Park_Cake.configure(state=DISABLED)
        E_Queen_Park_Cake.set("0")

def generate_receipt_reference():
    #Generate a cryptographically secure random reference number for the receipt
    return "BILL" + str(secrets.randbelow(609235 - 10903) + 10903)

def Receipt():
    #Generate and display a receipt with a random reference number.
    txtReceipt.delete("1.0", END)
    random_ref = generate_receipt_reference()
    Receipt_Ref.set(random_ref)

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
                  bg="#B0E0E6",command=check_latta).grid(row=0,sticky=W)
Espresso=Checkbutton(Drinks_F,text="Espresso",variable=var2,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_espresso).grid(row=1,sticky=W)
Iced_Latta=Checkbutton(Drinks_F,text="Iced_Latta",variable=var3,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_iced_latta).grid(row=2,sticky=W)
Vale_Coffee=Checkbutton(Drinks_F,text="Vale Coffee",variable=var4,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_vale_coffee).grid(row=3,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text="Cappuccino",variable=var5,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_cappucino).grid(row=4,sticky=W)
African_Coffee=Checkbutton(Drinks_F,text="African Coffee",variable=var6,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_african_coffee).grid(row=5,sticky=W)
American_Coffee=Checkbutton(Drinks_F,text="American Coffee",variable=var7,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_american_coffee).grid(row=6,sticky=W)
Iced_Cappuccino=Checkbutton(Drinks_F,text="Iced Cappuccino",variable=var8,onvalue=1,offvalue=0,font=("arial",18,"bold"),
                  bg="#B0E0E6",command=check_iced_cappucino).grid(row=7,sticky=W)
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
                  bg="#B0E0E6",command=check_school_cake).grid(row=0,sticky=W)
Sunny_AO_Cake=Checkbutton(Cake_F,text="Sunny O Cake",variable=var10,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_sunny_ao_cake).grid(row=1,sticky=W)
Jonathan_YO_Cake=Checkbutton(Cake_F,text="Jonathan O Cake",variable=var11,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_jonathan_yo_cake).grid(row=2,sticky=W)
West_African_Cake=Checkbutton(Cake_F,text="West African Cake",variable=var12,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_west_africa_cake).grid(row=3,sticky=W)
Lagos_Choclate_Cake=Checkbutton(Cake_F,text="Lagos Choclate Cake",variable=var13,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_lagos_choclte_cake).grid(row=4,sticky=W)
Kilburn_Choclate_Cake=Checkbutton(Cake_F,text="Kilburn Choclate Cake",variable=var14,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_kilburn_chocolate_cake).grid(row=5,sticky=W)
Carlton_Hill_Cake=Checkbutton(Cake_F,text="Carlton Hill Cake",variable=var15,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_carlton_hill_cake).grid(row=6,sticky=W)
Queen_Park_Cake=Checkbutton(Cake_F,text="Queen Park Cake",variable=var16,onvalue=1,offvalue=0,font=("arial",16,"bold"),
                  bg="#B0E0E6",command=check_queen_park_cake).grid(row=7,sticky=W)

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
lblCostofDrinks=Label(Cost_F,font=("arial",14,"bold"),text="Cost of Drinks",bg="#B0E0E6",fg="black")
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,font=("arial",14,"bold"),textvariable=CostofDrinks,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes=Label(Cost_F,font=("arial",14,"bold"),text="Cost of Cakes",bg="#B0E0E6",fg="black")
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes=Entry(Cost_F,font=("arial",14,"bold"),textvariable=CostofCakes,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=("arial",14,"bold"),text="Service Charge",bg="#B0E0E6",fg="black")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,font=("arial",14,"bold"),textvariable=ServiceCharge,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

#----------------------------------Payment Information---------------------------#
lblPaidTax=Label(Cost_F,font=("arial",14,"bold"),text="Paid Tax",bd=7,bg="#B0E0E6",fg="black")
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,font=("arial",14,"bold"),textvariable=PaidTax,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=("arial",14,"bold"),text="Sub Total",bd=7,bg="#B0E0E6",fg="black")
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,font=("arial",14,"bold"),textvariable=SubTotal,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=("arial",14,"bold"),text="Total Cost",bd=7,bg="#B0E0E6",fg="black")
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,font=("arial",14,"bold"),textvariable=TotalCost,bd=7,bg="white",
                         insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)
#---------------------------------------------Receipt-------------------------------------------#
txtReceipt=Text(Receipt_F,width=46,height=12,bg="white",bd=4,font=("arial",12,"bold"))
txtReceipt.grid(row=0,column=0)
#-----------------------------------Buttons----------------------#
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Total",
                bg="#B0E0E6",command=calculate_costs).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Receipt",
                bg="#B0E0E6",command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Reset",
                bg="#B0E0E6",command=reset_values)#.grid(row=0,column=2)
btnReset.grid(row=0, column=2)

btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="Exit",
                bg="#B0E0E6",command=exit_application ).grid(row=0,column=3)
#-------------------------------Calculator Display-----------------------------
def btn_click(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btn_clear():
    global operator
    operator = ""
    text_Input.set("")

def btn_equals():
    global operator
    sum_up=str(eval(operator))
    text_Input.set(sum_up)
    operator=""
    
txtDisplay=Entry(Cal_F,width=45,bg="white",bd=4,font=("arial",12,"bold"),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#----------------------------------- calculator Buttons----------------------#
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="7",
                bg="#B0E0E6",command=lambda:btn_click(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="8",
                bg="#B0E0E6",command=lambda:btn_click(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="9",
                bg="#B0E0E6",command=lambda:btn_click(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="+",
                bg="#B0E0E6",command=lambda:btn_click("+")).grid(row=2,column=3)
#----------------------------------- calculator Buttons----------------------#
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="4"
               ,command=lambda:btn_click(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="5"
                ,command=lambda:btn_click(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="6"
                ,command=lambda:btn_click(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="-",
                bg="#B0E0E6",command=lambda:btn_click("-")).grid(row=3,column=3)
#----------------------------------- calculator Buttons----------------------#
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="1"
                ,command=lambda:btn_click(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="2"
                ,command=lambda:btn_click(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="3"
                ,command=lambda:btn_click(3)).grid(row=4,column=2)
btnMul=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="*",
                bg="#B0E0E6",command=lambda:btn_click("*")).grid(row=4,column=3)
#----------------------------------- calculator Buttons----------------------#
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="0",
                bg="#B0E0E6",command=lambda:btn_click(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="C",
                bg="#B0E0E6",command=btn_clear).grid(row=5,column=1)
btnEquals=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="=",
                bg="#B0E0E6",command=btn_equals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="/",
                bg="#B0E0E6",command=lambda:btn_click("/")).grid(row=5,column=3)
# Run the Tkinter event loop
root.mainloop()
