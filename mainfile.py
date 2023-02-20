from play import *
from time import *
set_backdrop('gray')
class Sprite_walk():
    def __init__(self,x,y,hp,sp) -> None:
        self.x = x
        self.y = y
        self.hp = hp
        self.sp = sp
        self.hello_up = 0
        self.hello_down = 0
        self.hello_side = 0
        self.img_up = ['baba_up1.png','baba_up2.png','baba_up3.png','baba_up4.png','baba_up5.png','baba_up6.png']
        self.img_down = ['baba_down1.png','baba_down2.png','baba_down3.png','baba_down4.png','baba_down5.png','baba_down6.png','baba_down7.png']
        self.img_side = ['baba_left1.png','baba_left2.png','baba_left3.png','baba_left4.png','baba_left5.png','baba_left6.png','baba_left7.png','baba_left8.png','baba_left9.png','baba_left10.png','baba_left11.png','baba_left12.png','baba_left13.png','baba_left14.png','baba_left15.png']
        self.img_current = 'baba_down4.png'
        self.sprite = new_image(self.img_current,self.x,self.y,1000,0,100)
    def control(self):
        if key_is_pressed('s'):
            self.y -= 10
            if self.hello_down < 6:
                self.hello_down += 1
            else:
                self.hello_down = 0
            self.image_current = self.img_down[self.hello_down]
        elif key_is_pressed('w'):
            self.y += 10
            if self.hello_up < 5:
                self.hello_up += 1
            else:
                self.hello_up = 0
            self.image_current = self.img_up[self.hello_up]
        elif key_is_pressed('a'):
            self.x -= 10
            if self.hello_side < 14:
                self.hello_side += 1
            else:
                self.hello_side = 0
            self.image_current = self.img_side[self.hello_side]
        elif key_is_pressed('d'):
            self.x += 10
#            if self.hello_down < 6:
#                self.hello_down += 1
#            else:
#                self.hello_down = 0
#            self.image_current = self.img_down[self.hello_down]
    def update(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.image = self.img_current
herio = Sprite_walk(0,0,1,0)
@repeat_forever
def game():
    herio.control()
    herio.update()
start_program()