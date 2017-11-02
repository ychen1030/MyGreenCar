import math
import re
masterkey = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

def strToInt( value ):
    #Declare Variables
    length = 0 #used to get out of the while loop
    magnitud_list = list() #list to save the zeroes (potence) you need to add to the int
    single_numbers = list() #list of the numbers in the integer
    complete_number = list() #contains all the numbers multiplied by the potence
    wordkey = list(value) #just contains a list of the values in the input string
    magnitud = (len(wordkey)) #just the length of the input value
    #Create a list of values containing the power of each number
    while length < len(wordkey): #create the potence (number of zeroes for each number)
        value_int = math.pow(10,magnitud-1)
        magnitud_list.append(value_int)
        length = length + 1
        magnitud -= 1
    #Create a separated list with each of the numbers
    for i in wordkey:
        current_number = masterkey[i]
        single_numbers.append(current_number)
    #Create a new list with each number multiplied by its power
    for i in range(len(wordkey)):
        total_number = magnitud_list[i]*single_numbers[i]
        complete_number.append(total_number)
    #sum each number in the list to obtain the complete number as an int
    final_number = int(sum(complete_number))
    return final_number

def strToFloat( value ):
    #Declare Variables
    #Variables needed to separate the number in integers and fractions
    list_values = value
    position = 0
    final_count = 0
    list_intgers = list()
    list_fraction = list ()
    #Part1. Deconstruct the number into integers and fraction
    for i in range(len(list_values)):
        if list_values[i] != ".":
            position +=1
        else:
            final_count = position
    #obtain integers
    for i in range(final_count):
        list_intgers.append(list_values[i])

    # for i in range(final_count + 1,len(list_values)-2,1):
    #     list_fraction.append(list_values[i])

    #Part2.
    #Declare Variables to construct the integer
    length = 0
    magnitud_list_int = list()
    single_numbers_int = list()
    complete_number_int = list()
    wordkey_int = list_intgers
    magnitud = (len(wordkey_int))
    #Declare variables needed to construct the fraction
    behind_dot = 0
    magnitud_list_fract = list()
    single_numbers_fract = list()
    complete_number_fract = list()
    wordkey_fract = list_fraction
    magnitud_fract = 0

    #Part3. Construct the integer
    while length < len(wordkey_int):
        value_int = math.pow(10,magnitud-1)
        magnitud_list_int.append(value_int)
        length = length + 1
        magnitud -= 1
    for i in wordkey_int:
        current_number = masterkey[i]
        single_numbers_int.append(current_number)
    for i in range(len(wordkey_int)):
        total_number = magnitud_list_int[i]*single_numbers_int[i]
        complete_number_int.append(total_number)

    final_number_int = int(sum(complete_number_int))
    #Part4. Construct the fraction
    # while behind_dot < len(wordkey_fract):
    #     value_fract = math.pow(10,magnitud-1)
    #     magnitud_list_fract.append(value_fract)
    #     behind_dot += 1
    #     magnitud -= 1
    # for i in wordkey_fract:
    #     current_number = masterkey[i]
    #     single_numbers_fract.append(current_number)
    # for i in range(len(wordkey_fract)):
    #     total_number = magnitud_list_fract[i]*single_numbers_fract[i]
    #     complete_number_fract.append(total_number)
    # final_number_fract = float(sum(complete_number_fract))
    # #Part4. Construct, print and return the number as a float
    # final_value = final_number_int + final_number_fract
    return final_number_int
    print final_number_int


def BigList(somevalue):
    value = somevalue
    num = strToFloat( value )
    print num
    print type(num)
    return (num)
