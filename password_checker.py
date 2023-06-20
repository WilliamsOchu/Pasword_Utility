#!/usr/bin/env python3

import os
import re

## Lets use regular expressions to check 


def check_password(filename):
	print("Know how tough your password is and take necessary action")
	print('Your password can be \"Weak",\"Strong" or \"Excellent"')
	print('\n')	
	
	password_to_check=re.search(r"[a-zA-Z0-9\?@#$%&*!^+]", filename)
	if password_to_check != None:
		password_length(filename)


def password_length(filename):
	files=open(filename, 'r')
	content=files.readline()
	len_content=len(content.strip())
	

	if len_content in range(0,8):
		remark='\033[1m\033[41mWeak Password\033[0m'
	elif len_content in range(9,14):
		remark='\033[1m\033[43mStrong Password\033[0m'
	elif len_content in range (15,100):
		remark='\033[1m\033[42mExcellent Password\033[0m'
 	
	print('Password Status: {}'.format(remark))



check_password('password_file.txt')

