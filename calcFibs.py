def calcFibs(n):
    output = [1,1]
    for i in range(1,n):
        output.append(output[i]+output[i-1])
    return output

print('The first 10 fibonacci numbers are: 'calFibs(10))
