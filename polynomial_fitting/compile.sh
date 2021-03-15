f2py3 -m pol_fit_mod -c pol_fit_mod.f90 cholesky_mod.f90
mv pol_fit_mod.cpython-38-x86_64-linux-gnu.so pol_fit_mod.so
python3 pol_fit.py
