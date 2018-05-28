import report2



data = [['1',' ','/','แผ่นเจียร์บาง 4 นิ้ว AC60','12.84/แผ่น','5/7/60','150']]
count = len(data)
countf = 9 - count

for i in range(countf):
	blank = ['-','　','　','　','　','　','　']

	if count < 9:
		data.append(blank)
	else:
		pass

t = report2.Test()
t.run('Report20.pdf',data)