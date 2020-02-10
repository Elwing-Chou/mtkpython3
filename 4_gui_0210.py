# 創造Frame -> 創造元件(Frame) -> 元件.pack()
import tkinter as tk
from jieba.analyse import extract_tags
def analyse():
    global t1
    global result
    text = t1.get("1.0", "end")
    result["text"] = str(extract_tags(text, 5))


window = tk.Tk()
window.geometry("500x500+200+200")
f1 = tk.Frame(window)
f1.pack()
l1 = tk.Label(f1, text="請輸入文章:")
l1.pack()
t1 = tk.Text(f1)
t1.pack()
b1 = tk.Button(f1, text="請點我分析", command=analyse)
b1.pack(expand=True, fill=tk.BOTH)
result = tk.Label(f1, text="按上面按鈕得到關鍵詞")
result.pack()
tk.mainloop()