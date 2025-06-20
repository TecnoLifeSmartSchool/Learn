
const socket = io.connect('http://' + document.domain + ':' + location.port);
window.onload = ()=>{


    
}
function alugar_sala(){

    let alugar_sala = document.querySelector('.alugar_sala').style.display = "block"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chat = document.querySelector('.chat').style.display = "none"
        let novo_chat = document.querySelector('.novo_chat').style.display = "none"
     let chatt = document.querySelector('.meuChat').style.display = "none"
     let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"


}
function home(){
    let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let chat = document.querySelector('.chat').style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "flex"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let shorte = document.querySelector('.shorte').style.display = "none"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "flex"
    let amigos = document.querySelector('.amigos').style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let sect1 = document.querySelector('.sect1').style.display = "flex"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    let header = document.querySelector('header').style.display = "flex"
}

function minha_sala(){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
 let chatt = document.querySelector('.meuChat').style.display = "none"
let chat = document.querySelector('.chat').style.display = "none"
let usuuario = document.querySelector('.user').style.display = "none"
let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
let curso = document.querySelector('.curso').style.display = "flex"
let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
let adicionar = document.querySelector(".adicionar").style.display = "none"
let notificar = document.querySelector('.notificar').style.display = "none"
let novo_chat = document.querySelector('.novo_chat').style.display = "none"



}

function MeuCurso(classe){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let entrar = classe.parentElement;
    let cfg1 = entrar.querySelector('.cfg1').innerHTML
    let sala = document.getElementById('SALA').value = cfg1
    let others = document.querySelector('.others').style.display = "none"
    socket.emit('set_sala_ativa' , {sala:sala})

}

function usuarios(){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"    
    let chat = document.querySelector('.chat').style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "block"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    let others = document.querySelector('.others').style.display = "block"


}
function cadastrar_se(sala){

    
    let clase = sala.parentElement;
    let professor = clase.querySelector('#professor').innerHTML
    let cursos = clase.querySelector('.curs').innerHTML
    let sala_cadastro = document.getElementById('sala_cadastro').value = cursos
    let formador = document.getElementById('formador').innerHTML =  professor
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    let chat = document.querySelector('.chat').style.display = "none"
    let compra_usuario = document.querySelector('.compra_usuario').style.display = "flex"
    let telefone = clase.querySelector('#telefone').innerHTML
    let tele = document.querySelector('#tele').href=`tel:+${telefone}`
    



}

function cadastrar_ses(sala){
    let clase = sala.parentElement;
    let cursos = clase.querySelector('.curs').innerHTML
    let sala_cadastro = document.getElementById('sala_cadastro').value = cursos
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "flex"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    let chat = document.querySelector('.chat').style.display = "none"
    let art2 = document.querySelector('.art2').style.display = "none"
    let art3 = document.querySelector('.art3').style.display = "flex"



}
function adicionar_video(){
    let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "flex"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    
    let chat = document.querySelector('.chat').style.display = "none"



}

function chat(){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    const messagesDiv = document.getElementById('menssagens').innerHTML = ""
    let chat = document.querySelector('.meuChat').style.display = "block"
    let chat2 = document.querySelector('.chat').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let notificar = document.querySelector('.notificar')
    notificar.style.display = "none"
    let subSMS = document.getElementById('subSMS')
    let renovar = document.querySelector('.subSMS')
    valor = Number(subSMS.innerHTML = 0)
    renovar.style.display = "none"
    let n = document.getElementById('n').innerHTML
    socket.emit('apagar_sms',{nome_remitente:n})
    document.querySelector('.ponto').style.display = "none"

    



}
let subs = document.querySelector('.subSMS')

if(subs.innerHTML!=0){

   subs.style.display = "flex"


}


function nota(){

let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let nome = document.getElementById('n').innerHTML
    const messagesDiv = document.getElementById('menssagens').innerHTML = ""
    let chat = document.querySelector('.meuChat').style.display = "none"
    let chat2 = document.querySelector('.chat').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let notificar = document.querySelector('.notificar')
    notificar.style.display = "block"
    let sub = document.querySelector('.sub').style.display = "none"
    socket.emit('limpa',{nome_remitente:nome})
    let receber = document.getElementById('sub')
    valor = Number(sub.innerHTML = 0)
    receber.innerHTML = valor
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    
 
    

}






function short(){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let shorte = document.querySelector('.shorte').style.display = "flex"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "none"
    let amigos = document.querySelector('.amigos').style.display = "none"
    let art1 = document.querySelector('.art1')
  
}
function shorts(){
let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
    let shorte = document.querySelector('.shorte').style.display = "flex"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "none"
    let amigos = document.querySelector('.amigos').style.display = "none"
    let art1 = document.querySelector('.art1').style.display = "flex"
    let art2 = document.querySelector('.art2').style.display = "none"
    let art3 = document.querySelector('.art3').style.display = "none"
    let art4 = document.querySelector('.art4').style.display = "none"
    document.querySelector('.art1').style.width = "100%"
    document.querySelector('.art1').style.boxShadow = "none"
    
    


}
function menu(){

    let shorte = document.querySelector('.shorte').style.display = "none"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "flex"
    let amigos = document.querySelector('.amigos').style.display = "none"
   

}
function adicionr_amigo(){

    let shorte = document.querySelector('.shorte').style.display = "none"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "none"
    let amigos = document.querySelector('.amigos').style.display = "block"
    let art1 = document.querySelector('.art1')




}

