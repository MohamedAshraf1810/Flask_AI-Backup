var loader = document.getElementById("preloader");
var auth = document.getElementById("authbtn");
window.addEventListener("load" , function()
{
    setTimeout(() =>
    {
      loader.style.display="none";
      
    },1);
})


// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };

// Define constants
const cameraView = document.querySelector("#videoElement"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#CANVAS"),
    cameraTrigger = document.querySelector("#facebtn")

// Access the device camera and stream to cameraView
function cameraStart() {
  navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function(stream) {
      track = stream.getTracks()[0];
      cameraView.srcObject = stream;
  })
  .catch(function(error) {
      console.error("Oops. Something is broken.", error);
  });
}

var x = false;

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() 
{
    document.getElementById("authenticationLoader").setAttribute('style','display:flex;');
    cameraSensor.width = cameraView.videoWidth;
        cameraSensor.height = cameraView.videoHeight;
        cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
        myImage = cameraSensor.toDataURL("image/png");
        console.log(myImage);
    
        var xhr = new XMLHttpRequest();
        xhr.open('POST','/uploadimage',true);
        xhr.setRequestHeader('Content-Type','application/json');
    setTimeout(() =>
    {
        xhr.onload = () => 
        {
            MyResponse = xhr.response;
            console.log( "My_Response is : ",MyResponse);
            console.log("type of my response ",typeof (MyResponse));
            console.log("***********************");
    
            if (MyResponse == 'True')
            {
                console.log("Type ",typeof(MyResponse));
                console.log("Tmaam Response :",MyResponse);
                window.open("http://192.168.1.11:5000/voiceAuth",'_self')
            }
            else
            {
                console.log("Type ",typeof(MyResponse));
                console.log("Me4 Tmaam response :",MyResponse);
                window.open("http://192.168.1.11:5000/",'_self')
            }
    
        };
        xhr.send(JSON.stringify({image:myImage}))
    },500);
    

};

// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
