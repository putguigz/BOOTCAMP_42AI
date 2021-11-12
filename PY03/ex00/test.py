from NumPyCreator import NumPyCreator

npc = NumPyCreator()

npc.from_list([[1,2,3],[6,3,4]])

npc.from_list([[1,2,3],[6,4]]) #==> NONE

npc.from_list([[1,2,3],["a","b","c"],[6,4,7]])

npc.from_list((1,2),(3,4))  #==> NONE

npc.from_tuple(("a","b","c"))

npc.from_tuple([[1,2,3],[6,3,4]])  #==> NONE

npc.from_iterable(range(5))

shape=(3,5)

npc.from_shape(shape)

npc.random(shape)

npc.identity(4)