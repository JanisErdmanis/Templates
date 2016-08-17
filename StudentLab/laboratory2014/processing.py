# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:10:41 2014

@author: akels
"""
from pandas import read_table,concat

# The statement 'from pandas import *' and then dismissing all 'plt' 
# from code is faster for coding but it also makes it harder to learn from code.
import pylab as plt

# --- Inputing the data ---

table = read_table('table.dat')

# Lets update namespace with new definitions
for col,series in table.iterkv():
    globals()[col]=series
# Now the variables FHWM,... have been created

# --- Generating new columns ---

# Just precise values in SI for various physical constants 
from scipy import constants

wavelength = constants.h*constants.c/(energy*constants.e) * 1e10 
error = FWHM/energy * wavelength

argument = 1 - plt.cos(angle*plt.pi/180) 

# --- Ploting ---

fig = plt.figure() # good habit

plt.errorbar(argument,wavelength, yerr=error, fmt ='.')
plt.xlabel(r'$1-\cos \phi$')
plt.ylabel(r'$\Delta \lambda \, [pm]$')

# Obtaining the best parameters to fit curve
from scipy.optimize import curve_fit
f = lambda x,m,n:m*x + n # m and n are parameters

# sigma=error is optional but so powerfull!
# par are list [m,n]
par, cov = curve_fit(f,argument,wavelength,sigma=error)

x = plt.linspace(0,2)
# but the *par just unpacks the list as direcly given f(x,n,m)
plt.plot(x,f(x,*par),label='par = {0} \n cov = {1}'.format(par,cov))

plt.legend(loc=2)
plt.show()

fig.savefig('plot.pdf') # also plot.png is valid

# --- Creating table for latex ---

# Asigning new names for columns
angle.name=r'$\phi \, [deg]$'
energy.name = r'$E \, [keV]$'
# FWHM has already satisfactory name
argument.name = r'1 - \cos \phi'
wavelength.name = r'$\lambda \, [pm]$'
error.name = '$\Delta \lambda$'

# Creating new DataFrame from series
# The wavelength.map('{:.3f}'.format) creates object with formated rows
formated_table = concat([angle,energy,FWHM,argument,wavelength.map('{:.3f}'.format),error],axis=1)

# Output latex representation of the table
formated_table.to_latex('table.tex')
