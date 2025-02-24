salario = float(input("Informe seu Salário: "))
porcen = float(input("Informe a porcentagem de seu imposto: "))
imposto = salario*(porcen/100)

liquid = salario - imposto

print(f"Seu salario bruto é de R${salario}\nSua porcentagem é de {porcen}%")
print(f"Seu salario liquido é de R$ {liquid}")