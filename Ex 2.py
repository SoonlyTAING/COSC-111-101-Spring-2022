print ("ex 2")
def index_power(array,index):
    try:
        array[index]    
    except IndexError:
        x=-1
        return x
    x=array[index]**index
    return x
print(index_power([1, 2, 3, 4], 3))

def index_power(array, index):
    if index < len(array):
        res = array[index] ** index
    else:
        res = -1
    return res


print(index_power([1, 3, 10, 100], 3))
