## Citibank csv statement parser

Simple script i wrote to return a sorted list of top withdrawals from citibank csv statements. 
Currently only credit card accounts and statements, starting with 'ACCT' are supported  

### Dependencies:  
- [Pandas](http://pandas.pydata.org)

### Usage:  
python2 parse_statements.py </dir/to/statements.csv> <currency>

example: python2 parse_statements.py /home/myuser RUR