function activar(){
        let art1 = document.querySelector('.art1').style.width = "100%"
}
let contador = 0
function artShort(){

    let art2 = document.querySelector('.art2').style.display = "none"
    let art4 = document.querySelector('.art4').style.display = "block"

  

}
function artShorts(){

    let art2 = document.querySelector('.art2').style.display = "none"
    let art4 = document.querySelector('.art4').style.display = "block"
    let art1 = document.querySelector('.art1').style.display = "none"
  

}
function curso(){

    let art2 = document.querySelector('.art2').style.display = "block"
    let art4 = document.querySelector('.art4').style.display = "none"

    


}
function cursos(){

    let art2 = document.querySelector('.art2').style.display = "block"
    let art4 = document.querySelector('.art4').style.display = "none"
    let art1 = document.querySelector('.art1').style.display = "none"
    


}
function home_grupo(){
    let chat_de_conversa_do_grupo_das_aulas = document.querySelector('.chat_de_conversa_do_grupo_das_aulas').style.display = "none"
    let conteiner_ds_aulas = document.querySelector('.conteiner_ds_aulas').style.display = "block"
    let ultimo2 = document.querySelector('.ultimo2').style.display = "flex"
}
function alunos_registrados_no_grupo(){
    let alunos_cadastrados = document.querySelector('.alunos_cadastrados').style.display = "flex"
    let video_lesson = document.querySelector('.video_lesson').style.display = "none"
    let volar_grupo = document.querySelector('.volar_grupo').style.display = "flex"
}
function voltar_grupo(){
    let alunos_cadastrados = document.querySelector('.alunos_cadastrados').style.display = "none"
    let video_lesson = document.querySelector('.video_lesson').style.display = "block"
    let volar_grupo = document.querySelector('.volar_grupo').style.display = "none"
}
function gosto(gostar){

    let gostei = gostar.parentElement;
    let gostos = document.getElementById('user')
    let like = gostei.querySelector('#like')
    
    contador ++
    
    like.innerHTML=Number(contador)

    

}

function perfil(){

    let sect1 = document.querySelector('.sect1').style.display = "none"
    let perfil = document.querySelector('.perfil').style.display = "flex"
    let header = document.getElementById('header').style.display = "none"
    entrada = document.createElement("input")



}


function cursoSearche(){

    let input = document.getElementById('result').value
    input = input.toLowerCase()
    let x = document.getElementsByClassName('cursoSearch')
    for (i = 0; i<x.length;i++){

        if(!x[i].innerHTML.toLocaleLowerCase().includes(input)){

            x[i].style.display = "none"

        }
        else{
            x[i].style.display = ""
        }

    }



}

function buscar(){

    let inputAmigo = document.getElementById('nomeAmigo').value
    inputAmigo = inputAmigo.toLocaleLowerCase()
    let y = document.getElementsByClassName('nomeAmigos')
    for (a = 0; a<y.length;a++){
        if(!y[a].innerHTML.toLocaleLowerCase().includes(inputAmigo)){

            y[a].style.display = "none"

        }
        else{
            y[a].style.display = ""
        }
    }

}



function adicionarAmigo(botao){

    let divPai = botao.parentElement;
    let nomeAmigo = divPai.querySelector('.nomeAmigo')
    let b = divPai.querySelector('.b')
    let imagem = divPai.querySelector('.imagem').src
    let meuChat =document.querySelector('.notificar')
    let nome_user = document.getElementById('n')
    let full = `${nomeAmigo.innerHTML}_${nome_user.innerHTML}`
    let s = ''


    socket.emit('sendNoticia' , {imagem:imagem , nome_remitente:nome_user.innerHTML , nome_destinatario: nomeAmigo.innerHTML , sala:full})
    
   

    socket.on('getNoticia' , (data)=>{


        meuChat.innerHTML+=`
    
       <!-- amizade -->
       <div class="amizade">

        <div class="imagemAmizade">
            <img src="${data.image}" alt="">
        </div>

        <div class="widgest">
            <button class="sujeitoAmizade"><b class="buscarUser">${data.nome_destinatario}</b> fez um pedido de amizade</button>
            
            <button class="verde" onclick="aceitar(this)"> <em class="em">aceitar</em> <em class="red">recusar</em> </button>
            
           
        </div>

    </div>
   <!-- fim amizade -->

    
    `




    })


   b.disabled = true
   b.style.backgroundColor = "grey"
   b.style.color = "#fff"
   b.innerHTML = "Enviado"
   b.style.cursor = "not-allowed"

}

