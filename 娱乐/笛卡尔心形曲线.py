import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5,5))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')


ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

ax.set_yticks([-1.0,-0.5,0.5,1.0,1.5])
ax.set_xticks([-1.0,-0.5,0.5,1.0])


plt.title('Cardioid', fontsize=24)
x = np.linspace(-1,1,200)
y1 = np.sqrt(1-np.power(x, 2)) + np.power(np.square(x), 0.33)
y2 = -np.sqrt(1-np.power(x, 2)) + np.power(np.square(x), 0.33)
plt.plot(x, y1, color='#FFC0CB')
plt.plot(x, y2, color='#FFC0CB')
plt.show()