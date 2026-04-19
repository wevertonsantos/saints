const divMainHeadlines = document.querySelector(".main-headlines")

export const mainHeadlines = (news) => {
    const divImages = document.createElement("div")
    const divTopHeadlines = document.createElement("div")

    divImages.classList.add("images")
    divTopHeadlines.classList.add("top-headlines")

    addItems(divImages,divTopHeadlines,news)
    
    divMainHeadlines.appendChild(divImages)
    divMainHeadlines.appendChild(divTopHeadlines)
}

const addItems = (divImages,divTopHeadlines,news) => {
    const addImg = (divImages,attribute, imgClass,linkClass, url) => {
        const link = document.createElement("a")
        const img = document.createElement("img")
        link.classList.add(linkClass)
        link.setAttribute("href", attribute)
        divImages.appendChild(link)
        img.classList.add(imgClass)
        link.appendChild(img)
        img.setAttribute("src", url)
    }
    
    for (let i = 1; i <= 3; i++){
        if (i == 1) {
            addImg(divImages, "#", `img-${i}`, 'main-img', "../assets/handontablets.jpg")
        } else if (i == 2) {
            addImg(divImages, "#", `img-${i}`,'second-img', "../assets/handontablets.jpg")
        } else {
            addImg(divImages, "#", `img-${i}`,'third-img', "../assets/handontablets.jpg")
        }
    }

    for (let i = 0; i < news.length; i++) {
        const item = document.createElement("li")
        const link = document.createElement("a")
        const square = document.createElement("div")
        const p = document.createElement("p")
        const headline = document.createTextNode(news[i]['title'])

        if (i == 0) {
            const h2 = document.createElement("h2")
            const text = document.createTextNode("Principais Manchetes")
            divTopHeadlines.appendChild(h2)
            h2.classList.add("text")
            h2.appendChild(text)
        }

        divTopHeadlines.appendChild(item)
        item.classList.add("headline")
        item.classList.add(`${i}`)
        item.appendChild(link)
        link.setAttribute("href", "#")
        square.classList.add("square")
        link.appendChild(square)
        link.appendChild(p)
        p.appendChild(headline)
    }
}