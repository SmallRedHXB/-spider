
from tkinter import Tk, Button, Entry, Label, Text, END
import pyYouDao
import json


# dict = {"type":"ZH_CN2EN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"123","tgt":"123"}]]}
# print(dict['translateResult'])
def Sub():
    res = pyYouDao.Search(ent.get())
    # print(res)
    res = json.loads(bytes.decode(res))
    # print(res['translateResult'][0][0]['tgt'])
    text.delete(1.0, END)
    text.insert(1.0, res['translateResult'][0][0]['tgt'])


window = Tk()
window.title('hxb词典')
window.geometry("300x400+600+250")

ent = Entry(window)
ent.place(x=10,y=10,width=220, height=30)

sub = Button(window, text = '翻译', command = Sub)
sub.place(x=235,y=10,width=55, height=30)

lab = Label(window, text = '翻译结果：')
lab.place(x=10,y=50)

text = Text(window, background='#ccc')
text.place(x=10,y=75,width=280, height=315)


window.mainloop()