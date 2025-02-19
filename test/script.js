const Borda = document.getElementById("Borda");

navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
        const audioContext = new (window.AudioContext ||
        window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        const source = audioContext.createMediaStreamSource(stream);

        source.connect(analyser);
        analyser.fftSize = 2048;
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        function Chamar() {
            requestAnimationFrame(Chamar);
            analyser.getByteTimeDomainData(dataArray);

            for (let i = 0; i < bufferLength; i++) {
                const v = dataArray[i] / 128.0;
                var widths = 50
                var heights = 50

                // if(String(v).indexOf(".") == 1){
                //     const y = String(v).split(".")[1]
                //     const separar = parseInt(y) / 10
                    
                //     widths = String(separar).slice(0,2)
                //     heights = String(separar).slice(0,2)
                // }else{
                //     widths = 50
                //     heights = 50
                // }

                
                

                Borda.style.width = widths + "vh"
                Borda.style.height = heights + "vh"
                
            }
        }

        Chamar();
    })
    .catch((err) => {
        console.error("Erro ao acessar o microfone:", err);
    });