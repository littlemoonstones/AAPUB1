## URL：： (lab)-(Jupyter) 
## 2019_ME2002 Wek05 Demo 
from pylab import *
import numpy as np
x = np.linspace(-np.pi, np.pi, num=256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
plot(x, y)
plot(x, y1)
# define plot title $\sin$表示希臘字母
title("Functions $\sin$ and $\cos$")
# set x limit
xlim(-3.0, 3.0)
# set y limit
ylim(-1.0, 1.0)
# format ticks at specific values
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
[r'$-1$', r'$0$', r'$+1$'])
show()