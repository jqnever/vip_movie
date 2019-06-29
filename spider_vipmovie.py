import requests
import re
import tkinter as tk
import webbrowser
url = 'http://www.qmaile.com/'
response = requests.get(url)
#response.encoding = 'utf-8' # response.apparent.encoding 自动获取他的编码格式
print(response.text)

reg = re.compile('<option value="(.*?)" selected="">')  #。*？万能匹配符
res = re.findall(reg, response.text)

print(res)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
six = res[5]

root = tk.Tk()
root.title('vip movie')
root.geometry('500x250') #100 100 是距离左上角的距离
l1 = tk.Label(root,text='播放接口：',font=12)
l1.grid(row=0,column=0)

var = tk.StringVar()
r1 = tk.Radiobutton(root, text='播放接口1',variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2',variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3',variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放接口4',variable=var, value=four)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放接口5',variable=var, value=five)
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='播放接口6',variable=var, value=six)
r6.grid(row=5, column=1)
l2 = tk.Label(root,text='播放连接：', font = 12)
l2.grid(row=6, column = 0)
e1 = tk.Entry(root,text='',width=50)
e1.grid(row=7, column=1)
def bf():
    webbrowser.open(var.get()+e1.get())
b1 = tk.Button(root,text='播放',font=12,width=8,command=bf)
b1.grid(row=8, column=1)

root.mainloop()
