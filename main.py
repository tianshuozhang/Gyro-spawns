
from compute import compute
#航行体的外部
import tkinter as tk
def process_data():
    root.withdraw()
    # 从输入框中获取用户输入的数据
    r1 = int(entry1.get())
    r2 = int(entry2.get())
    r3 = int(entry3.get())
    h1 = int(entry4.get())
    h2 = int(entry5.get())
    h3 = int(entry6.get())
    output=entry7.get()
    compute(r1,r2,r3,h1, h2, h3,output)
    # 在标签中显示用户输入的数据
    output_label.config(text="用户输入的数据为: " + output)
    root.deiconify()

# 创建主窗口
root = tk.Tk()
root.title("用户数据输入示例")

# 创建标签
label1 = tk.Label(root, text="请输入数据r1：")
label1.grid(row=0, column=0)# 创建输入框
entry1 = tk.Entry(root)
entry1.grid(row=0,column=1)

# 创建标签
label2 = tk.Label(root, text="请输入数据r2：")
label2.grid(row=1, column=0)# 创建输入框
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)

# 创建标签
label3 = tk.Label(root, text="请输入数据r3：")
label3.grid(row=2,column=0)
# 创建输入框
entry3 = tk.Entry(root)
entry3.grid(row=2,column=1)

# 创建标签
label4 = tk.Label(root, text="请输入数据h1：")
label4.grid(row=3,column=0)
# 创建输入框
entry4 = tk.Entry(root)
entry4.grid(row=3,column=1)

# 创建标签
label5 = tk.Label(root, text="请输入数据h2：")
label5.grid(row=4,column=0)
# 创建输入框
entry5 = tk.Entry(root)
entry5.grid(row=4,column=1)

# 创建标签
label6 = tk.Label(root, text="请输入数据h3：")
label6.grid(row=5,column=0)
# 创建输入框
entry6 = tk.Entry(root)
entry6.grid(row=5,column=1)

# 创建标签
label7 = tk.Label(root, text="请输入数据文件名：")
label7.grid(row=6,column=0)
# 创建输入框
entry7 = tk.Entry(root)
entry7.grid(row=6,column=1)

# 创建按钮
button = tk.Button(root, text="处理数据", command=process_data)
button.grid(row=7,column=0,columnspan=2)

# 创建用于显示输出的标签
output_label = tk.Label(root, text="")
output_label.grid(row=8,column=0,columnspan=2)

# 启动主循环
root.mainloop()


