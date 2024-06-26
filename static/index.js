let socket = io();

const btn = document.querySelector(".socket-btn");
btn.addEventListener("click", function() {
    const input = document.querySelector(".flask-input");
    socket.emit("change number", input.value);
});

socket.on("update value", function(data) {
    const val = document.querySelector(".db-num");
    val.innerText = data;
});

// ISSUE: if I change via socket first thing, the change works
// It does NOT work if I change "directly" with request.get, then with socket. Not
// that I will implement it this way, but just a note to self
// socket.on("refresh page", function() {
//     location.reload();
// });