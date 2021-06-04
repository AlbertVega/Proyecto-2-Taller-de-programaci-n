import pygame , random
pygame.init()
#pygame.mixer.init() #PARA AGREGAR EL SONIDO 


#DEFINIR LOS COLORES
BLACK=(0,0,0)
WHITE =(255,255,255)
GREEN=(0,255,0)
RED= (255,0,0)
BLUE= (0,0,255) 


#TAMAÑO DE LA VENTANA
WIDTH= 850
HEIGHT= 638
#CREAR UNA VENTANA
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock= pygame.time.Clock()

#SE COLOCA EL NOMBRE DE JUEGO Y EL ICONO EN LA VENTANA
pygame.display.set_caption("The Fish Adventure")
icon = pygame.image.load("PNG/Jugador1.png")
pygame.display.set_icon(icon)

#AGREGAR MUSICA DE FONDO
pygame.mixer.music.load("PNG/Music.mp3")
pygame.mixer.music.play(1)


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PNG/Jugador1.png").convert()   #AGREGAR LA IMAGEN
        self.image.set_colorkey(BLACK)   #SE ELIMINA EL COLOR DE FONDO
        self.rect = self.image.get_rect()  #POSICIONAR EL SPRITE
        self.rect.centerx = WIDTH // 2     #MOSTRARLA EN PANTALLA
        self.rect.bottom = HEIGHT - 55
        self.speed_x = 0 #VELOCIDAD CON LA QUE SE MOVERA 
        self.speed_y = 0

#FUNCION PARA EL MOVIMIENTO DEL JUGADOR POR MEDIO DE LAS TECLAS IZQ,DER,ABAJO,ARRIBA
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()  #VER SI UNA TECLA HA SIDO PRESIONADA
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        if keystate[pygame.K_UP]:
            self.speed_y = -6
        if keystate[pygame.K_DOWN]:
            self.speed_y = 6
        self.rect.x += self.speed_x  #SUMAR LA VELOCIDAD, ACTUALIZARLO
        self.rect.y += self.speed_y
        #PARA QUE EL JUGADOR NO SE DESPLAZE MAS ALLA DEL LIMITE DE LA VENTANA
        #LIMITA EL MARGEN DERECHO E IZQUIERDO
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        #LIMITA EL MARGEN INFERIOR Y SUPERIOR
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Tiburon1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PNG/tiburon11.png").convert()   #AGREGAR LA IMAGEN
        self.image.set_colorkey(BLACK)   #SE ELIMINA EL COLOR DE FONDO
        self.rect = self.image.get_rect()  #POSICIONAR EL SPRITE
        self.rect.x = random.randrange(WIDTH-self.rect.width) #VELOCIDAD CON LA QUE SE MOVERA 
        self.rect.y = random.randrange(HEIGHT-self.rect.height)
        self.speed_x = random.randrange(1,4)   #VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
        self.speed_y = random.randrange(1,4)
    
    def update(self):
        #ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        #LIMITA EL MARGEN DERECHO E IZQUIERDO
        if self.rect.right > WIDTH:
            self.speed_x -=1  #PARA QUE REBOTE
        if self.rect.left < 0:
            self.speed_x +=1

        #LIMITA EL MARGEN INFERIOR Y SUPERIOR
        if self.rect.bottom > HEIGHT:
            self.speed_y -=1
        if self.rect.top < 0:
            self.speed_y +=1



'''
class Tiburon2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tiburon2.png").convert()   #AGREGAR LA IMAGEN
        self.image.set_colorkey(BLACK)   #SE ELIMINA EL COLOR DE FONDO
        self.rect = self.image.get_rect()  #POSICIONAR EL SPRITE
        self.rect.centerx = WIDTH // 2     #MOSTRARLA EN PANTALLA
        self.rect.bottom = HEIGHT - 100
        self.speed_x = 0 #VELOCIDAD CON LA QUE SE MOVERA 
        self.speed_y = 0
 '''   
        


all_sprites= pygame.sprite.Group()  #ALMACENAR AL JUGADOR

#CANTIDAD DE TIBURONES AL AZAR
for i in range(random.randrange(5)+1):
    tiburon1= Tiburon1()
    all_sprites.add(tiburon1)




pez=Jugador()
all_sprites.add(pez)

tiburon1=Tiburon1()
all_sprites.add(tiburon1)

'''
tiburon2=Tiburon2()
all_sprites.add(tiburon2)
'''


done=False

#PARA COLOCAR UNA IMAGEN DE FONDO
fondo = pygame.image.load("PNG/fondo2.jpg").convert()

#PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True


    screen.blit(fondo,[0,0])
    
    all_sprites.update()


#ZONA DE DIBUJO 
    all_sprites.draw(screen) #PARA QUE SALGAN EN PANTALLA
    

#PARA ACTUALIZAR LA PANTALLA
    pygame.display.flip()
    clock.tick(60)