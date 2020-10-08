import numpy as np 
import math

r_x=2150
r_y=1650
r_z=2450
x=20
y=45
z=5
node_dist = 10  

def calc_distance(x, y, z):
    f_x = sqrt(math.pow((x-node_dist),2) + math.pow((y-0),2) + math.pow((z-0),2))
    f_y = sqrt(math.pow((x-0),2) + math.pow((y-node_dist),2) + math.pow((z-0),2))
    f_z = sqrt(math.pow((x-0),2) + math.pow((y-0),2) + math.pow((z-node_dist),2))
    
    return f_x, f_y, f_z

def gradient(x,y,z):
    for x in range(0,3):
        result[0]=([((x-node_dist)*f_x)/(f_x+r_x)] , [((y-0)*f_y)/(f_y+r_y)] , [((z-0)*f_z)/(f_z+r_z)])
        result[1]=([((x-0)*f_x)/(f_x+r_x)] , [((y-node_dist)*f_y)/(f_y+r_y)] , [((z-0)*f_z)/(f_z+r_z)])
        result[2]=([((x-0)*f_x)/(f_x+r_x)] , [((y-0)*f_y)/(f_y+r_y)] , [((z-node_dist)*f_z)/(f_z+r_z)])
    return result[x]    
