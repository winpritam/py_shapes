import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from sys import *
# from PIL import Image

rotation_x = 0 
rotation_y = 0

def somthing(h,k,r,z,num_points):
    vertices = []
    edges = []
    for i in range(num_points):
        theta = 2 * pi * i / num_points
        x = r * cos(theta)+ h
        y = r * sin(theta)+ k
        vertices.append((x, y, z))
        if i ==(num_points-1):
            edges.append((0,i))
        else:
            edges.append((i,i+1))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 1, 0))
            glVertex3fv(vertices[vertex])                
    glEnd()

def circle_draw(h,k,r,z,num_points):
    vertices = []
    edges = []
    for i in range(num_points):
        theta = 2 * pi * i / num_points
        x = r * cos(theta)+ h
        y = r * sin(theta)+ k
        vertices.append((x, y, z))
        if i ==(num_points-1):
            edges.append((0,i))
        else:
            edges.append((i,i+1))
    glBegin(GL_POLYGON)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 1, 0))
            glVertex3fv(vertices[vertex])                
    glEnd()

def loding(h,k,r1,r2,num_pnt=8):
    lines =[]
    for i in range(num_pnt):
        th = 2 * pi * i/num_pnt
        x1 = r1 * cos(th)+ h
        y1 = r1 * sin(th)+ k
        x2 = r2 * cos(th)+ h
        y2 = r2 * sin(th)+ k
        lines.append([(x1,y1,0),(x2,y2,0)])
    return lines

def draw_loading(lines):
    glBegin(GL_LINES)
    for line in lines:
        tm_ln=line
        for point in tm_ln:
            glColor3fv((0, 0, 1))
            glVertex3fv(point)   
    glEnd()


# def plane():

    # vertices = []
    # edges = []
    # for i in range(num_points):
        
    #     x = r * cos(theta)+ h
    #     y = r * sin(theta)+ k
    #     vertices.append((x, y, z))
    #     if i ==(num_points-1):
    #         edges.append((0,i))
    #     else:
    #         edges.append((i,i+1))

# def line(p1=(),p2=(),c):
#         vertices = []
#     edges = []
#     slp = (p2[1] - p1[1])/(p2[0] - p1[0])
#     for i in range():
        
        
#         vertices.append(())
#         if i ==(num_points-1):
#             edges.append((0,i))
#         else:
#             edges.append((i,i+1))

def draw_square(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(-1, -1)
    glTexCoord2f(1, 0)
    glVertex2f(1, -1)
    glTexCoord2f(1, 1)
    glVertex2f(1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, 1)
    glEnd() 

def cube():
    vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )
    faces=(
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,7,2),
        (4,0,3,6)
        # (0,1,5,4),
        # (1,2,7,5),
        # (3,2,7,6),
        # (4,5,7,6,),
        # (0,3,6,4)
    )
    colors=(
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,1),
        (0,0,0),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,1),
        (0,0,0),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,1),
        (0,0,0),
    )

    glBegin(GL_QUADS)
    x = 0
    for face in faces:
        x +=1
        for vertex in face:
            glColor3fv((colors[x]))
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:            
        for vertex in edge:
            # glColor3fv((0, 1, 0))
            glVertex3fv(vertices[vertex])                
    glEnd()
    
def handle_events():
    global rotation_x, rotation_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            # Get mouse movement
            dx, dy = event.rel
            sensitivity = 0.1
            rotation_x = dy * sensitivity
            rotation_y = dx * sensitivity
            print(f'{sensitivity=}, {rotation_x=}, {rotation_y=}')

# def vec_mouse():
#     dx1

# def load_texture(filename):
#     image = Image.open(filename)
#     texture_id = glGenTextures(1)
#     glBindTexture(GL_TEXTURE_2D, texture_id)
#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image.tobytes())
#     glGenerateMipmap(GL_TEXTURE_2D)
#     return texture_id
def angel(zH,display):
    handle_events()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hPx=sqrt((zH**2) + (mouse_x - display[0])**2)
    hPy=sqrt((zH**2) + (mouse_y - display[1])**2)
    angx = ((mouse_x -(display[0]/2))/hPx)
    angy = ((mouse_y -(display[1]/2))/hPy)
    return (angx,angy)

def main():
    global rotation_x, rotation_y
    zH=15
    pygame.init()
    display = (1300, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Pygame Image Sprite")
    pygame.mouse.set_pos(display[0]/2,display[1]/2)
    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    #this function set camera(field of view, (width/hight), close view, far view)

    glTranslatef(0.0, 0.0, -zH)
    lines = loding(1,1,3,7,24)

    # all game operation 
    while True:
        handle_events()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # mouse_x, mouse_y = pygame.mouse.get_pos()
            angx, angy = angel(zH,display)
        
            cube()
            circle_draw(0,0,5,0,100)
            draw_loading(lines)

            glRotatef(1,-1 * angx*rotation_x, -1 * angy*rotation_y,0)
            # glRotatef(1,0,,0)s
            # glRotatef(5,0,0,1)
            # if rotation_y <= 0:
            # print(asin(15/((1+mouse_x)/2)))
            
            # glRotatef(asin(15/(mouse_y-(display[1]/2))),0,1,0)
            

    # Print the coordinates
            # print(f"Mouse Coordinates: ({mouse_x}, {mouse_y})")

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # Left mouse button
            #         glRotatef(1, rotation_x, rotation_y, 0)
                # elif event.button == 3:  # Right mouse button
                #     print("Right mouse button down")
            # circle_draw(0,0,5,0,64)

            pygame.display.flip()
            pygame.time.wait(10)
        

if __name__ == "__main__":
    main()
