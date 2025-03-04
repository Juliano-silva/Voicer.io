function Microfone(Ligado){
    document.getElementById("Microfone").innerHTML = ""
    if(Ligado){
        const recognition = new webkitSpeechRecognition();

        recognition.lang = "pt-BR"
        recognition.continuous = true
        recognition.interimResults = true
    
        recognition.onresult = (event) => {
            let transcript = ""
    
            for(let i = event.resultIndex; i < event.results.length; i++){
                transcript += event.results[i][0].transcript
            }
    
            document.getElementById("Microfone").innerHTML = transcript
            $.ajax({
                url:"/Main_Microfone",
                type:"POST",
                contentType: 'application/json',
                data: JSON.stringify({"Value":transcript})
            })
        }
    
        recognition.start();
        document.getElementById("Main").style.borderColor = "green"
    }
    else{
        document.getElementById("Main").style.borderColor = "red"
    }
}

var Alavanca = true

document.getElementById("Main").addEventListener("click",function(){
    if(Alavanca){
        console.log("Microfone Off");
        Alavanca = false
    }else{
        console.log("Microfone On");
        Alavanca = true
    }    

    Microfone(Alavanca)
})