def strings_eq2_first_last(list):
    count = 0
    for i in list:
        if (len(i) >= 2) and (i[0] == i[-1]):
            #print(i)
            count +=1
    return count

print(strings_eq2_first_last(['aba', 'xyz', 'aa', 'x', 'bbb']))

print(strings_eq2_first_last(['x', 'xy', 'xyx', 'xx', '']))