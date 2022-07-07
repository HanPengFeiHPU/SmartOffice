# encoding=utf-8
from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_split(pdf_in,pdf_out,start,end):
    # 初始化一个pdf
    output = PdfFileWriter()
    # 读取pdf
    with open(pdf_in, 'rb') as in_pdf:
        pdf_file = PdfFileReader(in_pdf)
        # 从pdf中取出指定页
        for i in range(start, end):
            output.addPage(pdf_file.getPage(i))
        # 写出pdf
        with open(pdf_out, 'ab') as out_pdf:
            output.write(out_pdf)

if __name__ == '__main__':
    pdf_in = '2022年招生之友理科_2.pdf'
    pdf_out = '2022年招生之友理科_2_1.pdf'
    s, e = 385, 426  # 拆分的起始位置和结束位置
    pdf_split(pdf_in, pdf_out, s, e)