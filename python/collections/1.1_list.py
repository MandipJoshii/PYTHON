#so basically this is how to make a list in python
my_List = [1,2,3,4,"hello", 'hello']
flowers = list(("lilly", "tulips","daisy","orchids"))

flowers[1] = "cherry blossom"   

print(my_List)
print(flowers)

# ///////////////////////////////////////////////////

values = [1,2,3,4,5,6]

values[2:5] = list((200,300,400))

print(values)

print("<---------------ADD--------------->")

# ///////////////////////////////////////////////////

for_append = [1,2,3,4,5,6]

for_insert = [2,4,6,8,10]

for_extend = [1,3,5,7,9]

for_append.append(7)
for_insert.insert(2,12)
for_extend.extend([11,13,15])

print(for_append)
print(for_insert)
print(for_extend)

print("<---------------REMOVE--------------->")

#//////////////////////////////////////////////////////////

for_remove = [1,2,3,4,5,6,3]
for_pop = [2,4,6,8,10]
for_clear = [1,3,5,7,9]
for_del = [1,2,3,4,'a','b','c','d']

for_remove.remove(3)
pop1 = for_pop.pop() # pops the last
pop2 = for_pop.pop(3) # pops the third index value

del for_del[2]
print(for_del)
del for_del[1:6]
print(for_del)

for_clear.clear() # makes everything empty from the list,  like your life hehehe

print(for_remove)
print(pop1)
print(pop2)
print(for_clear)
