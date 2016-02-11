try:
    from IPython.html import widgets
    from IPython.html.widgets import *
except:
    try:
        from ipywidgets import widgets
        from ipywidgets.widgets import *
    except:
        print 'do: pip install --user ipywidgets'
        
    
from IPython.display import clear_output, display, HTML
import pylab as plt
import numpy as np

def show_args(**kwargs):
    w = int(kwargs['a'])
    sd = float(kwargs['sd'])
    filt = {}
    filt['Low Pass'] = np.array([1./w]*w).astype(float)
    filt['1st Order High Pass'] = np.array([0]*w).astype(float)
    filt['1st Order High Pass'][0] = 1
    filt['1st Order High Pass'][-1] = -1
    filt['2nd Order High Pass'] = np.array([0]*w).astype(float)
    filt['2nd Order High Pass'][0] = 1
    filt['2nd Order High Pass'][-1] = 1
    filt['2nd Order High Pass'][w/2] = -2

    x = np.linspace(0, 100, 500)

    y = {}
    y['Step'] = np.ones_like(x);
    y['Step'][x<=x.max()/2] = 0.

    y['Ramp'] = x.copy()/x.max()
    y['Ramp'][x>x.max()/2] = 1. - y['Ramp'][x>x.max()/2]
    y['Ramp'] *= 2

    y['Flat'] = x*0 + 0.5
    y['Pulse'] = y['Step'].copy()
    half = y['Pulse'][::2]
    other = half[::-1]

    y['Pulse'] = np.append(half,other).flatten()

    xx = x.copy()
    yy = y[kwargs['Signal']].copy()
    ff = filt[kwargs['FilterType']].copy()
    if sd:
      yy = np.random.normal(yy, sd)
    rr = np.convolve(yy,ff,'same')

    #s = '<h3>Filter:</h3><table>\n'
    #for k,v in kwargs.items():
    #    s += '<tr><td>{0}</td><td>{1}</td></tr>\n'.format(k,v)
    #s += '</table>'
   
    #display(HTML(s))
    plt.figure(1,figsize=(10,7))
    plt.plot(xx,yy,'k-')
    
    plt.ylim(-1.5,1.5)

    plt.plot(xx,rr,'r')



interact(show_args,
         Signal =['Step','Ramp','Flat','Pulse'],
         FilterType =['Low Pass','1st Order High Pass','2nd Order High Pass'],
         a=widgets.FloatSlider(min=2, max=100, step=1, value=3, description="Filter width"),
         sd=widgets.FloatSlider(min=0.0, max=0.3, step=0.01,value = 0.0, description="noise sd")
         )
