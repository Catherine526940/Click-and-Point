import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# 初始化窗口
root = tk.Tk()
root.title("图片处理")

# 全局变量
img = None
img_tk = None
draw = None
line_width = 5  # 设置线的宽度

# 加载图片
def load_image(image_path):
    global img, img_tk, draw
    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk
    draw = ImageDraw.Draw(img)  # 创建一个可以在img上绘图的对象

# 画线
def draw_line(event):
    global draw
    if draw is not None:
        x = event.x
        # 在点击的位置画一条竖直的白线，可以通过line_width调整线的粗细
        draw.line((x, 0, x, img.height), fill="white", width=line_width)
        # 更新图片显示
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

# 保存图片
def save_image():
    global img
    if img is not None:
        img.save("processed_image.png")
        tk.messagebox.showinfo("保存成功", "图片已保存为 processed_image.jpg")
    else:
        tk.messagebox.showinfo("错误", "没有加载图片")

# 创建图片标签
img_label = tk.Label(root)
img_label.pack()

# 创建按钮
load_button = tk.Button(root, text="加载图片", command=lambda: load_image("D:\\My_Table\\17.png"))
load_button.pack()

draw_button = tk.Button(root, text="画线", command=draw_line)
draw_button.pack()

save_button = tk.Button(root, text="保存图片", command=save_image)
save_button.pack()

# 绑定鼠标点击事件
img_label.bind("<Button-1>", draw_line)

root.mainloop()