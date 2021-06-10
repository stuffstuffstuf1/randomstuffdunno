#import random (randomiser) and string (randomised)
import random
import string

#welcome message
print('Hello, Welcome to Password generator!')

#ask for the length
length = int(input('\nEnter the length of the password (max 4500): '))                      

#define the different parts of your password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
stuff = string.hexdigits
stuff_two = string.octdigits

#create all
all = lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols +lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + lower + upper + num + symbols + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two + stuff_two

#randomise
temp = random.sample(all,length)

#join password
password = "".join(temp)

#print password
print(password)
