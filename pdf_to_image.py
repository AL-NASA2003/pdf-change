import io
from PyPDF2 import PdfReader
from PIL import Image, ImageDraw, ImageFont


def pdf_to_image(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        if len(pdf_reader.pages)!= 1:
            raise ValueError("Only single - page PDFs are supported.")
        page = pdf_reader.pages[0]
        xObject = page['/Resources']['/XObject'].get_object()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].get_data()
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"
                img = Image.open(io.BytesIO(data))
                img = img.convert('RGB')
                return img


if __name__ == "__main__":
    pdf_path = "追求理想，共建美好大学生活演讲稿.pdf"
    img = pdf_to_image(pdf_path)
    if img:
        img.save("output.jpg", "JPEG")

