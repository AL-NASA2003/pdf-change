import fitz

def pdf_to_image(pdf_path, output_path):
    """
    将单页 PDF 转换为图片
    :param pdf_path: PDF 文件的路径
    :param output_path: 输出图片的路径
    """
    try:
        # 打开 PDF 文件
        pdf_document = fitz.open(pdf_path)
        if len(pdf_document) != 1:
            raise ValueError("仅支持单页 PDF 文件。")
        # 获取第一页
        page = pdf_document[0]
        # 设置缩放比例以提高图片清晰度
        zoom_x = 2.0
        zoom_y = 2.0
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat)
        # 保存图片
        pix.save(output_path)
        pdf_document.close()
        print(f"PDF 已成功转换为图片，保存路径为: {output_path}")
    except Exception as e:
        print(f"转换过程中出现错误: {e}")


if __name__ == "__main__":
    pdf_path = "input.pdf"
    output_path = "output.png"
    pdf_to_image(pdf_path, output_path)