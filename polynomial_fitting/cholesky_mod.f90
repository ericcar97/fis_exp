module cholesky_mod
    implicit none
contains
subroutine cholesky_inv(S,N)
    real(kind = 8), dimension(0:N,0:N), intent(inout) :: S
    real(kind = 8)      :: suma
    integer, intent(in) :: N
    integer             :: i, j, k

    S(0,0) = 1/sqrt(S(0,0))
    
    do j=1, N
        S(0,j) = S(0,j)*S(0,0)
    end do
    
    do i=1, N-1
        suma = 0
        do k=0, i-1
            suma = suma + S(k,i)**2
        end do
        S(i,i) = 1/sqrt(S(i,i) - suma)
        do j=i+1, N
            suma = 0
            do k=0, i-1
                suma = suma + S(k,i)*S(k,j)
            end do
            S(i,j) = (S(i,j) - suma)*S(i,i)
        end do
    end do
    
    suma = 0
    do k=0, N-1
        suma = suma + S(k,N)**2
    end do
    S(N,N) = 1/sqrt(S(N,N) - suma)
    
    do j=1, N
        do i=0, j-1
            suma = 0
            do k=i, j-1
                suma = suma + s(k,i)*s(k,j)
            end do
            s(j,i) = -s(j,j)*suma
        end do
    end do
    do i=0, N
        do j=i, N
            suma = 0
            do k=j+1, N
                suma = suma + s(k,i)*s(k,j)
            end do
            s(i,j) = s(j,i)*s(j,j) + suma
            s(j,i) = s(i,j)
        end do
    end do

end subroutine
end module