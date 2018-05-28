import io

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import TableStyle


def make_doc():
    pdf = io.BytesIO()
    
    doc = SimpleDocTemplate(pdf, pagesize=letter)

    story = []

    data= [['00', '01', '02', '03', '04'],
     ['10', '11', '12', '13', '14'],
     ['20', '21', '22', '23', '24'],
     ['30', '31', '32', '33', '34']]
    
    t=Table(data)
    
    t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2), colors.green),
     ('TEXTCOLOR',(0,0),(1,-1), colors.red)]))

    story.append(t)

    doc.build(story)
    pdf.seek(0)

    return pdf


if __name__ == "__main__":
    pdf = make_doc()