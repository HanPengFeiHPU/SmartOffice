import os
from fpdf import FPDF
import fpdf
import tkinter as tk
import tkinter.messagebox
from html.parser import HTMLParser


class img2Pdf:
    def __init__(self,path,file_name_list):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(0)  # 自动分页设为False
        self.path = path
        self.file_name_list = file_name_list

    def __del__(self):
        pass

    def img_pdf(self):
        msg = "成功"
        try:
            self.file_name_list = self.file_name_list.split(',')

            for image in self.file_name_list:

                if os.path.isfile(self.path+'\\'+image):
                    self.pdf.add_page()
                    self.pdf.image(os.path.join(self.path, image), w=int(210*0.9), h=int(297*0.9))  # 指定宽高
                else:
                    msg = "失败：文件不存在" + image

            self.pdf.output(os.path.join(self.path, self.file_name_list[0]+".pdf"), "F")
        except Exception as e:
            msg = "失败："+e
        finally:
            return msg


class img2pdf_tkinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('IMG===》PDF')
        # 传值变量
        self.textVar_Path = tk.StringVar()
        self.textVar_Path.set('示例:'+r'D:\Img2Pdf')
        self.textVar_File = tk.StringVar()
        self.textVar_File.set('示例:001.jpg,002.jpg')
        self.msg = ""
        self.source_path = ""
        self.file_name_list = ""
        self.img2Pdf = img2Pdf(path=self.source_path, file_name_list=self.file_name_list)

    def __del__(self):
        pass
    def window(self):
        # 两个sticky=W实现第一列左对齐
        tk.Label(self.root, text='文件地址').grid(row=0, sticky=tk.W)

        tk.Label(self.root, text='图片名称').grid(row=1, sticky=tk.W)

        # rowspan=2可以让图片横跨2行

        photo = tk.PhotoImage(file='./640041e03e438197442f8c82a81acca1.png')

        tk.Label(self.root, image=photo).grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        tk.Entry(self.root,textvariable=self.textVar_Path).grid(row=0, column=1)

        tk.Entry(self.root,textvariable=self.textVar_File).grid(row=1, column=1)

        # columnspan=3可以让按钮横跨3列

        tk.Button(text='提交', width=10, command=self.getText).grid(row=2, columnspan=3, pady=5)

        tk.mainloop()

    def getText(self):
        self.source_path = self.textVar_Path.get().strip()
        self.file_name_list = self.textVar_File.get().strip().replace('，',',')
        self.img2Pdf = img2Pdf(path=self.source_path, file_name_list=self.file_name_list)
        self.msg = self.img2Pdf.img_pdf()
        if len(self.msg):
            if '失败' in self.msg:
                tkinter.messagebox.showerror('错误', self.msg)
            else:
                tkinter.messagebox.showinfo('提示', '转换成功')


if __name__ == '__main__':
    img2pdf_tkinter = img2pdf_tkinter()
    img2pdf_tkinter.window()
