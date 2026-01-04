def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma

s = soma_todos(1,2,3,4,5)
print(s)

s2 = soma_todos(1,2,3,4,5,6,7,8,9,10)
print(s2)