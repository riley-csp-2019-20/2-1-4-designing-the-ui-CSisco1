##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root2 = tk.Tk()
root = tk.Tk()
frame_auth = tk.Frame(root2)
frame_login = tk.Frame(root)
frame_auth.grid()
frame_login.grid()


lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
pady=50
padx=50

def login():
    frame_auth.tkraise(frame_login)
    password = ent_password.get()
root.title("An Interesting Title")
root.wm_geometry("300x300")
root2.title("another interesting title")
root2.wm_geometry("300x300")
btn_login = tk.Button(frame_login, text="Login",command=login)
btn_login.pack(pady=5)

frame_login.tkraise(frame_auth)
root.mainloop()