function aceitar(busca){


    let nome_remitente = document.getElementById('n').innerHTML
    let pai = busca.parentElement;
    let buscarUser = pai.querySelector('.buscarUser').innerHTML
    let sala = pai.querySelector('#sala').innerHTML
    alert(sala)
    let notificar = document.querySelector('.notificar')
    let meuChat = document.querySelector('.meuChat')

    

    meuChat.innerHTML+=`
    
       <p class="userMeuChat">
                                <img src="../static/arquivo_imagem/person_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.svg" alt="">
                                <button class="amigo">${buscarUser}</button>
                                <button onclick="conversa(this)" class="anima">conversar</button>
                                <span id="sala" style = "display:none">${sala}</span>
        </p>
    
    `
    socket.emit('criar_sala',{sala:sala,nome_remitente:nome_remitente,nome_destinatario:buscarUser})

    

}


    let nome_remitente = document.getElementById('n').innerHTML
    let nome_destinatario = ''
    let imagem = ''
    socket.emit('conn',{nome_remitente:nome_remitente})



    contador = 0
    socket.on('getNoticia', function(data) {
        console.log('Notificação recebida:', data);
        // Aqui você deve adicionar a lógica para exibir a notificação ao usuário
        const nomeDestinatario = data.nome_destinatario;
        const imagem = data.image;
        let meuChat =document.querySelector('.notificar')
        alert(`Nova notificação de: ${nomeDestinatario} com imagem: ${imagem}`); // Exemplo simples
        let sub = document.querySelector('.sub').style.display = "flex"
        let valor = Number(document.getElementById('sub').innerHTML)
        resultado = document.getElementById('sub')
        soma = valor + 1
        resultado.innerHTML = soma

     
        
   



        meuChat.innerHTML+=`
    
                            <!-- amizade -->
                            <div class="amizade">
                    
                            <div class="imagemAmizade">
                                <img src="${data.image}" alt="">
                            </div>
                    
                            <div class="widgest">
                                <button class="sujeitoAmizade"><b class="buscarUser">${data.nome_destinatario}</b> fez um pedido de amizade</button>
                                
                                <button class="verde" onclick="aceitar(this)"> <em class="em">aceitar</em> <em class="red">recusar</em> </button>
                                <span style="display: none;" id="sala">${data.sala}</span>
                                
                            </div>
                    
                        </div>
                        <!-- fim amizade -->
                    
                        
                        `
 


    });

    socket.on('nova_sala_criada_notificacao',(data)=>{


        alert(`${data.sala}_muito bem`)
        let meuChat = document.querySelector('.meuChat')
        meuChat.innerHTML+=`
    
        <p class="userMeuChat">
                                 <img src="../static/arquivo_imagem/person_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.svg" alt="">
                                 <button class="amigo">${data.nome_remitente}</button>
                                 <button onclick="conversa(this)" class="anima">conversar</button>
                                 <span id="sala" style = "display:none">${data.sala}</span>
         </p>
    ` 


    })

function eliminar(elimina){

        let nome_usuario = document.getElementById('n').innerHTML
        let deletar = elimina.parentElement;
        let texto = deletar.querySelector('.texto').innerHTML
        alert(nome_usuario)
        socket.emit('deletar_amigo',{nome_amigo:texto , nome_remitente:nome_usuario})

}

const videoElement = document.querySelector('video');

if (videoElement) {
  videoElement.addEventListener('contextmenu', function(e) {
    e.preventDefault(); // Impede a exibição do menu de contexto padrão
  });
}

let sub = document.querySelector('.sub')
receber = Number(sub.innerHTML)
if (receber!=0){

    sub.style.display = "flex"

}


function adicionr_amigos(){

    let shorte = document.querySelector('.shorte').style.display = "none"
    let amigos = document.querySelector('.amigos').style.display = "block"
    let menu = document.querySelector('.menuArt1').style.display = "none"
    let art1 = document.querySelector('.art1').style.width = "100%"
    document.querySelector('.art1').style.height = "100%"
    document.querySelector('.art1').style.marginTop = "-0%"
    // document.querySelector('.art1').style.borderRadius = "100%"
    let art2 = document.querySelector('.art1').style.background = "none"
    let footer = document.querySelector("footer").style.display = "none"
    // let art1 = document.querySelector('.art1').style.display = "none"



}
function alugar_salas(){

    let alugar_sala = document.querySelector('.alugar_sala').style.display = "block"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chat = document.querySelector('.chat').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let art3 = document.querySelector('.art3').style.display = "flex"
    let art2 = document.querySelector('.art2').style.display = "none"
    let art4 = document.querySelector('.art4').style.display = "none"
    // let footer = document.querySelector("footer").style.display = "none"
    let art1 = document.querySelector('.art1').style.display = "none"
    

}
function homes(){

    let chat = document.querySelector('.chat').style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "flex"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let shorte = document.querySelector('.shorte').style.display = "none"
    let ar1Menu = document.querySelector('.menuArt1').style.display = "flex"
    let amigos = document.querySelector('.amigos').style.display = "none"
    let notificar = document.querySelector('.notificar').style.display = "none"
    let art1 = document.querySelector('.art1').style.width = "20%"
    document.querySelector('.art1').style.height = "70%"
    document.querySelector('.art1').style.marginTop = "5%"
    let sect1 = document.querySelector('.sect1').style.display = "flex"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let art3 = document.querySelector('.art3').style.display = "none"
    document.querySelector("header").style.display = "flex"
    document.querySelector('.art4').style.display = "block"
    document.querySelector('.art2').style.display = "none"
    if(document.querySelector('.art1').style.display === "flex"){
        document.querySelector('.art1').style.display = "none"
        document.querySelector(".novo_chat").style.display = "none"
        
        
        // let art2 = document.querySelector('.art1').style.background = "var(--core_branco)"
    }
    else{
        document.querySelector('.art1').style.display = "flex"
    }
    document.querySelector('.menu_do_conteiner_das_aulas').style.display = "none"
    document.querySelector('.ultimo').style.display = "flex"

    

}
function usuarioss(){

 
    let notificar = document.querySelector('.notificar').style.display = "none"
    let chatt = document.querySelector('.meuChat').style.display = "none"    
    let chat = document.querySelector('.chat').style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    usuuario.style.display = "block"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let art3 = document.querySelector('.art3')
    let art4 = document.querySelector('.art4').style.display = "none"
    art3.style.display = "flex"
    document.querySelector('.art1').style.display = "none"
    document.querySelector(".novo_chat").style.display = "none"
        document.querySelector(".form").style.display = "none"


    

}
function tira(){
    document.querySelector('.ultimo').style.display = "none"
}
let titulo_menu = document.querySelector('#tg').innerHTML
if (titulo_menu!==""){
     document.querySelector('.ultimo').style.display = "none"
     document.querySelector('.ultimo2').style.display = "flex"
     let header = document.querySelector('header').style.display = "none"
}

