function showMessage() {
    const message = document.getElementById("message");
    const button = document.querySelector("button");

    // Toggle the message
    if (message.textContent === "") {
        message.textContent = "You clicked the button!";
        button.setAttribute("aria-pressed", "true");
    } else {
        message.textContent = "";
        button.setAttribute("aria-pressed", "false");
    }
}
