print("CALCULADORA DE IMC")

peso = float(input("Digite seu peso em kg: "))

altura = float(input("Digite sua altura em metros: "))

def calcular_imc(peso, altura):
  
  imc = peso / (altura * altura)


  if (imc < 18.5):
    categoria = "Abaixo do peso"

  elif (imc < 25):
    categoria = "Normal"
    
  elif (imc < 30):
    categoria = "Sobrepeso"
  elif (imc < 35):

    categoria = "Obesidade I"
  elif (imc < 40):
    categoria = "Obesidade II"
  else:

    categoria = "Obesidade morbida"

  return (f"O seu IMC é: {imc}")

resultado = calcular_imc(peso, altura)
print(resultado)

calcularNovo = input("Deseja calcular o IMC de outra pessoa? (s/n): ")

while calcularNovo == "s":
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    resultado = calcular_imc(peso, altura)

    print(resultado)
    calcularNovo = input("Deseja calcular o IMC de outra pessoa? (s/n): ")
else:
  print("Encerrando a calculadorita... ")
