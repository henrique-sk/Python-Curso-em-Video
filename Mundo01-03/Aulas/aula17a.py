num = [2, 5, 9, 1]
print(num)
num[2] = 3 # muda a pos 2 para 3
print('\n', num)
num.append(7) # add nova pos com valor 7
print('\n', num)
num.sort(reverse=True)
print('\n', num)
print(len(num))
num.insert(2, 0) # add nova pos 2 com 0
print('\n', num)
num.pop() # deleta ultima pos
print('\n', num)
num.pop(2) # del pos 2
print('\n', num)
num.insert(2, 2) # add nova pos 2 com 2
print('\n', num)
num.remove(2) # remove 1° valor 2
print('\n', num)
