import time
from scratch import Scratch
import tkinter as tk
from tkinter import messagebox

def invite():
    sc = Scratch(entry_name.get,entry_name.get)
    followers = sc.get_followers(entry_name.get)

    for user in followers:
        sc.invite_curator(entry_name.get,entry_studio.get)
        time.sleep(2)
        
    messagebox.showinfo("全員の招待に成功しました！")

root = tk.Tk()
root.title("Scratch自動化")
root.geometry("300x250")

label_name = tk.Label(root, text="ユーザーネーム:")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

label_password = tk.Label(root, text="パスワード:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

label_studio = tk.Label(root, text="スタジオid:")
label_studio.pack(pady=5)
entry_studio = tk.Entry(root, width=40)
entry_studio.pack(pady=5)

submit_button = tk.Button(root, text="OK！", command=invite)
submit_button.pack(pady=20)

# メインループ
root.mainloop()