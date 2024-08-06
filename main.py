# main.py

# import statements
import pandas as pd
from person import Person


def main():
	# main body code
	filename = input("Please enter file name (must be in \'inputs\\\': ")
	df = pd.read_csv('inputs/' + filename)

	print(df)

	return -1