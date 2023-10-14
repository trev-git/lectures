n_vals = [1, 3, 5, 7, 9, 11, 13, 15, 19, 21, 23, 25, 27, 29, 31, 33]
m = 34

for val in n_vals:
    for val2 in n_vals:
        res = (val * val2) % m;
        if res == 1:
            print(f'{val} = {val2}')
