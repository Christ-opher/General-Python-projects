
#toblerone_monolith

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math

def plot(ax):
    width = 70# X direction and z directions
    length = 70   # Y direction
    

    vertices = [None]*14

    #The vertices were marked starting from the origin and went to the right then towards the  + y direction in a zigzag pattern
    #first set of vertices 
    vertices[0] = (0, 0, 0)  
    vertices[11] = (0, length * 3, 0)  
    
    #second set vertices
    vertices[5] = (width / 5, length, width * (math.sqrt(3) / 5))  
    vertices[10] = (width / 5, length * 2, width * (math.sqrt(3) / 5))  

    #middle set of vertices
    vertices[1] = (width / 2, 0 , width * (math.sqrt(3) / 2))    
    vertices[4] = (width / 2, length * (3/4), width * (math.sqrt(3) / 2))  
    vertices[6] = (width / 2, length * (5/4), width * (math.sqrt(3) / 2))  
    vertices[7] = (width / 2, length * (7/4), width * (math.sqrt(3) / 2))  
    vertices[9] = (width / 2, length * (9/4), width * (math.sqrt(3) / 2))  
    vertices[12] = (width / 2, length * 3, width * (math.sqrt(3) / 2))  

    #second furthest left set of vertices
    vertices[3] = (width * (4/5), length, width * (math.sqrt(3) / 5))  
    vertices[8] = (width * (4/5), length * 2, width * (math.sqrt(3) / 5))  

    #furthest left set of vertices
    vertices[2] = (width, 0, 0)  
    vertices[13] = ( width, length * 3, 0)  

    facets = [None]*9
    #back face
    facets[0] = (vertices[0], vertices[1], vertices[2])
    #bottom face
    facets[1] = (vertices[0], vertices[2], vertices[13], vertices[11])  
    #front face
    facets[2] = (vertices[11], vertices[12], vertices[13])
    #right face
    facets[3] = (vertices[1], vertices[2], vertices[13], vertices[12], vertices[9], 
    vertices[8], vertices[7], vertices[6], vertices[3], vertices[4])  
    #left face
    facets[4] = (vertices[1], vertices[0], vertices[11], vertices[12], vertices[9], 
    vertices[10], vertices[7], vertices[6], vertices[5], vertices[4]) 
    #first(counting from the back face) inner face
    facets[5] = (vertices[4], vertices[3], vertices[5]) 
    #second inner face
    facets[6] = (vertices[6], vertices[3], vertices[5])  
    #third inner face
    facets[7] = (vertices[7], vertices[8], vertices[10]) 
    #fourth inner face
    facets[8] = (vertices[9], vertices[8], vertices[10]) 

    p = Poly3DCollection(facets, linewidth=3,
                         edgecolors=['maroon'],
                         facecolors=['chocolate'])

    ax.add_collection3d(p)

    ax.view_init(azim=-45)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xlim3d(xmin=-100, xmax=100)
    ax.set_ylim3d(ymin=-100, ymax=210)
    ax.set_zlim3d(zmin=0, zmax=100)


def main():
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(10, 8)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection='3d')
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
