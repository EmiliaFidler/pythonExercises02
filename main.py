# homwework -- exercices 02 --

# exercise 1:

def count_integer(numbers, integer):
    if integer not in numbers:
        return 42

    count = 0  # counter variable
    for number in numbers:
        if number == integer:
            count += 1

    return count


numbers = [1, 1, 2, 3, 5, 5, 5, 6, 9]
print(count_integer(numbers, 1))


# exercise 2:

def list_func(numbers, integer):
    if integer not in numbers:
        return []

    for idx, number in enumerate(numbers):
        if number == integer:
            numbers[idx] = 6

    x = list(reversed(numbers))
    print(x)

    return numbers


print(list_func(numbers, 3))


# exercise 3:

def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


def compare_lists_2(list1, list2):
    result = []
    for x in list1:
        if x in list2:
            result += [x]

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]
print(compare_lists(list1, list2))

print(compare_lists_2(list1, list2))


# exercise 4:

def remove_duplicates(lst):
    print(set(lst))


lst = ['cat', 'dog', 'cat', 'bird']
print(remove_duplicates(lst))


# exercise 5:

def dict_func(dictionary):
    if 'Type' not in dictionary:
        dictionary["Type"] = 'unknown type'
    if 'Brand' not in dictionary:
        dictionary["Brand"] = 'unknown brand'
    if 'Price' not in dictionary:
        dictionary["Price"] = 'unknown price'
    if 'OS' not in dictionary:
        dictionary["OS"] = 'Linux'

    print(f'You have a {dictionary["Type"]} from {dictionary["Brand"]} that costs {dictionary["Price"]}.')
    print(dictionary)

    return dictionary


dict_func({"Type": "Laptop", "Brand": "HP", "Price": "1750€"})
