def calcular_pegada_carbono():
    print("Para o primeiro acesso")
    senha_c = int(input("Digite uma senha: "))
    cdv_c = int(input("Digite um código de verificação: "))
    
    print("\n........SUA SENHA E CÓDIGO DE VERIFICAÇÃO FORAM SALVOS........\n")
    senha_d = int(input("Digite sua senha: "))
    cdv_d = int(input("Digite seu código de verificação: "))
    
    if cdv_d == cdv_c and senha_d == senha_c:
        print("\n......SUA SENHA E CÓDIGO DE VERIFICAÇÃO ESTÃO CORRETOS......\n")
        
        familia = int(input("Quantas pessoas moram com você? [Até 5 pessoas]: "))
        
        eletricidade = float(input("Quanto de energia você gasta por mês em kWh? "))
        eleT = eletricidade * 0.1295
        
        kmM = float(input("Quantos quilômetros de moto você dirige por mês? "))
        kmMt = kmM * 0.10106
        
        gas = float(input("Quanto de gás natural você usa em quilogramas de CO₂ por mês? [cada m³ de GLP pesa 2,3 kg]: "))
        gT = gas * 0.18293
        
        alimento = float(input("Quantos reais você gasta com produtos alimentares e bebidas por mês? "))
        aliT = alimento * 0.10174829
        
        km = float(input("Quantos quilômetros de carro você dirige por mês? "))
        kmT = km * 0.17246
        
        onibus = float(input("Quantos quilômetros de transporte público você utiliza por mês? "))
        onibusT = onibus * 0.0928533
        
        totalf = gT + eleT + kmT + onibusT + kmMt + aliT
        if familia > 0:
            totali = totalf / familia
        else:
            totali = totalf
        
        print("\nResultados:")
        print(f"A pegada de carbono total da sua família é: {totalf:.2f} kg de CO₂ por mês.")
        if familia > 1:
            print(f"Cada membro da família produz, em média, {totali:.2f} kg de CO₂ por mês.")
        else:
            print(f"Sua pegada de carbono individual é: {totali:.2f} kg de CO₂ por mês.")
    else:
        print("\n......SUA SENHA OU CÓDIGO DE VERIFICAÇÃO ESTÁ INCORRETO. TENTE NOVAMENTE......")

# Execução do programa
if __name__ == "__main__":
    calcular_pegada_carbono()