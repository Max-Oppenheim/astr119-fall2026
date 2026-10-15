import numpy as np

b = 5.67e-8

def t_eq(L, d):
    T = (L / (16*np.pi*b*d**2))**(1/4)
    return T


planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
    ]





if __name__ == '__main__':
    t_eq()