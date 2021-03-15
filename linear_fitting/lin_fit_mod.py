#Linear Regression module
from numpy import *

def s_lin_reg(x_data, y_data, N):
    sum_x = sum(x_data)
    sum_y = sum(y_data)
    sum_xx = sum(x_data**2) 
    sum_yy = sum(y_data**2)
    sum_xy = sum(x_data*y_data)
    
    SXY = sum_xy - sum_x*sum_y/N
    SXX = sum_xx - sum_x**2/N
    SYY = sum_yy - sum_y**2/N

    a = SXY/SXX
    b = (sum_y - a*sum_x)/N

    SSE = sum((y_data-a*x_data-b)**2)

    sigma = sqrt(SSE/(N-2))
    r_squared = 1 - SSE/SYY

    sa = sigma/sqrt(SXX)
    sb = sa*sqrt(sum_xx/N)
    return a, b, sa, sb, r_squared, sigma

def w_lin_reg(x_data, y_data, y_error, N):
    wsum_x = sum(x_data/y_error**2)
    wsum_y = sum(y_data/y_error**2)
    wsum_xx = sum(x_data**2/y_error**2)
    wsum_xy = sum(x_data*y_data/y_error**2)
    wsum_1 = sum(1/y_error**2)
    sum_y = sum(y_data)
    sum_yy = sum(y_data**2)


    Delta = wsum_1*wsum_xx - wsum_x**2
    a =  (wsum_1*wsum_xy - wsum_x*wsum_y)/Delta
    b = (wsum_xx*wsum_y - wsum_x*wsum_xy)/Delta
    sa = sqrt(wsum_1/Delta)
    sb = sqrt(wsum_xx/Delta)

    SYY = sum_yy - sum_y**2/N
    SSE = sqrt(sum((y_data-a*x_data-b)**2))


    sigma = sqrt(SSE/(N-2))    
    r_squared = 1 - SSE/SYY
    return a, b, sa, sb, r_squared, sigma
