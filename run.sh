#!/bin/bash
python -O travelling_salesman.py 2 citiesAndDistances.pickled  outputs/output2.pickled
python -O travelling_salesman.py 3 citiesAndDistances.pickled  outputs/output3.pickled
python -O travelling_salesman.py 4 citiesAndDistances.pickled  outputs/output4.pickled
python -O travelling_salesman.py 5 citiesAndDistances.pickled  outputs/output5.pickled
python -O travelling_salesman.py 6 citiesAndDistances.pickled  outputs/output6.pickled
python -O travelling_salesman.py 7 citiesAndDistances.pickled  outputs/output7.pickled
python -O travelling_salesman.py 8 citiesAndDistances.pickled  outputs/output8.pickled
python -O travelling_salesman.py 9 citiesAndDistances.pickled  outputs/output9.pickled
python -O travelling_salesman.py 10 citiesAndDistances.pickled  outputs/output10.pickled
python -O travelling_salesman.py 11 citiesAndDistances.pickled  outputs/output11.pickled
python -O travelling_salesman.py 12 citiesAndDistances.pickled  outputs/output12.pickled
python -O travelling_salesman.py 13 citiesAndDistances.pickled  outputs/output13.pickled
python -O travelling_salesman.py 14 citiesAndDistances.pickled  outputs/output14.pickled

python -O tests.py
