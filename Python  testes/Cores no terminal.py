from termcolor import colored
import colorama
colorama.init()

#this way uses termcolor, is too easy to use 
print(colored('this way wil work', 'blue'))

#This way is confusing to understand, but it works to
print('\033[0;31;43mText\033[m')

