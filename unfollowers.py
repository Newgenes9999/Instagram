import time
import getpass # 패스워드 입력 시, 패스워드를 가려줌
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
username = input('Username:')
password = getpass.getpass("Password:")

wait = WebDriverWait(driver, 5)

username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

username_field.send_keys(username)
password_field.send_keys(password)

login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
login_button.click()



time.sleep(10)

driver.get(f'https://www.instagram.com/{username}/')

time.sleep(5)


# 팔로워 수 가져오기
followers_element = driver.find_element(By.XPATH,f'//a[@href="/{username}/followers/"]/span')
followers_count = followers_element.get_attribute('title')

time.sleep(2)

# 팔로잉 수 가져오기
following_element = driver.find_element(By.XPATH,f'//a[@href="/{username}/following/"]/span/span')
following_count = following_element.text


time.sleep(2)


##########################
# 팔로워 목록 열기
followers_link = driver.find_element(By.XPATH, f'//a[@href="/{username}/followers/"]')
followers_link.click()

time.sleep(5)  # 팔로워 목록이 로드될 때까지 대기

followers_list = []

# 팔로워 목록을 스크롤

pop_up_window = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CLASS_NAME, '_aano')))

    # 스크롤을 다음 위치로 이동
for i in range(int(followers_count)//2):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', pop_up_window)
    time.sleep(1)

##



followers_elements = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd"]')
followers_list.extend([element.text for element in followers_elements])




driver.get(f'https://www.instagram.com/{username}/')

time.sleep(2)
############################
# 팔로잉 목록 열기
followers_link = driver.find_element(By.XPATH, f'//a[@href="/{username}/following/"]')
followers_link.click()

time.sleep(5)  # 팔로잉 목록이 로드될 때까지 대기

following_list = []

# 팔로잉 목록을 스크롤

pop_up_window = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CLASS_NAME, '_aano')))

for i in range(int(following_count)//2):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', pop_up_window)
    time.sleep(1)

following_elements = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd"]')
following_list.extend([element.text for element in following_elements])


final = []

for i in following_list:
    if i not in followers_list:
        final.append(i)
print(f'unfollwers:{final}')