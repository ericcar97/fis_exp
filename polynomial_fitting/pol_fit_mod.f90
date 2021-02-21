module pol_fit_mod
    use cholesky_mod
    implicit none
    public pol_fit
   
contains
subroutine pol_fit(x_data, y_data, y_error, data_len, pol_grade, coeff, std_dev)
    integer, intent(in) :: data_len, pol_grade
    integer             :: j, k
    real(kind = 8), dimension(0:pol_grade), intent(out)  :: coeff, std_dev
    real(kind = 8), dimension(0:pol_grade, 0:pol_grade)  :: alpha
    real(kind = 8), dimension(0:pol_grade)               :: beta
    real(kind = 8), dimension(1:data_len), intent(in)    :: x_data, y_data, y_error
    do k = 0, pol_grade
        beta(k) = sum(y_data*x_data**k/y_error**2)
        do j = 0, pol_grade
            alpha(k,j) = sum(x_data**(k+j)/y_error)
        end do
    end do

    call cholesky_inv(alpha,pol_grade)
    coeff = matmul(alpha,beta)
    do j = 0, pol_grade
        std_dev(j) = sqrt(alpha(j,j))
    end do
end subroutine pol_fit
end module pol_fit_mod