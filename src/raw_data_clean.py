# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:15:56 2020

@author: Vidya

Semi automated budget list builder - this pgm will do the basic cleaning 
of the raw data 

"""
import re
import string
import pandas as pd


class DataClean:
    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.spl_chars_re = re.compile('[%s]' % re.escape(string.punctuation))
        self.master_data = []

        # Mangled data - checks for the same
        self.in_unit = ['per', 'gm']
        self.skip_in_unit = ['piece', 'pack', 'dozen', 'each', 'papaya',
                             'blueberry', 'for', 'moringa']

    def remove_spl_chars(self, str):
        return self.spl_chars_re.sub('', str)

    def numeric_split(self, str):
        return re.split('(\d+)', str)

    def remove_numbers(self, str):
        return re.sub(r'\d+', '', str)

    def get_data(self):

        category = '-'
        unit, unit_amount = '-', 0
        price = 0
        item_name = None

        skip_items = ['flowers', 'order', 'free', 'rates', 'cash',
                      'you', 'soil', 'deliver', 'sunday']

        with open(self.in_file, mode='r', encoding='utf-8') as f:

            all_lines = f.readlines()

            for line in all_lines:
                line = line.lower()

                if any(skip in line for skip in skip_items):
                    continue

                if '*' in line:
                    category = self.get_category(line)
                    unit, unit_amount, price = '-', 0, 0

                elif any(item in line for item in self.in_unit) and not \
                        any(skip in line for skip in self.skip_in_unit):
                    unit_amount, unit = self.get_unit(line)

                else:
                    # Assume it is the item itself
                    line = line.strip()

                    if line:

                        ls = line.split('rs')
                        price = ls[-1]

                        item_name = self.get_item_name(ls[0])

                        lst = [category, item_name,
                               unit_amount, unit, price, 0]
                        self.master_data.append(lst)

        df = pd.DataFrame(self.master_data)

        df.to_csv(self.out_file, sep=',', header=None)

    def get_item_name(self, line):
        # Sample line - 2. Carrot/गाजर 🥕- Rs 30
        ls = line.split('/')
        item = self.remove_spl_chars(ls[0])
        return self.remove_numbers(item)

    def get_category(self, line):

        if 'dairy' in line:
            return 'dairy products'
        category = line.split('**')[1]
        return category

    def get_unit(self, line):
        ls = line.split('/')

        # Remove special chars like ()
        amt = self.remove_spl_chars(ls[0])

        # Eg - 250gm
        # amt_unit = re.split('(\d+)', amt)

        amt_unit = self.numeric_split(amt)

        # print('amt_unit ', amt_unit)

        if len(amt_unit) > 1:
            amt = amt_unit[1]
            unit = amt_unit[2].strip().lower()
            return amt, unit.lower()

        return '', amt.lower()


if __name__ == '__main__':

    input_file = 'raw_data.txt'
    output_file = 'raw_data.csv'
    raw_data = DataClean(input_file, output_file)
    raw_data.get_data()
