import os
os.system("export PYSPARK_PYTHON=python3")
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import webbrowser
import makearray as mk
import pf as pf
from pyspark import SparkContext
#import numpy as mp

class Application:
    counter = 0
    
    def __init__(self, root):
        self.root = root
        self.root.title('Death Records Application')
        #ttk.Frame(self.root, width=500, height=500).pack()
        logo = PhotoImage(file="/opt/spark-1.6.0/deathproject/logo.gif")
        logolegend = "BM Soft Enterprises. All rights reserved. 2016 Release -, New York, NY"
        logolabel = Label(self.root, image=logo, background="white")
        logolabel.image = logo
        logolabel.pack(side="top", fill=BOTH, expand=1)
        logolegendlabel = Label(self.root, text=logolegend, font="Helvetica 14 italic", background="white")
        logolegendlabel.pack(side="top", fill=BOTH, expand=1)
        
        menu = Menu(self.root, tearoff=False)
        root.config(menu=menu)
        subMenu = Menu(menu)
        # Adds a drop down when "File" is clicked
        menu.add_cascade(label="File", underline=1, menu=subMenu)
        subMenu.add_command(label="New Project...", command=self.doNothing)
        subMenu.add_command(label="New...", command=self.doNothing)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.doNothing)

        editMenu = Menu(menu)
        menu.add_cascade(label="Functions", menu=editMenu)
        editMenu.add_command(label="Statistics", command=self.open_graph)
        editMenu.add_command(label="Descriptive Analysis", command=self.create_window)

        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About...", command=self.about_window)

        # Main variables
        self.gendersel = IntVar()
        self.residentsel = IntVar()        
        self.educationval = StringVar()
        self.yearsofeducationval = StringVar()
        self.placeofdeathval = StringVar()
        self.maritalsel = IntVar()
        self.injuryatworksel = IntVar()
        self.raceval = StringVar()
        self.activitycodeval = StringVar()
        self.placeofinjuryval = StringVar()
        self.diseaseval = StringVar()
        self.diseasecodeval = StringVar()
        self.ageval = StringVar()
        
        self.mannerofdeath = {'1':'Accident', '2':'Suicide', '3':'Homicide', '4':'Pending investigation', '5':'Could not determine', '6':'Self-inflicted', '7':'Natural', '0':'Not specified'}
        
        #self.AGE = 0
        
        status = Label(self.root, text="Ready", font="Arial 8", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        
        self.init_widgets()

    def init_widgets(self):
        self.entrytxt = tkinter.StringVar()

        self.rightframe = Frame(self.root)
        self.rightframe.pack(side="right", padx=20, pady=20)
        self.leftframe = Frame(self.root)
        self.leftframe.pack(side="left", padx=20, pady=20)

        statslabeltext = "View statistics in pie charts of different categorical features:"
        statslabel = Label(self.rightframe, text=statslabeltext, font="Helvetica 8 bold")
        statslabel.pack(side=TOP, padx=20, pady=20)
        ttk.Button(self.rightframe, command=self.open_graph, text='Launch Statistics').pack(side=BOTTOM, padx=10, pady=10)
                
        descriptivelabeltext = "Enter an individual's features and mathematically predict their manner of death:"
        statslabel = Label(self.leftframe, text=descriptivelabeltext, font="Helvetica 8 bold")
        statslabel.pack(side=TOP, padx=20, pady=20)
        ttk.Button(self.leftframe, text="Launch Descriptive Analysis", command=self.create_window).pack(side=BOTTOM, padx=10, pady=10)

    def create_window(self):

        self.counter += 1
        self.font = "Helvetica 12 italic"
        self.t = Toplevel(self.root)
        #self.tmainframe = Frame(self.t)
        #self.t.geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        #scrollbar = Scrollbar(self.tmainframe)
        #scrollbar.pack(side=RIGHT, fill=Y)
        #self.tmainframe.config(yscrollcommand=scrollbar.set)

        #scrollbar.config(command=self.tmainframe.yview)
        self.t.wm_title("Description query #%s" % self.counter)
        l = Label(self.t, text="Select Query attributes: ", font="Helvetica 12 bold italic")
        l.pack(side=TOP,padx=5, pady=5)

        l01 = Label(self.t, text="Gender: ", font=self.font)
        l01.pack(side=TOP, anchor=W, expand=True, padx=5, pady=1)
        self.frame01 = Frame(self.t)
        self.frame01.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        G1 = Radiobutton(self.frame01, text="Male", variable=self.gendersel, value=0, command=self.doNothing)
        G1.pack(side=LEFT, anchor = W )
        G2 = Radiobutton(self.frame01, text="Female", variable=self.gendersel, value=1,
                  command=self.doNothing)
        G2.pack(side=LEFT, anchor = W )

        l02 = Label(self.t, text="Resident Status: ", font=self.font)
        l02.pack(side=TOP, anchor=W, expand=True, padx=5, pady=1)
        self.frame02 = Frame(self.t)
        self.frame02.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        R1 = Radiobutton(self.frame02, text="Resident", variable=self.residentsel, value=0,
                 command=self.doNothing)
        R1.pack(side=LEFT, anchor = W )
        R2 = Radiobutton(self.frame02, text="Intrastate non-resident", variable=self.residentsel, value=1,
                  command=self.doNothing)
        R2.pack(side=LEFT, anchor = W )
        R3 = Radiobutton(self.frame02, text="Intersate non-resident", variable=self.residentsel, value=2,
                 command=self.doNothing)
        R3.pack(side=LEFT, anchor = W )
        R4 = Radiobutton(self.frame02, text="Foreign", variable=self.residentsel, value=3,
                  command=self.doNothing)
        R4.pack(side=LEFT, anchor = W )
        
        self.frame03 = Frame(self.t)
        self.frame03.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l03 = Label(self.frame03, text="Education Level:    ", font=self.font)
        l03.pack(side=LEFT, anchor=W, padx=5, pady=1)
        E1 = OptionMenu(self.frame03, self.educationval, "8th grade or less", "9 - 12th grade, no diploma", "High school graduate or GED completed", "Some college credit, but no degree", "Associate degree", "Bachelor's degree", "Master's degree", "Doctorate or professional degree", "Unknown" )
        E1.pack(side=LEFT, anchor = W )

        self.frame035 = Frame(self.t)
        self.frame035.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l035 = Label(self.frame035, text="Years of Education: ", font=self.font)
        l035.pack(side=LEFT, anchor=W, padx=5, pady=1)
        Y1 = OptionMenu(self.frame035, self.yearsofeducationval, "No formal education", "1 year of Elementary School", "2 years of Elementary School", "3 years of Elementary School", "4 years of Elementary School", "5 years of Elementary School", "6 years of Elementary School", "7 years of Elementary School", "8 years of Elementary School", "1 year of High School", "2 years of High School", "3 years of High School", "4 years of High School", "1 year of College", "2 years of College", "3 years of College", "4 years of College", "5 or more years of College", "Not Stated"  )
        Y1.pack(side=LEFT, anchor = W )

        self.frame04 = Frame(self.t)
        self.frame04.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l04 = Label(self.frame04, text="Place of Death: ", font=self.font)
        l04.pack(side=LEFT, anchor=W, padx=5, pady=1)
        P1 = OptionMenu(self.frame04, self.placeofdeathval, "Med Facility - Inpatient", "Med Facility - ER", "Med Facility - Dead at arrival", "Home", "Hospice Facility", "Nursing Home", "Other", "Unknown" )
        P1.pack(side=LEFT, anchor = W )


        l05 = Label(self.t, text="Marital Status: ", font=self.font)
        l05.pack(side=TOP, anchor=W, expand=True, padx=5, pady=1)
        self.frame05 = Frame(self.t)
        self.frame05.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        M1 = Radiobutton(self.frame05, text="Single", variable=self.maritalsel, value=0,
                 command=self.doNothing)
        M1.pack(side=LEFT, anchor = W )
        M2 = Radiobutton(self.frame05, text="Married", variable=self.maritalsel, value=1,
                  command=self.doNothing)
        M2.pack(side=LEFT, anchor = W )
        M3 = Radiobutton(self.frame05, text="Divorced", variable=self.maritalsel, value=2,
                 command=self.doNothing)
        M3.pack(side=LEFT, anchor = W )
        M4 = Radiobutton(self.frame05, text="Widowed", variable=self.maritalsel, value=3,
                  command=self.doNothing)
        M4.pack(side=LEFT, anchor = W )
        M5 = Radiobutton(self.frame05, text="Unknown", variable=self.maritalsel, value=4,
                  command=self.doNothing)
        M5.pack(side=LEFT, anchor = W )

        l06 = Label(self.t, text="Injury at work: ", font=self.font)
        l06.pack(side=TOP, anchor=W, expand=True, padx=5, pady=1)
        self.frame06 = Frame(self.t)
        self.frame06.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        I1 = Radiobutton(self.frame06, text="Yes", variable=self.injuryatworksel, value=0,
                 command=self.doNothing)
        I1.pack(side=LEFT, anchor = W )
        I2 = Radiobutton(self.frame06, text="No", variable=self.injuryatworksel, value=1,
                  command=self.doNothing)
        I2.pack(side=LEFT, anchor = W )
        I3 = Radiobutton(self.frame06, text="Unknown", variable=self.injuryatworksel, value=2,
                 command=self.doNothing)
        I3.pack(side=LEFT, anchor = W )

        self.frame07 = Frame(self.t)
        self.frame07.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l07 = Label(self.frame07, text="Race:           ", font=self.font)
        l07.pack(side=LEFT, anchor=W, padx=5, pady=1)
        RACE1 = OptionMenu(self.frame07, self.raceval, "White", "Black", "American Indian", "Chinese", "Japanese", "Hawaiian", "Filipino", "Asian Indian", "Korean", "Samoan", "Vietnamese", "Guamanian", "Other Asian or Pacific Islander", "Other Asian origin", "Other" )
        RACE1.pack(side=LEFT, anchor = W )


        self.frame08 = Frame(self.t)
        self.frame08.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l08 = Label(self.frame08, text="Activity code:           ", font=self.font)
        l08.pack(side=LEFT, anchor=W, padx=5, pady=1)
        AC1 = OptionMenu(self.frame08, self.activitycodeval, "While engaged in sports activity", "While engaged in a work activity", "During unspecified activity", "Not applicable" )
        AC1.pack(side=LEFT, anchor = W )


        self.frame09 = Frame(self.t)
        self.frame09.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l09 = Label(self.frame09, text="Place of Injury:           ", font=self.font)
        l09.pack(side=LEFT, anchor=W, padx=5, pady=1)
        PI1 = OptionMenu(self.frame09, self.placeofinjuryval, "Home", "Residential institution", "School, other institution and public administrative area", "Sports and athletics area","Street and highway", "Trade and service area", "Industrial and construction area", "Farm", "Other", "Unspecified Place", "Other injury causes" )
        PI1.pack(side=LEFT, anchor = W )

        self.frame10 = Frame(self.t)
        self.frame10.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)

        self.frame105 = Frame(self.t)
        self.frame105.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l105 = Label(self.frame105, text="Or enter a disease code:           ", font=self.font)
        l105.pack(side=LEFT, anchor=W, padx=5, pady=1)
        DC = Entry(self.frame105, textvariable=self.diseasecodeval, width=6)
        DC.pack(side=LEFT)

        DC.delete(0, END)
        DC.insert(0, "")


        l10 = Label(self.frame10, text="Disease:           ", font=self.font)
        l10.pack(side=LEFT, anchor=W, padx=5, pady=1)
        D1 = OptionMenu(self.frame10, self.diseaseval, "Hypertensive heart disease", "Unspecified diabetes mellitus", "Other endocrine disorders")#, command=DC.delete )
        D1.pack(side=LEFT, anchor = W )

        '''
        self.frame105 = Frame(self.t)
        self.frame105.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l105 = Label(self.frame105, text="Or enter a disease code:           ", font=self.font)
        l105.pack(side=LEFT, anchor=W, padx=5, pady=1)
        DC = Entry(self.frame105, textvariable=self.diseasecodeval, width=6)
        DC.pack(side=LEFT)

        DC.delete(0, END)
        DC.insert(0, "")
        '''
        #print(DC.get())


        self.frame11 = Frame(self.t)
        self.frame11.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        l11 = Label(self.frame11, text="Age: ", font=self.font)
        l11.pack(side=LEFT, anchor=W, padx=5, pady=1)
        AGE = Entry(self.frame11, textvariable=self.ageval, width=3)
        AGE.pack(side=LEFT)

        AGE.delete(0, END)
        AGE.insert(0, "18")
        print(AGE.get())
        ttk.Button(self.t, text="Calculate prediction", command=self.calculate_prediction).pack(side=TOP, fill=BOTH, padx=15, pady=15)


