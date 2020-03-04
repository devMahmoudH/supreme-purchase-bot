#A Selenium Python bot to autofill Billing info on Supreme.com

#Created 8/26/2019

#Note this program will run on Linux, however replacing the webdriver with the latest Windows version-
#  will allow it to work on windows.

#Last test successfully purchased a product in less than 13 seconds.



from config import keys
from selenium import webdriver
import time

def order(k):

	driver = webdriver.Chrome('./chromedriver')
	driver.get(k['product_url'])

	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
	#driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
	driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card_number"])
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[4]').click()
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[2]').click()
	driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])
#State
	driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[13]').click()

#Terms and Conditions
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

#Process Payment
	driver.find_element_by_xpath('//*[@id="pay"]/input').click()



if __name__ == '__main__':
	order(keys)