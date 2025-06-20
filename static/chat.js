



function conversa(sujeit) {


    // const messagesDiv = document.getElementById('menssagens').innerHTML = "";
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const roomInput = document.getElementById('room-input');
    const usernameInput = document.getElementById('username-input');
    const joinRoomButton = document.getElementById('join-room-button');
    const typingIndicator = document.getElementById('typing-indicator');
    let novo_chat = document.querySelector('.novo_chat').style.display = "flex"
    let textoChat = document.getElementById('textoChat')
    let ponto = document.querySelectorAll('.ponto')

   

    

    

    
    let username = document.getElementById('n').innerHTML;
    let divPai = sujeit.parentElement;
    let amigoElement = divPai.querySelector('.amigo');
    let sala = divPai.querySelector('#sala').innerHTML
    let destinatario = amigoElement.innerHTML;
    let fullRoon = sala
    textoChat.innerHTML = amigoElement.innerHTML
    let nome_remitente = document.getElementById('n').innerHTML
    let nome_destinatario = destinatario

    c = ponto.length
    v = Number(c)
    for (t=0;t<v;t++){

        if(ponto[t].innerHTML === "None"){
      
        }
        else if(ponto[t].innerHTML!=="None" && destinatario){
            let b = divPai.querySelector('.ponto').style.display = "none"
        }

    }


    socket.emit('visto',{nome_remitente:nome_remitente,nome_destinatario:nome_destinatario})


    
    let meuLindoChatDiv = document.querySelector('.meuLindoChat');
    let chatDiv = document.querySelector('.chat');
    let meuChatDiv = document.querySelector('.meuChat');
    let sujeitoElement = document.getElementById('sujeito');
    let receberElement = document.getElementById('receber');
    let destinoElement = document.getElementById('destinatario');
    let userChatElement = document.getElementById('userChat');
        const messagesDivs = document.getElementById('menssagens');
        messagesDivs.innerHTML = ""

    socket.emit('join', { room: fullRoon, user: username });


    currentRoom = fullRoon;
   

    if (meuLindoChatDiv) meuLindoChatDiv.style.display = "none";
    if (chatDiv) chatDiv.style.display = "flex";
    if (meuChatDiv) meuChatDiv.style.display = "none";
    if (sujeitoElement) sujeitoElement.innerHTML = destinatario;
    if (receberElement) receberElement.innerHTML = destinatario;
    if (destinoElement) destinoElement.innerHTML = destinatario; 
    if (userChatElement) userChatElement.innerHTML = destinatario;


// (${msg.timestamp})


        const messagesDiv = document.getElementById('menssagens').innerHTML = ""
        socket.once('carregar_mensagenss', (data) => {
        const messagesDiv = document.getElementById('menssagens')
        let username = document.getElementById('n').innerHTML
        data.messages.forEach(msg => {
        
   
            const messageElement = document.createElement('p');
            const div = document.createElement('div')
            messageElement.innerHTML = `${msg.text}`;
            div.textContent = `${msg.timestamp}`

            
            if (msg.sender == username) {
                messageElement.classList.add('mim');
                div.classList.add('mim')
                messagesDiv.appendChild(messageElement);
                
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
                    document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
            }
            else{
                messageElement.classList.add('ele');
                div.classList.add('ele')
                messagesDiv.appendChild(messageElement);
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
                 document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
            }
            
        });
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
    });

    socket.on('new_message', (data) => {
        const messagesDiv = document.getElementById('menssagens')
        let username = document.getElementById('n').innerHTML
        const messageElement = document.createElement('p');
        messageElement.textContent = `${data.text}`;
            let subSMS = document.querySelector('.subSMS')
            let recebere = document.getElementById('subSMS')
            let textoChat = document.querySelector('#textoChat').innerHTML

            valore = Number(recebere.innerHTML)
            subSMS.innerHTML = Number(subSMS.innerHTML) + 1



            socket.emit('nova__menssagem',{contador:subSMS.innerHTML, nome_destinatario:textoChat,nome_remitente:username})
          
            
        if (data.sender == username) {
            messageElement.classList.add('mim');
            messagesDiv.appendChild(messageElement);
            document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
            subSMS.style.display = "none"
            subSMS.innerHTML = 0
            
                        
        }
        else{
            messageElement.classList.add('ele');
            messagesDiv.appendChild(messageElement);
            document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
            subSMS.style.display = "flex"
            document.querySelector('.ponto').style.display = "flex"
          
        

        }
        
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
         document.querySelector('.menssagens').scrollTop = document.querySelector('.menssagens').scrollHeight
    });
    let userChat = document.getElementById('textoChat')
    novo = userChat.innerHTML
    messageInput.addEventListener('input', () => {
        isTyping = false
        if (messageInput.value !=="" && !isTyping) {
            
            socket.emit('typing', { room: currentRoom, user: username });
            isTyping = true;
        } else if (messageInput.value.trim() && isTyping) {
            userChat.innerHTML = ""
            socket.emit('stop_typing', { room: currentRoom, user: username });
            isTyping = false;
            
            
        }
         if (messageInput.value == ""){

           
            socket.emit('stop_typing', { room: currentRoom, user: username });
            isTyping = false;

            

         }
    });

    socket.on('user_typing', (data) => {
        if (data.user !== username && data.room === currentRoom) {
            let userChat = document.getElementById('textoChat')
            
         

            userChat.innerHTML = (messageInput.value == "" ? `${data.user} <b>está digitando...</b>`:`${data.user} <b>está digitando...</b>`)
           





            
           
        }
    });


    socket.on('user_stopped_typing', (data) => {
        if (data.user !== username && data.room === currentRoom) {
            let userChat = document.getElementById('textoChat')
            userChat.innerHTML = novo
            
           
           
        }
    });



    messageInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            sendButton.click();
            event.preventDefault();
        }
    });

    window.addEventListener('beforeunload', () => {
        if (currentRoom && username) {
            socket.emit('leave', { room: currentRoom, user: username });
        }
    });







  }



  
  function enviar(){

    const messagesDiv = document.getElementById('menssagens');
    let username = document.getElementById('n').innerHTML;
    let message = document.getElementById("message-input").value
    let nome_destinatario = document.getElementById('textoChat')
    let subSMS = document.querySelector('.subSMS')    
    document.querySelector('.menssagens').scrollHeight = document.querySelector('.menssagens').scrollTop
    let imagem = ''
    document.querySelector('.input').value = ""
    sala = ""
    



  
    if (message && currentRoom && username) {
        socket.emit('message', { room: currentRoom, message: message, sender: username });
        socket.emit('menssagem_em_tempo_real', { nome_destinatario:nome_destinatario.innerHTML, message: message, nome_remitente: username });

        message.value = "";
        messageInput = "";
        socket.emit('stop_typing', { room: currentRoom, user: username });
        isTyping = false;
    }
  


}
let x = document.querySelectorAll('.ponto')
c = x.length
v = Number(c)

for(t=0;t<v;t++){

    if(x[t].innerHTML === "None"){
        x[t].style.display = "none"
    }


}
// const socket = io.connect('http://' + document.domain + ':' + location.port);


