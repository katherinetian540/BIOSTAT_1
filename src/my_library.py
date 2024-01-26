def count_has_2(lst) -> list:
    count = 0
    for i in lst:
        if '2' in str(i):
            count +=1
    return count