from tkinter import*

#A small text conversion tool with Tkinter
#Add more options, some day.
def main():
    #define root
    root = Tk()
    root.geometry()
    root.title("Python Text Converter Thing")

    #Text conversion functions (add more)
    #To UPPERCASE
    def converterFunctionOne():
        fetchedText = textbox.get("1.0",END).upper()
        textbox.delete("1.0", "end")
        textbox.insert(END, fetchedText)

    #To lowercase
    def converterFunctionTwo():
        fetchedText = textbox.get("1.0", END).lower()
        textbox.delete("1.0", "end")
        textbox.insert(END, fetchedText)

    #Remove spaces (maybe make this so that the user can pick the replaced symbols/letters?
    def converterFunctionThree():
        fetchedText = textbox.get("1.0", END).lower()
        fetchedText = fetchedText.replace(" ","")
        textbox.delete("1.0", "end")
        textbox.insert(END, fetchedText)

    ########################
    #WIDGETS USED######

    #Frame
    frameForTextAndButtons = Frame(root, bg="gray", padx=10,pady=10)
    frameForTextAndButtons.grid()
    #Text
    textbox = Text(frameForTextAndButtons, bg="beige")
    textbox.grid(columnspan=6)

    #Buttons for executing functions
    button1 = Button(frameForTextAndButtons, text="<UPPERCASE>",padx=10, command=converterFunctionOne)
    button1.grid(column=0, row=1)
    button2 = Button(frameForTextAndButtons, text="<lowercase>",padx=10,command=converterFunctionTwo)
    button2.grid(column=1, row=1)
    button3 = Button(frameForTextAndButtons, text="<Remove space)>",padx=10, command=converterFunctionThree)
    button3.grid(column=2, row=1)

    root.mainloop()

if __name__ == '__main__':
    main()
