const elementMainHeadlines = document.querySelector(".main-headlines")

export const mainHeadlines = () => {
    const list = document.createElement("ul")
    list.classList.add("items")
    items(list)
    elementMainHeadlines.appendChild(list)
}

const items = (list) => {
    for (let i = 0; i < 3; i++){
        const item = document.createElement("li")
        list.appendChild(item)
        const link = document.createElement("a")
        link.setAttribute("href","#")
        item.appendChild(link)
        const img = document.createElement("img")
        link.appendChild(img)

        if (i == 0) {
            img.classList.add("main-img")
            img.setAttribute("src","../assets/handontablets.jpg")
        }
    }    
}