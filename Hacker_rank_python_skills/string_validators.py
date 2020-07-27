# qA2
def strValidators(validators, string):
        for validator in validators:
            if validator in dir(str):
                yield any(getattr(char, validator)() for char in string)
s = input()
v = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
for boolean in strValidators(v, s):
    print(boolean)