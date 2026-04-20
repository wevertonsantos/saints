import { fetchNews } from "../services/api.js"
import { showLogo } from "../components/logo.js"
import { mainHeadlines } from "../components/mainHeadlines.js"

const home = async () => {
    const news = await fetchNews()
    showLogo()
    mainHeadlines(news)
}

home()