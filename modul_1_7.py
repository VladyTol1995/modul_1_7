immutable_var = 1,2, "a", "B", True
print( immutable_var)
print (immutable_var [0])
#immutable_var [0] = 10000
#print (immutable_var)
# Элемент кортежа нельзя изменить, так как кортеж является неизменяемым, с целью сохранения данных заключенных в него, а также для уменьшения занимаемого количества памяти
mutable_list = [1, 2, "A", "B", True]
print(type(mutable_list))
mutable_list[0] = 47
mutable_list [1] = 77
mutable_list [2] = "CD"
mutable_list [3] = "EF"
mutable_list [4] = False
print(mutable_list)