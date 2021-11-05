# Imports
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd

def scrape_info():

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # --------------------------

    # Visit the mars news website
    mars_news_url = 'https://redplanetscience.com/'
    browser.visit(mars_news_url)

    # Scrape page into beautiful soup (bs)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the news title and paragraph
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    print(news_title, news_p)

    # --------------------------

    # Visit the images website
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)

    # Scrape the page into beautiful soup (bs)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the ltest image
    img = soup.find('img', class_='headerimage fade-in')
    rel_path = img['src']
    mars_img = jpl_url + rel_path
    mars_img

    # --------------------------

    # Visit the facts website
    mars_facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(mars_facts_url)
    
    # Use pandas to read the 'Facts about Mars' table
    table = pd.read_html(mars_facts_url)

    mars_facts_df = table[0]

    # Convert to html
    mars_facts = mars_facts_df.to_html(index=False, header=False)

    print(mars_facts)

    # --------------------------

    # Visit hemisphere website
    hem_url = 'https://marshemispheres.com/'
    browser.visit(hem_url)

    # Scrape page into beautiful soup (bs)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the hemisphere images results
    results = soup.find_all('div', class_='item')

    # Create dictionary to populate using a for loop
    hem_imgs = []

    for result in results:

        img_dict = {}
        
        item = result.find('div', class_='description')
        header = item.find('h3').text
        
        browser.links.find_by_partial_text(header).click()
        
        html_2 = browser.html
        soup_2 = bs(html_2, 'html.parser')
        
        hem_img = soup_2.find('img', class_='wide-image')
        hem_rel_path = hem_img['src']
        hem_abs_path = hem_url + hem_rel_path
        
        browser.visit(hem_url)
        
        img_dict['title'] = header
        img_dict['img_url'] = hem_abs_path
        hem_imgs.append(img_dict)

    # Store data into a dictionary
    mars_dict = {
        'news_title': news_title,
        'news_p': news_p,
        'mars_img': mars_img,
        'mars_facts': mars_facts,
        'hem_imgs': hem_imgs
    }

    browser.quit()

    return mars_dict

# if __name__ == '__main__':
#     print(scrape_info())