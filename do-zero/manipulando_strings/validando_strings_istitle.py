# istitle() =  do Python verifica se uma string está no formato "título". Ele retorna True se todas as palavras começarem
# com letra maiúscula e as demais letras forem minúsculas, e False caso contrário

texto = "Curso De Python"
print(texto.istitle())

texto2 = "Curso de python"
print(texto2.istitle())

texto3 = "CURSO De Python"
print(texto3.istitle())