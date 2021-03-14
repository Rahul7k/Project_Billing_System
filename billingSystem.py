from tkinter import*
import math, random, os
from tkinter import messagebox
class billingApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing Software",bd=5,relief=RIDGE,bg="navy",fg="mistyrose",font=("arial",30,"bold"),pady=2).pack(fill=X)


        #===============Variables===============================#
        #----------Starters--------------#
        self.starter1 = IntVar()
        self.starter2 = IntVar()
        self.starter3 = IntVar()
        self.starter4 = IntVar()
        self.starter5 = IntVar()
        self.starter6 = IntVar()

        #----------Main Course------------#
        self.main1 = IntVar()
        self.main2 = IntVar()
        self.main3 = IntVar()
        self.main4 = IntVar()
        self.main5 = IntVar()
        self.main6 = IntVar()

        #----------dessert---------------#
        self.dessert1 = IntVar()
        self.dessert2 = IntVar()
        self.dessert3 = IntVar()
        self.dessert4 = IntVar()
        self.dessert5 = IntVar()
        self.dessert6 = IntVar()

        #--------------Total Product Price & Tax Variables--------#
        self.starter_price = StringVar()
        self.main_price = StringVar()
        self.dessert_price = StringVar()

        self.starter_tax = StringVar()
        self.main_tax = StringVar()
        self.dessert_tax = StringVar()

        #------------Customer------------------#
        self.c_name = StringVar()
        self.c_phone = StringVar() 
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()






        #-------Customer Details Frame--------#
        F1=LabelFrame(self.root,text="Customer Details",bd=5,relief=GROOVE ,font=("arial",15,"bold"),bg="steelblue",fg="navy")        #F=frame
        F1.place(x=0,y=70,relwidth=1)

        cname_label = Label(F1,text="Customer Name",font=("arial",16,"bold"),bg="steelblue",fg="mistyrose").grid(row=0,column=0,padx=20,pady=5)            #cname=Customer Name
        cname_text = Entry(F1,textvariable=self.c_name ,width=15,font=("arial",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label = Label(F1,text="Mobile No",font=("arial",16,"bold"),bg="steelblue",fg="mistyrose").grid(row=0,column=2,padx=20,pady=5)            #cphone=Customer Phone
        cphone_text = Entry(F1,textvariable=self.c_phone ,width=15,font=("arial",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_label = Label(F1,text="Bill Number",font=("arial",16,"bold"),bg="steelblue",fg="mistyrose").grid(row=0,column=4,padx=20,pady=5)            #cname=Customer Name
        cbill_text = Entry(F1,textvariable=self.search_bill ,width=15,font=("arial",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill ,width=10,bd=7,font=("arial",12,"bold"),relief=RAISED,activebackground="steelblue",activeforeground="mistyrose").grid(row=0,column=6,padx=10,pady=10)

        #-------Starters Frame--------#
        F2 = LabelFrame(self.root,bd=5,text="Starters",relief=GROOVE ,font=("arial",15,"bold"),bg="steelblue",fg="navy")
        F2.place(x=5,y=170,width=325,height=380)

        mtikka_label=Label(F2, text="Mushroom Tikka", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        mtikka_txt=Entry(F2,textvariable=self.starter1 ,width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        ptikka_label=Label(F2, text="Paneer Tikka", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ptikka_txt=Entry(F2,textvariable=self.starter2, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        mchaap_label=Label(F2, text="Malai Chaap", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        mchaap_txt=Entry(F2, textvariable=self.starter3, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        clollipop_label=Label(F2, text="Chicken Lollipop", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        clollipop_txt=Entry(F2, textvariable=self.starter4, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        achicken_label=Label(F2, text="Afghani Chicken", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        achicken_txt=Entry(F2, textvariable=self.starter5, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        ffry_label=Label(F2, text="Fish Fry", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        ffry_txt=Entry(F2, textvariable=self.starter6, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        

        #-------Main Course Frame--------#
        F3 = LabelFrame(self.root,bd=5,text="Main Course",relief=GROOVE ,font=("arial",15,"bold"),bg="steelblue",fg="navy")
        F3.place(x=340,y=170,width=325,height=380)

        spaneer_label=Label(F3, text="Shahi Paneer", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        spaneer_txt=Entry(F3, textvariable=self.main1, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)

        amattar_label=Label(F3, text="Aloo Mattar", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        amattar_txt=Entry(F3, textvariable=self.main2, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)

        dmakhani_label=Label(F3, text="Dal Makhani", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        dmakhani_txt=Entry(F3, textvariable=self.main3, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        bchicken_label=Label(F3, text="Butter Chicken", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=3, column=2, padx=10, pady=10, sticky="w")
        bchicken_txt=Entry(F3, textvariable=self.main4, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=3, padx=10, pady=10)

        hchicken_label=Label(F3, text="Handi Chicken", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=4, column=2, padx=10, pady=10, sticky="w")
        hchicken_txt=Entry(F3, textvariable=self.main5, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=3, padx=10, pady=10)

        ecurry_label=Label(F3, text="Egg Curry", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=5, column=2, padx=10, pady=10, sticky="w")
        ecurry_txt=Entry(F3, textvariable=self.main6, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=3, padx=10, pady=10)

        #-------Dessert Frame--------#
        F4 = LabelFrame(self.root,bd=5,text="Desserts",relief=GROOVE ,font=("arial",15,"bold"),bg="steelblue",fg="navy")
        F4.place(x=670,y=170,width=325,height=380)

        gjamun_label=Label(F4, text="Gulab Jamun", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=0, column=4, padx=10, pady=10, sticky="w")
        gjamun_txt=Entry(F4, textvariable=self.dessert1, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=10)

        rabri_label=Label(F4, text="Rabri", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=1, column=4, padx=10, pady=10, sticky="w")
        rabri_txt=Entry(F4, textvariable=self.dessert2, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=5, padx=10, pady=10)

        rmalai_label=Label(F4, text="Rasmalai", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=2, column=4, padx=10, pady=10, sticky="w")
        rmalai_txt=Entry(F4, textvariable=self.dessert3, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=5, padx=10, pady=10)

        mdhalwa_label=Label(F4, text="Moong Dal Halwa", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=3, column=4, padx=10, pady=10, sticky="w")
        mdhalwa_txt=Entry(F4, textvariable=self.dessert4, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=5, padx=10, pady=10)

        icecream_label=Label(F4, text="Icecream", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=4, column=4, padx=10, pady=10, sticky="w")
        icecream_txt=Entry(F4, textvariable=self.dessert5, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=5, padx=10, pady=10)

        cdrink_label=Label(F4, text="Cold Drink", font=("arial",12,"bold"), bg= "steelblue", fg="mistyrose").grid(row=5, column=4, padx=10, pady=10, sticky="w")
        cdrink_txt=Entry(F4, textvariable=self.dessert6, width=10, font=("arial",12,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=5, padx=10, pady=10)


        #-------Bill Area Frame--------#
        F5 = Frame(self.root,bd=5,relief=GROOVE)
        F5.place(x=1005,y=170,width=340,height=380)
        bill_title=Label(F5, text="Bill Area", font=("arial",15,"bold"), bd=5, relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5, orient=VERTICAL)
        self.textarea=Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        #----------------Button Frame---------------#
        F6 = LabelFrame(self.root,bd=5,text="Bill Menu",relief=GROOVE ,font=("arial",15,"bold"),bg="steelblue",fg="navy")
        F6.place(x=0,y=555,relwidth=1,height=160)
        m1_label=Label(F6, text="Total Starters Price",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=0,column=0,padx=20,pady=7,sticky="w")
        m1_txt=Entry(F6, textvariable=self.starter_price, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_label=Label(F6, text="Total Main Course Price",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=1,column=0,padx=20,pady=7,sticky="w")
        m2_txt=Entry(F6,textvariable=self.main_price, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_label=Label(F6, text="Total Desserts Price",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=2,column=0,padx=20,pady=7,sticky="w")
        m3_txt=Entry(F6,textvariable=self.dessert_price, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_label=Label(F6, text="Starters Tax",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=0,column=2,padx=20,pady=7,sticky="w")
        c1_txt=Entry(F6,textvariable=self.starter_tax, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_label=Label(F6, text="Main Course Tax",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=1,column=2,padx=20,pady=7,sticky="w")
        c2_txt=Entry(F6,textvariable=self.main_tax, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_label=Label(F6, text="Desserts Tax",font=("arial",12,"bold"),bg="steelblue", fg="mistyrose").grid(row=2,column=2,padx=20,pady=7,sticky="w")
        c3_txt=Entry(F6,textvariable=self.dessert_tax, width=10,font=("arial",12,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_F=Frame(F6, bd=7, relief=GROOVE, bg="steelblue")
        btn_F.place(x=730, y=10, width=600, height=90)

        total_btn=Button(btn_F, command=self.total, text="Total", bg="mistyrose", fg="black", pady=15, relief=RAISED, bd=4, width=12, font=("arial",12,"bold")).grid(row=0,column=0, padx=5, pady=5)
        gbill_btn=Button(btn_F, command=self.bill_area, text="Generate Bill", bg="mistyrose", fg="black", pady=15, relief=RAISED, bd=4, width=12, font=("arial",12,"bold")).grid(row=0,column=1, padx=5, pady=5)
        clear_btn=Button(btn_F, text="Clear",command=self.clear_data, bg="mistyrose", fg="black", pady=15, relief=RAISED, bd=4, width=12, font=("arial",12,"bold")).grid(row=0,column=2, padx=5, pady=5)
        exit_btn=Button(btn_F, text="Exit",command=self.exit_app, bg="mistyrose", fg="black", pady=15, relief=RAISED, bd=4, width=12, font=("arial",12,"bold")).grid(row=0,column=3, padx=5, pady=5)
        self.welcome_bill()


    #==============Bill Calculations===============#
    def total(self):
        self.star1=self.starter1.get()*80
        self.star2=self.starter2.get()*120
        self.star3=self.starter3.get()*160
        self.star4=self.starter4.get()*90
        self.star5=self.starter5.get()*150
        self.star6=self.starter6.get()*180

        self.total_starter_price = float(
                                        self.star1+
                                        self.star2+
                                        self.star3+
                                        self.star4+
                                        self.star5+
                                        self.star6
                                        )
        self.starter_price.set("Rs "+str(self.total_starter_price))
        self.st_tax=round((self.total_starter_price*0.05),2)
        self.starter_tax.set("Rs "+str(self.st_tax))      #--Tax % (0.05 --> 5% tax)----- 2 is upto 2 decimal point---# 


        self.maincourse1=self.main1.get()*180
        self.maincourse2=self.main2.get()*220
        self.maincourse3=self.main3.get()*260
        self.maincourse4=self.main4.get()*220
        self.maincourse5=self.main5.get()*280
        self.maincourse6=self.main6.get()*160

        self.total_main_price = float(
                                    self.maincourse1+
                                    self.maincourse2+
                                    self.maincourse3+
                                    self.maincourse4+
                                    self.maincourse5+
                                    self.maincourse6
                                    )
        self.main_price.set("Rs "+str(self.total_main_price))
        self.ma_tax=round((self.total_main_price*0.08),2)
        self.main_tax.set("Rs "+str(self.ma_tax))      #--Tax % (0.08 --> 8% tax)--#



        self.dess1=self.dessert1.get()*25
        self.dess2=self.dessert2.get()*50
        self.dess3=self.dessert3.get()*60
        self.dess4=self.dessert4.get()*80
        self.dess5=self.dessert5.get()*40
        self.dess6=self.dessert6.get()*35

        self.total_dessert_price = float(
                                        self.dess1+
                                        self.dess2+
                                        self.dess3+
                                        self.dess4+
                                        self.dess5+
                                        self.dess6
                                        )
        self.dessert_price.set("Rs "+str(self.total_dessert_price))
        self.de_tax=round((self.total_dessert_price*0.05),2)
        self.dessert_tax.set("Rs "+str(self.de_tax))      #--Tax % (0.05  --> 5% tax)--#

        self.total_bill=float(  self.total_starter_price+
                                self.total_main_price+
                                self.total_dessert_price+
                                self.st_tax+
                                self.ma_tax+
                                self.de_tax
                            )

        #==========Bill Area===============#

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWelcome to Billing System\n")
        self.textarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n======================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Message", "Please enter the Customer Details")
        elif self.starter_price.get()=="Rs 0.0" and self.main_price.get()=="Rs 0.0" and self.dessert_price.get()=="Rs 0.0" :
            messagebox.showerror("Message", "No Product Selected")
        else:
            self.welcome_bill()
            #========Starter===========#
            if self.starter1.get()!=0:
                self.textarea.insert(END,f"\n Mushroom Tikka\t\t{self.starter1.get()}\t\t{self.star1}")

            if self.starter2.get()!=0:
                self.textarea.insert(END,f"\n Paneer Tikka\t\t{self.starter2.get()}\t\t{self.star2}")
            
            if self.starter3.get()!=0:
                self.textarea.insert(END,f"\n Malai Chaap\t\t{self.starter3.get()}\t\t{self.star3}")
            
            if self.starter4.get()!=0:
                self.textarea.insert(END,f"\n Chicken Lollipop\t\t{self.starter4.get()}\t\t{self.star4}")
            
            if self.starter5.get()!=0:
                self.textarea.insert(END,f"\n Afghani Chicken\t\t{self.starter5.get()}\t\t{self.star5}")
            
            if self.starter6.get()!=0:
                self.textarea.insert(END,f"\n Fish Fry\t\t{self.starter6.get()}\t\t{self.star6}")

            #===========Main Course============#
            if self.main1.get()!=0:
                self.textarea.insert(END,f"\n Shahi Paneer\t\t{self.main1.get()}\t\t{self.maincourse1}")

            if self.main2.get()!=0:
                self.textarea.insert(END,f"\n Aloo Mattar\t\t{self.main2.get()}\t\t{self.maincourse2}")
            
            if self.main3.get()!=0:
                self.textarea.insert(END,f"\n Dal Makhani\t\t{self.main3.get()}\t\t{self.maincourse3}")
            
            if self.main4.get()!=0:
                self.textarea.insert(END,f"\n Butter Chicken\t\t{self.main4.get()}\t\t{self.maincourse4}")
            
            if self.main5.get()!=0:
                self.textarea.insert(END,f"\n Handi Chicken\t\t{self.main5.get()}\t\t{self.maincourse5}")
            
            if self.main6.get()!=0:
                self.textarea.insert(END,f"\n Egg Curry\t\t{self.main6.get()}\t\t{self.maincourse6}")

            #========Desserts=============#
            if self.dessert1.get()!=0:
                self.textarea.insert(END,f"\n Gulab Jamun\t\t{self.dessert.get()}\t\t{self.dess1}")

            if self.dessert2.get()!=0:
                self.textarea.insert(END,f"\n Rabri\t\t{self.dessert2.get()}\t\t{self.dess2}")
            
            if self.dessert3.get()!=0:
                self.textarea.insert(END,f"\n Rasmalai\t\t{self.dessert3.get()}\t\t{self.dess3}")
            
            if self.dessert4.get()!=0:
                self.textarea.insert(END,f"\n Moong Dal Halwa\t\t{self.dessert4.get()}\t\t{self.dess4}")
            
            if self.dessert5.get()!=0:
                self.textarea.insert(END,f"\n Ice Cream\t\t{self.dessert5.get()}\t\t{self.dess5}")
            
            if self.dessert6.get()!=0:
                self.textarea.insert(END,f"\n Cold Drink\t\t{self.dessert6.get()}\t\t{self.dess6}")


            self.textarea.insert(END, f"\n-------------------------------------")
            if self.starter_tax.get()!="Rs 0.0":
                self.textarea.insert(END, f"\n Starters Tax\t\t\t{self.starter_tax.get()}")
            if self.main_tax.get()!="Rs 0.0":
                self.textarea.insert(END, f"\n Main Course Tax\t\t\t{self.main_tax.get()}")
            if self.dessert_tax.get()!="Rs 0.0":
                self.textarea.insert(END, f"\n Dessert Tax\t\t\t{self.dessert_tax.get()}")
            self.textarea.insert(END, f"\n-------------------------------------")
            self.textarea.insert(END, f"\n Total Bill\t\t\t Rs {self.total_bill}")
            self.textarea.insert(END, f"\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0', END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill Number : {self.bill_no.get()} Saved Successfulley")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0', END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error", "Invalid Bill Number")

    #=======Clear Data Button============#
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear data?")
        if op>0:
            #----------Starters--------------#
            self.starter1.set(0)
            self.starter2.set(0)
            self.starter3.set(0)
            self.starter4.set(0)
            self.starter5.set(0)
            self.starter6.set(0)

            #----------Main Course------------#
            self.main1.set(0)
            self.main2.set(0)
            self.main3.set(0)
            self.main4.set(0)
            self.main5.set(0)
            self.main6.set(0)

            #----------dessert---------------#
            self.dessert1.set(0)
            self.dessert2.set(0)
            self.dessert3.set(0)
            self.dessert4.set(0)
            self.dessert5.set(0)
            self.dessert6.set(0)

            #--------------Total Product Price & Tax Variables--------#
            self.starter_price.set("")
            self.main_price.set("")
            self.dessert_price.set("")

            self.starter_tax.set("")
            self.main_tax.set("")
            self.dessert_tax.set("")

            #------------Customer------------------#
            self.c_name.set("")
            self.c_phone .set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()


    #=======Clear Data Button============#
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()




root = Tk()
obj = billingApp(root)
root.mainloop()