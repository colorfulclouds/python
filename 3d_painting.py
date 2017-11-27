from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D




fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(10, 13, 0.025)
Y = np.arange(4, 6, 0.025)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(np.sin(X**2) + np.log(Y))
#Z = R


Z = 21.5 + X*np.sin(4*np.pi*X) + Y*np.sin(20*np.pi*Y)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm)

plt.show()
