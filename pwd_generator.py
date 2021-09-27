#Simple Password Generator

import numpy as np
import random as rm 

#List for base_digits
word_list   =   np.array(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F','g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L','m', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R','s', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ])
              
number_list =   np.array(['1', '2', '3' , '4', '5', '6', '7','8', '9'])

symbol_list =   np.array(['!','@','#','$','%','^','&','*'])

#for 16 digits take 60% digits string, take 25% numbers and 15 % symbols;
word_count      =   16
weight_string   =   .60
weight_number   =   .25
weight_symbols  =   .15

ratio_string    =   (int) (word_count * weight_string)
ratio_numbers   =   (int) (word_count * weight_number)
ratio_symbols   =   (int) (word_count * weight_symbols)


#Code for filling in any gaps that occured when creating integer ratios
while (ratio_numbers + ratio_string + ratio_symbols < word_count):
    
    ratio_increase  =   rm.choice([1,2,3])
    
    if ratio_increase   ==    1:
        ratio_string    +=  1
    elif ratio_increase ==  2:
        ratio_numbers   +=  1
    else:
        ratio_symbols   +=  1


#raw_password: meaning a list of selected strings, numbers and symbols to create pwd from
raw_password = np.array([])

while (raw_password.size < ratio_string):
    raw_password    =    np.append(raw_password,rm.choice(word_list))
while (raw_password.size - ratio_string < ratio_numbers):
    raw_password    =   np.append(raw_password, rm.choice(number_list))
while (raw_password.size -ratio_numbers -ratio_string < ratio_symbols):
    raw_password    =   np.append(raw_password, rm.choice(symbol_list))

dict1   ={k:True for k in raw_password}

password    =   np.array([])

#Final Password
while(password.size < word_count):
    a = rm.choice(raw_password)
    if(dict1[a] == True):
        password = np.append(password,a)
        dict1[a] = False



