lst = [1,2,3]

lst2 = [4,5]

lst.append(6)
lst.extend(lst2)
lst.insert(1,[5,6])
print(lst)
# ========================================================================

lst.append(6)
print(lst)

lst.remove(6)
print(lst)
lst.clear()

lst = ['a' , 'b' , 'ab']
lst.sort(reverse=False)
print(lst)

print(sorted(lst , reverse=False))
# ========================================================================
lst.clear()

dic = {'a' : 1}
lst = [dic]

print(id(dic) , id(lst[0]))

print({1,2,3} & {2})
print({1,2,3} | {2})
print({1,2,3} - {2})