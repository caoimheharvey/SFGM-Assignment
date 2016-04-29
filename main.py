"""
*
* Caoimhe Harvey - C14724965
* Software for a Global Market 2
* DT282-2 Computer Science International
*
* High Fidelity
*
"""
import sys
from tkinter import *
import calendar
#from tkinter.tkk import *

#--------------------------------setting up window-------------------------------#
root = Tk()
root.geometry("835x580")
root.title("Home Page")
root.config(background = '#3D3D3D')

#-------------------------importing file for to do list--------------------------#
todolist = ['','','']

file = open("file.txt")
i = 0
for f in file.readlines():
    todolist[i] = f
    print(f)
    i = i +1

file.close()

#put text into arrays having a spanish array and an english array
#use a boolean to switch between the two
english_titles = ['Home','Modules','To Do List','Grades','Calendar','Announcements','Espanol']
spanish_titles = ['Inicio','Classes','Para Hacer','Notas','Calendario','Anuncios','English']

languageToggle = 0 #when false language is English

#----------------------------------- Header ---------------------------------#
class header:
    def __init__(self, master):
      wlogo = Label(master, text="Webcourses", bg = '#284872', fg = '#ffffff', font=("Helvetica", 26))
      wlogo.config(anchor="w", width = "1280", pady = "10", padx = "10")
      wlogo.pack()
      
      """ 
      self.b=Button(master,justify = LEFT)
      self.photo=PhotoImage(file="ring.gif")
      self.b.config(image=self.photo,width="100",height="70")
      self.b.pack(side=LEFT)
      """
#--------------------------------Settings Window---------------------------------#
def checkLang():
    if languageToggle == 0:
        languageToggle = 1
        print ("Switched to spanish")
    if languageToggle == 1:
        languageToggle = 0
        print("Switched to English")

#---------------------------------Tabs--------------------------------------#
class tabs:
    def __init__(self, master):
        #formatting the buttons positioning 
        self.homeBtn = Button(master, width=10)
        self.homeBtn.pack(side=LEFT)
        self.homeBtn.place(rely=0.075)

        self.modBtn = Button(master, width=10, command = self.new_window)
        self.modBtn.pack(side=LEFT)
        self.modBtn.place(rely=0.075, x = 64 + 54)

        self.tdList = Button(master, width=10)
        self.tdList.pack(side=LEFT)
        self.tdList.place(rely=0.075, x= 144 + 92)

        self.gradesBtn = Button(master, width=10, command = showGrades)
        self.gradesBtn.pack(side=LEFT)
        self.gradesBtn.place(rely=0.075, x = 234 + 120)

        self.calBtn = Button(master, width=10, command = showCal)
        self.calBtn.pack(side=LEFT)
        self.calBtn.place(rely=0.075, x = 305 + 167)

        self.annBtn = Button(master, width=11)
        self.annBtn.pack(side=LEFT)
        self.annBtn.place(rely=0.075, x = 385 + 205)

        self.settingsBtn = Button(master, width=10, command = checkLang)
        self.settingsBtn.pack(side=LEFT)
        self.settingsBtn.place(rely=0.075, x = 512 + 205)
        
        
        #checking language formatting
        if languageToggle == 0:
            self.homeBtn.config(text = english_titles[0])
            self.modBtn.config(text = english_titles[1])
            self.tdList.config(text = english_titles[2])
            self.gradesBtn.config(text = english_titles[3])
            self.calBtn.config(text = english_titles[4])
            self.annBtn.config(text = english_titles[5])
            self.settingsBtn.config(text = english_titles[6])
        else:
            self.homeBtn.config(text = spanish_titles[0])
            self.modBtn.config(text = spanish_titles[1])
            self.tdList.config(text = spanish_titles[2])
            self.gradesBtn.config(text = spanish_titles[3])
            self.calBtn.config(text = spanish_titles[4])
            self.annBtn.config(text = spanish_titles[5])
            self.settingsBtn.config(text = spanish_titles[6])

    #add functionality to open new window for each
    #modules window
    def new_window(self):
        print("Clicked")
        toplevel=Toplevel()
        toplevel.title('New Window')
        toplevel.focus_set()
        toplevel.geometry("700x500")
        text = Label(toplevel, text="You have sucessfully opened a new window")
        text.pack()

