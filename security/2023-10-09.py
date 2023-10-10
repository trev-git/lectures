n_vals = [1, 2, 3,]

def euler_function(m: int) -> list[int]:
    res = []
    for i in range(1, m+1):
        if m % i != 0 or i == 1:
            res.append(i)
    return res

m = 24
print(euler_function(m))

for val in n_vals:
    for val2 in n_vals:
        res = (val * val2) % m;
        if res == 1:
            print(f'| {val} | {val2} |')
