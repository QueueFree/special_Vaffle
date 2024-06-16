n = 8
nu = ['6', '2', '4', '9', '3', '1', '8', '7']
counter = 0
cc = 0
for run in range(n-1):
    for i in range(n - 1):
        if nu[i] > nu[i + 1]:
            counter += 1
            nu[i], nu[i + 1] = nu[i + 1], nu[i]
    print(nu)
print(counter)
