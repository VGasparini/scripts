from selenium import webdriver
from time import sleep
from random import randint


def post(cont, comment_text, target_url, param1=10, param2=5):
    for j in range(param1):
        browser.get(target_url)
        sleep(5)
        for i in range(param2):

            comment_field = browser.find_element_by_class_name(class_name)
            comment_field.click()
            sleep(randint(10, 100)/100)

            comment_field = browser.find_element_by_class_name(class_name)
            comment_field.send_keys(comment_text)
            sleep(randint(10, 100)/100)

            comment_field = browser.find_element_by_class_name(class_name)
            comment_field.submit()
            sleep(randint(10, 100)/100)

            cont += 1
            espera = randint(40, 60)
            print(f'Ok: {cont}, proximo em {espera}')
            sleep(espera)

        browser.get(homepage_url)
        sleep(randint(50, 70))


homepage_url = 'https://www.instagram.com/'
target_url = 'https://www.instagram.com/'  # set target photo url

username = ''  # set your username
secret = ''  # set your secret
comment_text = ''  # set your comment message

'''set your comments limit, it'll multiplied by 50 (default).
You can change passing as param1 and param2 on call post function'''
comment_limit = 1

browser = webdriver.Firefox()
browser.implicitly_wait(60)
browser.get(homepage_url)

user_field = browser.find_element_by_name('username')
secret_field = browser.find_element_by_name('password')

user_field.click()
user_field.send_keys(username)
sleep(1)

secret_field.click()
secret_field.send_keys(secret)
sleep(10)

browser.get(target_url)
sleep(1)
class_name = 'Ypffh'  # comment component id

for i in range(1, comment_limit+1):
    try:
        post(i, comment_text, target_url)
    except:
        print('Erro')
        pass
