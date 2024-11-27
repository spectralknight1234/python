import tkinter as tk
from tkinter import messagebox

# Variáveis globais para armazenar as credenciais do usuário
usuario_cadastrado = None
senha_cadastrada = None

def cadastrar_usuario():
    def salvar_cadastro():
        global usuario_cadastrado, senha_cadastrada
        usuario_cadastrado = entrada_usuario.get()
        senha_cadastrada = entrada_senha.get()
        
        if usuario_cadastrado and senha_cadastrada:
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            janela_cadastro.destroy()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("300x200")

    tk.Label(janela_cadastro, text="Nome de Usuário:").pack(pady=5)
    entrada_usuario = tk.Entry(janela_cadastro)
    entrada_usuario.pack(pady=5)

    tk.Label(janela_cadastro, text="Senha:").pack(pady=5)
    entrada_senha = tk.Entry(janela_cadastro, show="*")
    entrada_senha.pack(pady=5)

    tk.Button(janela_cadastro, text="Cadastrar", command=salvar_cadastro).pack(pady=10)

def autenticar_usuario():
    def validar_login():
        global usuario_cadastrado, senha_cadastrada
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        
        if usuario == usuario_cadastrado and senha == senha_cadastrada:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela_login.destroy()
            calcular_pegada_carbono()
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
    
    janela_login = tk.Toplevel()
    janela_login.title("Login")
    janela_login.geometry("300x200")

    tk.Label(janela_login, text="Nome de Usuário:").pack(pady=5)
    entrada_usuario = tk.Entry(janela_login)
    entrada_usuario.pack(pady=5)

    tk.Label(janela_login, text="Senha:").pack(pady=5)
    entrada_senha = tk.Entry(janela_login, show="*")
    entrada_senha.pack(pady=5)

    tk.Button(janela_login, text="Entrar", command=validar_login).pack(pady=10)

def calcular_emissao(eletricidade, km_moto, gas, alimento, km_carro, onibus, aviao, barco):
    # Fatores de emissão em kg CO₂ por unidade
    eleT = eletricidade * 0.1295
    kmMt = km_moto * 0.10106
    gT = gas * 0.18293
    aliT = alimento * 0.10174829
    kmT = km_carro * 0.17246
    onibusT = onibus * 0.0928533
    aviaoT = aviao * 0.254
    barcoT = barco * 0.059
    
    totalf = eleT + kmMt + gT + aliT + kmT + onibusT + aviaoT + barcoT
    return totalf

def calcular_pegada_carbono():
    def calcular():
        try:
            familia = int(entrada_familia.get())
            eletricidade = float(entrada_eletricidade.get())
            km_moto = float(entrada_km_moto.get())
            gas = float(entrada_gas.get())
            alimento = float(entrada_alimento.get())
            km_carro = float(entrada_km_carro.get())
            onibus = float(entrada_onibus.get())
            aviao = float(entrada_aviao.get())
            barco = float(entrada_barco.get())
            
            totalf = calcular_emissao(eletricidade, km_moto, gas, alimento, km_carro, onibus, aviao, barco)
            totali = totalf / familia if familia > 0 else totalf
            
            messagebox.showinfo(
                "Resultados",
                f"Pegada de carbono total: {totalf:.2f} kg de CO₂/mês\n"
                f"Pegada individual: {totali:.2f} kg de CO₂/mês"
            )
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    
    janela_calculo = tk.Toplevel()
    janela_calculo.title("Cálculo de Pegada de Carbono")
    janela_calculo.geometry("400x600")

    campos = [
        ("Quantas pessoas moram com você?", "familia"),
        ("Energia gasta por mês (kWh):", "eletricidade"),
        ("KM dirigidos de moto por mês:", "km_moto"),
        ("Gás natural usado (kg de CO₂):", "gas"),
        ("Gasto com alimentos (R$):", "alimento"),
        ("KM dirigidos de carro por mês:", "km_carro"),
        ("KM de transporte público por mês:", "onibus"),
        ("KM viajados de avião por mês:", "aviao"),
        ("KM viajados de barco por mês:", "barco")
    ]

    entradas = {}

    for texto, chave in campos:
        tk.Label(janela_calculo, text=texto).pack(pady=5)
        entrada = tk.Entry(janela_calculo)
        entrada.pack(pady=5)
        entradas[chave] = entrada

    entrada_familia = entradas["familia"]
    entrada_eletricidade = entradas["eletricidade"]
    entrada_km_moto = entradas["km_moto"]
    entrada_gas = entradas["gas"]
    entrada_alimento = entradas["alimento"]
    entrada_km_carro = entradas["km_carro"]
    entrada_onibus = entradas["onibus"]
    entrada_aviao = entradas["aviao"]
    entrada_barco = entradas["barco"]

    tk.Button(janela_calculo, text="Calcular", command=calcular).pack(pady=20)

def iniciar_aplicacao():
    janela = tk.Tk()
    janela.title("Calculadora de Pegada de Carbono")
    janela.geometry("300x200")

    tk.Button(janela, text="Cadastrar Usuário", command=cadastrar_usuario).pack(pady=10)
    tk.Button(janela, text="Login", command=autenticar_usuario).pack(pady=10)

    janela.mainloop()

# Início da aplicação
if __name__ == "__main__":
    iniciar_aplicacao()

