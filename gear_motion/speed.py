'''Calculate the maximum speed of a point on the planet gear surface'''
import numpy as np
import matplotlib.pyplot as plt

def EpiCycloid_Calc(a, b, omega):
    '''
    :param a: radius of the inner circle
    :param b: radius of the outer circle
    :param omega: rotation speed of the planet carrier
    :return:
    '''

    # set the angle for two separate motions, theta_p for self-rotation and theta_pc for planet carrier
    # choose counterclockwise to be the positive direction
    theta_p = np.arange(np.pi, np.pi + 2*np.pi*15/7, 0.05*15/7)
    theta_pc = np.arange(0, -2*np.pi, -0.05)
    omega_pc = omega
    omega_p = 15*omega_pc/7


    # radius of the planet carrier
    R = a+b
    # radius of the interested point towards planet gear center
    r = b

    vx = omega_p * r * np.cos(theta_p + np.pi/2) + omega_pc * R * np.cos(theta_pc - np.pi/2)
    vy = omega_p * r * np.sin(theta_p + np.pi/2) + omega_pc * R * np.sin(theta_pc - np.pi/2)
    v = np.sqrt(vx**2 + vy**2)

    v_max = np.max(v)
    v_min = np.min(v)
    print("the maximum speed: %.4f mm/s" %v_max)
    print("the minimum speed: %.4f mm/s" %v_min)
    plt.figure()
    plt.ylabel("speed: mm/s")
    plt.xlabel('angle: rad')
    plt.plot(theta_p, v, '*', 'b')
    plt.show()
    return v_max

if __name__ == '__main__':
    V = EpiCycloid_Calc(54.5, 58, 8*2*np.pi)
