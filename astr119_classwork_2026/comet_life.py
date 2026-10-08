#This code finds the change in radius of a comet per orbit around the sun
#To run it, press the button and input the radius of the comet you're researching

import numpy as np

a = 4.6488e11 #distance in meters
R = float(input("What is the radius: ")) #radius of comet in meters
A = 0 #albedo
L = 3.8e26
GM_sun = 1.3271e20
rho = 500
e1 = 0.5
H_ice = 2.5e6


H = (np.pi/2)*(1-A)*(R**2)*((L/np.sqrt(GM_sun))*(1/np.sqrt(a*(1-e1**2))))
delta_M = H/H_ice
dr = delta_M/(rho*np.pi*4*R**2)
num_orbits = R/dr

print(f'This is the decrease in radius per orbit {dr}')
print(f'This is the radius of the comet in meters {R}')
print(f'This is the number of orbits the comet will last {num_orbits}')

