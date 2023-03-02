var loader = document.getElementById("preloader");
window.addEventListener("load" , function()
{
    setTimeout(() =>
    {
      loader.style.display="none";
      
    },1000);
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

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    myImage = cameraSensor.toDataURL("image/png");
    console.log(myImage);

    var xhr = new XMLHttpRequest();
    xhr.open('POST','/uploadimage',true);
    xhr.setRequestHeader('Content-Type','application/json');
    xhr.send(JSON.stringify({image:myImage}))
};


// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
