f2py3 -m lin_fit_mod -c lin_fit_mod.f90
mv lin_fit_mod.cpython-38-x86_64-linux-gnu.so lin_fit_mod.so
python3 lin_fit.py
