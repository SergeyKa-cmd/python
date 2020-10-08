import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle


rf_xx = pickle.load(open('rfc_x.sav', 'rb'))
rf_yy = pickle.load(open('rfc_y.sav','rb')) # Renamed from open to codecs.open due to using python 3
rf_zz = pickle.load(open('rfc_z.sav','rb')) # Renamed from open to codecs.open due to using python 3
while True:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    print "Enter X dist, Y dist and Z dist in range of(0-100)"
    dist_1 = [int(raw_input("X dist: "))] # Renamed from raw_input to input due to using python 3
    dist_2 = [int(raw_input("Y dist: "))] # Renamed from raw_input to input due to using python 3
    dist_3 = [int(raw_input("Z dist: "))] # Renamed from raw_input to input due to using python 3
    compute = input("Compute? Y/n   :")
    if compute.lower() != 'y':
        break
    X = rf_xx.predict(np.array([dist_1, dist_2, dist_3]).reshape(1, -1))
    Y = rf_yy.predict(np.array([dist_1, dist_2, dist_3]).reshape(1, -1))
    Z = rf_zz.predict(np.array([dist_1, dist_2, dist_3]).reshape(1, -1))
    print(X, Y, Z)
    ax.plot(X, Y, Z, ls="None", marker='^')
    ax.set_xlim3d([0, 25])
    ax.set_ylim3d([0, 50])
    ax.set_zlim3d([0, 10])
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")
    plt.show()