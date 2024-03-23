from PyPDF2 import PdfReader, PdfWriter
from xlsxHandler import readAndConvertToDict
from helper import map_fields
from sample import sample_data
from write_to_pdf import write_name_on_pdf
import fitz
import locations

def fill_pdf_fields(input_pdf_path, output_pdf_path, mapped_data):
    doc = fitz.open(input_pdf_path)

    for field, data in mapped_data.items():
        field_info = locations.pdf_locs.get(field)
        if not field_info:
            continue

        page_number = field_info["page"] - 1
        page = doc[page_number]

        if field_info["type"] == "Text Field":
            position = field_info["position"]
            text_position = fitz.Point(position["x0"], position["y0"])
            page.insert_text(text_position, str(data["value"]), fontsize=12, color=fitz.utils.getColor("black"))

        elif field_info["type"] == "Checkbox":
            center_x = (field_info["position"]["x0"] + field_info["position"]["x1"]) / 2
            center_y = (field_info["position"]["y0"] + field_info["position"]["y1"]) / 2
            if data["value"] == "x":
                page.insert_text((center_x, center_y), "x", fontsize=12, color=fitz.utils.getColor("black"))

    doc.save(output_pdf_path)
    doc.close()


if __name__ == "__main__":
    input_pdf = "template2.pdf"
    output_pdf = "output.pdf"
    mapped_data = map_fields(sample_data)
    fill_pdf_fields(input_pdf, output_pdf, mapped_data)