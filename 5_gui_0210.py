# 創造Frame -> 創造元件(Frame) -> 元件.pack()
import tkinter as tk
from jieba.analyse import extract_tags

class JiebaFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.init_element()

    def init_element(self):
        self.l1 = tk.Label(self, text="請輸入文章:")
        self.l1.pack()
        self.t1 = tk.Text(self)
        self.t1.pack()
        self.b1 = tk.Button(self,
                            text="請點我分析",
                            command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH)
        self.result = tk.Label(self, text="按上面按鈕得到關鍵詞")
        self.result.pack()

    def analyse(self):
        text = self.t1.get("1.0", "end")
        self.result["text"] = str(extract_tags(text, 5))

window = tk.Tk()
window.geometry("500x500+200+200")
f1 = JiebaFrame(window)
f1.pack()
tk.mainloop()