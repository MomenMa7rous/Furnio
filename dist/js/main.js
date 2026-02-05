// Nav Menu
let navMenuBtn = document.getElementById("navMenuBtn")
let navMenu = document.getElementById("navMenu")
let navCloseBtn = document.getElementById("navCloseBtn")
let overlay = document.getElementById("overlay")

document.addEventListener("click", (ev) => {
    if ([navMenuBtn, navCloseBtn].includes(ev.target)) {
        navMenu.classList.toggle("-translate-x-full")
        overlay.classList.toggle("translate-x-full")
    }
})