def string_match(a, b):
    num_times = 0
    for i in range((min(len(a), len(b)))-1):
        # print(range(min(len(a), len(b))))
        a_ins = a[i:(i + 2)]
        b_ins = b[i:(i + 2)]
        if (a_ins == b_ins):
            print(a_ins, b_ins)
            num_times += 1
    return num_times

print(string_match('xxcaazz', 'xxbaazsss'))
# string_match('abc', 'abc')
# string_match('abc', 'axc')