from tkinter import ttk, Text, Button, LabelFrame, VERTICAL, E, NS, Scrollbar, Tk, BOTH, Frame, Entry 


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master

    def initUI (self):

        self.master.title('BMI')
        self.pack(fill=BOTH, expand = 1)


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Window()
    root.mainloop() 



if __name__ == '__main__':
   main()

