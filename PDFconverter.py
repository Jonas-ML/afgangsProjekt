from fpdf import FPDF

class TextToPDF:
    def __init__(self, title):
        self.pdf = FPDF()
        self.title = title
        self.setup_document()
    
    
    def setup_document(self):
        self.pdf.add_page() # Add the root page

        self.pdf.set_title(self.title)
        self.pdf.set_font("Arial", size=12)
        
        self.add_title() # Sets the graphical title
        
    def add_title(self):
        self.pdf.set_font("Arial", 'B', 20)
        self.pdf.cell(0, 10, self.title, 0, 1, 'C') # Formatting of the title
        self.pdf.ln(10) # Adds a line break after the  title
    
    def add_text(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, text) # Makes auto line breaks based on text
        
    def createPDF(self, text, name):
        self.add_text(text)
        self.pdf.output(name)
    

