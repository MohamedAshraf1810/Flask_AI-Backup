var loader = document.getElementById("preloader");
window.addEventListener("load" , function()
{
  setTimeout(() =>
  {
    loader.style.display="none";
  },1000);
})


const recordAudio = () =>
  new Promise(async (resolve) => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    let audioChunks = [];

    mediaRecorder.addEventListener("dataavailable", (event) => {
      audioChunks.push(event.data);
    });

    const start = () => {
      audioChunks = [];
      mediaRecorder.start();
    };

    const stop = () =>
      new Promise((resolve) => {
        mediaRecorder.addEventListener("stop", () => {
          const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          const play = () => audio.play();
          resolve({ audioChunks, audioBlob, audioUrl, play });
        });
        mediaRecorder.stop();
      });

    resolve({ start, stop });
  });

const sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
const recordButton = document.querySelector("#record");
const stopButton = document.querySelector("#stop");
const audioPlayer = document.querySelector("#AudioPlayer");
const recGif = document.querySelector(".recGif")
const authButton = document.querySelector("#facebtn");

let recorder;
let audio;

recordButton.addEventListener("click", async () => {
  console.log("Record Started");
  recordButton.setAttribute("disabled", true);
  recGif.setAttribute("style","display:inline" );
  recordButton.setAttribute("style", "background-color: #d6d6cd ; color: white; cursor: default"); 
  stopButton.setAttribute("style", "background-color: #88acce ; color: black; cursor: pointer"); 
  stopButton.removeAttribute("disabled");
  if (!recorder) {
    recorder = await recordAudio();
  }
  recorder.start();
});


stopButton.addEventListener("click", async () => {
  console.log("Record Stoped");
  recordButton.removeAttribute("disabled");
  stopButton.setAttribute("disabled", true);
  recGif.setAttribute("style","display:none" );
  recordButton.setAttribute("style", "background-color: #88acce ; color: black; cursor: pointer"); 
  stopButton.setAttribute("style", "background-color: #d6d6cd ; color: white; cursor: default"); 
  audio = await recorder.stop();
  audioPlayer.removeAttribute("display");
  audioPlayer.setAttribute("src" , audio.audioUrl);

  const reader = new FileReader();
  reader.readAsDataURL(audio.audioBlob);
  reader.onload = function () {
    base64Audio = reader.result;
  };
});


authButton.addEventListener("click", async()=>{
  console.log(base64Audio);
})