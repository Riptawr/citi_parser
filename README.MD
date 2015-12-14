## Citibank csv statement parser

Simple script i wrote to return a sorted list of top withdrawals from citibank csv statements. 
Currently only credit card accounts and statements, starting with 'ACCT' are supported  

### Dependencies:  
- [Pandas](http://pandas.pydata.org)
- [python-matplotlib](http://matplotlib.org/users/installing.html)
- [jupyter notebook - former ipython](https://jupyter.readthedocs.org/en/latest/install.html)

### Usage:  
from the console (boring):  
python2 parse_statements.py </dir/to/statements.csv> <currency>  
example: python2 parse_statements.py /home/myuser RUR  

from the browser:
- start jupyer notebook, load citibank_csv_parser.ipynb  
- run the cells  

