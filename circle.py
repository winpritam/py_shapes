from math import *


def circle(offset_x=0,offset_y=0,offset_z=0,redious=0,point_resuliotion=8):
    vertices = []
    edges = []
    print (point_resuliotion)
    for i in range(point_resuliotion):
        theta = 2 * pi * i / point_resuliotion
        x = redious * cos(theta)+ offset_x
        y = redious * sin(theta)+ offset_y
        vertices.append((x, y, offset_z))
        if i ==(point_resuliotion-1):
            edges.append((i,0))
        else:
            edges.append((i,i+1))
    return vertices

# Example usage:
print(circle(0,0,0,50,20))

