def merge(list1,list2):
    merged_list=tuple(zip(list1, list2))
    return merged_list
list1=[1,2,3,4]
list2=['ab','cd','ef','gh']
print(merge(list1,list2))
