
from tkinter import *
import pygame, random
import time


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
    pygame.init()
    pygame.mixer.init() 
    pygame.mixer.music.load("PNG/Intro.mp3")
    pygame.mixer.music.play(1)
    

    #------------------------------------------------------------------------------------------------------
    # GAME WINDOWS
    #------------------------------------------------------------------------------------------------------
    def Level1():

        # GET THE NAME INTRODUCED
        Playername = text_box.get()

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
        pygame.mixer.music.load("PNG/Lebel 1.mp3")
        pygame.mixer.music.play(1)

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
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(2,4)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(2,4)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE
                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(2,4)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(2,4)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE

                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1

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

        # TIME TRANSCURRED
        Time = 0
        # PUNCTUATION
        Punctuation = 0
        # PLAYER'S LIFE
        PlayerLife = 3

        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done = True

        while done:
            Time = pygame.time.get_ticks()/1000
            Punctuation = Time
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False
                        pygame.quit()
                        StartingWindow()
                
            screen.blit(fondo,[0,0])
            all_sprites.update()
            enemies_sprites.update()

            # COLISIONES
            collides = pygame.sprite.spritecollide(pez,enemies_sprites,True)

            if collides:
                PlayerLife -= 1

            # IF PLAYER'S LIFE IS 0 THE GAME ENDS
            if PlayerLife == 0:
                done = False
                pygame.quit()
                StartingWindow()

            if int(Time) == 60:
                Level2()

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
            enemies_sprites.draw(screen)

            # DRAW THE PUNTUATION ON THE SCREEN
            draw_punctuation(screen, "Puntuación: {}".format(str(int(Punctuation))), 25, 100, 650)

            # DRAW THE TIME ON THE SCREEN
            draw_time(screen, "Tiempo: {}".format(str(int(Time))),25, 300, 650)

            # DRAW THE PLAYER'S LIFE SCORE ON THE SCREEN
            draw_player_life(screen, "Vida: {}".format(PlayerLife),25, 450, 650)

            # DRAW THE PLAYER'S NAME ON THE SCREEN
            PlayerName(screen,Playername,25, 750, 650)

        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()
            

        pygame.quit()

    def Level2():

        # GET THE NAME INTRODUCED
        Playername2 = text_box.get() 

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
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(3,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(3,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE
                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(3,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(3,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE
                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1

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

        tiburon4=Tiburon1()
        enemies_sprites.add(tiburon4)

        tiburon5=Tiburon1()
        enemies_sprites.add(tiburon5)
        # TIME TRANSCURRED
        Time = 0
        # PUNCTUATION
        Punctuation = 0
        # PLAYER'S LIFE
        PlayerLife = 3

        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done = True

        while done:
            Time = pygame.time.get_ticks()/1000
            Punctuation = Time
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False
                        pygame.quit()
                        StartingWindow()
                
            screen.blit(fondo,[0,0])
            all_sprites.update()
            enemies_sprites.update()

            # COLISIONES
            collides = pygame.sprite.spritecollide(pez,enemies_sprites,True)

            if collides:
                PlayerLife -= 1

            # IF PLAYER'S LIFE IS 0 THE GAME ENDS
            if PlayerLife == 0:
                done = False
                pygame.quit()
                StartingWindow()

            if int(Time) == 60:
                pygame.quit()
                Level3()

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
            enemies_sprites.draw(screen)

            # DRAW THE PUNTUATION ON THE SCREEN
            draw_punctuation(screen, "Puntuación: {}".format(str(int(Punctuation))), 25, 100, 650)

            # DRAW THE TIME ON THE SCREEN
            draw_time(screen, "Tiempo: {}".format(str(int(Time))),25, 300, 650)

            # DRAW THE PLAYER'S LIFE SCORE ON THE SCREEN
            draw_player_life(screen, "Vida: {}".format(PlayerLife),25, 450, 650)

            # DRAW THE PLAYER'S NAME ON THE SCREEN
            PlayerName(screen,Playername2,25, 750, 650)

        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()
            

        pygame.quit()

    def Level3():
       
        # GET THE NAME INTRODUCED
        Playername = text_box.get()

        # CLOSE THE STARTING WINDOW
        window.destroy()

        # OPEN THE GAME WINDOW 
        pygame.init()
        pygame.mixer.init() 

        #TAMAÑO DE LA VENTANA
        WIDTH= 900
        HEIGHT= 700

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
        pygame.mixer.music.play(2)


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
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(3,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(3,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE
                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1


        class Tiburon2(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("PNG/tiburon2.png").convert_alpha()   #AGREGAR LA IMAGEN
                self.rect = self.image.get_rect()  
                # POSICIONAR EL SPRITE
                self.rect.x = random.randrange(WIDTH) 
                # VELOCIDAD CON LA QUE SE MOVERA 
                self.rect.y = 100
                self.speed_x = random.randrange(3,5)   
                # VELOCIDAD CON LA QUE SE MOVERA (SERA UNA DIFERENTE PARA CADA UNO)
                self.speed_y = random.randrange(3,5)
            
            def update(self):
                # ACTUALIZAR LA VELOCIDAD DEL ENEMIGO
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                
                # LIMITA EL MARGEN DERECHO E IZQUIERDO
                if self.rect.right > WIDTH:
                    self.speed_x -=1  #PARA QUE REBOTE
                if self.rect.left < 0:
                    self.speed_x +=1

                # LIMITA EL MARGEN INFERIOR Y SUPERIOR
                if self.rect.bottom > HEIGHT:
                    self.speed_y -=1
                if self.rect.top < 0:
                    self.speed_y +=1

        #ALMACENAR AL JUGADOR
        all_sprites= pygame.sprite.Group()  

        pez=Jugador()
        all_sprites.add(pez)

        tiburon1=Tiburon1()
        all_sprites.add(tiburon1)

        tiburon2=Tiburon2()
        all_sprites.add(tiburon2)

        tiburon3=Tiburon1()
        all_sprites.add(tiburon3)

        tiburon4=Tiburon2()
        all_sprites.add(tiburon4)

        tiburon5=Tiburon1()
        all_sprites.add(tiburon5)
        
        tiburon6=Tiburon2()
        all_sprites.add(tiburon6)

        tiburon7=Tiburon1()
        all_sprites.add(tiburon7)

        #PARA PODER CERRAR LA VENTANA AL PRESIONAR LA "X"
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done=True
                        pygame.quit()
                        StartingWindow()
                
            screen.blit(fondo,[0,0])
            all_sprites.update()

            #PARA QUE SALGAN EN PANTALLA
            all_sprites.draw(screen) 
        
        #PARA ACTUALIZAR LA PANTALLA
            pygame.display.flip()
            clock.tick(60)

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

    # ABOUT BUTTON
    AboutButton = Button(window, text = "About", command = AboutWindow, font = ("Ebrima 15"))
    AboutButton.place(x = 100, y = 315)

    mainloop()

StartingWindow()