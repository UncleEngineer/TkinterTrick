import win32ui
import win32print
import win32api


def out(s):
    print (s)


def PrinterTest(s):
    out("win32ui printing test")
    th = 100
    x = 50
    y = 50

    lines = s.split("\n")

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC("Brother MFC-L2700D series")    #! change printer name

    hDC.StartDoc("Python Printer Test")
    hDC.StartPage()
    for line in lines:
        hDC.TextOut(x, y, line)
        y += th

    hDC.EndPage()
    hDC.EndDoc()

def printpdf():
    filename ='test.pdf'
    win32api.ShellExecute (
      0,
      "print",
      filename,
      #
      # If this is None, the default printer will
      # be used anyway.
      #
      '/d:"%s"' % win32print.GetDefaultPrinter (),
      ".",
      0
    )

#PrinterTest('Test')
printpdf()