import numpy as np
import math
def calc_distance(x, y, z):
    radius_d1 = math.pow((x-node_dist),2) + math.pow((y-0),2) + math.pow((z-0),2)
    radius_d2 = math.pow((x-0),2) + math.pow((y-node_dist),2) + math.pow((z-0),2)
    radius_d3 = math.pow((x-0),2) + math.pow((y-0),2) + math.pow((z-node_dist),2)
    
    return radius_d1, radius_d2, radius_d3

node_dist = 10
start = 0
stop_height = 10.5
stop_wide = 25.5
stop_depth = 50.5
step = 0.5
data = np.empty((6))
for x in np.arange(start, stop_wide, step):
    for y in np.arange(start, stop_depth, step):
        for z in np.arange(start, stop_height, step):
            radius_d1, radius_d2, radius_d3 = calc_distance(x, y, z)
            row_to_add = np.array([x, y, z, radius_d1, radius_d2, radius_d3])
            data = np.vstack([data, row_to_add])
            

data = data[1:, :]
print data
np.savetxt("data10_25_50_Sphere.txt",data,'%f')
