'''function used to get Hypocycloid'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches

# a is the radius of the outer circle, b is the radius of the inner circle.
a = 16.05
b = 5.25
pb = 4.15  # parameter for the reference marks

# range of theta to show the HypoCycloid
theta = np.arange(0, 6.4, 0.05)

# create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.xlim((-18, 18))
plt.ylim((-18, 18))

# add a colored rectangular as the imaging frame
left, bottom, width, height = (5.45, -2.203, 3.266, 4.406)
rect = mpatches.Rectangle((left, bottom), width, height, alpha=0.1, facecolor='red')
plt.gca().add_patch(rect)

# line1 and line2 show the contact region between the sun gear and the planet gear, while
# line3 and line4 show the contact region between the planet gear and the ring gear
line_x = np.linspace(0, 18, 100)
line1_y = line_x * np.tan(24.6638 * np.pi / 180)
line2_y = -line1_y
# line3_y = line_x * np.tan(15.9035 * np.pi / 180)
# line4_y = -line3_y
# ax.plot(line_x, line1_y, 'r', line_x, line2_y, 'r', line_x, line3_y, 'cyan', line_x, line4_y, 'cyan')
# ax.plot(line_x, line3_y, 'cyan', line_x, line4_y, 'cyan')
ax.plot(line_x, line1_y, 'r', line_x, line2_y, 'r')

# add a colored circle to show the sun gear
circle = mpatches.Circle((0, 0), radius=6, facecolor='blue')
plt.gca().add_patch(circle)

# create a text title to show the current theta
theta_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)
textTemplate = '''θ = %.1frad\n'''

# plot configurations
ax.grid()
xCircle, yCircle = np.cos(theta), np.sin(theta)
ax.plot(a*xCircle, a*yCircle, '-', lw=1)
# pt stands for the tracked feature point - mesh node
pt, = ax.plot([a], [0], '*')
cir, = ax.plot(a+b+b*yCircle, b*yCircle, '-', lw=1)

# pt1 and pt2 stand for the tracked two feature points - reference marks
pt1, = ax.plot([a-b+pb*np.cos(-np.pi/21)], [a-b-pb*np.sin(-np.pi/21)], '*')
pt2, = ax.plot([a-b+pb*np.cos(np.pi/21)], [a-b-pb*np.sin(np.pi/21)], '*')

xs, ys = [], []
xs1, ys1 = [], []
xs2, ys2 = [], []

# plot configurations
def animate(t):
    if t == 0:
        xs.clear()
        ys.clear()

    cenX = (a-b)*np.cos(t)
    cenY = (a-b)*np.sin(t)

    cir.set_data(cenX+b*xCircle, cenY+b*yCircle)

    '''HypoCycloid analysis for the planet gear and the ring gear'''
    # newX = cenX + b * np.cos(15 * t / 7)
    # newY = cenY - b * np.sin(15 * t / 7)
    # 
    # newX_1 = cenX + pb*np.cos(15*t/7 - np.pi/21)
    # newY_1 = cenY - pb*np.sin(15*t/7 - np.pi/21)
    # newX_2 = cenX + pb * np.cos(15 * t / 7 + np.pi / 21)
    # newY_2 = cenY - pb * np.sin(15 * t / 7 + np.pi / 21)

    '''HypoCycloid analysis for the sun gear and planet ring gear'''
    newX = cenX + b * np.cos(15 * t / 7 + np.pi)
    newY = cenY - b * np.sin(15 * t / 7 + np.pi)

    newX_1 = cenX + pb * np.cos(15 * t / 7 - np.pi / 21 + np.pi)
    newY_1 = cenY - pb * np.sin(15 * t / 7 - np.pi / 21 + np.pi)
    newX_2 = cenX + pb * np.cos(15 * t / 7 + np.pi / 21 + np.pi)
    newY_2 = cenY - pb * np.sin(15 * t / 7 + np.pi / 21 + np.pi)

    xs.append(newX)
    ys.append(newY)
    xs1.append(newX_1)
    ys1.append(newY_1)
    xs2.append(newX_2)
    ys2.append(newY_2)
    pt.set_data(xs, ys)

    colormap = ['black', 'gray', 'r', 'peru', 'orange', 'yellow', 'lawngreen', 'cyan', 'royalblue']
    color_num = len(xs) % 9
    # ax.plot((newX, newX_1), (newY, newY_1), (newX, newX_2), (newY, newY_2), (newX_1, newX_2), (newY_1, newY_2))  # print the line between two tracked points

    ax.plot((newX, newX_1), (newY, newY_1), color=colormap[color_num])
    ax.plot((newX, newX_2), (newY, newY_2), color=colormap[color_num])
    ax.plot((newX_1, newX_2), (newY_1, newY_2), color=colormap[color_num])

    pt1.set_data(xs1, ys1)
    pt2.set_data(xs2, ys2)

    theta_text.set_text(textTemplate % t)
    n = 0
    for i in range(len(xs)):
        # if left < xs[i] < (left + width) and bottom < ys[i] < (bottom + height):
        if left < xs[i] < (left + width) and bottom < ys[i] < (bottom + height) and \
                left < xs1[i] < (left + width) and bottom < ys1[i] < (bottom + height) and \
                left < xs2[i] < (left + width) and bottom < ys2[i] < (bottom + height):
            n += 1

    print('number of tracked points inside the ROI: ', n)

    return cir, pt, pt1, pt2, theta_text

if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, -theta, interval=50, blit=True)
    Writer = animation.FFMpegWriter(fps=20, metadata=dict(artist='Me'))
    file_string = r'D:\Daten\TUD SS2020\Masterarbeit\EpiCycloid\HypoCycloidanimation_tryout_01.mp4'
    ani.save(file_string, writer=Writer)
