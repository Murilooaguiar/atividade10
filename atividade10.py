# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

limite_de_velocidade = 60
multa= 7

velocidade = int(input("digite a velocidade em km/h :"))

velocidade_total = velocidade - limite_de_velocidade 
valor_multa = velocidade_total+multa 

if velocidade > limite_de_velocidade:
   print("a multa aplicada no veiculo é: R$"+ valor_multa)
else: 
    print("o veiculo esta dentro do limite de velocidade")

    