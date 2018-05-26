def test_24_PieCharts():
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
    from reportlab.pdfbase import pdfmetrics
    from reportlab.graphics.shapes import Drawing
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.graphics.charts.piecharts import Pie

    pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))
    stylesheet = getSampleStyleSheet()

    elements = []
    doc = SimpleDocTemplate("demo.pdf")

    elements.append(Paragraph('<font name="chsFont">ทดสอบ</font>', stylesheet['Title']))
    elements.append(Spacer(1,1*inch))

    d = Drawing(400,200)
    data = [13,5,20,22,37,45]
    pc = Pie()
    pc.x = 65
    pc.y = 15
    pc.width = 150
    pc.height = 150
    pc.data = data
    pc.labels = ['a','b','c','d','e','f']
    d.add(pc)

    elements.append(d)

    doc.build(elements)
        
test_24_PieCharts()
print("Success")