function chats(){

    let art4 = document.querySelector('.art4').style.display = "none"
    let art3 = document.querySelector('.art3').style.display = "flex"
    document.querySelector('.art3').style.height = "99%"
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    const messagesDiv = document.getElementById('menssagens').innerHTML = ""
    let chat = document.querySelector('.meuChat').style.display = "block"
    let chat2 = document.querySelector('.chat').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let notificar = document.querySelector('.notificar')
    notificar.style.display = "none"
    let subSMS = document.getElementById('subSMS')
    let renovar = document.querySelector('.subSMS')
    valor = Number(subSMS.innerHTML = 0)
    renovar.style.display = "none"
    let n = document.getElementById('n').innerHTML
    socket.emit('apagar_sms',{nome_remitente:n})
    // let ultimo = document.querySelector('.ultimo').style.display = "none"
    let art1 = document.querySelector('.art1').style.display = "none"
    document.querySelector('header').style.display = "none"
    let ultimo = document.querySelector('.ultimo').style.display = "none"
   


}
function regressar(){

    let art4 = document.querySelector('.art4').style.display = ""
    let art3 = document.querySelector('.art3').style.display = "none"
    let art2 = document.querySelector('.art2').style.display = "none"
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    const messagesDiv = document.getElementById('menssagens').innerHTML = ""
    let chat = document.querySelector('.meuChat').style.display = "none"
    let chat2 = document.querySelector('.chat').style.display = "none"
    let adicionar = document.querySelector(".adicionar").style.display = "none"
    let alugar_sala = document.querySelector('.alugar_sala').style.display = "none"
    let primeiro_comando = document.querySelector('.primeiro_comando').style.display = "none"
    let usuuario = document.querySelector('.user')
    let novo_chat = document.querySelector('.novo_chat').style.display = "none"
    usuuario.style.display = "none"
    let cadastra_se_ = document.querySelector('.cadastra_se').style.display = "none"
    let curso = document.querySelector('.curso').style.display = "none"
    let notificar = document.querySelector('.notificar')
    notificar.style.display = "none"
    let subSMS = document.getElementById('subSMS')
    let renovar = document.querySelector('.subSMS')
    valor = Number(subSMS.innerHTML = 0)
    renovar.style.display = "none"
    let n = document.getElementById('n').innerHTML
    socket.emit('apagar_sms',{nome_remitente:n})
    let ultimo = document.querySelector('.ultimo')
    let ultimo2 = document.querySelector('.ultimo2').style.display = "none"
    ultimo.style.display = "flex"
    document.querySelector('.video_aula_usuario').style.display = "none"
    document.querySelector('header').style.display = "flex"
    let art1 = document.querySelector('.art1').style.display = "none"
    document.querySelector('.conteiner_ds_aulas').style.display = "none"
    document.querySelector('.sect1').style.display = "flex"

  
    

}
function chat_grupo(){
    let chat_de_conversa_do_grupo_das_aulas = document.querySelector('.chat_de_conversa_do_grupo_das_aulas').style.display = "block"
    let conteiner_ds_aulas = document.querySelector('.conteiner_ds_aulas').style.display = "none"
    let ultimo2 = document.querySelector('.ultimo2').style.display = "none"
}
socket.on('ola',(data)=>{

    alert('ola mundo')
    nome_destinatario = data.nome_remitente
    let amigo = document.querySelectorAll('.amigo')
    let ponto = document.querySelectorAll('.ponto')
    
    t = amigo.length
    c = Number(t)
    alert(t)

    for(v = 0; v<c; v++){

        console.log(amigo[v].innerHTML)
        if (amigo[v].innerHTML === nome_destinatario){
            ponto[v].style.display = 'flex'
            let g = document.querySelector('.ponto2').style.display = "flex"
      


        }


    }

    



})




