print ("Hello World")

# Declaring Variables
name = "Gio"
print (name)
print ("Hello " + name)
print (f'Hello {name}')

#Working with List
li = [12, 5, 65, 15]
li.append(11)
print(li) 

#Loop
for number in li:
    print(number)

for (i, e) in enumerate(li):
    print(f'Element at {i} is {e}')

squares = [num*num for num in li]

#for sqr in li:
#    squares.append(sqr*sqr)

print(squares)

evens = [num for num in li if num % 2 == 0]

#for num in li:
#    if num % 2 == 0:
#        evens.append(num)

print(evens)
