from tkinter import Tk
from tkinter.filedialog import askopenfilename
from gtts import gTTS
import PyPDF2


Tk().withdraw()
filename = askopenfilename()

text = ""

obj = open(filename,'rb')

reader = PyPDF2.PdfFileReader(obj)

pages = reader.numPages

for i in range(0,int(pages)):
    obj1 = reader.getPage(i)
    text += obj1.extractText()

tts = gTTS(text=text,lang='en',tld='com')

tts.save("audio.mp3")

obj.close()
