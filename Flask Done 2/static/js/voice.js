
        var loader = document.getElementById("preloader");
        window.addEventListener("load" , function()
        {
            setTimeout(() =>
            {
              loader.style.display="none";
            },1000);
        })
        function PopUpclose(){
             window.location.href = 'index.html' ;
        }

        if (navigator.mediaDevices.getUserMedia)
          {
            navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function (stream)
            {

            })
            .catch(function (error)
            {
              console.log("Something went wrong!");
            });
          }