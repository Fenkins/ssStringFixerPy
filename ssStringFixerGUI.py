from Tkinter import *

class Application(Frame):
    
    def compute(self):
        
        line = self.textFieldInput.get()
        line = '/'+line.replace('\n', '|')+'/i'
        self.textFieldOutput.delete(0,END)
        self.textFieldOutput.insert(0,line)

        
    def createWidgets(self):
        self.winfo_toplevel().title("ssStringFixer")

        
        self.labelOne = Label(self)
        self.labelOne["text"] = "Paste your stuff here:"
        self.labelOne.grid(row=0, sticky='E', padx=5, pady=2)
        self.labelOne.grid(sticky="W")


        self.textFieldInput = Entry(self)
        self.textFieldInput.grid(row=1,sticky='E', padx=5, pady=2)




        self.computeButton = Button(self)
        self.computeButton["text"] = "fix it for me would ya"
        self.computeButton["fg"]   = "brown"
        self.computeButton["command"] =  self.compute

        self.computeButton.grid(row=2,sticky='E', padx=5, pady=2)
        self.computeButton.grid(sticky="W")


        

        self.textFieldOutput = Entry(self)
        self.textFieldOutput.insert(END, 'Output should be here')
        self.textFieldOutput.grid(row=3,sticky='E', padx=5, pady=2)



        
    def __init__(self, master=None):
        master.minsize(width=200, height=150)
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()