import customtkinter
import tkinter
def Submit():
    my_label.configure(text=f'Hello {my_entry.get()}')
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

def clear():
    my_entry.configure(state="normal")
    my_entry.delete(0,tkinter.END)

root = customtkinter.CTk()

root.title('Custom Tkinter Label')
root.geometry('600x350')


my_label = customtkinter.CTkLabel(root, text='Hello', font=('Helvetica',24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root,
placeholder_text='Enter your name:',
height=50,
width=200,
font=("Helvetica",18),
corner_radius=50,
text_color="green",
placeholder_text_color="darkblue",
fg_color=("blue","lightblue"),
state="normal",

)
my_entry.pack(pady=20)

my_button=customtkinter.CTkButton(root,text="Submit", command=Submit)
my_button.pack(pady=10)

clear_button= customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)
root.mainloop()