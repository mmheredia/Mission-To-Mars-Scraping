# Web Scraping Challenge

---

This project consisted of building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

---

## Scraping

1. The first website scraped was: https://redplanetscience.com/ 
   This website was scraped for the latest news title and paragraph text. 

2. The second website scraped was: https://spaceimages-mars.com/
This website was scraped for the current featured image.

3. The third website scraped was: https://galaxyfacts-mars.com/
This website was scraped for the table containing facts about the planet, including diameter, mass, et.

4. The fourth and last website scraped was: https://marshemispheres.com/
This website was scraped for the high resolution images for each of Mars' hemispheres.

## MongoDB and Flask Application

After scraping, MongoDB with Flask templating was used to create a new HTML webpage that displayes all of the scraped information. 