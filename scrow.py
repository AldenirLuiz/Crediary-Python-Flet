from tkinter import *

root = Tk()
root.geometry('400x400')
container = Frame(root)
canvas = Canvas(container)

scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

count = 0
for linha in range(16):
    frm_0 = Frame(scrollable_frame)
    for n in range(4):
        label_ = Label(frm_0, text=f'Label_{count:2.2f}')
        label_.pack(expand=1, fill='both')
        count += 1
    frm_0.pack()

container.pack(expand=1, fill='both')
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
