import tkinter as tk

def click(event):
    global screen_val
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen_val.get()))
            screen_val.set(result)
        except Exception as e:
            screen_val.set("Error")
    elif text == "C":
        screen_val.set("")
    else:
        screen_val.set(screen_val.get() + text)

# Create window
root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

screen_val = tk.StringVar()
entry = tk.Entry(root, textvar=screen_val, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=4, height=2)
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
