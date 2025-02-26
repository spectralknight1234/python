<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Pegada de Carbono</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            background: linear-gradient(to bottom, #a2d9ff, #ffffff);
            font-family: 'Arial', sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 2.5rem;
            font-weight: bold;
            color: #0056b3;
            text-shadow: 1px 1px 2px #ddd;
        }
        .container {
            max-width: 700px;
            margin: 50px auto;
            text-align: center;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .btn {
            width: 80%;
            font-size: 1.1rem;
            padding: 10px 0;
            border-radius: 25px;
            font-weight: bold;
        }
        .btn-primary {
            background-color: #007bff;
            border: none;
        }
        .btn-warning {
            background-color: #ff9800;
            border: none;
        }
        .modal-title {
            font-size: 1.8rem;
            color: #0056b3;
        }
        .modal-content {
            border-radius: 15px;
        }
        .dicas {
            margin-top: 20px;
        }
        .dica {
            padding: 10px;
            margin: 5px;
            border-radius: 10px;
            font-weight: bold;
        }
        .dica:nth-child(odd) {
            background-color: #ffcc80;
        }
        .dica:nth-child(even) {
            background-color: #81c784;
        }
        .grafico-container {
            margin-top: 30px;
        }
        .header-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .resultado-final {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.9);
            justify-content: center;
            align-items: center;
            flex-direction: column;
            z-index: 1000;
        }
        .resultado-final h2 {
            font-size: 2rem;
            margin-bottom: 20px;
        }
        .resultado-final p {
            font-size: 1.2rem;
            margin-bottom: 20px;
        }
        .resultado-final .btn {
            margin-top: 20px;
        }
        .loading-screen {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.9);
            justify-content: center;
            align-items: center;
            flex-direction: column;
            z-index: 1000;
        }
        .spinner {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #007bff;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <!-- Tela de Carregamento -->
    <div class="loading-screen" id="loadingScreen">
        <div class="spinner"></div>
        <p style="margin-top: 20px; font-size: 1.2rem;">Carregando resultados...</p>
    </div>

    <!-- Tela de Resultado Final -->
    <div class="resultado-final" id="resultadoFinal">
        <h2 id="tituloResultado">Seu Resultado</h2>
        <p id="mensagemResultado"></p>
        <button class="btn btn-primary" onclick="mostrarGraficos()">Clique aqui para se aprofundar mais</button>
    </div>

    <div class="container">
        <img src="https://images.unsplash.com/photo-1588702547919-260cf4931d91?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" 
             alt="Pegada de Carbono" 
             class="header-image">
        <h1>Calculadora de Pegada de Carbono</h1>
        <div id="loginSection">
            <h3>Faça Login ou Cadastre-se</h3>
            <input type="text" id="username" class="form-control mb-3" placeholder="Nome de Usuário">
            <input type="password" id="password" class="form-control mb-3" placeholder="Senha">
            <button class="btn btn-primary mb-3" onclick="login()">Login</button>
            <button class="btn btn-warning" onclick="register()">Cadastrar</button>
        </div>
        <div id="mainContent" style="display: none;">
            <div class="text-start mt-4">
                <h3>O que é a Pegada de Carbono?</h3>
                <p>A pegada de carbono representa a quantidade total de gases do efeito estufa (principalmente CO₂) emitidos direta ou indiretamente por nossas atividades diárias, como o consumo de energia, transporte e hábitos de consumo.</p>
            </div>
            <div class="d-flex flex-column align-items-center mt-4">
                <button class="btn btn-warning mb-3" onclick="abrirCalculadora()">Calcular Pegada de Carbono</button>
            </div>
        </div>
    </div>

    <!-- Modal de Cálculo -->
    <div class="modal" id="modalCalculo" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Calcular Pegada de Carbono</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <input type="number" id="luz" class="form-control mb-3" placeholder="Consumo de eletricidade (kWh)">
                    <input type="number" id="carro" class="form-control mb-3" placeholder="Km rodados de carro/mês">
                    <input type="number" id="aviao" class="form-control mb-3" placeholder="Km voados de avião/mês">
                    <input type="number" id="barco" class="form-control mb-3" placeholder="Km percorridos de barco/mês">
                </div>
                <div class="modal-footer">
                    <button class="btn btn-primary" onclick="iniciarCalculo()">Calcular</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Gráficos -->
    <div class="container grafico-container" id="graficoContainer" style="display: none;">
        <h3>Impacto da Sua Pegada de Carbono</h3>
        <canvas id="graficoPegada"></canvas>
    </div>
    <div class="container grafico-container" id="impactoAmbiental" style="display: none;">
        <h3>Impacto no Meio Ambiente</h3>
        <canvas id="graficoImpacto"></canvas>
    </div>

    <!-- Resultado Descritivo -->
    <div class="container resultado-descricao" id="resultadoDescricao" style="display: none;">
        <h3>Interpretação do Resultado</h3>
        <p id="descricaoResultado"></p>
    </div>

    <!-- Dicas -->
    <div class="container dicas" id="dicasContainer" style="display: none;">
        <h3>Dicas para Reduzir sua Pegada de Carbono</h3>
        <div id="dicas"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        let users = JSON.parse(localStorage.getItem("users")) || [];

        function register() {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            if (!username || !password) {
                alert("Por favor, preencha todos os campos.");
                return;
            }
            if (users.find(user => user.username === username)) {
                alert("Usuário já cadastrado.");
                return;
            }
            users.push({ username, password });
            localStorage.setItem("users", JSON.stringify(users));
            alert("Cadastro realizado com sucesso!");
        }

        function login() {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            const user = users.find(user => user.username === username && user.password === password);
            if (user) {
                document.getElementById("loginSection").style.display = "none";
                document.getElementById("mainContent").style.display = "block";
            } else {
                alert("Usuário ou senha incorretos.");
            }
        }

        function abrirCalculadora() {
            new bootstrap.Modal(document.getElementById('modalCalculo')).show();
        }

        function iniciarCalculo() {
            // Exibir tela de carregamento
            document.getElementById("loadingScreen").style.display = "flex";

            // Simular um pequeno atraso para a animação de carregamento
            setTimeout(() => {
                calcularPegada();
                document.getElementById("loadingScreen").style.display = "none";
            }, 2000); // 2 segundos de carregamento
        }

        function calcularPegada() {
            let luz = parseFloat(document.getElementById("luz").value) || 0;
            let carro = parseFloat(document.getElementById("carro").value) || 0;
            let aviao = parseFloat(document.getElementById("aviao").value) || 0;
            let barco = parseFloat(document.getElementById("barco").value) || 0;
            let pegada = (luz * 0.5) + (carro * 0.21) + (aviao * 0.2) + (barco * 0.12);

            // Comparação com média global fictícia
            let mediaGlobal = 120; // Média fictícia baseada em dados reais
            let comparacao = pegada < mediaGlobal ? "abaixo" : "acima";

            // Mensagem de resultado
            let mensagem = `Sua pegada de carbono é de ${pegada.toFixed(2)} kg de CO₂/mês. Isso está ${comparacao} da média global.`;

            // Definir cor do título com base no resultado
            let corTitulo = "";
            if (pegada < 50) {
                corTitulo = "#28a745"; // Verde
            } else if (pegada >= 50 && pegada < 150) {
                corTitulo = "#ffc107"; // Amarelo
            } else {
                corTitulo = "#dc3545"; // Vermelho
            }

            // Exibir tela de resultado final
            document.getElementById("tituloResultado").style.color = corTitulo;
            document.getElementById("mensagemResultado").innerText = mensagem;
            document.getElementById("resultadoFinal").style.display = "flex";
        }

        function mostrarGraficos() {
            document.getElementById("resultadoFinal").style.display = "none";
            document.getElementById("graficoContainer").style.display = "block";
            document.getElementById("impactoAmbiental").style.display = "block";
            document.getElementById("dicasContainer").style.display = "block";
        }

        function mostrarDicas() {
            let dicas = [
                "Use lâmpadas de LED para economizar energia.",
                "Reduza o consumo de carne, especialmente bovina.",
                "Opte por transportes públicos, bicicleta ou caminhar mais.",
                "Evite o desperdício de água e energia.",
                "Utilize sacolas reutilizáveis ao fazer compras.",
                "Plante árvores para compensar suas emissões.",
                "Reduza o uso de plásticos descartáveis.",
                "Recicle seus resíduos corretamente.",
                "Escolha produtos sustentáveis e de empresas responsáveis.",
                "Apoie e incentive o uso de energia renovável."
            ];
            let dicasContainer = document.getElementById("dicas");
            dicasContainer.innerHTML = "";
            dicas.forEach(dica => {
                let div = document.createElement("div");
                div.classList.add("dica");
                div.innerText = dica;
                dicasContainer.appendChild(div);
            });
            document.getElementById("dicasContainer").style.display = "block";
        }

        function gerarGrafico(luz, carro, aviao, barco) {
            let ctx = document.getElementById("graficoPegada").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: ["Eletricidade", "Carro", "Avião", "Barco"],
                    datasets: [{
                        data: [luz, carro, aviao, barco],
                        backgroundColor: ["#ffcc80", "#81c784", "#64b5f6", "#ff8a65"]
                    }]
                }
            });
        }

        function gerarGraficoImpacto(pegada) {
            let ctx = document.getElementById("graficoImpacto").getContext("2d");
            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["Florestas", "Oceanos", "Atmosfera", "Biodiversidade"],
                    datasets: [{
                        label: "Impacto (%)",
                        data: [pegada * 0.4, pegada * 0.3, pegada * 0.2, pegada * 0.1],
                        backgroundColor: ["#4caf50", "#03a9f4", "#ff5722", "#9c27b0"]
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        }
    </script>
</body>
</html>