const rabbit = document.querySelector(".rabbit");
const message = document.querySelector("#rabbit-message");

rabbit.addEventListener("click", () => {
    rabbit.classList.add("hop");
    message.textContent = "The hare got away! 🐇";
    setTimeout(() => rabbit.classList.remove("hop"), 350);
});
