import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from scipy.misc import imread
import matplotlib.cbook as cbook
import numpy as np
import pickle



rf_xx = pickle.load(open('rfc_x.sav','rb')) 
rf_yy = pickle.load(open('rfc_y.sav','rb'))
rf_zz = pickle.load(open('rfc_z.sav','rb'))
while True:
    fig = plt.figure()
    ax=fig.add_subplot(111)
    print ("Enter X dist, Y dist and Z dist in range of(0-100)")
    dist_1 = [int(raw_input("X dist: "))]
    dist_2 = [int(raw_input("Y dist: "))]
    dist_3 = [int(raw_input("Z dist: "))]
    compute = raw_input("Compute? Y/n   :") ##Enter distance in mellimeters, result = coordinates 
    if compute.lower() != 'y':
        break
    X=rf_xx.predict(np.array([dist_1,dist_2,dist_3]).reshape(1,-1)) ##Random Forest predictiion from datasets rfc_x.sav, rfc_y.sav,rfc_z.sav
    Y=rf_yy.predict(np.array([dist_1,dist_2,dist_3]).reshape(1,-1))
    Z=rf_zz.predict(np.array([dist_1,dist_2,dist_3]).reshape(1,-1))
    print(X, Y, Z)
    datafile = cbook.get_sample_data('C:\python\map_1.jpg') ##Load from file bitmap on plot
    img = imread(datafile)
    ax.set_xlim([0, 25])
    ax.set_ylim([0, 50])


    plt.imshow(img, zorder=0, extent=[0,25,0,50]) ##Show picture centered
    
    plt.scatter(X, Y, c=Z, s=50) ##Point options
    plt.clim(0,10) ##Colorbar range (0-10)
    plt.gray() ##Depends where it can be placed(color of point may vary)
    
    
    plt.grid() ##Show grid
    
    plt.colorbar() ##Show colorbar
    #z_mass[X,Y] = Z
    #plt.colorbar(Z) 
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    plt.show()
    