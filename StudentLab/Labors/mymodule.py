# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 18:17:41 2014

@author: akels
"""

from pandas import read_table


# %% The processing of pulsation time dependance
ni=1
tab = read_table("data/SPEKTRS-{0}.txt".format(ni),decimal=",",header=0,names=["t","v"])

ti = tab['t']                
vi = tab['v']
    
import numpy as np

vi = vi - np.average(vi)

import pylab as plt

fig1 = plt.figure()
plt.plot(ti,vi-np.average(vi))
plt.xlabel('time [sec]')
plt.ylabel('v [m/sec]')

from numpy import log

power = np.abs(np.fft.rfft(vi-np.average(vi)))**2
freq = np.fft.rfftfreq(ti.shape[-1],d=ti[1]-ti[0])


lpower = log(power)


window = 5
weights = np.repeat(1.,window)/window
lpower_conv = np.convolve(lpower,weights,'valid')

fig3 = plt.figure()
plt.plot(freq[:-window+1],lpower_conv)

plt.xlim(0,500)
plt.ylim(0,8)
plt.ylabel('log(Power spectrum)')
plt.xlabel('Frequency [Hz]')

# %% The procesing of graduation line

tab2 = read_table("data/okal.txt",decimal=",",header=0,names=["v","U",' ',' ',' ',"vpred"])

figo = plt.figure()
plt.plot(tab2.v,tab2.U,'.')
plt.plot(tab2['vpred'],tab2["U"])
plt.xlim(0,14)
plt.ylim(1.60,2.20)
plt.xlabel('v [m/sec]')
plt.ylabel('Voltage on sensor [V]')


# %% Velocity distribution

tab3 = read_table("data/sadal.txt",decimal=",",header=0,names=["x",'','',"Umean","Urms"])


fig4 = plt.figure()
plt.plot(tab3["x"],tab3["Umean"],'.-')
plt.xlabel('x [mm]')
plt.ylabel('U mean [m/sec]')


fig5 = plt.figure()
plt.plot(tab3["x"],tab3["Urms"],'.-')
plt.xlabel('x [mm]')
plt.ylabel('Urms [m/sec]')

fig6 = plt.figure()
plt.plot(tab3["x"],tab3["Urms"]/tab3['Umean'],'.-')
plt.xlabel('x [mm]')
plt.ylabel('Tu')


# %% k-epsilon modelis

#fig7 = plt.figure()
#plt.plot(log(tab3["Urms"] * tab3["x"]/1.67e-5),tab3["Urms"]/tab3["Umean"],'.-')


# %%

if True:
    
    from matplotlib.backends.backend_pdf import PdfPages

    with PdfPages('results/figs.pdf') as pdf:
    
        pdf.savefig(fig1)
        pdf.savefig(fig3)
        pdf.savefig(figo)
        pdf.savefig(fig4)
        pdf.savefig(fig5)
        pdf.savefig(fig6)
        
    from pandas import DataFrame,ExcelWriter
    
    tab = DataFrame.from_items([['t [sec]',ti],['v [m/sec]',vi],['v-mean(v) [m/sec]',vi-np.average(vi)]])
    
    writer = ExcelWriter('results/output.xlsx')
    tab[::100].to_excel(writer,'time spectrum')
    tab2[['v','U','vpred']].to_excel(writer,'graduation')
    tab3[['x','Umean','Urms']].to_excel(writer,'sadalijumi')
    
    #tab.to_latex()