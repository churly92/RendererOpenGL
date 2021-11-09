import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

vertex_data = np.array([-0.5,-0.5, 0.5, 1.0, 0.0, 0.0,
                        -0.5, 0.5, 0.5, 0.0, 1.0, 0.0,
                         0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                         0.5,-0.5, 0.5, 1.0, 1.0, 0.0,
                        -0.5,-0.5,-0.5, 1.0, 0.0, 1.0,
                        -0.5, 0.5,-0.5, 0.0, 1.0, 1.0,
                         0.5, 0.5,-0.5, 1.0, 1.0, 1.0,
                         0.5,-0.5,-0.5, 0.0, 0.0, 0.0], dtype = np.float32)

index_data = np.array([0,1,3, 1,2,3,
                       1,5,2, 5,6,2,
                       4,5,0, 5,1,0,
                       3,2,7, 6,2,7,
                       4,0,7, 0,3,7,
                       5,4,6, 4,7,6], dtype = np.uint32)

cube = Model(vertex_data, index_data )

cube.position.z = -5.0

rend.scene.append( cube )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        rend.camPosition.z += 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 1 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime


    # Movimiento de objeto
    rend.scene[0].rotation.x += 10 * deltaTime
    rend.scene[0].rotation.y += 10 * deltaTime
    rend.scene[0].rotation.z += 10 * deltaTime


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()
