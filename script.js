const rabbit = document.querySelector(".rabbit");
const message = document.querySelector("#rabbit-message");

let messageTimer;

rabbit.addEventListener("click", () => {
    rabbit.classList.add("hop");
    message.textContent = "The hare got away! 🐇";

    clearTimeout(messageTimer);
    messageTimer = setTimeout(() => {
        message.textContent = "";
    }, 3000);

    setTimeout(() => rabbit.classList.remove("hop"), 350);
});

rabbit.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        rabbit.click();
    }
});
