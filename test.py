'''
Case swaping
'''
input_string = "HELLO WORLD"
string = ''.join([i.lower() if i.isupper() else i.upper() for i in input_string ])

print string
