import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.optimize import curve_fit
from matplotlib import rc
from numpy import *
from tabulate import tabulate
from scipy.stats import t

###Importing and cleaning the data
file = 'vC_RC'
data = pd.read_csv(file + '.csv')
column = data.columns
data[column[1]] = -data[column[1]] #The multimeter got an inverse measure
fig = px.scatter(data, y = column[1])
fig.show()
print('From: ')  #for the sample file, try from 225 to 280
ni = input()
print('To: ')
nf = input()
data = data.loc[ni:nf]
print(data)
x_data = data[column[0]].values
x_data = x_data - x_data[0]
y_data = data[column[1]].values
y_error = 0.1*y_data
N = len(data)

###Defying the model
def V_model(t,V,tau):
    return V*(1-exp(-t/tau))

###Model fitting
V0, tau0 = 3. , 1.
init_values = [V0,tau0]
fit, covariance = curve_fit(V_model,x_data,y_data,
                            p0 = init_values,
                            absolute_sigma = True,
                            sigma = y_error)
nu = N - 2 #### degrees of freedom = number of data points - number of parameters fitted
std_dev = sqrt(diag(covariance))
residuals = y_data - V_model(x_data,fit[0],fit[1])
std_error = sqrt(diag(covariance)*sum(residuals**2)/nu)

#Confidence interval IC
alpha = 0.05 #95%
t = t.ppf(1-alpha/2, df = nu)

#Results
print('results: ', fit)
print('standar deviations: ', std_dev)
print('standar error: ', std_error)
print('adjusted standard error with t distribution: ', std_error*t)
print('Confidence interval: ', fit - std_error*t, 'to', fit + std_error*t)


#Plotting
xmin = (x_data[0]- x_data[1])*2
xmax = x_data[N-1]+(x_data[N-1] - x_data[N-2])*2
xfit = linspace(xmin,xmax,1000)
yfit = V_model(xfit,fit[0],fit[1])
fig = plt.figure(1, figsize = (8,5))
gs = gridspec.GridSpec(2, 1, height_ratios = [6,2],
                       hspace= 0.15)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
def plotStyle():
    plt.grid(b = True, ls = '--',
            lw = 0.5, c = 'k')
    plt.xlim(xmin,xmax)
 
#Subplot: fitted function
ax1 = fig.add_subplot(gs[0])
ax1.set_ylabel('Voltaje [V]')
ax1.scatter(x_data,y_data,c = 'r',s = 0.5)
ax1.errorbar(x_data,y_data, ls = 'none',
             c = 'k',
             yerr = y_error,
             elinewidth= 0.5,
             capsize = 1,
             capthick = 0.5)
ax1.plot(xfit,yfit,lw = 0.5,
             c = 'k')
#ax1.set_xticklabels([])
plotStyle()

#Subplot: Residuals
ax2 = fig.add_subplot(gs[1])
ax2.scatter(x_data,residuals,c = 'r')
ax2.set_xlabel('Tiempo [s]')
ax2.set_ylabel('Residuos')
plotStyle()
plt.savefig(file + '.eps')