const divMainHeadlines = document.querySelector(".main-headlines")

export const mainHeadlines = () => {
    const list = document.createElement("ul")
    const list2 = document.createElement("ul")

    list.classList.add("images")
    list2.classList.add("top-headlines")

    addItems(list,list2)
    
    divMainHeadlines.appendChild(list)
    divMainHeadlines.appendChild(list2)
}

const addItems = (list,list2) => {    
    for (let i = 0; i < 3; i++){
        const item = document.createElement("li")
        const link = document.createElement("a")
        const img = document.createElement("img")
        
        list.appendChild(item)
        link.setAttribute("href","#")
        item.appendChild(link)
        link.appendChild(img)

        if (i == 0) {
            item.classList.add("img-1")
            img.classList.add("main-img")
            img.setAttribute("src", "../assets/handontablets.jpg")
        } else if (i == 1) {
            item.classList.add("img-2")
            img.classList.add("second-img")
            img.setAttribute("src","../assets/handontablets.jpg")
        } else {
            item.classList.add("img-3")
            img.classList.add("third-img")
            img.setAttribute("src","../assets/handontablets.jpg")
        }
    }

    for (let i = 0; i < 11; i++) {
        const item = document.createElement("li")
        const h2 = document.createElement("h2")
        const p = document.createElement("p")
        const text = document.createTextNode("Principais Manchetes")
        const headline = document.createTextNode("YouTube livestreams will now hold back ads during peak engagement to protect the vibe")

        if (i == 0) {
            list2.appendChild(h2)
            h2.classList.add("text")
            h2.appendChild(text)
        } else {
            list2.appendChild(item)
            item.classList.add("headline")
            item.classList.add(`${i}`)
            item.appendChild(p)
            p.appendChild(headline)
        }
    }
}