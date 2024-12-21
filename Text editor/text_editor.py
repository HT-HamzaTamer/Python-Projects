import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfilename

def open_file() :
    file_path = askopenfilename(
        filetypes=[("Text Files","*.txt")]
    )
    if not file_path :
        return
    
    text_box.delete(1.0,tk.END)
    with open(file_path , "r") as input_file :
        text = input_file.read()
        text_box.insert(tk.END , text)

def save_as_file():
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files","*.txt")]
    )

    if not file_path :
        return
    
    with open(file_path , "w") as output_file:
        text = text_box.get(1.0,tk.END)
        output_file.write(text)

window = tk.Tk()
window.title("Text Editor")
window.minsize(width=1000 , height=500)

frame1 = tk.Frame(window)
frame1.place(x=15, y=25)

frame2 = tk.Frame(window)
frame2.place(x=15, y=115)

frame3 = tk.Frame(window)
frame3.place(x=180 , y=25)

open_btn = tk.Button(frame1,command=open_file, text="OPEN" , width=11 , height=3 , bd=7 , font=("",12,"bold") )
save_btn = tk.Button(frame2,command=save_as_file, text="SAVE AS" , width=11 , height=3 , bd=7 , font=("",12,"bold")  )

text_box = tk.Text(frame3, font=("",14),width=73 ,height=20.5)

open_btn.pack()
save_btn.pack()
text_box.pack()

window.mainloop()