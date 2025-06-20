

function cadastro(){

    location = "cadastro"

}

function conversar(){


    alert('esta a funcionar nesta aba!')


}

let contador = 0
let texto = "Learn width Me"
function digitar(){

    if (contador<texto.length){

        document.getElementById('meuTitulo').innerHTML += texto.charAt(contador)
        contador++
        setTimeout(digitar,90)

    }
  

}

digitar()