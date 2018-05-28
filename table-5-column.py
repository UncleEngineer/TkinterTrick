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



pdfReportPages = "thaitesttable.pdf"
doc = SimpleDocTemplate(pdfReportPages, pagesize=A4)
#Setting font
pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))
stylesheet = getSampleStyleSheet()

# container for the "Flowable" objects
elements = []
styles=getSampleStyleSheet()
styleN = styles["Normal"]

# Make heading for each column and start data list
CH1 = Paragraph("<font name='chsFont'>ลำดับ</font>", stylesheet['Title'])
CH2 = Paragraph("<font name='chsFont'>วัสดุ</font>", stylesheet['Title'])
CH3 = Paragraph("<font name='chsFont'>อุปกรณ์</font>", stylesheet['Title'])
Ch4 = Paragraph("<font name='chsFont'>รายการและเหตุผลการสั่งซื้อ</font>", stylesheet['Title'])
# Assemble data for each column using simple loop to append it into data list
data = [[CH1,CH2,CH3,Ch4]]

textlist = [('1','','/','แผ่นเจียร์ยาว 4 นิ้ว'),('2','/','','ลวดเชื่อม')]
count = len(textlist)

# for i in range(count):
# 	t1 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][0]),styleN)
# 	t2 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][1]),styleN)
# 	t3 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][2]),styleN)
# 	t4 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][3]),styleN)
#     data.append([t1,t2,t3,t4])
t3 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[1][2]),styleN)
t4 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[0][3]),styleN)

data.append(['','',t3,t4])

tableThatSplitsOverPages = Table(data, [1 * cm, 4 * cm], repeatRows=1)

tableThatSplitsOverPages.hAlign = 'LEFT'

tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                       ('BOX',(0,0),(-1,-1),1,colors.black),
                       ('BOX',(0,0),(0,-1),1,colors.black)])

tblStyle.add('BACKGROUND',(0,0),(1,0),colors.white)
tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)

tableThatSplitsOverPages.setStyle(tblStyle)

elements.append(tableThatSplitsOverPages)

doc.build(elements)
print('PDF was Generated')
