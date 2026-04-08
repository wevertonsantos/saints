const sectionMainHeadlines = document.querySelector(".main-headlines")

export const mainHeadlines = () => {
    const list = document.createElement("ul")

    list.classList.add("items")

    items(list)
    
    sectionMainHeadlines.appendChild(list)
}

const items = (list) => {
    for (let i = 0; i < 3; i++){
        const item = document.createElement("li")
        const link = document.createElement("a")
        const img = document.createElement("img")

        list.appendChild(item)
        link.setAttribute("href","#")
        item.appendChild(link)
        link.appendChild(img)

        if (i == 0) {
            img.classList.add("main-img")
            img.setAttribute("src", "../assets/handontablets.jpg")
        } else if (i == 1) {
            img.classList.add("second-img")
            img.setAttribute("src","../assets/handontablets.jpg")
        } else {
            img.classList.add("third-img")
            img.setAttribute("src","../assets/handontablets.jpg")
        }
    }
}