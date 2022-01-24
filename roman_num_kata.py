# Part 1

numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L':50, 'XC': 90, 'C': 100, 'CD': 400, 'D':500, 'CM': 900, 'M':1000}


# Test to print out the dictionary
# for k,v in numerals.items():
#     print(k,v)
#     print()


def convert_to_roman(input_number):
    range_flag = None
    for symbol, integer in numerals.items():
        if integer == input_number:
            return symbol
        
        if input_number > integer:
            range_flag = symbol

    remaining = input_number - numerals[range_flag]
    return range_flag + convert_to_roman(remaining)

# Test out different numbers in the parentheses
print(convert_to_roman(4))


# Part 2

symbol_number = input("Write a roman numer to convert to a digit: ")
x = input()

digits = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L':50, 'XC': 90, 'C': 100, 'CD': 400, 'D':500, 'CM': 900, 'M':1000}
answer = 0

for i in range(len(symbol_number)):
    if i+1 != len(symbol_number) and digits[symbol_number[i]] < digits[symbol_number[i+1]]:
        answer = answer - digits[symbol_number[i]]
    else:
        answer = answer + digits[symbol_number[i]]

print(x)
print(f'This is: {answer}')