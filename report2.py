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
    def run(self,filename,data):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate(filename,pagesize=A4, rightMargin=30,leftMargin=30, topMargin=50,bottomMargin=18)
        self.story = [Spacer(1, 1*cm)]
        self.createLineItems(data)
 
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
 
        header_text = "<font name='chsFont'><b>บริษัท มาล์เทครับเบอร์ จำกัด</b></font>"
        p = Paragraph(header_text, normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(0, 12, mm))
 
        ptext = """<font name='chsFont'>แบบฟอร์มแจ้งการสั่งซื้อที่ออฟฟิศ</font>"""
 
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(0, 20, mm))
 
        ptext = """<font name='chsFont'>หมายเหตุ</font>"""
        
        normal.fontSize = 12
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(-70, 120, mm))
    #----------------------------------------------------------------------
    def createLineItems(self,datatext):
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





        # Header of Table
        CH1 = Paragraph("<font size=13 name='chsFont'>ลำดับ</font>", styleT)
        CH2 = Paragraph("<font size=13 name='chsFont'>วัสดุ</font>", styleT)
        CH3 = Paragraph("<font size=13 name='chsFont'>อุปกรณ์</font>", styleT)
        CH4 = Paragraph("<font size=13 name='chsFont'>รายการและเหตุผลการสั่งซื้อ</font>", styleT)
        CH5 = Paragraph("<font size=13 name='chsFont'>ราคา(ประมาณ)</font>", styleT)
        CH6 = Paragraph("<font size=13 name='chsFont'>ซื้อล่าสุดเมื่อ</font>", styleT)
        CH7 = Paragraph("<font size=13 name='chsFont'>จำนวณที่สั่ง</font>", styleT)


        
        data = [[CH1,CH2,CH3,CH4,CH5,CH6,CH7]]


        # Data of Table
        textlist = datatext
        #[['1','','/','แผ่นเจียร์ยาว 4 นิ้ว'],[2,'/','','ลวดเชื่อม']]

        count = len(textlist)

        for i in range(count):
            t1 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][0]),styleN)
            t2 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][1]),styleN)
            t3 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][2]),styleN)
            t4 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][3]),styleN)
            t5 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][4]),styleN)
            t6 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][5]),styleN)
            t7 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][6]),styleN)
            data.append([t1,t2,t3,t4,t5,t6,t7])
 
        tableThatSplitsOverPages = Table(data, [1 * cm, 1 * cm, 1 * cm, 7 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm], repeatRows=1)

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
                               ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
                               ('BOX', (0,0), (-1,-1), 1, colors.black),
                               ])

        # tblStyle.add('BACKGROUND',(0,0),(1,0),colors.white)
        # tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)

        tableThatSplitsOverPages.setStyle(style2)
 
        self.story.append(tableThatSplitsOverPages)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    sparepart = [['1','','/','แผ่นเจียร์ยาว 4 นิ้ว'],[2,'/','','ลวดเชื่อม']]
    t.run('test4.pdf',sparepart)