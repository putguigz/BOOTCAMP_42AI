from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print("******** TEST 1 ***********")
to_print = npc.from_list([[1,2,3],[6,3,4]]) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 2 ***********")
to_print = npc.from_list([[1,2,3],[6,4]])
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 3 ***********")
to_print = npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 4 ***********")
to_print = npc.from_list(((1,2),(3,4))) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 5 ***********")
to_print = npc.from_tuple(("a","b","c")) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 6 ***********")
to_print = npc.from_tuple([[1,2,3],[6,3,4]]) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 7 ***********")
to_print = npc.from_iterable(iter(range(5))) 
#print(type(to_print))
print(to_print)
#print(to_print.dtype)


print("******** TEST 8 ***********")
shape=(3,5)
to_print = npc.from_shape(shape)
#print(type(to_print))
print(to_print)
#print(to_print.dtype)


print("******** TEST 9 ***********")
to_print = npc.random(shape)
#print(type(to_print))
print(to_print)
#print(to_print.dtype)

print("******** TEST 10 ***********")
to_print = npc.identity(4)
print(type(to_print))
print(to_print)
print(to_print.dtype)