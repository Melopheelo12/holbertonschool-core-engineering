const socket = new WebSocket("ws://localhost:8000/ws");

const messages = document.getElementById("messages");
const input = document.getElementById("messageInput");
const button = document.getElementById("sendButton");


socket.onopen = () => {
    addMessage("Connected");
};


socket.onmessage = (event) => {
    addMessage(event.data);
};


socket.onclose = () => {
    addMessage("Disconnected");
};


button.onclick = () => {
    const message = input.value;

    if (message) {
        socket.send(message);
        input.value = "";
    }
};


function addMessage(message) {
    const div = document.createElement("div");
    div.textContent = message;
    messages.appendChild(div);
}