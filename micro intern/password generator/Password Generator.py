import tkinter as tk
import random
import string

def generate_password():
    length = 12  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("650x650")
root.configure(bg="#34495e")  


frame = tk.Frame(root, bg="#ecf0f1", bd=5, relief="ridge", width=600, height=600)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.pack_propagate(False)

password_var = tk.StringVar()


label = tk.Label(frame, text="Generated Password:", font=("Arial", 14, "bold"), fg="#2c3e50", bg="#ecf0f1")
label.place(relx=0.5, rely=0.3, anchor="center") 

password_entry = tk.Entry(frame, textvariable=password_var, font=("Arial", 16, "bold"), width=30, fg="#2c3e50", bg="#ffffff", justify="center", bd=3, relief="solid")
password_entry.place(relx=0.5, rely=0.4, anchor="center")  

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=("Arial", 14, "bold"), 
                            bg="#e74c3c", fg="white", padx=10, pady=5, relief="raised", bd=3)
generate_button.place(relx=0.5, rely=0.5, anchor="center") 

root.mainloop()
