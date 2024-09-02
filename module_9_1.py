def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results


def min_(int_list):
    result = int_list[0]
    for i in int_list:
        if i < result:
            result = i
    return result


def max_(int_list):
    result = int_list[0]
    for i in int_list:
        if i > result:
            result = i
    return result


def len_(int_list):
    return len(int_list)


def sum_(int_list):
    result = 0
    for i in int_list:
        result += i
    return result


def sorted_(int_list):
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
