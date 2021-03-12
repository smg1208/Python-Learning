# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks 
For 
Life'''
print("\nCreating a multiline String: ")
print(String1)

# Python Program to Access
# characters of String

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

Tuple = list(String1)
Len = [x for x in range(0, 13)]
Lenrevs = [x for x in range(-13, 0)]
S1 = S2 = S3 = ''
for x in range(0, 13):
    S1 += (5 - len(Tuple[x]))*' ' + Tuple[x]    
    S2 += (5 - len(str(Len[x])))*' ' + str(Len[x])
    S3 += (5 - len(str(Lenrevs[x])))*' ' + str(Lenrevs[x])
print(S1)
print(S2)
print(S3)


# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 


# Python Program for Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 
# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

# To demonstrate aligning of spaces 
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009) 
print(String1) 

# Python Program for 
# Old Style Formatting 
# of Integers 

Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %.4f' %Integer1) 


string = 'ablakjdflds'
print(max(string))
string = '123456'
print(string.isdecimal())
string = '123456ac'
print(string.isalnum())