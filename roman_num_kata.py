# Part 1

numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L':50, 'XC': 90, 'C': 100, 'CD': 400, 'D':500, 'CM': 900, 'M':1000}

# Test to print out the dictionary
# for k,v in numerals.items():
#     print(k,v)
#     print()

input_number = int(input("Write a number to convert to roman numeral: "))

def convert_to_roman(input_number):
    range_flag = None
    for symbol, integer in numerals.items():
        if integer == input_number:
            return symbol
        
        if input_number > integer:
            range_flag = symbol

    remaining = input_number - numerals[range_flag]
    return range_flag + convert_to_roman(remaining)


answer1 = convert_to_roman(input_number)
print(f'The converted roman numeral is: {answer1}')

# Part 2

symbol_number = input("Write a roman numeral to convert to a number: ")

answer = 0
for i in range(len(symbol_number)):
    if i+1 != len(symbol_number) and numerals[symbol_number[i]] < numerals[symbol_number[i+1]]:
        answer = answer - numerals[symbol_number[i]]
    else:
        answer = answer + numerals[symbol_number[i]]


print(f'The converted roman numeral is: {answer}')