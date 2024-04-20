#>>>>>>>>>>>>>>> This projecct is for language convertor <<<<<<<<<<<<<<<<<<<<<<<<<<


#import tkinter GUI 
from tkinter import *
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


def DeleteText():
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)

def Convert():
    input_text = text1_field.get("1.0", "end")[:-1]
    output_text = transliterate(input_text, sanscript.ITRANS, sanscript.DEVANAGARI)
    text2_field.insert('end -1 chars', output_text)

if __name__ == "__main__":
    root = Tk()
    root.configure(background='black')
    root.geometry("600x450")
    root.minsize(480,500)
    root.maxsize(450,550)
    root.title("Text Converter")

    headlabel = Label(root, text='Welcome to English(Latin) to Hindi(Devanagiri) text converter', fg='black', bg="red")
    label1 = Label(root, text="English Text", fg='black', bg='green')
    label2 = Label(root, text="Hindi Text", fg='black', bg='green')

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=3, column=0, padx=10, pady=10)

    text1_field = Text(root, height=5, width=25, font="lucida 13")
    text2_field = Text(root, height=5, width=25, font="lucida 13")

    text1_field.grid(row=1, column=1, padx=10, pady=10)
    text2_field.grid(row=3, column=1, padx=10, pady=10)

    button1 = Button(root, text="Convert into Hindi text", bg="red", fg="black", command=Convert)
    button1.grid(row=2, column=1)

    button2 = Button(root, text="Clear", bg="red", fg="black", command=DeleteText)
    button2.grid(row=4, column=1)

    root.mainloop()

#from tkinter import *
# root = Tk()
# root.geometry("400x600")
# button = Button(root, text = "welcome", fg = "green", bg = "white").grid()
# root.mainloop()
