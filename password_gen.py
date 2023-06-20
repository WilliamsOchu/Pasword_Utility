#!/usr/bin/env python3

import random
import string
import time 
import os



def password_initializer():
    
	print('\033[1m\033[40mWelcome to Lucid Password Generator, Kindly follow the interctive prompt to generate a strong password\033[0m')
	
	print("\n")
	password_jam()



## Now let us put the first password

def password_letter():
    while True:
        try:
            letter_count=int(input("How many alphabets do you want in your password? Must be less than 15 characters: "))
        except ValueError:
            print('You must enter a numeric digit')
            print('\n')
            
    
        else:
            if letter_count <= 15:
                password_rand_letters=''.join(random.choice(string.ascii_letters) for x in range(letter_count))
            else:
                print('It must be less than 15 characeters')
                print('\n')
                return password_letter()
                
            print('\n')
            return password_rand_letters

                
    
    
    
  
    
    
def password_number():
    while True:
        try:
            
            number_count=int(input('How many numbers do you want in your password? (0-9 only): '))
        except ValueError:
            print('You must enter a numeric digit')
            print('\n')
            
        else:
            
            if number_count < 10:
                password_rand_nums=''.join(["{}".format(random.randint(0,9)) for num in range(0,number_count)])
            else:
                print("(0 - 9 only)")
                print('\n')
                return password_number()
        
            print('\n')
            return password_rand_nums
    
    
    

def password_symbol():
    
    symbols=['?','@','#','$','%','&','*','!','^','+']
    
    while True:
        try:
            
    
            symbol_count=int(input("How many symbols do you want in your password? Max number is 5 symbols: "))
            
        except ValueError:
            print('You must enter a numeric digit')
            print('\n')
            
        else:
            
            if symbol_count <=5:
                password_rand_syms=random.choices(symbols, k=symbol_count)
        
        
            else:
                print('You must enter a number not greater than 5')
                print('\n')
                return password_symbol()
        
            print('\n')
            return password_rand_syms



def password_jam():
    a=password_letter()
    b=password_number()
    c=password_symbol()
    
    password=''
    d=password.join(a)
    e=password.join(b)
    f=password.join(c)
    
    
    g=d+e+f
    
    ## Lets shuffle the password 
    
    shuffle_password=list(g)
    random.shuffle(shuffle_password)
    final_password=''.join(shuffle_password)
    
    
    print('Generating Password')
    countdown_indicator()
    print('\n')
    print('Your password is: \033[1m\033[40m{}\033[0m'.format(final_password))
    
    password_file=open('password_file.txt', 'w+')
    password_file.write('{} \n'.format(final_password))
    password_file.close()
 
 

    
def countdown_indicator():
	n=0
	while n <=4:
		
		print("\033[1m.\033[0m",end=" ")
		time.sleep(0.25)
		n+=1


password_initializer()      