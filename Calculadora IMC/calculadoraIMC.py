from tkinter import *

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
        self.thirdContainer['bg'] = '#18191A'
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer['pady'] = 20
        self.fourthContainer['bg'] = '#18191A'
        self.fourthContainer.pack()

        self.fifithContainer = Frame(master)
        self.fifithContainer['bg'] = '#18191A'
        self.fifithContainer.pack()

        self.titulo = Label(self.firstContainer, text='CALCULADORA IMC')
        self.titulo['bg'] = '#18191A'
        self.titulo['fg'] = '#E4E6EB'
        self.titulo['font'] = ('Calibri', '11', 'bold')
        self.titulo.pack()

        self.pesoLabel = Label(self.secondContainer, text='Peso')
        self.pesoLabel['font'] = self.fontePadrao
        self.pesoLabel['bg'] = '#18191A'
        self.pesoLabel['fg'] = '#E4E6EB'
        self.pesoLabel.pack(side=LEFT)

        self.peso = Entry(self.secondContainer)
        self.peso['width'] = 10
        self.peso['font'] = self.fontePadrao
        self.peso.pack(side=RIGHT)

        self.alturaLabel = Label(self.thirdContainer, text='Altura')
        self.alturaLabel['font'] = self.fontePadrao
        self.alturaLabel['bg'] = '#18191A'
        self.alturaLabel['fg'] = '#E4E6EB'
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.thirdContainer)
        self.altura['width'] = 9
        self.altura['font'] = self.fontePadrao
        self.altura.pack(side=RIGHT)

        self.calcular = Button(self.fourthContainer)
        self.calcular['text'] = 'Calcular IMC'
        self.calcular['font'] = ('Calibri', '10')
        self.calcular['width'] = 15 
        self.calcular['bg'] = '#3A3B3C'
        self.calcular['fg'] = '#E4E6EB'
        self.calcular['command'] = self.calculaimc
        self.calcular.pack()

        self.message1 = Label(self.fifithContainer, text='')
        self.message1['bg'] = '#18191A'
        self.message1['fg'] = '#E4E6EB'
        self.message1.pack()

        self.message2 = Label(self.fifithContainer, text='')
        self.message2['bg'] = '#18191A'
        self.message2['fg'] = '#E4E6EB'
        self.message2.pack()        
       

    def calculaimc(self):
        try:
            peso = float(self.peso.get())
            self.message1['text'] = ''                
        except:
            self.message1['text'] = 'Erro! Valor do peso inválido.'       
        try:
            altura = float(self.altura.get())
            self.message2['text'] = ''
        except:
            self.message2['text'] = 'Erro! Valor da altura inválido.'            

        imc = peso / (altura * altura)
            
        if imc < 17:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Muito abaixo do peso')
        elif imc < 18.49:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Abaixo do peso')
        elif imc < 24.99:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Peso normal')
        elif imc < 29.99:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Acima do peso')
        elif imc < 34.99:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Obesidade I')
        elif imc < 39.99:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Obesidade II')
        else:
            self.message1['text'] = (f'Valor do IMC: {imc:.2f}')
            self.message2['text'] = ('Classificação: Obesidade III (mórbida)')

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb    
    

gui = Tk()
gui.title('IMC')
gui.geometry('220x240')
gui.config(bg='#18191A')
Application(gui)
gui.mainloop()