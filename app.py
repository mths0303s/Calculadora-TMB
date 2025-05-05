peso = float(input("Digite seu peso (em KG): "))
altura = int(input("Digite sua altura (em centímetros): "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo(F/M): ").strip() .lower()
nivel_atividade = input("Digite seu nível de atividade física durante o dia (Leve, Moderada ou Intensa): ").strip() .lower()

# Verificação da atividade
if nivel_atividade == "leve":
    fator_atividade = 1.55

elif nivel_atividade == "moderada":
        fator_atividade = 1.84
    
elif nivel_atividade == "intensa":
        fator_atividade = 2.2
    
else:
      fator_atividade = 1.0


# Verificação do sexo e exibição TMB
if sexo == "m":
    tmb = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)

elif sexo == "f":
    tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)  

else:
      tmb = 0

gasto_total = tmb * fator_atividade

print("Sua taxa metabólica basal é: %.2f " % tmb, "e seu gasto calórico diário total é de: %.2f" % gasto_total)

prosseguir = input("\n\nDeseja continuar com o calculo da divisão por refeição? (S/N): ").strip().lower()

if prosseguir == "s":
    objetivo = input("\n\nVocê deseja emagrecer, manter ou ganhar peso? (emagrecer/manter/ganhar): ").strip().lower()
    if objetivo == "emagrecer":
        print("\n\nPara emagrecer, você deve diminuir 1000 calorias do seu gasto total diário.")
        gasto_total -= 1000
    elif objetivo == "ganhar":
        print("\n\nPara ganhar, você deve aumentar 800 calorias do seu gasto total diário.")
        gasto_total += 800
    else:
         print("\n\nPara manter, você deve ingerir as mesmas calorias do seu gasto total diário.")
         gasto_total = gasto_total

    print("\n\nVamos prosseguir com o cálculo da divisão calórica por refeição...\n")
    print("As 8h00, No café você pode ingerir: %.2f calorias" % (gasto_total * 0.25))
    print("As 11h00, No lanche da manhã você pode ingerir: %.2f calorias" % (gasto_total * 0.10))
    print("As 13h00, No almoço você pode ingerir: %.2f calorias" % (gasto_total * 0.30))
    print("As 16h00, No lanche da tarde você pode ingerir: %.2f calorias" % (gasto_total * 0.10))
    print("As 19h00, No jantar você pode ingerir: %.2f calorias" % (gasto_total * 0.20))
    print("As 21h00, No lanche da noite você pode ingerir: %.2f calorias" % (gasto_total * 0.05))

input("\n\nPressione ENTER para sair...")