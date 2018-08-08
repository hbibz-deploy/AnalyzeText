/*let textArea = document.querySelector("#InputText")
console.log(textArea)*/
//var $ = jQuery;
var socket = io.connect('http://127.0.0.1:5000');
socket.on('connect', () => {
    socket.send('User connected');
});

var delay = (function(){
    var timer = 0;
    return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
   };
})();

textArea = $("#InputText")
$(textArea).on("keyup", () => {
    delay(()=>{
        socket.send(textArea.val())
    }, 2000);
})

socket.on("message", (msg) => {
    console.log(msg);
    $('#result').html("HeadLine Results: "+msg['headline_results']
                    +"<br>"+"Sentiment: "+parseFloat(msg['sentiment']).toFixed(4)
                    +"<br>"+"Subjectivity: "+parseFloat(msg['subjectivity'])).toFixed(4);
})