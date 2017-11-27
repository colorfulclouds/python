#! /bin/
#-*- utf-8 -*-

#__author__


import csv
from itertools import islice

def load_data(file_name = 'train_csv'):
	csv_reader = csv.reader(open(file_name))
	
	train_set = []
	
	for row in islice(csv_reader , 1 , None):
		train_set.append(row)

	return train_set