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