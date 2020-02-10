import tkinter as tk
from model import *
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class QueryFrame(tk.LabelFrame):
    def __init__(self, root, engine):
        tk.LabelFrame.__init__(self, root, text="輸入學生姓名")
        self.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)
        self.session = sessionmaker(bind=engine)()
        self.init_elements()

    def init_elements(self):
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.btn = tk.Button(self, text="點擊查詢",
                                   command=self.query)
        self.btn.pack()
        self.result = tk.Label(self, text="點上方按鈕")
        self.result.pack()

    def query(self):
        print(self.e1.get())

fn = os.path.join(os.path.dirname(__file__), "data.sqlite")
fn = "sqlite:///" + fn
engine = create_engine(fn, echo=False)
window = tk.Tk()
window.geometry("500x500+250+250")
QueryFrame(window, engine)
tk.mainloop()