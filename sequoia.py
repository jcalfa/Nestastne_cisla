string  = input("Type your entry word: ")
result = len({char for char in string if char in 'aeiou'}) == 5
print(result)