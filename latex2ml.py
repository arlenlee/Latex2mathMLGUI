# -*- coding: utf-8 -*-
"""
@Time: 2020/7/26 0026 14:44
@Author: Arlen Lee
"""
from tkinter import messagebox
import latex2mathml.converter
import pyperclip as pp
import tkinter
import re

class Covert:
    def parser_latex(latex_string):
        latex_input = latex_string
        mathml_output = latex2mathml.converter.convert(latex_input)
        pp.copy(mathml_output)
def main():
    app = tkinter.Tk()
    app.title('Latex转换器')
    app.iconbitmap(r'math.ico')
    app.geometry("260x50")
    App(app)
    app.mainloop()

class App:
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.covert = tkinter.Button(frame, text ="covert",
                                     command = self.get_text)
        self.covert.pack(side=tkinter.LEFT)
        self.about = tkinter.Button(frame, text ="About",
                                    command = self.About)
        self.about.pack(side=tkinter.RIGHT)

    def get_text(self):
        text=pp.paste()
        r1 = re.search('^(\$\$)(.*)(\$\$)$', text)
        r2 = re.search('(^\$)(.*)(\$$)', text)
        if  r1 is not None:
            return  Covert.parser_latex(r1.group(2))
        elif r2 is not None:
            return Covert.parser_latex(r2.group(2))
        else:
            pp.copy('非公式')
    def About(self):
        messagebox.askyesno('关于 ',
                            '使用本软件默认同意以下条款\n '
                            '软件有且仅有latex转换一个功能\n '
                            '1. 软件为本人兴趣所做不负一切责任\n '
                            '2. 如若文件丢失中毒等非本软件所涵盖功能\n'
                            '3. 如果你想增加功能请您忍住\n'
                            '如果你有好的点子可以联系我\n'
                            'arlenlee#foxmail.com')
if __name__ == '__main__':
    main()