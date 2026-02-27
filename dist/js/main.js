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

const swiper = new Swiper('.swiper', {
    loop: true,

    pagination: {
        el: '.swiper-pagination',
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    
    autoplay: {
        delay: 5000,
    },

    slidesPerView: 1,
    spaceBetween: 10,

    breakpoints: {
        992: {
            slidesPerView: 2,
            // spaceBetween: 40
        },
        1200: {
            slidesPerView: 3,
            // spaceBetween: 40
        }
    }
});