!DOCTYPE html>
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
    </style>
</head>

<body>
    <div class="container">
        <h1>Calculadora de Pegada de Carbono</h1>

        <div class="text-start mt-4">
            <h3>O que é a Pegada de Carbono?</h3>
            <p>A pegada de carbono representa a quantidade total de gases do efeito estufa (principalmente CO₂) emitidos direta ou indiretamente por nossas atividades diárias, como o consumo de energia, transporte e hábitos de consumo.</p>
        </div>

        <div class="d-flex flex-column align-items-center mt-4">
            <button class="btn btn-warning mb-3" onclick="abrirCalculadora()">Calcular Pegada de Carbono</button>
        </div>
    </div>

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
                    <button class="btn btn-primary" onclick="calcularPegada()">Calcular</button>
                </div>
            </div>
        </div>
    </div>

    <div class="container grafico-container" id="graficoContainer" style="display: none;">
        <h3>Impacto da Sua Pegada de Carbono</h3>
        <canvas id="graficoPegada"></canvas>
    </div>

    <div class="container dicas" id="dicasContainer" style="display: none;">
        <h3>Dicas para Reduzir sua Pegada de Carbono</h3>
        <div id="dicas"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function abrirCalculadora() {
            new bootstrap.Modal(document.getElementById('modalCalculo')).show();
        }

        function calcularPegada() {
            let luz = parseFloat(document.getElementById("luz").value) || 0;
            let carro = parseFloat(document.getElementById("carro").value) || 0;
            let aviao = parseFloat(document.getElementById("aviao").value) || 0;
            let barco = parseFloat(document.getElementById("barco").value) || 0;

            let pegada = (luz * 0.5) + (carro * 0.21) + (aviao * 0.2) + (barco * 0.12);
            alert("Sua pegada de carbono mensal estimada é de " + pegada.toFixed(2) + " kg de CO₂.");

            mostrarDicas();
            gerarGrafico(luz, carro, aviao, barco);
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
            document.getElementById("graficoContainer").style.display = "block";
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
    </script>
</body>
