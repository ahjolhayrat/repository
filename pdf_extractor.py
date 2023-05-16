from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams
import os


def extract_text_from_pdf(pdf_path):
    laparams = LAParams()
    text = ''

    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for element in page_layout:
            if hasattr(element, "get_text"):
                text += element.get_text()

    return text


def save_text(text, output_folder, output_filename):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    with open(f'{output_folder}/{output_filename}', 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    pdf_path = 'E:/Tanlab/articles/PGC expansion/Long-term expansion with germline potential of human primordial germ cell-like cells in vitro(1).pdf'  # 替换为你的PDF文件路径
    output_folder = 'output'  # 保存提取内容的文件夹
    output_filename = 'extracted_text.txt'  # 输出纯文本文件的名称

    text = extract_text_from_pdf(pdf_path)
    save_text(text, output_folder, output_filename)
    print("提取完成!")
