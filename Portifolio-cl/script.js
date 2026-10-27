// SAUDAÇÃO AUTOMÁTICA
const saudacao = document.getElementById("saudacao");
const hora = new Date().getHours();

if (hora >= 5 && hora < 12) {
    saudacao.textContent = "Bom dia! Seja bem-vindo(a).";
} else if (hora >= 12 && hora < 18) {
    saudacao.textContent = "Boa tarde! Seja bem-vindo(a).";
} else {
    saudacao.textContent = "Boa noite! Seja bem-vindo(a).";
}

// MENU PARA CELULAR
const menuToggle = document.getElementById("menu-toggle");
const menu = document.getElementById("menu");

menuToggle.addEventListener("click", function () {
    const aberto = menu.classList.toggle("aberto");

    menuToggle.setAttribute("aria-expanded", aberto);
    menuToggle.setAttribute(
        "aria-label",
        aberto ? "Fechar menu" : "Abrir menu"
    );
});

// FECHAR MENU AO CLICAR EM UM LINK
const linksMenu = menu.querySelectorAll("a");

linksMenu.forEach(function (link) {
    link.addEventListener("click", function () {
        menu.classList.remove("aberto");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Abrir menu");
    });
});

// ALTERNAR MODO CLARO E ESCURO
const botaoTema = document.getElementById("tema");

botaoTema.addEventListener("click", function () {
    document.body.classList.toggle("modo-claro");

    const modoClaro = document.body.classList.contains("modo-claro");

    botaoTema.textContent = modoClaro ? "☾" : "☼";
    botaoTema.setAttribute(
        "aria-label",
        modoClaro ? "Ativar modo escuro" : "Ativar modo claro"
    );
});

// ATUALIZAR O ANO AUTOMATICAMENTE
document.getElementById("ano").textContent = new Date().getFullYear();

// VALIDAR E PREPARAR O FORMULÁRIO DE CONTATO
const formulario = document.getElementById("form-contato");
const statusForm = document.getElementById("status-form");

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const mensagem = document.getElementById("mensagem").value.trim();
    const consentimento = document.getElementById("consentimento").checked;

    if (nome.length < 2) {
        statusForm.textContent = "Digite seu nome completo.";
        document.getElementById("nome").focus();
        return;
    }

    if (!emailValido(email)) {
        statusForm.textContent = "Digite um e-mail válido.";
        document.getElementById("email").focus();
        return;
    }

    if (mensagem.length < 10) {
        statusForm.textContent = "A mensagem precisa ter pelo menos 10 caracteres.";
        document.getElementById("mensagem").focus();
        return;
    }

    if (!consentimento) {
        statusForm.textContent = "Marque a opção de consentimento para continuar.";
        document.getElementById("consentimento").focus();
        return;
    }

    const destinatario = "caioleonardo804@gmail.com";
    const assunto = encodeURIComponent("Contato pelo portfólio");
    const corpo = encodeURIComponent(
        "Nome: " + nome +
        "\nE-mail: " + email +
        "\n\nMensagem:\n" + mensagem
    );

    statusForm.textContent =
        "Abrindo seu aplicativo de e-mail para preparar a mensagem.";

    window.location.href =
        "mailto:" + destinatario +
        "?subject=" + assunto +
        "&body=" + corpo;
});

// VERIFICAR FORMATO DO E-MAIL
function emailValido(email) {
    const formato = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return formato.test(email);
}