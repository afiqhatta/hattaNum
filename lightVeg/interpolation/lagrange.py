from lightVeg import datapoints

def lagrange_interpolate(x_points,y_points, value):
    delta_polys = []
    for item in x_points:
        delta_polys.append(delta_poly(x_points, value, item))
    return dot_product(delta_polys, y_points)

def dot_product(list1, list2):
    sum = 0
    for item in list1:
        sum += item*list2[list1.index(item)]
    return sum

def sum_elements(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def multiply_elements(list):
    product = 1
    for num in list:
        product = product*num
    return product

def delta_poly(list, value, item):
    temp = item
    new_list = list
    new_list.remove(item)
    z = []
    for num in new_list:
        z.append((value-num)/(temp-num))
    return multiply_elements(z)

print(lagrange_interpolate([1,2,3], [2,4,6], 3))