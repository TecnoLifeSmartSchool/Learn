
function mobile(){


    let menu = document.querySelector('.menu_mobile').style.display = "flex"


}
function sair(){
      v = 10


        
     
      let menu = document.querySelector('.menu_mobile').style.display ="none"
        // menu.style.display = "none"
        
        
              
}

function limpar(){
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    let nome = document.getElementById('n').innerHTML
    socket.emit('limpar',{nome_remitente:nome})
    let meuChat =document.querySelector('.notificar').innerHTML=""
    setTimeout(() => {
        document.querySelector('.boxa').style.display = "flex"
    }, 200);
  setInterval(() => {
    document.querySelector('.boxa').style.display = "none"

  }, 2000);

}
// function eliminar(elimina){

//   let deletar = elimina.parentElement;
//   let texto = deletar.querySelector('.texto').innerHTML
//   alert(texto)

// }

function deletar_amigos(){

  let menu_mobile = document.querySelector('.menu_mobile_menu').style.display = "none"
  let deletar = document.querySelector('.lista_amigo_delete').style.display = "flex"

}
function voltar_deletar(){

  let menu_mobile = document.querySelector('.menu_mobile_menu').style.display = "flex"
  let deletar = document.querySelector('.lista_amigo_delete').style.display = "none"


}



function lista(elementoLi) {
  // Encontra a div "sobre" que está no mesmo nível do botão pai do li clicado
  const divSobre = elementoLi.closest('.short').querySelector('.sobre');

  // Verifica o estado atual do display
  if (divSobre.style.display === 'flex') {
    // Se estiver flex, muda para none
    divSobre.style.display = 'none';
  } else {
    // Se não estiver flex (ou estiver vazio), muda para flex
    divSobre.style.display = 'flex';
  }
}


function editar_imagem(){

  document.querySelector('.modificar').style.display = "flex"


}
function voltar_editar_imagem(){

    document.querySelector('.modificar').style.display = "none"

}

function editar_nome(){

  document.querySelector('.modificar2').style.display = "flex"

}