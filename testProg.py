user_int = int(input('Enter integer (32 - 126):\n'))
# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_flt = float(input('Enter float: \n'))
user_chr = input('Enter character:\n')
user_str = str(input('Enter string:\n'))  

result = str(user_int) +' '+str(user_flt)+' '+str(user_chr)+' '+user_str
print(result)
words = result.split(' ')
print (len(words))
reverse_Sentence = ' '.join(reversed(words))
print(reverse_Sentence)

print(chr(user_int))
print('Test')