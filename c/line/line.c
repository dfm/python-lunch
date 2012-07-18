double compute_chi2(double m, double b, double *x, double *y, double *yerr,
        int N)
{
    int i;
    double chi2 = 0.0;

    for (i = 0; i < N; i++) {
        double d = (y[i] - (m * x[i] + b)) / yerr[i];
        chi2 += d * d;
    }

    return chi2;
}
