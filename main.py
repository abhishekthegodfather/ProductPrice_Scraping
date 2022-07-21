from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


def amazon(product):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://www.amazon.in/')
    searchBox = driver.find_element(By.ID, "twotabsearchtextbox")
    searchBox.send_keys(product);
    searchBtn = driver.find_element(By.ID, "nav-search-submit-button")
    searchBtn.click()

    namePhone = []
    rating_arr = []
    price_arr = []
    dil_date = []
    off_arr = []

    time.sleep(10)
    phone_names = driver.find_elements(By.CSS_SELECTOR, "h2>a>Span")
    for i in phone_names:
        i = i.get_attribute("innerHTML")
        namePhone.append(i)

    print(namePhone)

    time.sleep(10)
    rating = driver.find_elements(By.CSS_SELECTOR, "a>i>Span")
    # rating_arr = []
    for i in rating:
        i = i.get_attribute("innerHTML")
        rating_arr.append(i)

    print(rating_arr)

    time.sleep(10)
    prices = driver.find_elements(By.CSS_SELECTOR, "span>span.a-price-whole")
    # price_arr = []
    for i in prices:
        i = i.get_attribute("innerHTML")
        price_arr.append(i)

    print(price_arr)

    time.sleep(10)
    dilevary = driver.find_elements(By.CSS_SELECTOR, "span>span.a-color-base.a-text-bold")
    # dil_date = []
    for i in dilevary:
        i = i.get_attribute("innerHTML")
        dil_date.append(i)

    print(dil_date)

    time.sleep(10)
    offers = driver.find_elements(By.CSS_SELECTOR, "span>span>span>span.a-truncate-cut")
    # off_arr = []
    for i in offers:
        i = i.get_attribute("innerHTML")
        off_arr.append(i)

    print(off_arr)

    time.sleep(10)
    original_pricce = driver.find_elements(By.CSS_SELECTOR, "span.a-price.a-text-price>span.a-offscreen")
    original_arr = []
    for i in original_pricce:
        i = i.get_attribute("innerHTML")
        original_arr.append(i)

    print(original_arr)


    data = pd.DataFrame({"Product Name":pd.Series(namePhone),
                        "Product Rating": pd.Series(rating_arr),
                        "Product Price (discounted)":pd.Series(price_arr),
                        "product Price (Original)":pd.Series(original_arr),
                        "Dilivary Date": pd.Series(dil_date),
                        "Offers": pd.Series(off_arr)
                        })
    data.to_csv("Amazon_Product_Scrap.csv")

    driver.close()

def flipkart(product):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://www.flipkart.com/')

    cross = driver.find_element(By.CSS_SELECTOR, "div>div>div>button")
    cross.click()

    cross = driver.find_element(By.CSS_SELECTOR, "div>div>input")
    cross.send_keys(product)

    btn = driver.find_element(By.CLASS_NAME, "L0Z3Pu")
    btn.click()

    time.sleep(10)
    name = []
    nameProduct = driver.find_elements(By.CLASS_NAME, "_4rR01T")
    for i in nameProduct:
        i = i.get_attribute("innerHTML")
        name.append(i)
    print(name)

    time.sleep(10)

    discount = driver.find_elements(By.CSS_SELECTOR, "div._25b18c>div._30jeq3._1_WHN1")
    dis_arr = []    
    for i in discount:
        i = i.get_attribute("innerHTML")
        dis_arr.append(i)
    print(dis_arr)

    time.sleep(10)
    original = driver.find_elements(By.CSS_SELECTOR, "div._3I9_wc._27UcVY")
    ori_arr = []    
    for i in original:
        i = i.get_attribute("innerHTML")
        ori_arr.append(i)
    print(ori_arr)

    time.sleep(10)
    rating = driver.find_elements(By.CSS_SELECTOR, "div._3LWZlK")
    rating_arr = []    
    for i in rating:
        i = i.text
        rating_arr.append(i)
    print(rating_arr)

    data = pd.DataFrame({"Product Name":name,
                        "Product Rating": rating_arr,
                        "Product Price (discounted)":dis_arr,
                        "product Price (Original)":ori_arr,
                        })
    data.to_csv("FlipKart_Product_Scrap.csv")
    driver.close()

def chroma(product):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://www.croma.com/')

    input_fld = driver.find_element(By.ID, "search")
    input_fld.send_keys(product)

    clk = driver.find_element(By.CSS_SELECTOR, "span.icon")
    input_fld.send_keys(Keys.RETURN)

    

    dis_arr = []
    old_arr = []
    dil_arr = []
    review_arr = []

    time.sleep(10)
    nameProduct = driver.find_elements(By.CSS_SELECTOR, ".product-title.plp-prod-title>a")
    name = []
    for i in nameProduct:
        i = i.text
        name.append(i)
    print(name)

    time.sleep(10)
    discount = driver.find_elements(By.CSS_SELECTOR, "span.new-price>span.amount")
    
    for i in discount:
        i = i.text
        dis_arr.append(i)
    print(dis_arr)

    time.sleep(10)
    oldPrices = discount = driver.find_elements(By.CSS_SELECTOR, "span.old-price>span.amount")
    
    for i in oldPrices:
        i = i.text
        old_arr.append(i)
    print(old_arr)

    time.sleep(10)
    dilivary = discount = driver.find_elements(By.CLASS_NAME, "discount")
    dis_arr = []
    for i in dilivary:
        i = i.text
        dil_arr.append(i)
    print(dil_arr)

    time.sleep(10)
    review = discount = driver.find_elements(By.CSS_SELECTOR, "div.cp-rating>span.text")
    
    for i in review:
        i = i.text
        i = i.replace('\n', ' ')
        review_arr.append(i)
    print(review_arr)

    data = pd.DataFrame({"Product Name":pd.Series(name),
                        "Product Review": pd.Series(review_arr),
                        "Product Price (discounted)":pd.Series(dis_arr),
                        "product Price (Original)":pd.Series(old_arr),
                        "Discount Percentage": pd.Series(dil_arr)
                        })
    data.to_csv("Chroma_Product_Scrap.csv")

    driver.close()



product = input("What the Product name you want to scrap: ")
# print(type(product))
amazon(product)
flipkart(product)
chroma(product)

