import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

a = 2 # Amplitude
time=1 # second
freq=2
w = 2 * np.pi * freq # radian/sec
samples_per_sec = freq * 30
total_samples = samples_per_sec * time
t = np.arange(total_samples) / samples_per_sec # [0,1,2,3,4,5] * 0.1
x = a*np.sin(w*t)
x_axis = t
y_axis = x
#ax.plot([2,5,7,9],[1,2,3,4])
#ax.scatter([1,2,3,4],[1,2,3,4])
#ax.plot([4,5,6,7],[1,2,3,4])
ax.plot(x_axis, y_axis)
plt.show()
