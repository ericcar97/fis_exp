import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px
from matplotlib import rc
from numpy import *
from pol_fit_mod import pol_fit_mod

#importing the data
file = 'data.dat'
data = pd.read_csv(file)
column = data.columns
x_data = data[column[0]].values
y_data = data[column[1]].values
y_error = data[column[2]].values
N = len(data)


#polinomial fit
pol_grade = 2
coeff, std_dev = pol_fit_mod.pol_fit(x_data, y_data, y_error, pol_grade, N)


#using horner algorithm to make the polynomial function
def horner(coeff,x):
    p = 0
    for i in range (0,pol_grade + 1):
        p = coeff[pol_grade - i] + x*p
    return p


residuals = y_data - horner(coeff,x_data)

#Results
print(coeff)
print(std_dev)



#plotting
x_min = x_data[0] - (x_data[1] - x_data[0])/2
x_max = x_data[N-1] + (x_data[N-1]- x_data[N-2])/2
x_fit = linspace(x_min, x_max,1000)
y_fit = horner(coeff,x_fit)
fig = plt.figure(1, figsize = (8,5))
gs = gridspec.GridSpec(2, 1, height_ratios = [6,2],
                       hspace = 0.15)
plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')
def plotStyle():
    plt.grid(b = True, ls = '--',
             lw = 0.5, c = 'grey')
    plt.xlim(x_min,x_max)

ax1 = fig.add_subplot(gs[0])
ax1.set_title('Ajuste Polinomial')
ax1.set_ylabel('Variable dependiente')
ax1.scatter(x_data, y_data, c = 'r', s = 0.5)
ax1.errorbar(x_data, y_data , yerr = y_error,
            ls =  'none', elinewidth = 0.5,
            capsize = 1, capthick = 0.5, c = 'k')
ax1.plot(x_fit, y_fit, lw = 0.5, c = 'k')
#ax1.set_xticklabels([])
plotStyle()

ax2 = fig.add_subplot(gs[1])
ax2.set_xlabel('Variable dependiente')
ax2.set_ylabel('Residuos')
ax2.scatter(x_data, residuals, c = 'r')
ax2.plot(x_fit, x_fit*0, ls = '--', lw = 0.5, c = 'k')
plotStyle()
plt.savefig('plot.eps')