#----------------------------------Calendar-------------------------------------#
class Calendar:
    def __init__(self,master):
        #title
        title = Label(master, bg = '#97233B', text = "Calendar", fg = '#ffffff')
        title.config(anchor = "sw", height = 2, width = 28, font=("Helvetica", 16))
        title.pack()
        title.place(x = 595, y = 387)

        #container
        container = Label(master, bg = '#CFCECF')
        container.config(height = 8, width = 25)
        container.pack()
        container.place(x = 595, y = 430)

        #calendar
        cal_x = calendar.month(2016, 4, w = 2, l = 1)
        cal_out = Label(master, text = cal_x, font=('courier', 12, 'bold'), bg='#ffffff')
        cal_out.pack(padx = 3, pady = 10)
        cal_out.place(x = 635, y = 440)

    #calendar tab from main menu
    def calTab():
        print("calclicked")
        toplevel=Toplevel()
        toplevel.title('Calendar')
        toplevel.focus_set()
        toplevel.geometry("700x500")
        yrcal = calendar.calendar(2016, 2,1,10)
        yrCalOut = Label(toplevel, text = yrcal, font=('courier', 12, 'bold'), bg='#ffffff')
        yrCalOut.pack()

yrCal = 'calTab'
showCal = getattr(Calendar, yrCal)

#----------------------------------------Modules--------------------------------#
class modules:
    def __init__(self, master):
        #Module Title
        title = Label(master, bg = '#97233B', fg = '#ffffff')
        title.config(anchor = "sw", height = 2, width = 70, font=("Helvetica", 16))
        title.pack()
        title.place(x = 15, y = 100)

        if languageToggle == 0:
            title.config(text = english_titles[1])
        else:
            title.config(text = spanish_titles[1])

        #Module Background Container
        container = Label(master, bg = '#CFCECF')
        container.config(height = 14, width = 62)
        container.pack()
        container.place(x = 15, y = 144)

        #potential to be made more efficient with a for loop
        #Module Buttons
        self.mod1 = Button(master, text="Algorithms and Data Structures", justify=CENTER, command = self.module_window)
        self.mod1.config(font=("Helvetica", 12))
        self.mod1.pack()
        self.mod1.place(x = 25, y = 155, height = 100, width = 100)

        self.mod2 = Button(master, text="Course Information", justify=CENTER)
        self.mod2.config(font=("Helvetica", 12))
        self.mod2.pack()
        self.mod2.place(x = 135, y = 155, height = 100, width = 100)

        self.mod3 = Button(master, text="Human Computer Interaction", justify=CENTER)
        self.mod3.config(font=("Helvetica", 12))
        self.mod3.pack()
        self.mod3.place(x = 245, y = 155, height = 100, width = 100)

        self.mod4 = Button(master, text="Data Communications", justify=CENTER)
        self.mod4.config(font=("Helvetica", 12))
        self.mod4.pack()
        self.mod4.place(x = 355, y = 155, height = 100, width = 100)

        self.mod5 = Button(master, text="Databases", justify=CENTER)
        self.mod5.config(font=("Helvetica", 12))
        self.mod5.pack()
        self.mod5.place(x = 465, y = 155, height = 100, width = 100)

        self.mod6 = Button(master, text="German", justify=CENTER)
        self.mod6.config(font=("Helvetica", 12))
        self.mod6.pack()
        self.mod6.place(x = 25, y = 265, height = 100, width = 100)

        self.mod7 = Button(master, text="Mathematics", justify=CENTER)
        self.mod7.config(font=("Helvetica", 12))
        self.mod7.pack()
        self.mod7.place(x = 135, y = 265, height = 100, width = 100)

        self.mod8 = Button(master, text="Object Oriented Programming", justify=CENTER)
        self.mod8.config(font=("Helvetica", 12))
        self.mod8.pack()
        self.mod8.place(x = 245, y = 265, height = 100, width = 100)

        self.mod9 = Button(master, text="Operating Systems", justify=CENTER)
        self.mod9.config(font=("Helvetica", 12))
        self.mod9.pack()
        self.mod9.place(x = 355, y = 265, height = 100, width = 100)

        self.mod10 = Button(master, text="Software Engineering", justify=CENTER)
        self.mod10.config(font=("Helvetica", 12))
        self.mod10.pack()
        self.mod10.place(x = 465, y = 265, height = 100, width = 100)

    def module_window(self):
        print("Clicked")
        toplevel=Toplevel()
        toplevel.title('Module Window')
        toplevel.focus_set()
        toplevel.geometry("700x500")
        text = Label(toplevel, text="You have entered a module")
        text.pack()
        