function enviar_denuncia_usuario(){

    let sujeito = document.getElementById('receber_nome_sujeito').innerHTML
    let descricao = document.getElementById('denuncia_usuario').value
    let remitente = document.getElementById('n').innerHTML
    socket.emit('denuncia',{sujeito:sujeito,descricao:descricao,remitente:remitente})
    let receber_recado = document.getElementById('receber_recado').innerHTML = "denuncia enviada."
    document.querySelector('.configuration').style.display = "none"
    alert(`vc denunciou ${sujeito}. A sua denuncia será reencaminhada para o administrador. Obrigado`)
   

}
function cancelar(){

       document.querySelector('.configuration').style.display = "none"

}
function minha_denuncia(){
        document.querySelector('.configuration').style.display = "flex"
        let others = document.querySelector('.others').style.display = "block"
}

let contadora = 0
let txt = `Diga para nós o que devemos melhorar ou acrescentar para que a nossa escola online venha a satisfazer a  necessidade de todos`
let h1 = document.getElementById('txt_melhore')

function digitar(){

    if(contadora<txt.length){
        h1.innerHTML+=txt.charAt(contadora)
        contadora++
        setTimeout(digitar,60)
    }


}
digitar()

function melhor(){

    let nome_remitente = document.querySelector('#n').innerHTML
    let textos = document.getElementById('textos').value
    socket.emit('melhor',{nome_remitente:nome_remitente,texto:textos})
    alert('comentario enviado com sucesso!')


}
function voltar_melhor(){

    document.querySelector('.melhor').style.display = "none"

}
function melhoria(){
        document.querySelector('.melhor').style.display = "flex"
}

let contador2 = 0
let texto2 = "Cláudio Avelino"
let h2 = document.getElementById('texto2')
function digitar2(){

    if(contador2<texto2.length){
        h2.innerHTML+=texto2.charAt(contador2)
        contador2++
        setTimeout(digitar2,60)
    }


}
digitar2()

function pesquisa_denuncia(){



    let pesquisa_denuncia = document.getElementById('pesquisa_denuncia').value
    pesquisa_denuncia = pesquisa_denuncia.toLocaleLowerCase()
    let nome_denuncia = document.getElementsByClassName('nome_denuncias')
    for (x=0;x<nome_denuncia.length;x++){
        if(!nome_denuncia[x].innerHTML.toLocaleLowerCase().includes(pesquisa_denuncia)){
            nome_denuncia[x].style.display = "none"
        }
        else{
            nome_denuncia[x].style.display = ""
        }
    }



}



    let resultado = document.getElementById("resultado").innerHTML
 
    if(document.getElementById("resultado").innerHTML !== "None"){
        document.querySelector('.sect1').style.display = "none"
        document.querySelector('.video_aula_usuario').style.display = "flex"
        document.querySelector('header').style.display = "none"
    }
    else{
        document.querySelector('.video_aula_usuario').style.display = "none"
        document.querySelector('.sect1').style.display = "flex"

    }



    function alunos(){
        let video_lesson = document.querySelector('.video_lesson').style.display = "none"
        let alunos_cadastrados = document.querySelector('.alunos_cadastrados').style.display = "flex"
    }
    function curso_actual(){
        let video_lesson = document.querySelector('.video_lesson').style.display = ""
        let alunos_cadastrados = document.querySelector('.alunos_cadastrados').style.display = "none"

    }






    function sendMenssageGrupo(){
        let menssagem_grupo = document.getElementById("menssagem_grupo").value

        let nome_user_grupo = document.getElementById("nome_user_grupo").innerHTML
        let sala_do_grupo   = document.getElementById("sala_do_grupo").innerHTML
        document.getElementById("menssagem_grupo").value = ""
        socket.emit('grupo',{remitente:nome_user_grupo , menssagem:menssagem_grupo , sala_do_grupo:sala_do_grupo})
        socket.emit('set_sala_ativa' , {sala:sala_do_grupo})


    }

        socket.on('getMenssageGupo',(data)=>{
            
            nome_da_sala = data.nome_da_sala
            if (nome_da_sala === nome_da_sala){

            let menssagem_grupo = document.querySelector('.menssagem_grupo')
            valor = 
            `
            <li class="msg_grupo ${(data.nome_destinatario == document.getElementById("nome_user_grupo").innerHTML) ? 'mims':'eles'}">
                <em class="em">${data.nome_destinatario}</em>
                ${data.menssagem}
            </li>
            `
            menssagem_grupo.innerHTML+=valor


            }
           
        })
        
        
        function MostraTexto(mostra){

            mostra.classList.toggle('shortTextoMostrar')
            

        }


        function transmitir(){
            let nome_da_sala = document.getElementById('nome_da_sala').innerHTML
            let nome_user_grupo = document.getElementById('nome_user_grupo').innerHTML
            localStorage.nome_da_sala = nome_da_sala
            localStorage.nome_user_grupo = nome_user_grupo
            location = "transmitir"
        }
    
        function gerar_codigo(){
            let nome_da_sala = document.getElementById('nome_da_sala').innerHTML
            let nome_user_grupo = document.getElementById('nome_user_grupo').innerHTML
            socket.emit('gerar_codigo' , {nome_da_sala:nome_da_sala , nome_usuario:nome_user_grupo})
            alert('vc adicionou um novo codigo de confirmação!')
        }
        function carregar(){
            let loader = document.querySelector('.loader').style.display = "flex"
        }
        function carregar2(){
            let loader = document.querySelector('.loader').style.display = "flex"
            let menssagem_carregando = document.getElementById('menssagem_carregando').innerHTML = "Enviando nova aula ao curso."
        }
        function gerados(){
            let video_lesson = document.querySelector('.video_lesson')
            let guardar_codigos_gerados = document.querySelector('.guardar_codigos_gerados')
            if (guardar_codigos_gerados.style.display === "none"){
                document.querySelector('.guardar_codigos_gerados'). style.display = "flex"
                document.querySelector('.video_lesson').style.display = "none"
            }
            else{
                document.querySelector('.guardar_codigos_gerados').style.display = "none"
                document.querySelector('.video_lesson').style.display = "flex"
            }
        }
        function confirmar_compra(){

            let formador = document.getElementById('formador').innerHTML
            let nome_do_usuario = document.getElementById('n').innerHTML
            let codigo_digitado_pelo_usuario = document.getElementById('codigo_digitado_pelo_usuario').value
            if(codigo_digitado_pelo_usuario!==""){
            
            socket.emit('Verificar_Codigo' , {nome_do_usuario:nome_do_usuario , nome_do_formador:formador , codigo_digitado_pelo_usuario:codigo_digitado_pelo_usuario})
            document.getElementById('codigo_digitado_pelo_usuario').value = ""
          
            }
           

        }
       
        socket.on('codigos' , (data)=>{
            
            let nome_remitente = document.getElementById('n').innerHTML
            console.log(data.nome_remitente)
            console.log('-'*50)
            console.log(nome_remitente)
            condição = "Aprovado"
            localStorage.codigo = data.menssagem 
            receber = localStorage.getItem('codigo')
            alert('esta activo')
            
      
            if(receber === condição){
                let compra_usuario = document.querySelector('.compra_usuario').style.display = "none"
                let cadastra_se = document.querySelector('.cadastra_se').style.display = "flex"
            }
           

        })
     


