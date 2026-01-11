"""
tipo string

em python, um dado é considerado do tipo string sempre que
- estiver entre aspas simples
- estiver entre aspas duplas
- estiver entre aspas simples triplas
"""
nome1 = 'geek university'
print(nome1)
print(type(nome1))

nome2 = "geek university"
print(nome2)
print(type(nome2))

nome3 = 'geek \nuniversity'
print(nome3)
print(type(nome3))

nome4 = """geek 
university"""
print(nome4)
print(type(nome4))

nome5 = "geek university"
print(nome5.upper())
print(nome5.lower())