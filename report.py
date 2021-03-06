from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
#Add font
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
 
########################################################################
class Test(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()
 
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
 
    #----------------------------------------------------------------------
    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate("test.pdf",pagesize=A4, rightMargin=30,leftMargin=30, topMargin=50,bottomMargin=18)
        self.story = [Spacer(1, 1*cm)]
        self.createLineItems()
 
        self.doc.build(self.story, onFirstPage=self.createDocument)
        print ("finished!")
 
    #----------------------------------------------------------------------
    def createDocument(self, canvas, doc):
        """
        Create the document
        """
        pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))

        self.c = canvas
        normal = self.styles["Title"]
 
        header_text = "<b>This is a test header</b>"
        p = Paragraph(header_text, normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(30, 12, mm))
 
        ptext = """<font name='chsFont'>ให้ใส่เครื่องหมายถูกในช่องวัสดุ</font>"""
 
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(30, 20, mm))
 
 
    #----------------------------------------------------------------------
    def createLineItems(self):
        """
        Create the line items
        """
        pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))
        stylesheet = getSampleStyleSheet()

        # container for the "Flowable" objects
        elements = []
        styles=getSampleStyleSheet()
        styleN = styles["Normal"]
        styleT = styles["Title"]


        style_center = ParagraphStyle(name='right', parent=styles['Normal'], fontName='chsFont',
                        fontSize=13, alignment=TA_CENTER)
        # styleN.fontSize = 15
        # styleN.alignment=TA_JUSTIFY

        TH15 = ParagraphStyle(name='TH12', fontName='chsFont', fontSize=15, alignment=TA_JUSTIFY)





        # Make heading for each column and start data list
        CH1 = Paragraph("<font size=10 name='chsFont'>ลำดับ</font>", styleT)
        CH2 = Paragraph("<font name='chsFont'>วัสดุ</font>", styleT)
        CH3 = Paragraph("<font name='chsFont'>อุปกรณ์</font>", styleT)
        Ch4 = Paragraph("<font name='chsFont'>รายการและเหตุผลการสั่งซื้อ</font>", styleT)
        # Assemble data for each column using simple loop to append it into data list
        data = [[CH1,CH2,CH3,Ch4]]

        textlist = [['1','','/','แผ่นเจียร์ยาว 4 นิ้ว'],[2,'/','','ลวดเชื่อม']]

        count = len(textlist)

        for i in range(count):
            t1 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][0]),styleN)
            t2 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][1]),styleN)
            t3 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][2]),styleN)
            t4 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][3]),style_center)
            data.append([t1,t2,t3,t4])
 
        tableThatSplitsOverPages = Table(data, [2 * cm, 2 * cm, 2 * cm, 10 * cm], repeatRows=2)

        tableThatSplitsOverPages.hAlign = 'LEFT'

        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(0,-1),1,colors.black)])

        style2 = TableStyle([  ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                                ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('VALIGN',(0,0),(-1,-1),'TOP'), 
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ])

        # tblStyle.add('BACKGROUND',(0,0),(1,0),colors.white)
        # tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)

        tableThatSplitsOverPages.setStyle(style2)
 
        self.story.append(tableThatSplitsOverPages)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    t.run()