
from tkinter import *
import pygame, random
import time
from io import open 
from pygame import Rect, rect

#GLOBAL VARIABLE
Playername = "0"
puntuacion1 = 0
puntuacion2 = 0
puntuacion3 = 0
puntuacionglobal = 0


def StartingWindow():
    #------------------------------------------------------------------------------------------------------
    # STARTING WINDOW
    #------------------------------------------------------------------------------------------------------

    window = Tk()
    window.title("The Fish Adventure")

    # WINDOW DIMENTIONS
    window.geometry("900x700")

    # BACKGROUND
    image = PhotoImage(file = "PNG/Start Background.png")
    background = Label(image = image)
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    # LABEL "CREA UN NOMBRE"
    commentary = Label(window, text = "Crea Un Nombre ", font = ("Ebrima",22))
    commentary.place(x = 335, y = 390 )

    # LABEL "SELECCIONA UN NIVEL"
    selectLevel = Label(window, text = "Selecciona Un Nivel ", font = ("Ebrima",15))
    selectLevel.place(x = 700, y = 320 )

    # TEXT BOX
    entry = StringVar
    text_box = Entry(window, textvariable = entry, font = ("Ebrima",18))
    text_box.place(x = 355, y = 450, height = 30, width = 200)

    # ADD MUSIC 
    pygame.mixer.init() 
    pygame.mixer.music.load("PNG/Intro.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.5)


                  
    #-------------------------------------------------------------------
    #                        LEVEL 1
    #-------------------------------------------------------------------
                           
    def Level1():
        global Playername
        global puntuacion1
        global puntuacion2
        global puntuacion3
        global puntuacionglobal
        # GET THE NAME INTRODUCED
        if Playername == "0":
            Playername = " " + text_box.get()
        
        # CLOSE THE STARTING WINDOW
            window.destroy()
        

        # OPEN THE GAME WINDOW 
        pygame.init()
        pygame.mixer.init() 
        
        #TAMAÑO DE LA VENTANA
        WIDTH = 900
        HEIGHT = 700

        WHITE = (0,0,0)

        #CREAR UNA VENTANA
        screen= pygame.display.set_mode((WIDTH,HEIGHT))
        clock= pygame.time.Clock()

        #SE COLOCA EL NOMBRE DE JUEGO Y EL ICONO EN LA VENTANA
        pygame.display.set_caption("The Fish Adventure")
        icon = pygame.image.load("PNG/icono.png")
        pygame.display.set_icon(icon)
        
        #PARA COLOCAR UNA IMAGEN DE FONDO
        fondo = pygame.image.load("PNG/Game Background.png").convert_alpha()

        #AGREGAR MUSICA DE FONDO

        pygame.mixer.music.load("PNG/Lebel 1.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.4)


        #------------------------------------------------------------------------------------------------------
        # DRAW ELEMENTS ON WINDOW
        #------------------------------------------------------------------------------------------------------
        # PUNTUATION
        def draw_punctuation(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        
        # TIME TRASNCURRED
        def draw_time(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        # PLAYER'S LIFE
        def draw_player_life(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        # PLAYER'S NAME
        def PlayerName(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        def ExitButton(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        
        rectangulo = pygame.Rect(15,10,80,50)
            

        class Jugador(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                #AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/Jugador1.png").convert_alpha() 
                #POSICIONAR EL SPRITE
                self.rect = self.image.get_rect()  
                #MOSTRARLA EN PANTALLA
                self.rect.centerx = WIDTH // 2 
                self.rect.bottom = HEIGHT - 55
                #VELOCIDAD CON LA QUE SE MOVERA 
                self.speed_x = 0 
                self.speed_y = 0

            #FUNCION PARA EL MOVIMIENTO DEL JUGADOR POR MEDIO DE LAS TECLAS IZQ,DER,ABAJO,ARRIBA
            def update(self):
                self.speed_x = 0
                self.speed_y = 0
                
                # VER SI UNA TECLA HA SIDO PRESIONADA
                keystate = pygame.key.get_pressed()  
                if keystate[pygame.K_LEFT]:
                    self.speed_x = -5
                if keystate[pygame.K_RIGHT]:
                    self.speed_x = 5
                if keystate[pygame.K_UP]:
                    self.speed_y = -6
                if keystate[pygame.K_DOWN]:
                    self.speed_y = 6
                
                #SUMAR LA VELOCIDAD, ACTUALIZARLO
                self.rect.x += self.speed_x  
                self.rect.y += self.speed_y
                
                #--------------------------------------------------------------------
                #PARA QUE EL JUGADOR NO SE DESPLAZE MAS ALLA DEL LIMITE DE LA VENTANA
                #--------------------------------------------------------------------
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
                # AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/tiburon11.png").convert_alpha()   
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(1,4)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(1,4)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
   
                if self.rect.left < 0:
                    self.speed_x +=1

                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1

                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.top < 0:
                    self.speed_y +=1

                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(-2,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(-2,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.left < 0:
                    self.speed_x +=1

                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                
                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.top < 0:
                    self.speed_y +=1

                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
                          
        #ALMACENAR AL JUGADOR
        all_sprites= pygame.sprite.Group()

        enemies_sprites = pygame.sprite.Group()  

        pez=Jugador()
        all_sprites.add(pez)

        tiburon1=Tiburon1()
        enemies_sprites.add(tiburon1)

        tiburon2=Tiburon2()
        enemies_sprites.add(tiburon2)

        tiburon3=Tiburon1()
        enemies_sprites.add(tiburon3)

        tiburon4=Tiburon2()
        enemies_sprites.add(tiburon4)

    
        # PUNCTUATION
        Punctuation = 0
         

        # PLAYER'S LIFE
        PlayerLife = 3

        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done = True

        start_time = time.time()

        while done:
            actual_time = time.time() - start_time
            puntuacion1 = Punctuation
            Punctuation = int(actual_time)
            clock.tick(60)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rectangulo.collidepoint(pygame.mouse.get_pos()):
                        done = False
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()
                    

   
            screen.blit(fondo,[0,0])
            all_sprites.update()
            enemies_sprites.update()

            #COLISIONES
            collides = pygame.sprite.spritecollide(pez,enemies_sprites,True)

            if collides:
                PlayerLife -= 1
                puntuacionglobal -= 1

            # IF PLAYER'S LIFE IS 0 THE GAME ENDS
            if PlayerLife == 0:
                done = False
                Playername = "0"
                puntuacion1 = 0
                puntuacion2 = 0
                puntuacion3 = 0
                pygame.quit()
                StartingWindow()
                
            
            if int(actual_time) == 10:
                pygame.quit()
                Level2()
        

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
            enemies_sprites.draw(screen)

            # DRAW THE PUNTUATION ON THE SCREEN
            draw_punctuation(screen, "Puntuación: {}".format(str(int(Punctuation))), 25, 100, 650)

            # DRAW THE TIME ON THE SCREEN
            draw_time(screen, "Tiempo: {}".format(str(int(actual_time))),25, 300, 650)

            # DRAW THE PLAYER'S LIFE SCORE ON THE SCREEN
            draw_player_life(screen, "Vida: {}".format(PlayerLife),25, 450, 650)

            # DRAW THE PLAYER'S NAME ON THE SCREEN
            PlayerName(screen,Playername,25, 750, 650)

            if rectangulo.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen,(235, 52, 52),rectangulo,0)

            else:
                pygame.draw.rect(screen,(255,255,255),rectangulo,0)

            # DRAW THE EXIT BUTTON ON THE SCREEN
            ExitButton(screen,"Salir", 25, 55,20)

        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()

         

        pygame.quit()

#---------------------------------------------------
#                  LEVEL 2
#--------------------------------------------------

    def Level2():
        global Playername
        global puntuacion1
        global puntuacion2
        global puntuacion3
        global puntuacionglobal
        # GET THE NAME INTRODUCED
        if Playername == "0":
            Playername = " " + text_box.get() 
        
        # CLOSE THE STARTING WINDOW
        
            window.destroy()
        
        # OPEN THE GAME WINDOW 
        pygame.init()
        pygame.mixer.init() 

        #TAMAÑO DE LA VENTANA
        WIDTH= 900
        HEIGHT= 700

        WHITE = (0,0,0)

        #CREAR UNA VENTANA
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        clock= pygame.time.Clock()

        #SE COLOCA EL NOMBRE DE JUEGO Y EL ICONO EN LA VENTANA
        pygame.display.set_caption("The Fish Adventure")
        icon = pygame.image.load("PNG/icono.png")
        pygame.display.set_icon(icon)
        
        #PARA COLOCAR UNA IMAGEN DE FONDO
        fondo = pygame.image.load("PNG/Game Background.png").convert_alpha()

        #AGREGAR MUSICA DE FONDO
        pygame.mixer.music.load("PNG/Lebel 2.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.5)

        #------------------------------------------------------------------------------------------------------
        # DRAW ELEMENTS ON WINDOW
        #------------------------------------------------------------------------------------------------------
        # PUNTUATION
        def draw_punctuation(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        
        # TIME TRASNCURRED
        def draw_time(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        # PLAYER'S LIFE
        def draw_player_life(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        # PLAYER'S NAME
        def PlayerName(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        def ExitButton(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        rectangulo = pygame.Rect(15,10,80,50)

        class Jugador(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                #AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/Jugador1.png").convert_alpha() 
                #POSICIONAR EL SPRITE
                self.rect = self.image.get_rect()  
                #MOSTRARLA EN PANTALLA
                self.rect.centerx = WIDTH // 2 
                self.rect.bottom = HEIGHT - 55
                #VELOCIDAD CON LA QUE SE MOVERA 
                self.speed_x = 0 
                self.speed_y = 0

            #FUNCION PARA EL MOVIMIENTO DEL JUGADOR POR MEDIO DE LAS TECLAS IZQ,DER,ABAJO,ARRIBA
            def update(self):
                self.speed_x = 0
                self.speed_y = 0
                
                #VER SI UNA TECLA HA SIDO PRESIONADA
                keystate = pygame.key.get_pressed()  
                if keystate[pygame.K_LEFT]:
                    self.speed_x = -5
                if keystate[pygame.K_RIGHT]:
                    self.speed_x = 5
                if keystate[pygame.K_UP]:
                    self.speed_y = -6
                if keystate[pygame.K_DOWN]:
                    self.speed_y = 6
                
                #SUMAR LA VELOCIDAD, ACTUALIZARLO
                self.rect.x += self.speed_x  
                self.rect.y += self.speed_y
                
                #--------------------------------------------------------------------
                #PARA QUE EL JUGADOR NO SE DESPLAZE MAS ALLA DEL LIMITE DE LA VENTANA
                #--------------------------------------------------------------------
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
                # AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/tiburon11.png").convert_alpha()   
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(-4,4)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(2,3)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.left < 0:
                    self.speed_x +=1

                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1

                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
                if self.rect.top < 0:
                    self.speed_y +=1

                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(-5,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(1,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
                    
                if self.rect.left < 0:
                    self.speed_x +=1

                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1

                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
                if self.rect.top < 0:
                    self.speed_y +=1

                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

        #ALMACENAR AL JUGADOR
        all_sprites= pygame.sprite.Group()

        enemies_sprites = pygame.sprite.Group()  

        pez=Jugador()
        all_sprites.add(pez)

        tiburon1=Tiburon1()
        enemies_sprites.add(tiburon1)

        tiburon2=Tiburon2()
        enemies_sprites.add(tiburon2)

        tiburon3=Tiburon1()
        enemies_sprites.add(tiburon3)

        tiburon4=Tiburon2()
        enemies_sprites.add(tiburon4)

        tiburon5=Tiburon1()
        enemies_sprites.add(tiburon5)

        # PUNCTUATION
        Punctuation = 0      

        # PLAYER'S LIFE
        PlayerLife = 3

        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done = True

        start_time = time.time()

        while done:   
            actual_time = time.time() - start_time
            puntuacion2 = Punctuation
            Punctuation = int(actual_time) * 3            
            clock.tick(60)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rectangulo.collidepoint(pygame.mouse.get_pos()):
                        done = False
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()
                
            screen.blit(fondo,[0,0])
            all_sprites.update()
            enemies_sprites.update()

            # COLISIONES
            collides = pygame.sprite.spritecollide(pez,enemies_sprites,True)

            if collides:
                PlayerLife -= 1
                puntuacionglobal -= 3
            # IF PLAYER'S LIFE IS 0 THE GAME ENDS
            if PlayerLife == 0:
                done = False
                Playername = "0"
                puntuacion1 = 0
                puntuacion2 = 0
                puntuacion3 = 0
                pygame.quit()
                StartingWindow()

            if int(actual_time) == 10:
                pygame.quit()
                Level3()

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
            enemies_sprites.draw(screen)

            # DRAW THE PUNTUATION ON THE SCREEN
            draw_punctuation(screen, "Puntuación: {}".format(str(int(Punctuation))), 25, 100, 650)

            # DRAW THE TIME ON THE SCREEN
            draw_time(screen, "Tiempo: {}".format(str(int(actual_time))),25, 300, 650)

            # DRAW THE PLAYER'S LIFE SCORE ON THE SCREEN
            draw_player_life(screen, "Vida: {}".format(PlayerLife),25, 450, 650)

            # DRAW THE PLAYER'S NAME ON THE SCREEN
            PlayerName(screen,Playername,25, 750, 650)

            if rectangulo.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen,(235, 52, 52),rectangulo,0)

            else:
                pygame.draw.rect(screen,(255,255,255),rectangulo,0)

            # DRAW THE EXIT BUTTON ON THE SCREEN
            ExitButton(screen,"Salir", 25, 55,20)

        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()

         

        pygame.quit()


#---------------------------------------------
#               LEVEL 3
#---------------------------------------------

    def Level3():
        global Playername
        global puntuacion1
        global puntuacion2
        global puntuacion3
        global puntuacionglobal

        # GET THE NAME INTRODUCED
        if Playername == "0":
            Playername = " " + text_box.get() 
        
        # CLOSE THE STARTING WINDOW
            window.destroy()
        

        # OPEN THE GAME WINDOW 
        pygame.init()
        pygame.mixer.init() 

        #TAMAÑO DE LA VENTANA
        WIDTH= 900
        HEIGHT= 700
        WHITE = (0,0,0)

        #CREAR UNA VENTANA
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        clock= pygame.time.Clock()

        #SE COLOCA EL NOMBRE DE JUEGO Y EL ICONO EN LA VENTANA
        pygame.display.set_caption("The Fish Adventure")
        icon = pygame.image.load("PNG/icono.png")
        pygame.display.set_icon(icon)
        
        #PARA COLOCAR UNA IMAGEN DE FONDO
        fondo = pygame.image.load("PNG/Game Background.png").convert_alpha()

        #AGREGAR MUSICA DE FONDO
        pygame.mixer.music.load("PNG/Lebel 3.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        #------------------------------------------------------------------------------------------------------
        # DRAW ELEMENTS ON WINDOW
        #------------------------------------------------------------------------------------------------------
        # PUNTUATION
        def draw_punctuation(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        
        # TIME TRASNCURRED
        def draw_time(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        # PLAYER'S LIFE
        def draw_player_life(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        # PLAYER'S NAME
        def PlayerName(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        def ExitButton(surface, text, size, x, y):
            font = pygame.font.SysFont("serif",size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)
        
        rectangulo = pygame.Rect(15,10,80,50)

        class Jugador(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                #AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/Jugador1.png").convert_alpha() 
                #POSICIONAR EL SPRITE
                self.rect = self.image.get_rect()  
                #MOSTRARLA EN PANTALLA
                self.rect.centerx = WIDTH // 2 
                self.rect.bottom = HEIGHT - 55
                #VELOCIDAD CON LA QUE SE MOVERA 
                self.speed_x = 0 
                self.speed_y = 0

            #FUNCION PARA EL MOVIMIENTO DEL JUGADOR POR MEDIO DE LAS TECLAS IZQ,DER,ABAJO,ARRIBA
            def update(self):
                self.speed_x = 0
                self.speed_y = 0
                
                #VER SI UNA TECLA HA SIDO PRESIONADA
                keystate = pygame.key.get_pressed()  
                if keystate[pygame.K_LEFT]:
                    self.speed_x = -7
                if keystate[pygame.K_RIGHT]:
                    self.speed_x = 7
                if keystate[pygame.K_UP]:
                    self.speed_y = -7
                if keystate[pygame.K_DOWN]:
                    self.speed_y = 7
                
                #SUMAR LA VELOCIDAD, ACTUALIZARLO
                self.rect.x += self.speed_x  
                self.rect.y += self.speed_y
                
                #--------------------------------------------------------------------
                #PARA QUE EL JUGADOR NO SE DESPLAZE MAS ALLA DEL LIMITE DE LA VENTANA
                #--------------------------------------------------------------------
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
                # AGREGAR LA IMAGEN
                self.image = pygame.image.load("PNG/tiburon11.png").convert_alpha()   
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(-1,3)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(3,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.left < 0:
                    self.speed_x +=1

                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1

                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()
                    
                if self.rect.top < 0:
                    self.speed_y +=1
                
                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH-self.rect.width) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(-1,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(1,3)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1 #PARA QUE REBOTE   

                if self.rect.right == WIDTH:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.left < 0:
                    self.speed_x +=1
                    
                if self.rect.left == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1

                if self.rect.bottom == HEIGHT:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

                if self.rect.top < 0:
                    self.speed_y +=1

                if self.rect.top == 0:
                    golpe=pygame.mixer.Sound("PNG/golpe1.mp3")
                    golpe.play()

        #ALMACENAR AL JUGADOR
        all_sprites= pygame.sprite.Group()  
        enemies_sprites = pygame.sprite.Group() 

        pez=Jugador()
        all_sprites.add(pez)

        tiburon1=Tiburon1()
        enemies_sprites.add(tiburon1)

        tiburon2=Tiburon2()
        enemies_sprites.add(tiburon2)

        tiburon3=Tiburon1()
        enemies_sprites.add(tiburon3)

        tiburon4=Tiburon2()
        enemies_sprites.add(tiburon4)

        tiburon5=Tiburon1()
        enemies_sprites.add(tiburon5)
        
        tiburon6=Tiburon2()
        enemies_sprites.add(tiburon6)

        tiburon7=Tiburon1()
        enemies_sprites.add(tiburon7)

        # PUNCTUATION
        Punctuation = 0
        
        # PLAYER'S LIFE
        PlayerLife = 3


        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done=True
        start_time = time.time()

        while done:           
            actual_time = time.time() - start_time
            puntuacion3 = Punctuation
            Punctuation = int(actual_time) * 5 
            clock.tick(60)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rectangulo.collidepoint(pygame.mouse.get_pos()):
                        done = False
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False 
                        Playername = "0"
                        pygame.quit()
                        StartingWindow()
                
            screen.blit(fondo,[0,0])
            all_sprites.update()
            enemies_sprites.update()


            # COLISIONES
            collides = pygame.sprite.spritecollide(pez,enemies_sprites,True)

            if collides:
                PlayerLife -= 1
                puntuacionglobal -= 5

            # IF PLAYER'S LIFE IS 0 THE GAME ENDS
            if PlayerLife == 0:
                done = False
                Playername = "0"
                puntuacion1 = 0
                puntuacion2 = 0
                puntuacion3 = 0
                pygame.quit()
                StartingWindow()

            if int(actual_time) == 10:
                pygame.quit()
                StartingWindow()

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
            enemies_sprites.draw(screen)

            # DRAW THE PUNTUATION ON THE SCREEN
            draw_punctuation(screen, "Puntuación: {}".format(str(int(Punctuation))), 25, 100, 650)

            # DRAW THE TIME ON THE SCREEN
            draw_time(screen, "Tiempo: {}".format(str(int(actual_time))),25, 300, 650)

            # DRAW THE PLAYER'S LIFE SCORE ON THE SCREEN
            draw_player_life(screen, "Vida: {}".format(PlayerLife),25, 450, 650)

            # DRAW THE PLAYER'S NAME ON THE SCREEN
            PlayerName(screen,Playername,25, 750, 650)

            if rectangulo.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen,(235, 52, 52),rectangulo,0)

            else:
                pygame.draw.rect(screen,(255,255,255),rectangulo,0)

            # DRAW THE EXIT BUTTON ON THE SCREEN
            ExitButton(screen,"Salir", 25, 55,20)
        
        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()
         
        pygame.quit()


    # BUTTON "EMPEZAR"
    StartButton = Button(window, text = "Empezar", height = 1, width = 10, command = Level1, font = ("Ebrima",17))
    StartButton.place(x = 385, y = 500)

    # LEVEL 1 RADIOBUTTON
    num = IntVar()
    levelOne = Radiobutton(window, text = "Nivel 1",value = 1, variable = num, font = ("Ebrima",17), command= Level1)
    levelOne.place(x = 737, y = 390)

    # LEVEL 2 RADIOBUTTON
    levelTwo = Radiobutton(window, text = "Nivel 2", value = 2 , variable = num, font = ("Ebrima",17), command= Level2)
    levelTwo.place(x = 737, y = 450)

    # LEVEL 2 RADIOBUTTON
    levelThree = Radiobutton(window, text = "Nivel 3", value = 3, variable = num, font = ("Ebrima",17), command= Level3)
    levelThree.place(x = 737, y = 510)
    #------------------------------------------------------------------------------------------------------
    # ABOUT WINDOW
    #------------------------------------------------------------------------------------------------------
    def AboutWindow():
        Aboutwindow = Toplevel()
        Aboutwindow.title("The Fish Adventure")

        # WINDOW DIMENTIONS
        Aboutwindow.geometry("900x700")

        # BACKGROUND
        image = PhotoImage(file = "PNG/About Background.png")
        background = Label(Aboutwindow, image = image)
        background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # PRODUCTION COUNTRY LABEL
        Country = Label(Aboutwindow, text = "Costa Rica", font = ("Ebrima",20))
        Country.place(x = 390, y = 50)

        # UNIVERSITY LABEL
        University = Label(Aboutwindow, text = "Instituto Tecnológico de Costa Rica (TEC)", font = ("Ebrima",20))
        University.place(x = 210, y = 120)

        # CARRER LABEL
        Carrer = Label(Aboutwindow, text = "Ingeniería en Computadores", font = ("Ebrima",20))
        Carrer.place(x = 280, y = 190)

        # SIGNATURE LABEL
        SignatureYearGroup = Label(Aboutwindow, text = "Taller de Programación 2021 Grupo 03", font = ("Ebrima",20))
        SignatureYearGroup.place(x = 225, y = 260)

        # PROFESSOR LABEL
        Professor = Label(Aboutwindow, text = "Leonardo Araya Martínez", font = ("Ebrima",20))
        Professor.place(x = 305, y = 330)

        # VERSION LABEL
        Version = Label(Aboutwindow, text = "Python 3.9.4", font = ("Ebrima",20))
        Version.place(x = 375, y = 400)
        
        # AUTHORS LABELS
        Authors = Label(Aboutwindow, text = "Creado por:", font = ("Ebrima",20))
        Authors.place(x = 377, y = 470)

        Author1 = Label(Aboutwindow, text = "Albert Vega Camacho", font = ("Ebrima",20))
        Author1.place(x = 325, y = 540)

        Author2 = Label(Aboutwindow, text = "Meibel Ceciliano Picado", font = ("Ebrima",20))
        Author2.place(x = 312, y = 610)

        mainloop()

    def BestScores():

        global Playername
        global puntuacion1
        global puntuacion2
        global puntuacion3
        global puntuacionglobal

        #SONIDO
        pygame.mixer.init() 
        pygame.mixer.music.load("PNG/Scores.mp3")
        pygame.mixer.music.play(1)

        Bestscores = Toplevel()
        Bestscores.title("The Fish Adventure")

        image = PhotoImage(file = "PNG/Best_scores_background.png")
        background = Label(Bestscores, image = image)
        background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # WINDOW DIMENTIONS
        Bestscores.geometry("900x700")

        archivo = open("mejorespuntajes.txt","r+")

        puntuaciones = []

        for line in archivo:
            puntuaciones.append(line)

        puntuacionglobal += puntuacion1 + puntuacion2 + puntuacion3

        puntuaciones.append(str(puntuacionglobal) + Playername + "\n")

        def quick_sort(lista):
            quick_sort_auxiliar(lista, 0, len(lista) - 1)

        def quick_sort_auxiliar(lista, inicio, fin):
            if inicio < fin:
                punto_particion = particionar(lista, inicio, fin)

                quick_sort_auxiliar(lista, inicio, punto_particion - 1)
                quick_sort_auxiliar(lista, punto_particion + 1, fin)

        def particionar(lista, inicio, fin):
            pivote = lista[inicio]

            izquierda = inicio + 1
            derecha = fin
            terminado = False

            while not terminado:
                while izquierda <= derecha and lista[izquierda] <= pivote:
                    izquierda += 1

                while lista[derecha] >= pivote and derecha >= izquierda:
                    derecha -= 1

                if derecha < izquierda:
                    terminado = True
                else:
                    lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

            lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

            return derecha

        quick_sort(puntuaciones)

        puntuaciones.reverse()

        archivo.seek(0)

        archivo.writelines(puntuaciones) 

        print(puntuaciones)

        archivo.close()

        player1= Label(Bestscores, text=puntuaciones[0], font=("Ebrima",20))
        player1.place(x = 420, y = 250)

        player2= Label(Bestscores, text=puntuaciones[1], font=("Ebrima",20))
        player2.place(x = 420, y = 300)

        player3= Label(Bestscores, text=puntuaciones[2], font=("Ebrima",20))
        player3.place(x = 420, y = 350)

        player4= Label(Bestscores, text=puntuaciones[3], font=("Ebrima",20))
        player4.place(x = 420, y = 400)

        player5= Label(Bestscores, text=puntuaciones[4], font=("Ebrima",20))
        player5.place(x = 420, y = 450)

        player6= Label(Bestscores, text=puntuaciones[5], font=("Ebrima",20))
        player6.place(x = 420, y = 500)

        player7= Label(Bestscores, text=puntuaciones[6], font=("Ebrima",20))
        player7.place(x = 420, y = 550)

        mainloop()
        
    # ABOUT BUTTON
    AboutButton = Button(window, text = "About", command = AboutWindow, font = ("Ebrima 15"))
    AboutButton.place(x = 100, y = 315)

    # BEST SOCORES'S BUTTON
    BestScoresButton = Button(window, text = "Puntajes", command = BestScores, font = ("Ebrima 17"))
    BestScoresButton.place(x = 83, y = 500)

    mainloop()

StartingWindow()