

function modo_escuro(){

    a = "--body_escuro"


    let bady = document.querySelector("body")
    let header = document.querySelector("header")
    let root = document.querySelector(':root')
    header.style.boxShadow = "none"
    header.style.backgroundColor = "var(--header_escuro)"
    bady.style.backgroundColor = "var(--body_escuro)"
    root.style.setProperty("--core_branco","teal")
    root.style.setProperty("--core_vermelho","#1f1f1f")
    root.style.setProperty("--core_letra","#fff")



}




