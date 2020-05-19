pip install ..
cd ..
python run_tests.py
cd docs
rm source/naivert.*
rm source/modules.rst
sphinx-apidoc -o ./source ../naivert
make clean
make html
make latex
cd build/latex
make
