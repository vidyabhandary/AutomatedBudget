# Semi Automated Weekly Budget

Weekly budget is discretionary spending but I think mine can benefit from 
from some automation. Especially for the regular items (staples). 
The idea is to create an automated list of items to buy within the specified 
budget. It can obviously be manually tweaked as desired.

While there are many approaches to this - I am sticking to the one that solves
my problem.

I get the raw data in the form of a text file. So this will be cleaned and then
used to generate the items to be purchased (within budget).

## Steps - 
## 1. Receive raw data and perform basic cleaning using a python program

The raw data can be found in `raw_data.txt` which is then cleaned using 
`raw_data_clean.py` from within the jupyter notebook - `Automate_Budget.ipynb`.

## 2. In-depth data cleaning is performed in the jupyter notebook - `Automate_Budget.ipynb`

The display of the dataframe helps to see the data cleaning results.

## 3. Staples are priority 1 items
Priority 4 and 5 items are not 
automated. They can be added as per discretion.

## 4. The priority index is present in `staples_master_data.csv` 
This file can be updated directly if priority items need to be changed. It will 
get be read from and reflected in the jupyter notebook - `Automate_Budget.ipynb`.

## 5. Budget Amount
The budget amount to adhere to is present on a single line (only numeric) in `budget.txt`. It contains no other information

All items as per priority are added while adhering to the budget

## 6. The output is a transaction list of items to be purchased.

This output is stored in `weekly_order.txt` in the format that is received by 
my provider.

## 7. Data is added to the sqllite database
This is to facilitate further analysis which can be done after data has been 
collected for a period of time.
