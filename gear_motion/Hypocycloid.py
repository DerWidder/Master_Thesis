'''function used to get Hypocycloid'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches

# a is the radius of the outer circle, b is the radius of the inner circle.
a = 17.05
b = -5.8  # b<0, HypoCycloid

# range of theta to show the HypoCycloid
theta = np.arange(-0.5, 6.4, 0.05)

# create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.xlim((-18, 18))
plt.ylim((-18, 18))

# add a colored rectangular as the imaging frame
left, bottom, width, height = (17.05 - 2.766, -3.406, 3.266, 4.406)
rect = mpatches.Rectangle((left, bottom), width, height, alpha=0.1, facecolor='red')
plt.gca().add_patch(rect)

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
pt, = ax.plot([a], [0], '*')
cir, = ax.plot(a+b+b*yCircle, b*yCircle, '-', lw=1)
cycloid, = ax.plot([], [], '-', lw=1)

xs, ys = [], []

# plot configurations
def animate(t):
    if t == 0:
        xs.clear()
        ys.clear()

    cenX = (a+b)*np.cos(t)
    cenY = (a+b)*np.sin(t)
    cir.set_data(cenX+b*xCircle, cenY+b*yCircle)
    newX = cenX - b*np.cos((a+b)*t/b)
    newY = cenY - b*np.sin((a+b)*t/b)

    xs.append(newX)
    ys.append(newY)
    pt.set_data(xs, ys)
    cycloid.set_data(xs, ys)
    theta_text.set_text(textTemplate % t)
    n = 0
    for i in range(len(xs)):
        if left < xs[i] < (left + width) and bottom < ys[i] < (bottom + height):
            n += 1

    print('number of tracked points inside the ROI: ', n)

    return cycloid, cir, pt, theta_text
if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, -theta, interval=50, blit=True)
    Writer = animation.FFMpegWriter(fps=20, metadata=dict(artist='Me'))
    file_string = r'D:\Daten\TUD SS2020\Masterarbeit\EpiCycloid\HypoCycloidanimation_tryout.mp4'
    ani.save(file_string, writer=Writer)

