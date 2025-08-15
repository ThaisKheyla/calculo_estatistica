peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura**2)
continuar = float(input("Deseja calcular o imc de outra pessoa? s/n"))
if (continuar == "s"):
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    
else:
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

  imc = peso / (altura * altura)
  print(f"Seu imc é de: {imc}")