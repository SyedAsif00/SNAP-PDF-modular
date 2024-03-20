from PyPDF2 import PdfReader, PdfWriter
from xlsxHandler import readAndConvertToDict
from helper import map_fields
from sample import sample_data
from write_to_pdf import write_name_on_pdf
import fitz
import locations

def fill_pdf_fields(input_pdf_path, output_pdf_path, mapped_data):
    # Open the PDF with fitz
    doc = fitz.open(input_pdf_path)

    # Iterate over each item in the mapped_data dictionary
    for field, data in mapped_data.items():
        # Get the corresponding field information from the locations dictionary
        field_info = locations.pdf_locs.get(field)
        # If field is not found, continue to next item
        if not field_info:
            continue

        # Get the page number and page object
        page_number = field_info["page"] - 1
        page = doc[page_number]

        # Handle different field types
        if field_info["type"] == "Text Field":
            # For text fields, insert the text
            position = field_info["position"]
            text_position = fitz.Point(position["x0"], position["y0"])
            page.insert_text(text_position, str(data["value"]), fontsize=12, color=fitz.utils.getColor("black"))

        elif field_info["type"] == "Checkbox":
            # Calculate the center position of the checkbox
            center_x = (field_info["position"]["x0"] + field_info["position"]["x1"]) / 2
            center_y = (field_info["position"]["y0"] + field_info["position"]["y1"]) / 2
            # Check if the value indicates the box should be checked
            if data["value"] == "check":
                # Insert an "X" to indicate the checkbox is selected
                page.insert_text((center_x, center_y), "x", fontsize=12, color=fitz.utils.getColor("black"))

    # Save the filled PDF to a new file
    doc.save(output_pdf_path)
    # Close the document
    doc.close()

# Example usage
if __name__ == "__main__":
    input_pdf = "template2.pdf"
    output_pdf = "output.pdf"
    # Assume sampledata and map_fields are defined elsewhere
    mapped_data = map_fields(sample_data)
    # Now fill in the PDF
    fill_pdf_fields(input_pdf, output_pdf, mapped_data)