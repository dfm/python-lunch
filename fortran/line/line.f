      subroutine chi2(m, b, x, y, yerr, N, res)

        integer :: i
        real :: d

        integer, intent(in) :: N
        real, intent(in) :: m, b
        real, dimension(N), intent(in) :: x, y, yerr
        real, intent(out) :: res

        res = 0.0

        do i=1,N

            d = (y(i) - (m * x(i) + b)) / yerr(i)
            res = res + d * d

        enddo

      end subroutine
