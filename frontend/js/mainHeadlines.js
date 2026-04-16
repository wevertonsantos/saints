const divMainHeadlines = document.querySelector(".main-headlines")

export const mainHeadlines = () => {
    const divMainImg = document.createElement("div")
    const divTwoImgs = document.createElement("div")
    const divTopHeadlines = document.createElement("div")
    const div4 = document.createElement("div")

    divMainImg.classList.add("main-img")
    divTwoImgs.classList.add("two-imgs")
    divTopHeadlines.classList.add("top-headlines")

    addItems(divMainImg,divTwoImgs,divTopHeadlines,)
    
    divMainHeadlines.appendChild(divMainImg)
    divMainHeadlines.appendChild(divTwoImgs)
    divMainHeadlines.appendChild(divTopHeadlines)
}

const addItems = (divMainImg, divTwoImgs, divTopHeadlines) => {
    const addImg = (div,attribute, imgClass, url) => {
        const link = document.createElement("a")
        const img = document.createElement("img")
        link.setAttribute("href", attribute)
        div.appendChild(link)
        img.classList.add(imgClass)
        link.appendChild(img)
        img.setAttribute("src", url)
    }
       
    addImg(divMainImg, "#", "img-1", "../assets/handontablets.jpg")
    
    for (let i = 0; i < 2; i++){
        if (i == 0) {
            addImg(divTwoImgs, "#", "img-2", "../assets/handontablets.jpg")
        } else {
            addImg(divTwoImgs, "#", "img-3", "../assets/handontablets.jpg")
        }
    }

    for (let i = 0; i < 11; i++) {
        const item = document.createElement("li")
        const h2 = document.createElement("h2")
        const p = document.createElement("p")
        const text = document.createTextNode("Principais Manchetes")
        const headline = document.createTextNode("YouTube livestreams will now hold back ads during peak engagement to protect the vibe")

        if (i == 0) {
            divTopHeadlines.appendChild(h2)
            h2.classList.add("text")
            h2.appendChild(text)
        } else {
            divTopHeadlines.appendChild(item)
            item.classList.add("headline")
            item.classList.add(`${i}`)
            item.appendChild(p)
            p.appendChild(headline)
        }
    }

}