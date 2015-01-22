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
filts = np.array([1./size]*size)
filt = [1.0,-2.0, 1.0]
print 'filter 1:        ',str(['%4.2f'%i for i in filt]).replace("'",'')
print 'filter 2:        ',str(['%4.2f'%i for i in filts]).replace("'",'')


plt.figure(1,figsize=(15,10))
plt.subplot(221)
plt.plot(x,y_step,'k-')
fy_step = np.convolve(y_step, filt,'same')
fy_ramp = np.convolve(y_ramp, filt,'same')
fy_steps = np.convolve(fy_step, filts,'same')
fy_ramps = np.convolve(fy_ramp, filts,'same')

filt2 = np.convolve(filt, filts,'full')
print 'combined filter: ',str(['%4.2f'%i for i in filt2]).replace("'",'')

fy_steps = np.convolve(fy_step, filts,'same')
fy_ramps = np.convolve(fy_ramp, filts,'same')
fy_steps2 = np.convolve(y_step, filt2,'same')
fy_ramps2 = np.convolve(y_ramp, filt2,'same')



plt.plot(x,fy_step,'b-',linewidth=4.0)
plt.plot(x,fy_steps,'g-',linewidth=3.0)
plt.plot(x,fy_steps2,'r--',linewidth=2.0)

plt.title('step')
plt.ylim(-1.1,1.1)
plt.xlim(45,55)

plt.subplot(222)
plt.plot(x,y_ramp,'k-')
plt.plot(x,fy_ramp,'b-',linewidth=4.0)
plt.plot(x,fy_ramps,'g-',linewidth=3.0)
plt.plot(x,fy_ramps2,'r--',linewidth=2.0)

plt.title('ramp')
plt.ylim(-0.01,0.01)
plt.xlim(45,55)

plt.show()


