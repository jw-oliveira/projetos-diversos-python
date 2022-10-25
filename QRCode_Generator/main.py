from tkinter import *
from PIL import ImageTk, Image
import qrcode


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Calibri', '10')
        self.firstContainer = Frame(master)
        self.firstContainer['pady'] = 15
        self.firstContainer['bg'] = '#18191A'
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer['padx'] = 20
        self.secondContainer['bg'] = '#18191A'
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer['padx'] = 20
        self.thirdContainer['pady'] = 20
        self.thirdContainer['bg'] = '#18191A'
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer['padx'] = 20
        self.fourthContainer['bg'] = '#18191A'
        self.fourthContainer.pack()        

        self.titulo = Label(self.firstContainer, text='QR CODE GENERATOR')
        self.titulo['bg'] = '#18191A'
        self.titulo['fg'] = '#E4E6EB'
        self.titulo['font'] = ('Calibri', '11', 'bold')
        self.titulo.pack()

        self.textEntry = Entry(self.secondContainer, text='aa')
        self.textEntry['width'] = 20
        self.textEntry['font'] = self.fontePadrao
        self.textEntry.pack()

        self.generateButton = Button(self.thirdContainer)
        self.generateButton['text'] = 'Gerar QR CODE'
        self.generateButton['font'] = ('Calibri', '10')
        self.generateButton['width'] = 15
        self.generateButton['bg'] = '#3A3B3C'
        self.generateButton['fg'] = '#E4E6EB'
        self.generateButton['command'] = self.generate_qrcode
        self.generateButton.pack()

    
    def open_img(self):        
        img = ImageTk.PhotoImage(Image.open('QR Code Generator\Output\qrimg.png'))
        panel = Label(self.fourthContainer, image = img)
        panel.photo = img
        panel.pack()


    def generate_qrcode(self):

        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 2,
        )

        qr.add_data(self.textEntry.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('QR Code Generator\Output\qrimg.png')
       
        self.open_img()


gui = Tk()
gui.title('QR Code Generator')
gui.geometry('400x440')
gui.config(bg='#18191A')
Application(gui)
gui.mainloop()
