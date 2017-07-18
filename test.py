'''
Case swaping
'''
input_string = "HELLo WORLd"
string = ''.join([i.lower() if i.isupper() else i.upper() for i in input_string ])

print string
