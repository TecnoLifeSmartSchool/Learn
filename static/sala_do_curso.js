// const socket = io.connect('http://' + document.domain + ':' + location.port);
// document.querySelector('form').addEventListener('submit',(e)=>{

//     e.preventDefault()
//     let usuario = document.getElementById('usuario').innerHTML
//       let adiministrador = document.getElementById('adiministrador').innerHTML
//     let mensagem = e.target[0].value
//     let nome_da_sala = document.getElementById('nome_da_sala').innerHTML
//     socket.emit('grupo',{nome_remitente:usuario , menssagem_usuario:mensagem , nome_da_sala: nome_da_sala , adiministrador:adiministrador})

// })
// socket.on('novo_grupo' , (msg)=>{
//     let usuario = document.getElementById('usuario').innerHTML
  
//     let menssagens = document.querySelector('.menssagens')
//     if (usuario === msg.usuario){
//     resultado = `<p  class="mim"><b id="user">${msg.usuario}</b> <br>${msg.menssagem}</p>`
//     menssagens.innerHTML+=resultado

//     }
//     else{
//     resultado = `<p  class="ele"><b id="user">${msg.usuario}</b> <br>${msg.menssagem}</p>`
//     menssagens.innerHTML+=resultado
//     }



// })