//  conn = None # Inicializa conn como None
//     try:
//         conn = sqlite3.connect('Learn_width_me')
//         cursor = conn.cursor()

//         # Cria a tabela de usuário se não existir (apenas uma vez)
//         cursor.execute('''
//             CREATE TABLE IF NOT EXISTS usuario (
//                 id INTEGER PRIMARY KEY,
//                 nome CHAR(45),
//                 apelido CHAR(45),
//                 senha CHAR(45),
//                 telefone CHAR(45),
//                 foto CHAR(200),
//                 ID_usuario CHAR(45),
//                 curso_usuario TEXT
//             )
//         ''')
//         conn.commit() # Commit a criação da tabela

//         # Buscar o usuário pelo nome e senha
    
//         cursor.execute('SELECT nome, senha, foto, ID_usuario, curso_usuario FROM usuario WHERE nome = ? AND senha = ?', (nome, senha))
//         user_data = cursor.fetchone() # Busca apenas um resultado

//         # --- Lógica de Autenticação ---
//         if user_data:
//             # Autenticação bem-sucedida
//             # Armazena APENAS dados seguros na sessão, NUNCA a senha!
//             session['nome'] = user_data['nome']
//             session['ID_usuario'] = user_data['ID_usuario']
//             session['foto_usuario'] = user_data['foto']
//             session['curso_usuario'] = user_data['curso_usuario'] # Se precisar

//             flash(f'Bem-vindo, {user_data["nome"]}!', 'success')

//             # --- Conexões e Consultas de Outros Bancos de Dados ---
//             # Idealmente, estas operações deveriam ser carregadas conforme necessário
//             # em rotas separadas ou no template `inicio.html` via lazy loading.
//             # No entanto, para espelhar sua lógica, manterei aqui por enquanto.

//             # Conectar ao banco 'faceCurso'
//             conn_face = get_db_connection('faceCurso')
//             cursor_face = conn_face.cursor()
//             cursor_face.execute('''
//                 CREATE TABLE IF NOT EXISTS facess (
//                     id INTEGER PRIMARY KEY,
//                     nome_user CHAR(45),
//                     nome_curso CHAR(45),
//                     link_facebook CHAR(200),
//                     link_whatsapp CHAR(200),
//                     imagem_curso CHAR(200)
//                 )
//             ''')
//             conn_face.commit()
//             faceObter = cursor_face.execute('SELECT nome_user, nome_curso, link_facebook, link_whatsapp, imagem_curso FROM facess ORDER BY nome_curso ASC;').fetchall()
//             close_db_connection(conn_face)

//             # Conectar ao banco 'short'
//             conn_short = get_db_connection('short')
//             cursor_short = conn_short.cursor()
//             cursor_short.execute('''
//                 CREATE TABLE IF NOT EXISTS short (
//                     id INTEGER PRIMARY KEY,
//                     nome CHAR(45),
//                     whatsApp CHAR(200),
//                     short CHAR(200),
//                     texto CHAR(200)
//                 )
//             ''')
//             conn_short.commit()
//             obterListaShort = cursor_short.execute('SELECT nome, whatsApp, short, texto FROM short ORDER BY nome ASC;').fetchall()
//             close_db_connection(conn_short)

