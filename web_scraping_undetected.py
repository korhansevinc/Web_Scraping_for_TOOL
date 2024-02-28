'''
    A Web Scraper using undetected_chromedriver.
    Chrome may detect and may block our session usually after 50th-60th image. (In web_scraping.py we are facing this issue.)
    This is why we use undetected_chromedriver instead. 
'''

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
import sys
import random
import string

'''
    WARNING : GLOBAL CONSTANTS
    - DEBUG
    - FOLDER_PATH
    - LONG_DELAY
    - SHORT_DELAY
    - RANGE_OF_LARGE_SCROLLING
    Do not try to change them in runtime and while declaring variables, take them account.

'''
# DEBUG:
# True : Debug mod. Prints key values in key places.   
# False : Normal mod.
DEBUG = True
FOLDER_PATH = 'C:\\Users\\new\\Desktop\\WebScrapingImages\\images\\'
LONG_DELAY = 4
SHORT_DELAY = 2
RANDOM_STRING_LENGTH = 6
RANGE_OF_LARGE_SCROLLING = 3 # In large numbers, this can be vary. So you may need to change this. Usually in one scroll we get 50 - 120 images.


def get_input_from_user():
    '''
    Pass the necessary informations as argument :
    Arguments :
        image count (Integer) : The number of images that you want to scrape.
        query (String) : Pass the desired query as a string.
    Sample Usages :
        python web_scraping_undetected.py 30 dogs
        python web_scraping_undetected.py 50 lord of the rings
    '''
    image_count = sys.argv[1]
    image_count = (int)(image_count)
    arguments = sys.argv[2:] # Taking all of the args except the name of the script which is argv[0]
    if DEBUG :
        print("The arguments : ", arguments)
        print("Number of Image : ", image_count)
    return image_count , arguments


def random_string(length):
    """
    Belirtilen uzunlukta rastgele karakterlerden oluşan bir string oluşturur. Başına ve sonuna özel karakter yerleştirir. ( '_' )
    Script birden fazla kez aynı argümanlarla çağırılırsa resimlerin birbiri üstüne yazılmaması için kullanılıyor.

    Argümanlar:
    length (int): Oluşturulacak string'in uzunluğu.
    
    Return:
    str: Oluşturulan rastgele karakterlerden oluşan string.
    """
    characters = string.ascii_letters + string.digits
    
    random_string = ''.join(random.choice(characters) for _ in range(length))
    random_string = "_" + random_string + "_"
    return random_string

def create_prompt_query(input_list):
    '''
    Creates the prompt for query to passing to the url's body.
    '''
    query = ""
    if len(input_list) < 1:
        query = ""
    elif len(input_list) == 1:
        query = input_list[0]
    else:
        for word in input_list:
            query = query + "+" + word
        query = query.strip()
    if DEBUG :
        print(f"The query is : {query}")
    return query 


def get_images_from_chrome(numOfPics, query):
    '''
        Gets images from web and store their url's in an array and download them.
    '''
    # Launch Browser and Open the URL
    counter = 0
    for _ in range(numOfPics):
        # In older versions of selenium you must specify the PATH in the wd like here : webdriver.Chrome(PATH) / uc.Chrome(PATH)
        # But later versions (>4.16) we can use it without parameter PATH. Take it account while using. Only need is chromedriver.exe in your pwd.
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--disable-gpu") # Without this line , chrome still works after the scraping. Do not comment it.
        driver = uc.Chrome(options=options,no_sandbox=False)
        # Create url variable containing the webpage for a Google image search.
        url = "https://www.google.com/search?q=" + query + "&tbm=isch&ved=2ahUKEwjykJ779tbzAhXhgnIEHSVQBksQ2-cCegQIABAA&oq=" + query + "&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoHCCMQ7wMQJ1C_31NYvOJTYPbjU2gCcAB4AIABa4gBzQSSAQMzLjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=7vZuYfLhOeGFytMPpaCZ2AQ&bih=817&biw=1707&rlz=1C1CHBF_enCA918CA918"

        # Launch the browser and open the given url in your webdriver.
        try:
            driver.get(url)
        except:
            if DEBUG :
                print("Can not load the current url. Continuing...")
            continue

        # The execute script function will scroll down the body of the web page and load the images.
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(LONG_DELAY)
        if (numOfPics > 500):
            for i in range(0, RANGE_OF_LARGE_SCROLLING):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(SHORT_DELAY)
        if (numOfPics > 50):
            for i in range(0, 3):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(SHORT_DELAY)
        elif (numOfPics > 20):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(SHORT_DELAY)

        # Review the Web Page’s HTML Structure

        # We need to understand the structure and contents of the HTML tags and find an attribute that is unique only to images.
        
        img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

        image_urls = []
        
        how_many_images = 0
        for img in img_results:
            try:
                image_urls.append(img.get_attribute('src'))
                how_many_images +=1
                if DEBUG:
                    print("Found an image url. Appending to the download list.")
            except:
                if DEBUG:
                    print("There is an error in adding particular image's url to list. Continued...")
        print("The number of how_many_images : ", how_many_images)

        modifiedName = query.replace("+", " ")
        
        for i in range(numOfPics):
            try:
                counter += 1
                uniqueness = random_string(RANDOM_STRING_LENGTH)

                if DEBUG:
                    print("Uniqueness : ", uniqueness)

                urllib.request.urlretrieve(str(image_urls[i]), FOLDER_PATH + "{0} {1} {2}.jpg".format(modifiedName, counter, uniqueness))
                if DEBUG:
                    print("Image successfully downloaded.")
            except:
                if DEBUG:
                    print("For the particular image, i cannot download it. Going to next one.")
                continue

        driver.quit()
        if DEBUG:
            print("Counter : ",counter)
            print("Num of Pics : ", numOfPics)

        # If we had found enough pictures, end the process.
        if counter >= numOfPics :
            break

    counter = 0


def main():
    # Taking arguments as inputs. Behaviour explained in function declaration.
    numOfPics, user_input = get_input_from_user()
    query = create_prompt_query(user_input)
    get_images_from_chrome(numOfPics, query)
    print("Images successfully downloaded.")
    

if __name__ == "__main__":
    main()
    