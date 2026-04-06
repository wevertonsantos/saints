const navbar = document.querySelector(".navbar")
const text = document.querySelector(".text")

export const fixedMenu = () => {
    // se eu for para baixo
    window.addEventListener('scroll', () => {
        if (scrollY >= 67) {
            //navbar.style.position = "fixed";
            //text.style.display = "none"
        }
    })
    // menu fica fixo
    // some Saints
    // Saints aparece na navbar items
}