//             # Conectar ao banco de dados de chat do usuário
//             user_chat_db_name = f'{user_data["nome"]}_{user_data["ID_usuario"]}'
//             conn_chat = get_db_connection(user_chat_db_name)
//             cursor_chat = conn_chat.cursor()
//             cursor_chat.execute('''
//                 CREATE TABLE IF NOT EXISTS userChat (
//                     id INTEGER PRIMARY KEY,
//                     nome CHAR(45),
//                     foto CHAR(100)
//                 )
//             ''')
//             conn_chat.commit()
//             obterChat = cursor_chat.execute('SELECT nome, foto FROM userChat ORDER BY nome ASC;').fetchall()
//             close_db_connection(conn_chat)

//             # Conectar ao banco de dados de dados do usuário (sujeito.dados)
//             sujeito_db_name = f'{user_data["nome"]}_{user_data["ID_usuario"]}.dados'
//             conn_sujeito = get_db_connection(sujeito_db_name)
//             cursor_sujeito = conn_sujeito.cursor()
//             cursor_sujeito.execute(f'''
//                 CREATE TABLE IF NOT EXISTS {user_data["nome"]}_{user_data["ID_usuario"]}_table (
//                     id INTEGER PRIMARY KEY,
//                     nome_remitente CHAR(45),
//                     imagem_destinatario CHAR(100)
//                 )
//             ''')
//             conn_sujeito.commit()
//             obter3 = cursor_sujeito.execute(f'SELECT nome_remitente, imagem_destinatario FROM {user_data["nome"]}_{user_data["ID_usuario"]}_table;').fetchall()
//             close_db_connection(conn_sujeito)

//             # Conectar ao banco de dados de amigos do usuário (sujeito_FRIEND)
//             conn_friend = get_db_connection(f'{user_data["nome"]}_{user_data["ID_usuario"]}_FRIEND')
//             cursor_friend = conn_friend.cursor()
//             cursor_friend.execute(f'''
//                 CREATE TABLE IF NOT EXISTS {user_data["nome"]}_{user_data["ID_usuario"]}_tabela_conversa (
//                     id INTEGER PRIMARY KEY,
//                     nome_destinatario CHAR(45),
//                     nome_sala CHAR(45),
//                     foto CHAR(100),
//                     menssagem CHAR(45)
//                 )
//             ''')
//             conn_friend.commit()
//             OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {user_data["nome"]}_{user_data["ID_usuario"]}_tabela_conversa;').fetchall()
//             close_db_connection(conn_friend)

//             # Conectar ao banco de dados de números (sujeito.numero)
//             conn_numero = get_db_connection(f'{user_data["nome"]}_{user_data["ID_usuario"]}.numero')
//             cursor_numero = conn_numero.cursor()
//             cursor_numero.execute(f'''
//                 CREATE TABLE IF NOT EXISTS {user_data["nome"]}_{user_data["ID_usuario"]}_numero (
//                     id INTEGER PRIMARY KEY,
//                     nome CHAR(45),
//                     contador CHAR(100)
//                 )
//             ''')
//             conn_numero.commit()
//             listaNumero = cursor_numero.execute(f'SELECT id FROM {user_data["nome"]}_{user_data["ID_usuario"]}_numero').fetchall()
//             novo = 0
//             if listaNumero:
//                 vetor_numerico = [v['id'] for v in listaNumero]
//                 novo = max(vetor_numerico)
//             close_db_connection(conn_numero)

//             # Conectar ao banco de dados de SMS (sujeito_SMS)
//             conn_sms = get_db_connection(f'{user_data["nome"]}_{user_data["ID_usuario"]}_SMS')
//             cursor_sms = conn_sms.cursor()
//             cursor_sms.execute(f'''
//                 CREATE TABLE IF NOT EXISTS {user_data["nome"]}_{user_data["ID_usuario"]}_sms (
//                     id INTEGER PRIMARY KEY,
//                     destinatario CHAR(45),
//                     contador CHAR(45)
//                 )
//             ''')
//             conn_sms.commit()
//             obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {user_data["nome"]}_{user_data["ID_usuario"]}_sms;').fetchall()
//             v_sms = [sms['id'] for sms in obterSMS]
//             nome_sms = [sms['destinatario'] for sms in obterSMS]
//             z_sms = len(v_sms)
//             close_db_connection(conn_sms)

//             # Conectar ao banco de dados de DENUNCIAS
//             conn_denuncias = get_db_connection('DENUNCIAS')
//             cursor_denuncia = conn_denuncias.cursor()
//             cursor_denuncia.execute('''
//                 CREATE TABLE IF NOT EXISTS denuncia (
//                     id INTEGER PRIMARY KEY,
//                     sujeito CHAR(45),
//                     remitente CHAR(45),
//                     descricao CHAR(100)
//                 )
//             ''')
//             conn_denuncias.commit()
//             obter_denuncias = cursor_denuncia.execute('SELECT remitente, sujeito, descricao FROM denuncia ORDER BY id ASC;').fetchall()
//             close_db_connection(conn_denuncias)

