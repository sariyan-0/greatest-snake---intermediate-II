############################# Course Project #############################
#
# Collect news articles from:
#                           https://en.mehrnews.com/
##########################################################################
from functions.my_functions import *
import os
from datetime import date
import re
import requests
# ------------------------------------------------------------------------
def make_request(section_x):
    url = f"    {section_x}"
    response = requests.get(url)
    html_data = response.text
    return html_data

def extract_news_articles(html_data_x):
    result = re.findall(
        r'<h3><a href="/\w{1,}/\d{6}/\S{1,}" target="_blank">.{1,}</a>',
        html_data_x
    )

    lst_titles = []

    for item in result:
        cleaned = re.sub(
            r'<h3><a href="/\w{1,}/\d{6}/\S{1,}" target="_blank">',
            '',
            item
        )
        news_title = re.sub(r'</a>', '', cleaned)
        lst_titles.append(news_title)
    lst_hrefs = []
    for item in result:
        href = re.findall(r'href="/\w{1,}/\d{6}/\S{1,}"', item)
        lst_hrefs.append(href[0])
    return lst_titles, lst_hrefs

def save_to_db(dict_x):
    for section, lst_news in dict_x.items():
        if os.path.exists(section):
            os.chdir(section)
        else:
            os.mkdir(section)
            os.chdir(section)
        
        f = open(f'{section}_news.txt', 'a')
        f.write(date.today().strftime('%Y/%m/%d'))
        f.write('\n\n')
        
        for item in lst_news:
            f.write(f'{item}\n')
        
        f.write('_' * 100 + '\n\n\n')
        f.close()
        os.chdir(f'{desktop_path}/project_data')

def make_request_for_body(news_url):
    response = requests.get(news_url)
    html_data = response.text
    return html_data

def extract_news_body(html_data):
    news_body = re.findall(r"<p>.{1,}</p>", html_data)
    news_article = ""
    for para in news_body:
        clean_p = re.sub(r"<p>", "", para)
        final_p = re.sub(r"</p>", " ", clean_p)
        news_article += f" {final_p}"
    return news_article

def extract_image(html_data):
    result = re.search(
        r'property="og:image" content="([^"]+)"',
        html_data
    )

    if result:
        return result.group(1)

    result = re.search(
        r'<figure class="item-img">.*?<img src="([^"]+)"',
        html_data,
        # Match any character except a new line
        re.DOTALL
    )

    if result:
        # Get the image URL that the regex found
        return result.group(1)

    return None

def clean_folder_name(title):
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    title = title.replace(" ", "_")
    # Return the first 80 characters of title
    return title[:80]

def save_article_folder(title, body, image_url, section):
    folder_name = clean_folder_name(title)

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    os.chdir(folder_name)

    if section != "photo":
        f = open("body.txt", "w", encoding="utf-8")
        f.write(body)
        f.close()

    if image_url != None:
        image_data = requests.get(image_url, timeout=10).content # If no photo is found

        f = open("image.jpg", "wb")
        f.write(image_data)
        f.close()

    os.chdir("..")  

# ------------------------------------------------------------------------

home = os.getcwd()
desktop_path = '/Users/ari/Desktop'
os.chdir(desktop_path)

if not os.path.exists('project_data'):
    os.mkdir('project_data')

os.chdir('project_data')

today_folder = date.today().strftime('%Y-%m-%d')

if not os.path.exists(today_folder):
    os.mkdir(today_folder)

os.chdir(today_folder)

news_sections = ["politics", "photo", "sports", "technology"]

for section in news_sections:

    if not os.path.exists(section):
        os.mkdir(section)

    os.chdir(section)

    section_url = f"https://en.mehrnews.com/service/{section}"
    the_html_data = make_request(section_url)

    titles, hrefs = extract_news_articles(the_html_data)

    for i in range(len(titles)):
        title = titles[i]

        href = hrefs[i]
        href = href.replace('href="', '')
        href = href.replace('"', '')

        article_url = "https://en.mehrnews.com" + href

        article_html = make_request_for_body(article_url)

        body = extract_news_body(article_html)

        image_url = extract_image(article_html)
        save_article_folder(title, body, image_url, section)

        

    os.chdir("..")

    print(f"\n\nNews extraction for {section} is done!\n\n")