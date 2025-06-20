
function menuR(){

    let art1 = document.querySelector('.art1')
    if(art1.style.display === "flex"){
        art1.style.display = "none"
    }
    else{
        art1.style.display = "flex"
    }

}

function usuario_denuncia(parame){

    let parametro = parame.parentElement;
    let nome_sujeitos = parametro.querySelector('.oculto_nome').innerHTML
    let fundo = document.querySelector('.fundo_caxa_centro').style.display = "none"
    let remitente = parametro.querySelector('.remitente').innerHTML
    let cont_caxa_centro = document.querySelector('.cont_caxa_centro').style.display = "flex"
    let destnatario = parametro.querySelector('.oculto_nome').innerHTML
    let denuncia = parametro.querySelector('.oculto_comentario').innerHTML
    let receber_nome_remitente = document.querySelector('#nome_remitente').innerHTML = remitente
    let informa_denuncia = document.querySelector('#informa_denuncia').innerHTML = denuncia
    let receber_nome_destinatario = document.querySelector('#nome_destinatario').innerHTML = destnatario



    


}

function denunciar_sujeito(sujeitos){

    let sujeito = sujeitos.parentElement;
    let nome_denuncia = sujeito.querySelector('.nome_denuncia')
    let caxa_comentario = document.querySelector('.denuncia_usuario_caxa').style.display = "block"
    let receber_nome_sujeito = document.getElementById('receber_nome_sujeito')
    receber_nome_sujeito.innerHTML = nome_denuncia.innerHTML
    let caxa_configuration = document.querySelector('.caxa_configuration').style.display = "none"

}
function cancelar_denuncia_usuario(){

    let caxa_comentario = document.querySelector('.denuncia_usuario_caxa').style.display = "none"
    let caxa_configuration = document.querySelector('.caxa_configuration').style.display = "flex"



}

function voltar_admim(){

    let admim = document.querySelector('.admim').style.display = "none"

}
function configurações(){


        let admim = document.querySelector('.admim').style.display = "flex"

}