//             # Se a autenticação foi bem-sucedida, redireciona para a página de início
//             return render_template(
//                 'inicio.html',
//                 b=user_data['foto'], # sua variável 'b'
//                 n=user_data['nome'], # sua variável 'n'
//                 faceObter=faceObter,
//                 obterListaShort=obterListaShort,
//                 obterAmigos=cursor.execute('SELECT nome, foto, id, ID_usuario FROM usuario ORDER BY nome ASC;').fetchall(), # Recarrega lista de amigos
//                 codigo_usuario=user_data['ID_usuario'],
//                 obterChat=obterChat,
//                 obter3=obter3,
//                 sujeito=user_chat_db_name, # Ou sujeito_db_name, dependendo de qual você quer passar
//                 OBTER_LISTA_EMITENTE=OBTER_LISTA_EMITENTE,
//                 novo=novo,
//                 z=z_sms, # z para SMS
//                 nome_sms=nome_sms, # nome para SMS
//                 obter_denuncias=obter_denuncias,
//                 obter=cursor.execute('SELECT nome, senha, foto, ID_usuario, curso_usuario FROM usuario ORDER BY nome ASC;').fetchall() # Sua lista 'obter' original
//             )

//         # Caso de login "Avelino" e senha "422517Usuario"
//         elif nome == 'Avelino' and senha == '422517Usuario':
//             flash('Login de Administrador Avelino bem-sucedido!', 'info')
//             conn_admin = get_db_connection('Learn_width_me')
//             cursor_admin = conn_admin.cursor()
//             lista_admin = cursor_admin.execute('SELECT nome, apelido, telefone, foto FROM usuario ORDER BY nome ASC;').fetchall()
//             close_db_connection(conn_admin)
//             return render_template('usuario_cadastrado_na_Learn_To_Me.html', obter=lista_admin)

//         else:
//             # Falha na autenticação
//             flash('Nome de usuário ou senha inválidos!', 'danger')
//             return render_template('index.html')

//     except Exception as e:
//         flash(f'Ocorreu um erro: {e}', 'danger')
//         print(f"Erro na rota logar: {e}") # Para depuração
//         return render_template('index.html')
//     finally:
//         close_db_connection(conn) # Garante que a conexão principal seja fechada











// É bastante difícil determinar com certeza se um programador trabalhou sozinho ou em equipe apenas olhando para a interface. No entanto, podemos fazer algumas inferências baseadas na complexidade e polidez do projeto:

// Argumentos que poderiam sugerir um trabalho em equipe:

// Polimento e Detalhe: A interface é bastante limpa, consistente e tem um bom apelo visual. Em projetos maiores e mais polidos, é comum ter um designer de UI/UX dedicado ou alguém com forte aptidão para isso, o que nem sempre é o foco principal de um programador que trabalha sozinho.
// Amplitude de Funcionalidades: A interface apresenta diversas funcionalidades: navegação (menu lateral), busca, exibição de vídeos, perfil de usuário, "Cursos Grátis", e até opções como "alugar uma sala", "denunciar alguém", "Melhorar a Escola", "Adicionar amigo" e "Administrador". Implementar e integrar todas essas funcionalidades (incluindo o backend por trás delas) com um alto nível de qualidade pode ser um desafio significativo para uma única pessoa, mesmo um desenvolvedor sênior.
// Divisão de Especialidades (Frontend/Backend): Como mencionei anteriormente, a qualidade do frontend é alta, e as funcionalidades sugerem um backend robusto. Embora um desenvolvedor fullstack possa fazer ambos, é comum que em projetos maiores e mais complexos haja uma divisão de trabalho entre especialistas em frontend e backend.
// Opção "Administrador": A presença de uma opção "Administrador" no menu lateral sugere que o sistema foi projetado para ter diferentes níveis de usuário e gerenciamento de conteúdo, o que muitas vezes é um sinal de um projeto com escopo maior, que pode envolver uma equipe.
// Argumentos que poderiam sugerir um trabalho individual (menos provável, mas possível):

// Pequeno Projeto/MVP: Se este for um MVP (Minimum Viable Product) ou um projeto pessoal, é totalmente possível que um desenvolvedor fullstack muito competente e com bom senso estético tenha construído tudo sozinho.
// Ferramentas e Frameworks Modernos: Com frameworks como React, Vue, Angular (para frontend) e Node.js, Python/Django/Flask, Ruby on Rails (para backend), um único desenvolvedor pode ser bastante produtivo e criar interfaces complexas com relativa eficiência.
// Conclusão:

// Minha intuição, baseada na complexidade e no nível de polimento da interface, me inclina a pensar que é mais provável que tenha havido algum tipo de colaboração, ou que pelo menos um desenvolvedor Fullstack altamente experiente e com fortes habilidades de design tenha trabalhado no projeto.

// Um único programador (mesmo sênior) trabalhando sozinho conseguiria entregar algo assim, mas exigiria um tempo considerável e uma ampla gama de habilidades em design, frontend e backend, além de gerenciamento de banco de dados e possivelmente infraestrutura. A presença de "keepvid music" no canto superior esquerdo (se for parte do projeto e não um artefato de captura de tela) também pode indicar um logo ou marca que seria mais comum em um projeto com uma visão mais ampla, talvez de uma empresa ou um grupo.




// 974484650 aluno Adilson
// 941742188 josé

