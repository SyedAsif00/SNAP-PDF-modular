import fitz  # PyMuPDF

def write_name_on_pdf(pdf_path, output_pdf_path, name, x, y, page_number=0):
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Select the page
    page = doc[page_number]  # page numbering starts from 0
    
    # Text settings
    text = name  # The text to insert
    fontsize = 11  # font size
    color = fitz.utils.getColor("black")  # text color
    
    # Define the text's position and properties
    text_position = fitz.Point(x+10, y+20)
    
    # Write the name at the specified position
    page.insert_text(text_position, text, fontsize=fontsize, color=color)
    
    # Save the changes to a new PDF file
    doc.save(output_pdf_path)
    doc.close()