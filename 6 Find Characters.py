# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

newArr = []
for item in word_list:
    if item.find(char) != -1:
        newArr.append(item)
print newArr