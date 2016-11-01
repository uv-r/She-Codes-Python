# function that gets strings and
# make a dictionary that connect from alpa-biet to
# the num of times in appearance

def char_freq(str):
    freq = {}
    for val in str:
        times = str.count(val)
        freq[val] = times
    return freq

print(char_freq("abzz"))