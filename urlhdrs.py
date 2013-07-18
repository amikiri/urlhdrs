#! /usr/bin/env python3
''' This program will rerieve http response headers for a given url '''

import sys, os
from urllib.request import urlopen

def output_headers(url_file):
	''' Controls the output of the headers '''
#	if len(sys.argv) < 2:
#		print("USAGE: urlhdrs.py url output_file")
	if len(sys.argv) > 2:
		output_file = open(sys.argv[2], 'a')
		url_name = str(url_file.geturl())
		output_file.write(url_name + "\n")
		url_info = str(url_file.info())
		output_file.write(url_info + "\n")
		print(url_file.geturl())
		print(url_file.info())
	else:
		print("No output specified. Printing to terminal.")
		print("*" * 20)
		print(url_file.geturl())
		print(url_file.info())

def main():
	url_file = urlopen(sys.argv[1])
	output_headers(url_file)
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("USAGE: urlhdrs.py url output_file")
	else:
		main()