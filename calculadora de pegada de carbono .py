<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Pegada de Carbono</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-5">
    <h1 class="text-center">Calculadora de Pegada de Carbono</h1>
    <div class="d-flex flex-column align-items-center mt-4">
        <button class="btn btn-primary mb-3" onclick="abrirCadastro()">Cadastrar Usuário</button>
        <button class="btn btn-success mb-3" onclick="abrirLogin()">Login</button>
        <button class="btn btn-info mb-3" onclick="mostrarIdeias()">Ideias para Reduzir Pegada de Carbono</button>
    </div>
</div>

<!-- Modais -->
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
                <button class="btn btn-success" onclick="loginUsuario()">Entrar</button>
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

<script>
    const dbPromise = indexedDB.open("usuariosDB", 1);

    dbPromise.onupgradeneeded = (event) => {
        const db = event.target.result;
        if (!db.objectStoreNames.contains("usuarios")) {
            db.createObjectStore("usuarios", { keyPath: "id", autoIncrement: true });
        }
    };

    function abrirCadastro() {
        const modal = new bootstrap.Modal(document.getElementById('modalCadastro'));
        modal.show();
    }

    function cadastrarUsuario() {
        const usuario = document.getElementById("cadastroUsuario").value;
        const senha = document.getElementById("cadastroSenha").value;

        if (usuario && senha) {
            const transaction = dbPromise.result.transaction("usuarios", "readwrite");
            const store = transaction.objectStore("usuarios");
            const request = store.add({ usuario, senha });

            request.onsuccess = () => {
                alert("Cadastro realizado com sucesso!");
            };

            request.onerror = () => {
                alert("Erro: Usuário já existe!");
            };
        } else {
            alert("Por favor, preencha todos os campos.");
        }
    }

    function abrirLogin() {
        const modal = new bootstrap.Modal(document.getElementById('modalLogin'));
        modal.show();
    }

    function loginUsuario() {
        const usuario = document.getElementById("loginUsuario").value;
        const senha = document.getElementById("loginSenha").value;

        if (usuario && senha) {
            const transaction = dbPromise.result.transaction("usuarios", "readonly");
            const store = transaction.objectStore("usuarios");
            const request = store.openCursor();

            request.onsuccess = (event) => {
                const cursor = event.target.result;
                if (cursor) {
                    if (cursor.value.usuario === usuario && cursor.value.senha === senha) {
                        alert(`Bem-vindo, ${usuario}!`);
                        return;
                    }
                    cursor.continue();
                } else {
                    alert("Usuário ou senha incorretos.");
                }
            };
        } else {
            alert("Por favor, preencha todos os campos.");
        }
    }

    function mostrarIdeias() {
        const modal = new bootstrap.Modal(document.getElementById('modalIdeias'));
        modal.show();
    }
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
