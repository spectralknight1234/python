import tkinter as tk
from tkinter import messagebox
import sqlite3

def configurar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            acessos INTEGER DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

def cadastrar_usuario():
    def salvar_cadastro():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario and senha:
            try:
                conexao = sqlite3.connect("usuarios.db")
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                janela_cadastro.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Usuário já existe. Escolha outro nome de usuário.")
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
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario and senha:
            conexao = sqlite3.connect("usuarios.db")
            cursor = conexao.cursor()
            cursor.execute("SELECT id, acessos FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            resultado = cursor.fetchone()
            if resultado:
                user_id, acessos = resultado
                if acessos > 0:
                    messagebox.showinfo("Bem-vindo de volta", f"Bem-vindo de volta, {usuario}!")
                else:
                    messagebox.showinfo("Sucesso", f"Login realizado com sucesso, {usuario}!")
                cursor.execute("UPDATE usuarios SET acessos = acessos + 1 WHERE id = ?", (user_id,))
                conexao.commit()
                conexao.close()
                janela_login.destroy()
                calcular_pegada_carbono()
            else:
                messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
                conexao.close()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    
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

def mostrar_ideias():
    janela_ideias = tk.Toplevel()
    janela_ideias.title("Ideias para Reduzir Pegada de Carbono")
    janela_ideias.geometry("400x400")

    ideias = [
        "- Utilize lâmpadas de LED em casa para economizar energia.",
        "- Ande de bicicleta ou caminhe para trajetos curtos.",
        "- Consuma alimentos locais e de produtores orgânicos.",
        "- Reduza o uso de embalagens plásticas descartáveis.",
        "- Evite o desperdício de água e energia.",
        "- Planeje viagens para reduzir o uso de transporte aéreo.",
        "- Adote práticas de reciclagem e compostagem.",
        "- Participe de programas de reflorestamento.",
        "- Incentive o uso de energia renovável, como solar e eólica."
    ]

    beneficios = (
        "Benefícios para a sociedade:\n"
        "- Redução de emissões de gases de efeito estufa.\n"
        "- Melhoria da qualidade do ar e saúde pública.\n"
        "- Preservação de recursos naturais para as futuras gerações.\n"
        "- Fomento a economias locais e práticas sustentáveis."
    )

    tk.Label(janela_ideias, text="Ideias para Reduzir a Pegada de Carbono", font=("Arial", 14, "bold")).pack(pady=10)
    for ideia in ideias:
        tk.Label(janela_ideias, text=ideia, wraplength=380, justify="left").pack(anchor="w", padx=10, pady=2)
    tk.Label(janela_ideias, text="\n" + beneficios, wraplength=380, justify="left", fg="green").pack(pady=10)

def iniciar_aplicacao():
    configurar_banco()
    janela = tk.Tk()
    janela.title("Calculadora de Pegada de Carbono")
    janela.geometry("300x300")

    tk.Button(janela, text="Cadastrar Usuário", command=cadastrar_usuario).pack(pady=10)
    tk.Button(janela, text="Login", command=autenticar_usuario).pack(pady=10)
    tk.Button(janela, text="Ideias para Reduzir Pegada de Carbono", command=mostrar_ideias).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()