#label = Label(root)
#label.pack()

    def open_graph(self):
        new = 2
        url = "file:///home/jerry/Documents/bigdata/PYTHON/TkinterGUI3/startbootstrap-shop-item-1.0.4/index.html"
        webbrowser.open(url,new=new)

        #self.menu = Menu(self.root)
        #self.subMenu = Menu
    def insert_txt(self):
        if self.E1.get() == '':
            self.txt.insert(tkinter.INSERT, 'Statistics\n')
        else:
            number = int(self.E1.get())
            self.txt.insert(tkinter.INSERT, self.E1.get().upper() + '\n')
            self.E1.delete(0, 'end')
    def doNothing(self):
        print("ok ok I won't...")
        print(str(self.gendersel))
        print(str(self.residentsel))
        
    def clear_entry(self):
        self.DC.delete(0, END)

    def about_window(self):
        tkinter.messagebox.showinfo("About Death Records Application...", "Developed by JB nd AD.\nColumbia University.")

    def calculate_prediction(self):
    
        g = int(self.gendersel.get())
        r = int(self.residentsel.get())
        e = ""#str(self.educationval.get())
        y = ""#str(self.yearsofeducationval.get)
        pd = ""#str(self.placeofdeathval.get())
        m = int(self.maritalsel.get())
        iw = int(self.injuryatworksel.get())
        race = ""#str(self.raceval.get())
        ac = ""#str(self.activitycodeval.get())
        pi = ""#str(self.placeofinjuryval.get())
        d = str(self.diseaseval.get())
        dc = str(self.diseasecodeval.get())
        idc = ""

        if str(self.educationval.get()) == "8th grade or less": e = 0
        elif str(self.educationval.get()) == "9 - 12th grade, no diploma": e = 1
        elif str(self.educationval.get()) == "High school graduate or GED completed": e = 2
        elif str(self.educationval.get()) == "Some college credit, but no degree": e = 3
        elif str(self.educationval.get()) == "Associate degree": e = 4
        elif str(self.educationval.get()) == "Bachelor's degree": e = 5
        elif str(self.educationval.get()) == "Master's degree": e = 6
        elif str(self.educationval.get()) == "Doctorate or professional degree": e = 7
        elif str(self.educationval.get()) == "Unknown": e = 8
        
        if str(self.yearsofeducationval.get()) == "No formal education": y = 0
        elif str(self.yearsofeducationval.get()) == "1 year of Elementary School": y = 1
        elif str(self.yearsofeducationval.get()) == "2 years of Elementary School": y = 2
        elif str(self.yearsofeducationval.get()) == "3 years of Elementary School": y = 3
        elif str(self.yearsofeducationval.get()) == "4 years of Elementary School": y = 4
        elif str(self.yearsofeducationval.get()) == "5 years of Elementary School": y = 5
        elif str(self.yearsofeducationval.get()) == "6 years of Elementary School": y = 6
        elif str(self.yearsofeducationval.get()) == "7 years of Elementary School": y = 7
        elif str(self.yearsofeducationval.get()) == "8 years of Elementary School": y = 8
        elif str(self.yearsofeducationval.get()) == "1 year of High School": y = 9
        elif str(self.yearsofeducationval.get()) == "2 years of High School": y = 10
        elif str(self.yearsofeducationval.get()) == "3 years of High School": y = 11
        elif str(self.yearsofeducationval.get()) == "4 years of High School": y = 12
        elif str(self.yearsofeducationval.get()) == "1 year of College": y = 13
        elif str(self.yearsofeducationval.get()) == "2 years of College": y = 14
        elif str(self.yearsofeducationval.get()) == "3 years of College": y = 15
        elif str(self.yearsofeducationval.get()) == "4 years of College": y = 16
        elif str(self.yearsofeducationval.get()) == "5 or more years of College": y = 17
        elif str(self.yearsofeducationval.get()) == "Not Stated": y = 18
        
        if str(self.placeofdeathval.get()) == "Med Facility - Inpatient": pd = 0
        elif str(self.placeofdeathval.get()) == "Med Facility - ER": pd =1
        elif str(self.placeofdeathval.get()) == "Med Facility - Dead at arrival": pd = 2
        elif str(self.placeofdeathval.get()) == "Home": pd = 3
        elif str(self.placeofdeathval.get()) == "Hospice Facility": pd = 4
        elif str(self.placeofdeathval.get()) == "Nursing Home": pd = 5
        elif str(self.placeofdeathval.get()) == "Other": pd = 6
        elif str(self.placeofdeathval.get()) == "Unknown": pd = 7
        
        if str(self.raceval.get()) == "White": race = 1
        elif str(self.raceval.get()) == "Black": race = 2
        elif str(self.raceval.get()) == "American Indian": race = 3
        elif str(self.raceval.get()) == "Chinese": race = 4
        elif str(self.raceval.get()) == "Japanese": race = 5
        elif str(self.raceval.get()) == "Hawaiian": race = 6
        elif str(self.raceval.get()) == "Filipino": race = 7
        elif str(self.raceval.get()) == "Asian Indian": race = 10
        elif str(self.raceval.get()) == "Korean": race = 11
        elif str(self.raceval.get()) == "Samoan": race = 12
        elif str(self.raceval.get()) == "Vietnamese": race = 12
        elif str(self.raceval.get()) == "Guamanian": race = 14
        elif str(self.raceval.get()) == "Other Asian or Pacific Islander": race = 15
        elif str(self.raceval.get()) == "Other Asian origin": race = 16
        elif str(self.raceval.get()) == "Other": race = 0
        
        if str(self.activitycodeval.get()) == "While engaged in sports activity": ac = 0
        elif str(self.activitycodeval.get()) == "While engaged in a work activity": ac = 3
        elif str(self.activitycodeval.get()) == "During unspecified activity": ac = 6
        elif str(self.activitycodeval.get()) == "Not applicable": ac = 7
        
        if str(self.placeofinjuryval.get()) == "Home": pi = 0
        elif str(self.placeofinjuryval.get()) == "Residential institution": pi = 1
        elif str(self.placeofinjuryval.get()) == "School, other institution and public administrative area": pi = 2
        elif str(self.placeofinjuryval.get()) == "Sports and athletics area": pi = 3
        elif str(self.placeofinjuryval.get()) == "Street and highway": pi = 4
        elif str(self.placeofinjuryval.get()) == "Trade and service area": pi = 5
        elif str(self.placeofinjuryval.get()) == "Industrial and construction area": pi = 6
        elif str(self.placeofinjuryval.get()) == "Farm": pi = 7
        elif str(self.placeofinjuryval.get()) == "Other": pi = 8
        elif str(self.placeofinjuryval.get()) == "Unspecified Place": pi = 9
        elif str(self.placeofinjuryval.get()) == "Other injury causes": pi = 10
        
        if str(self.diseasecodeval.get()) == "":
            if str(self.diseaseval.get()) == "Hypertensive heart disease": icd = 3735
            elif str(self.diseaseval.get()) == "Unspecified diabetes mellitus": icd = 2075
            elif str(self.diseaseval.get()) == "Other endocrine disorders": icd = 2173
        else: icd = int(self.diseasecodeval.get())
        
        age = int(self.ageval.get())
        
        print(y, icd)
        #(g,r,e,pd,m,iw,race,ac,pi,icd,age)
        print(mk.makearray(g, r, e, y, pd, m, iw, race, ac, pi, icd, age))
        md = pf.predict(sc, mk.makearray(g, r, e, y, pd, m, iw, race, ac, pi, icd, age))
        
        self.font2 = "Helvetica 12 italic"
        self.t2 = Toplevel(self.root)
        
        self.t2.wm_title("Prediction results")
        l2 = Label(self.t2, text="Prediction Results: ", font="Helvetica 12 bold italic")
        l2.pack(side=TOP,padx=5, pady=5)
        self.text = self.mannerofdeath[str(md)]
        l201 = Label(self.t2, text=self.text, font=self.font2)
        l201.pack(side=TOP, anchor=W, expand=True, padx=5, pady=1)
        
        '''
        self.frame01 = Frame(self.t)
        self.frame01.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
        G1 = Radiobutton(self.frame01, text="Male", variable=self.gendersel, value=0, command=self.doNothing)
        G1.pack(side=LEFT, anchor = W )
        G2 = Radiobutton(self.frame01, text="Female", variable=self.gendersel, value=1,

                  command=self.doNothing)
        G2.pack(side=LEFT, anchor = W )
        '''


'''
   var = IntVar()
R1 = Radiobutton(root, text="Male", variable=var, value=1,
                 command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Female", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )


label = Label(root)
label.pack()

        photo = PhotoImage(file="/home/jerry/Documents/bigdata/PYTHON/TkinterGUI3/gender/Gender.jpeg")
        gender_im = Label(root, image=photo)
        gender_im.pack()            
'''
if __name__ == '__main__':
    root = tkinter.Tk()
    sc = SparkContext(appName="PythonRandomForestClassificationExample")
    Application(root)
    root.mainloop()
    #print(mk.makearray(self.G, self.R, self.E, self.P, self.M, self.I, self.RACE, self.A, self.PI, self.D, self.H))
