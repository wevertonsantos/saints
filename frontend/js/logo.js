const logo = document.querySelector(".logo")

export const showLogo = () => {
    const title = document.createElement("h1")
    const link = document.createElement("a")
    const text = document.createTextNode("Saints")
    logo.appendChild(title)
    title.classList.add("text")
    title.appendChild(link)
    link.appendChild(text)
    link.setAttribute("href", "home.html")
};