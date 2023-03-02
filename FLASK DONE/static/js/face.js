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
  console.log("CAMERA BEFORE START");
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
    fetch('http://192.168.1.11:8000/faceAuthCheck',{
    method : "POST",
    headers : {
      'X-CSRFToken':csrftoken,
    },
    data :
    {
      'image':myImage,
    },
  }).then(response => response.text())
  .then(result => console.log(result))
  .catch(e=>console.log(e))
};


// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