#-----------------------------------To Do List----------------------------------#
class toDoList:
    def __init__(self, master):
        #to do list title bar
        title = Label(master, bg = '#97233B', fg = '#ffffff')
        title.config(anchor = "sw", height = 2, width = 28, font=("Helvetica", 16))
        title.pack()
        title.place(x = 595, y = 100)

        if languageToggle == 0:
            title.config(text = english_titles[2])
        else:
            title.config(text = spanish_titles[2])
        
        #container
        container = Label(master, bg = '#CFCECF')
        container.config(height = 10, width = 25)
        container.pack()
        container.place(x = 595, y = 144)
        
        #content
        lb = Listbox(master)
        lb.insert(1, todolist[0])
        lb.insert(2, todolist[1])
        lb.pack()
        lb.place(x = 620, y = 155, height = 90)

        e1 = Entry(master)
        e1.pack()
        e1.place(x = 615, y = 250)

        add = Button(master, text = "Add", command = lambda: self.add_task(e1.get(), lb))
        add.pack()
        add.place(x = 615, y = 280)


    def add_task(self, text, lb):
        lb.insert(0, text)
        #create array for to-do-list items
        todolist.append(text)
        #adding task to text file
        fileadd = open("file.txt", "a")
        fileadd.write(text + '\n')
        fileadd.close()

        

#------------------------------------Grades--------------------------------------#
class grades:
    def __init__(self, master):

        self.displayGrades = Button(master, height = 2, width = 28, command = showGrades)
        self.displayGrades.pack()
        self.displayGrades.place(x = 595, y = 330)
        
        title = Label(master, bg = '#97233B', fg = '#ffffff')
        title.config(anchor = "sw", height = 2, width = 28, font=("Helvetica", 16))
        title.pack()
        title.place(x = 595, y = 330)

        if languageToggle == 0:
            title.config(text = english_titles[3])
        else:
            title.config(text = spanish_titles[3])

        

def showGrades():
    print("Grades Clicked")
    toplevel=Toplevel()
    toplevel.title('Grades')
    toplevel.focus_set()
    toplevel.geometry("500x300")

    algos = Label(toplevel, text = "Algorithms")
    algos.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    algos.pack()
    algos.place(x = 10, y = 50)
    
    hci = Label(toplevel, text = "Human Computer Interaction")
    hci.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    hci.pack()
    hci.place(x = 10, y = 70)

    dc = Label(toplevel, text = "Data Communications")
    dc.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    dc.pack()
    dc.place(x = 10, y = 90)

    db = Label(toplevel, text = "Databases")
    db.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    db.pack()
    db.place(x = 10, y = 110)

    germ = Label(toplevel, text = "German")
    germ.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    germ.pack()
    germ.place(x = 10, y = 130)

    maths = Label(toplevel, text = "Mathematics")
    maths.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    maths.pack()
    maths.place(x = 10, y = 150)

    oop = Label(toplevel, text = "Object Oriented Programming")
    oop.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    oop.pack()
    oop.place(x = 10, y = 170)

    os = Label(toplevel, text = "Operating Systems")
    os.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    os.pack()
    os.place(x = 10, y = 190)

    se = Label(toplevel, text = "Software Engineering")
    se.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    se.pack()
    se.place(x = 10, y = 210)

    sfgm = Label(toplevel, text = "Software for a Global Market")
    sfgm.config(anchor = W, font = ('Helvetica', 16, 'bold'))
    sfgm.pack()
    sfgm.place(x = 10, y = 230)



#---------------------------------------Announcements-------------------------------------#
class Announcements:
    def __init__(self,master):
        #Module Title
        title = Label(master, bg = '#97233B', fg = '#ffffff')
        title.config(anchor = "sw", height = 2, width = 70, font=("Helvetica", 16))
        title.pack()
        title.place(x = 15, y = 387)

        if languageToggle == 0:
            title.config(text = english_titles[5])
        else:
            title.config(text = spanish_titles[5])

        #Module Background Container
        container = Label(master, bg = '#CFCECF')
        container.config(height = 8, width = 62)
        container.pack()
        container.place(x = 15, y = 430)

        #Announcements within
        a1 = Label(master, text="Apply for Post Graduate Programme")
        a1.config(font=("Helvetica", 16))
        a1.pack(anchor = W)
        a1.place(x = 20, y = 440)

        a2 = Label(master, text="April Student Newsletter")
        a2.config(font=("Helvetica", 16))
        a2.pack(anchor = W)
        a2.place(x = 20, y = 460)

        a3 = Label(master, text="Software for a Global Market 2")
        a3.config(font=("Helvetica", 16))
        a3.pack(anchor = W)
        a3.place(x = 20, y = 480)
        #nested
        a1 = Label(master, text="・Proposal for Presentation Schedule Week 12 (W/S April 15)")
        a1.config(font=("Helvetica", 14))
        a1.pack(anchor = W)
        a1.place(x = 20, y = 500)

#--------------------------------Calling classes from Main---------------------------------#
#header
head=header(root)

#tabs
tab = tabs(root)

#modules
mod = modules(root)

#to do list
tdl = toDoList(root)

#grades
marks = grades(root)

#announcements
ann = Announcements(root)

#calendar
cal = Calendar(root)

root.mainloop()
