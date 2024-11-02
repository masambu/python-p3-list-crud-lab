def create_an_empty_list():
    empty_list = []
    return empty_list

print(create_an_empty_list())




def create_a_list():
    my_list = [1,2,3,4]
    return my_list

print(create_a_list())




def add_element_to_end_of_list(l ,element):
    l.append(element)
    return l

print(add_element_to_end_of_list([1,2,3,4],5))




def add_element_to_start_of_list(x, element):
    x.insert(0 , element)
    return x

print(add_element_to_start_of_list([2,3,4,5],1))




def remove_element_from_end_of_list(l):
    l.pop()
    return l

print(remove_element_from_end_of_list([1,2,3,4]))




def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

print(remove_element_from_start_of_list([1,2,3,4]))




def retrieve_first_element_from_list(l):
    return l[0]

print(retrieve_first_element_from_list([1,2,3,4]))




def retrieve_element_from_index(l, x):
    return l[x]

print(retrieve_element_from_index([1,2,3,4],1))




def retrieve_last_element_from_list(l):
    return l[-1]

print(retrieve_last_element_from_list([5,6,7,8]))
