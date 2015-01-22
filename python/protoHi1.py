# dont worry about this -- its to make the figures appear ...
import matplotlib.pyplot as plt
import numpy as np
# x
x = np.linspace(0, 100, 500)

y_step = np.ones_like(x);
y_step[x<=x.max()/2] = 0.

y_ramp = x.copy()/x.max()
y_ramp[x>x.max()/2] = 1. - y_ramp[x>x.max()/2]
y_ramp *= 2

size = 7
filt = [1.0,-1.0]
print 'filter',filt

plt.figure(1,figsize=(15,10))
plt.subplot(221)
plt.plot(x,y_step,'k-')
fy_step = np.convolve(y_step, filt,'same')
fy_ramp = np.convolve(y_ramp, filt,'same')

plt.plot(x,fy_step,'r--',linewidth=4.0)


plt.title('step')
plt.ylim(-0.1,1.1)

plt.subplot(222)
plt.plot(x,y_ramp,'k-')
plt.plot(x,fy_ramp,'r--',linewidth=4.0)

plt.title('ramp')
plt.ylim(-0.1,1.1)

plt.figure(2,figsize=(15,10))
y_stepn = np.random.normal(y_step, 0.05)
fy_stepn = np.convolve(y_stepn, filt,'same')

plt.subplot(221)
plt.plot(x,y_stepn,'k-')
plt.plot(x,fy_stepn,'r--',linewidth=4.0)

plt.title('noisy step')
plt.ylim(-0.1,1.1)

plt.subplot(222)
y_rampn = np.random.normal(y_ramp, 0.05)
fy_rampn = np.convolve(y_rampn, filt,'same')
plt.plot(x,fy_rampn,'r--',linewidth=4.0)

plt.plot(x,y_rampn,'k-')
plt.title('noisy ramp')
plt.ylim(-0.1,1.1)


plt.show()


