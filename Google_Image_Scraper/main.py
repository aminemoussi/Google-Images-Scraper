import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from display_img import display_img
from download_img import download_img


chrome_driver_path = "C:\\Users\\amine\\PycharmProjects\\Image_Scraper\\chromedriver-version130-win64\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

url = "https://www.google.com/search?q=mark+milley&sca_esv=825e01edc18a56f7&sca_upv=1&rlz=1C1JJTC_enDZ1123DZ1123&udm=2&sxsrf=ADLYWILuPaCG6Hx78c-bHT-rCowR2jQLXA%3A1726587549103&ei=naLpZqL2BbeF7NYPg_O2OA&oq=mark+mi&gs_lp=Egxnd3Mtd2l6LXNlcnAiB21hcmsgbWkqAggAMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEijJFDqB1jUFXADeACQAQCYAYwBoAHxBqoBAzAuN7gBA8gBAPgBAZgCCqACkwfCAgoQABiABBhDGIoFwgIGEAAYBxgewgIGEAAYBRgewgIGEAAYCBgemAMAiAYBkgcDMy43oAfVIg&sclient=gws-wiz-serp"

driver.get(url)

x = input("Scroll down if you want to generate more images, press enter when you are done... ")


driver.execute_script("window.scrollTo(0, 0);")



page_html = driver.page_source
#print(page_html)  #got the html of the entire page
soup = BeautifulSoup(page_html, "html.parser")

img_container = soup.find_all("div", {"class": "eA0Zlc WghbWd FnEtTd mkpRId m3LIae RLdvSe qyKxnc ivg-i PZPZlf GMCzAd"})

num_containers = len(img_container)
print("Number of images generated in the page:", num_containers)

x = int(input("How much you want: "))

if x>num_containers or x<1:
    x = num_containers

span = int(input("%s to be collected, Now enter the max time to wait for an image to load: " %x)) #because some take too long


folder_path = str(input("Where to save it (folder path): "))
file_name = str(input("What to name it (file name): "))

full_path = f"{folder_path}/{file_name}"


i = 1

scraping_start_time = time.time()

while (i != (x + 1)) and (i < num_containers):
    if (i % 25) == 0:
        i = i + 1
    else:    # mostly every 25th container is a related search container
        #xpath = f'//*[@id="rso"]/div/div/div[1]/div/div/div[ {i} ]'



        preview_img_xpath = """//*[@id="rso"]/div/div/div[1]/div/div/div[ %s ]/div[2]/h3/a/div/div/div/g-img/img"""%(i)


        try:
            preview_img_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, preview_img_xpath))
            )
            #preview_img_element = driver.find_element_by_xpath(preview_img_xpath)
            preview_img_url = preview_img_element.get_attribute("src")
            print("Thumbnail url: ",preview_img_url)


            preview_img_element.click()
            #time.sleep(5)

            #image_Element = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]""")
            image_Element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"""//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]"""))
            )
            image_url = image_Element.get_attribute("src")


            broke_off = False
            start_time = time.time()

            if "https://encrypted-tbn0.gstatic.com/images?q=tbn:" in image_url:
                while "https://encrypted-tbn0.gstatic.com/images?q=tbn:" in image_url:
                    try:
                        image_Element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH,"""//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]"""))
                        )
                        image_url = image_Element.get_attribute("src")
                        print("Clicked Thumbnail url: ", image_url)

                        current_time = time.time()
                        time_spent = int(current_time - start_time)

                        if time_spent > span:
                            broke_off = True
                            print("ABORT, for time span: ", time_spent, " Secs reached.")
                            break
                    except:
                        broke_off = True
                        print("ERROR, select the clicked thumbnail." % span)
                        break

                if not broke_off:
                    try:
                        download_img(image_url, full_path, i)
                        print("FINAL img url**** ", image_url)
                        #display_img(image_url)
                    except:
                        print("** Couldn't download image %s, continuing with the following..." %i)

            i = i + 1     #no matter what outcome you get -> go to next img :)

        except Exception as e:
            print(f"ERROR, finding or clicking preview image {i}: {e}")
            i = i + 1  # Continue with the next image in case of error

print("Done, ",i - 1," downloaded, %s seconds elapsed." %(time.time() - scraping_start_time))