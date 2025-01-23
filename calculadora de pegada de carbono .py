<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Pegada de Carbono com 2FA</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
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
            max-width: 600px;
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

        .btn-success {
            background-color: #28a745;
            border: none;
        }

        .btn-info {
            background-color: #17a2b8;
            border: none;
        }

        .btn:hover {
            opacity: 0.9;
        }

        .modal-title {
            font-size: 1.8rem;
            color: #0056b3;
        }

        .modal-content {
            border-radius: 15px;
        }

        .modal-body input {
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 10px;
        }

        ul {
            padding: 0;
            list-style-type: none;
        }

        ul li {
            text-align: left;
            margin-bottom: 10px;
        }

        ul li:before {
            content: "✔";
            color: #28a745;
            margin-right: 10px;
        }

        .alert {
            font-size: 1rem;
            font-weight: bold;
            color: #ffffff;
            background: #ff6b6b;
            border: none;
            border-radius: 10px;
        }

        .btn-close {
            background: transparent;
            border: none;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Calculadora de Pegada de Carbono</h1>
    <div class="d-flex flex-column align-items-center mt-4">
        <button class="btn btn-primary mb-3" onclick="abrirCadastro()">Cadastrar Usuário</button>
        <button class="btn btn-success mb-3" onclick="abrirLogin()">Login</button>
        <button class="btn btn-info mb-3" onclick="mostrarIdeias()">Ideias para Reduzir Pegada de Carbono</button>
    </div>
</div>

<div class="modal" id="modalCadastro" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Cadastro de Usuário</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="text" id="cadastroUsuario" class="form-control mb-3" placeholder="Nome de Usuário">
                <input type="password" id="cadastroSenha" class="form-control mb-3" placeholder="Senha">
                <input type="text" id="cadastroTelefone" class="form-control mb-3" placeholder="Número de Telefone (ex: +5591999999999)">
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary" onclick="cadastrarUsuario()">Cadastrar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="modalLogin" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Login</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="text" id="loginUsuario" class="form-control mb-3" placeholder="Nome de Usuário">
                <input type="password" id="loginSenha" class="form-control mb-3" placeholder="Senha">
            </div>
            <div class="modal-footer">
                <button class="btn btn-success" onclick="validarLogin()">Entrar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="modal2FA" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Autenticação de Dois Fatores</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p>Um código de verificação foi enviado para o seu número de telefone.</p>
                <input type="text" id="codigo2FA" class="form-control mb-3" placeholder="Digite o código recebido">
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary" onclick="verificarCodigo2FA()">Verificar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="modalIdeias" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Ideias para Reduzir a Pegada de Carbono</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <ul>
                    <li>Utilize lâmpadas de LED em casa para economizar energia.</li>
                    <li>Ande de bicicleta ou caminhe para trajetos curtos.</li>
                    <li>Consuma alimentos locais e de produtores orgânicos.</li>
                    <li>Reduza o uso de embalagens plásticas descartáveis.</li>
                    <li>Evite o desperdício de água e energia.</li>
                    <li>Planeje viagens para reduzir o uso de transporte aéreo.</li>
                    <li>Adote práticas de reciclagem e compostagem.</li>
                    <li>Participe de programas de reflorestamento.</li>
                    <li>Incentive o uso de energia renovável, como solar e eólica.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
    // Código JavaScript a ser adicionado aqui
</script>
</body>
</html>

