import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px
from matplotlib import rc
from lin_fit_mod import lin_fit_mod
from numpy import *
from scipy.stats import t

#importing and cleaning the data
file = 'data.csv'
data = pd.read_csv(file)
column = data.columns
fig = px.scatter(data,y = column)
fig.show()
print('From: ')
ni = input()
print('To: ')
nf = input()
data = data.loc[ni:nf]
x_data = data[column[0]].values
y_data = data[column[1]].values
y_error = data[column[2]].values
N = len(data)

# Linear Regression
#a, b, sa, sb, r_squared, sigma  = lin_fit_mod.w_lin_fit(x_data, y_data, y_error, N)  #Weighted linear regression
a, b, sa, sb, r_squared, sigma  = lin_fit_mod.s_lin_fit(x_data, y_data, N)   #Simple linear regression
residuals = y_data - (a*x_data + b)

#t-student distribution
alpha = 0.05
t = t.ppf(1-alpha/2, df = N - 2)

#Results
print('number of points: ', N)
print('slope: ', a)
print('intercept: ', b)
print('standar desviation of the slope: ', sa)
print('standar desviation of the intercept: ', sb)
print('a uncertainty: ' ,sa * t)

#plotting
x_min = x_data[0] - (x_data[1] - x_data[0])/2
x_max = x_data[N-1] + (x_data[N-1]- x_data[N-2])/2
x_fit = linspace(x_min,x_max,1000)
y_fit = a*x_fit + b

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
plotStyle()
plt.savefig('plot.eps')