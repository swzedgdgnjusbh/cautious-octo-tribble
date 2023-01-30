from play import *
from random import *
from time import *
set_backdrop('black')
ramka = new_box('gray',0,0,1000,1000,'orange',10)
class Cubo():
    def __init__(self,x,y,color,letter,number) -> None:
        self.x = x
        self.x_list = [self.x]
        self.y = y
        self.y_list = [self.y]
        self.color = color
        self.color_list = [self.color]
        self.set_color_list = ['red','orange','yellow','green','cyan','blue','purple','pink','brown','black']
        self.cube = new_box(self.set_color_list[self.color],-350+350*self.x,350-350*self.y,350,350,'gray',5,0,100,100)
        self.letter = letter
        self.letter_list = [self.letter]
        self.set_letter_list = ['A','B','C','D','E','F','G','H','I','J']
        self.number = number
        self.number_list = [self.number]
        self.let = new_text(self.set_letter_list[self.letter]+'  '+str(self.number),-350+350*self.x,350-350*self.y,None,150,'black',0,100,100)
    def update(self):
        self.cube.x = -350+350*self.x
        self.cube.y = 350-350*self.y
        #self.cube.color = self.set_color_list[self.color]
        self.cube.color = self.color_list[-1]
        self.let.x = -350+350*self.x
        self.let.y = 350-350*self.y
        self.let.words = self.set_letter_list[self.letter]+'  '+str(self.number)
    def new_value(self):
        self.x = randint(0,2)
        self.x_list.append(self.x)
        self.y = randint(0,2)
        self.y_list.append(self.y)
        self.color = randint(0,9)
        self.color_list.append(self.set_color_list[self.color])
        self.letter = randint(0,9)
        self.letter_list.append(self.set_letter_list[self.letter])
        self.number = randint(0,9)
        self.number_list.append(str(self.number))
        print(self.color_list)
empty_list = []
secret_x = randint(0,2)
secret_y = randint(0,2)
for j in range(3):
    for i in range(3):
        b1 = new_box('white',-350+350*i,350-350*(j),350,350,'gray',5)
        empty_list.append(b1)
cuba = Cubo(2,2,5,0,4)
@repeat_forever
def game():
    sleep(2)
    cuba.new_value()
    cuba.update()
start_program()