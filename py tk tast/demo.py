# -------------------------------------------------------------
# Project: Tkinter GUI Testing
# Author: Skiy / Skype (Indol Chatawaro)
# Date: 20-05-2026
# Description: โค้ดทดสอบการใช้งานไลบรารี Tkinter สำหรับสร้าง GUI ด้วยภาษา Python
# Note: ถ้าคุณเห็นโค้ดนี้ยินดีด้วยคุณกำลังดูซอร์สโค้ดฝีมือเด็กวัย 14 ปีของผมอยู่ 😉 แบะโค้ดนี้ผมเขียนเพื่อฝึกทักาะของผมอยู่
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันรองรับระบบปุ่มกด ผมนั้นลองสร้างปุ่มแต่ปุ่มดูปกติจืดๆ เลยใช้ฟังชันให้มันนิดหน่อย
def on_button_click():
    print("HI iM skiy IM a GOOD DEVELOPER")

root = tk.Tk()
root.title("Skiy's GUI Demo")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# === [ ส่วนนี้คือคอมโพเนนต์ที่สไกด์ทดสอบ สามารถเปิดใช้งานได้เลย ] ===
# canvas_test = tk.Canvas(frame, width=400, height=400)
# canvas_test.pack()
# canvas_test.create_rectangle(100, 50, 200, 100, fill="skyblue")
# canvas_test.create_text(150, 75, text="Tkinter", font=("Arial", 16))

# my_label = tk.Label(frame, text="HI iM skiy IM a GOOD DEVELOPER")
# my_label.pack()

# button = tk.Button(frame, text="click me", command=on_button_click)
# button.pack()

# user_entry = tk.Entry(frame)
# user_entry.pack()

# check_button = tk.Checkbutton(frame, text="check me")
# check_button.pack()

# radio_button = tk.Radiobutton(frame, text="radio me")
# radio_button.pack()

# item_listbox = tk.Listbox(frame)
# item_listbox.insert(1, "Python")
# item_listbox.insert(2, "Java")
# item_listbox.insert(3, "C++")
# item_listbox.insert(4, "HTML")
# item_listbox.insert(5, "Lua")
# item_listbox.pack()

# spin_box = tk.Spinbox(frame, from_=0, to=10)
# spin_box.pack()

# slider = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL)
# slider.pack()
# ==========================================================

# ส่วนแสดงผลหลัก (Main Display)
label = tk.Label(frame, text="Hello", fg="blue", font=("Arial", 24))
label.pack(pady=5)

canvas = tk.Canvas(frame, width=400, height=400, bg="white") # ใส่พื้นหลังสีขาวให้เห็นรูปชัดขึ้น
canvas.pack()

canvas.create_rectangle(50, 50, 150, 150, fill="red")
canvas.create_oval(200, 50, 300, 150, fill="green")
canvas.create_line(50, 200, 150, 300, fill="blue", width=3)
canvas.create_text(200, 200, text="Canvas Demo", font=("Arial", 16), fill="purple")

# if messagebox.askquestion("Question", "Do you like this demo?") == 'yes':
#     print("User likes the demo!")

root.mainloop()