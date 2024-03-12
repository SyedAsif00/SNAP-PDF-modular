from PyPDF2 import PdfReader, PdfWriter
from xlsxHandler import readAndConvertToDict
from helper import parse_name, map_fields
from sample import sampledata
from write_to_pdf import write_name_on_pdf
import fitz
import locations


def list_form_fields(pdf_path):
    reader = PdfReader(pdf_path)
    fields = reader.get_fields()   
    return fields


def fill_pdf_fields(input_pdf_path, output_pdf_path, data_dict):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    doc = fitz.open(input_pdf_path)

    # Copy over all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Update form fields
    for field, value in data_dict.items():
        # writer.update_page_form_field_values(writer.pages[0], {field: value})
        # Select the page
        p = locations.pdf_locs[field]

        page = doc[p["page"]-1]  # page numbering starts from 0
        x = p["position"]["x0"]
        y = p["position"]["y0"]
        print(p["page"], x, y, field, value)
        

        # Text settings
        text = value  # The text to insert
        fontsize = 12  # font size
        color = fitz.utils.getColor("black")  # text color

        # Define the text's position and properties
        text_position = fitz.Point(x + 10, y + 20)
    

        # Write the name at the specified position
        page.insert_text(text_position, text, fontsize=fontsize, color=color)

    doc.save(output_pdf_path)
    doc.close()


# fields = list_form_fields("template.pdf")
# print(fields)
# with open("data.txt", "w") as file:
#     for field in fields:
#         file.write(field)
#         file.write("    ")
#         file.write(str(fields[field]))
#         file.write("\n")


# # nameObj = parse_name(obj["Name, DOB, Address, Sex"])

input_pdf = "template2.pdf"
output_pdf = "output.pdf"
fill_pdf_fields(input_pdf, output_pdf, map_fields(sampledata))
########