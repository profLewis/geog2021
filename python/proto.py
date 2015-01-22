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

plt.figure(1,figsize=(15,10))
plt.subplot(221)
plt.plot(x,y_step,'k-')
plt.title('step')
plt.ylim(-0.1,1.1)

plt.subplot(222)
plt.plot(x,y_ramp,'k-')
plt.title('ramp')
plt.ylim(-0.1,1.1)

plt.figure(2,figsize=(15,10))
y_stepn = np.random.normal(y_step, 0.05)
plt.subplot(221)
plt.plot(x,y_stepn,'k-')
plt.title('noisy step')
plt.ylim(-0.1,1.1)

plt.subplot(222)
y_rampn = np.random.normal(y_ramp, 0.05)
plt.plot(x,y_rampn,'k-')
plt.title('noisy ramp')
plt.ylim(-0.1,1.1)


plt.show()


