var On_Neuron = document.getElementById("On_Neuron")
var output = document.getElementById("output")

var Microfone_Ligado = false

function On_Microfone(){
    if (!('webkitSpeechRecognition' in window)) {
        alert("Seu navegador não suporta a Web Speech API. Tente usar o Google Chrome.");
    }else{
    const recognition = new webkitSpeechRecognition();
  
    recognition.lang = "pt-BR"; 
    recognition.continuous = true; 
    recognition.interimResults = true; 
  
    recognition.onresult = (event) => {
      let transcript = "";
      for (let i = event.resultIndex; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
      }
      output.innerText = transcript;
      $.ajax({
        url:"/Voice",
        type:"POST",
        contentType: 'application/json',
        data:JSON.stringify({
            "Voz":transcript  
        })
      })
    };
  
    recognition.start();
  
    console.log("Reconhecimento de fala iniciado!");


    }
}

On_Neuron.addEventListener("click",function(){
    if(Microfone_Ligado == false){
        On_Neuron.style.border = "1vh solid green"
        On_Microfone()
        console.log("Microfone Ligado");
        Microfone_Ligado = true
    }
    else if(Microfone_Ligado == true){
        On_Neuron.style.border = "0vh"
        Microfone_Ligado = false
        console.log("Microfone Desligado");
        output.innerText = ""
    }
})

function Ligar(){
  $.ajax({
    url:"/YggDrasil",
    type:"GET",
    contentType: 'application/json'
  })
}