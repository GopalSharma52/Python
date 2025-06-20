import tkinter as tk
window = tk.Tk()
window.title("My first Window...")
window.geometry("800x700")
window.configure(bg="Red")
label=tk.Label(window,text="Hello Gopal Sharma ji...",bg="Yellow",font="Bold")    #label ki help se ham window par kuch bhi likhte hai
label.pack(pady=20,padx=100)
window.mainloop()
