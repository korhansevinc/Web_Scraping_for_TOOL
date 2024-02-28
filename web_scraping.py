from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import sys

# In older versions of selenium you must specify the PATH in the wd like here : webdriver.Chrome(PATH)
# But later versions (>4.16) we can use it without parameters. Take it account while using.
# PATH= "C:\\Users\\new\\Desktop\\WebScrapingImages\\chromedriver.exe"

wd = webdriver.Chrome()
# wd.get("https://www.google.com/")
# wd.quit()

def get_input_from_user():
	arguments = sys.argv[1:] # Taking all of the args except the name of the script which is argv[0]
	return arguments
	

def create_prompt_query(input_list):
    query = ""
    if len(input_list) < 1:
        query = ""
    elif len(input_list) == 1:
        query = input_list[0]
    else:
        for word in input_list:
            query = query + "+" + word
        query = query.strip()
    return query 
	

def get_images_from_google(input_from_user ,wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)
	query = create_prompt_query(input_from_user)
    # After search?q , we can specify our desired string as a query for the chrome.
	url = "https://www.google.com/search?q=" + query + "&tbm=isch&ved=2ahUKEwjykJ779tbzAhXhgnIEHSVQBksQ2-cCegQIABAA&oq=" + query + "&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoHCCMQ7wMQJ1C_31NYvOJTYPbjU2gCcAB4AIABa4gBzQSSAQMzLjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=7vZuYfLhOeGFytMPpaCZ2AQ&bih=817&biw=1707&rlz=1C1CHBF_enCA918CA918"
	wd.get(url)

	image_urls = set()
	skips = 0

	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				print("For this particular image, i cannot scrape. Going to next one.")
				continue

			#images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			images = wd.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)


def main():
	
	# Taking users input as an argument
    user_input = get_input_from_user()
    urls = get_images_from_google(user_input , wd, 2 , 20)

    for i, url in enumerate(urls):
        download_image("imgs/", url, user_input[0] + str(i) + ".jpg")

    wd.quit()
	

if __name__== "__main__":
	main()