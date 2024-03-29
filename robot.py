from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (NoSuchElementException,
                                        ElementNotInteractableException,
                                        UnexpectedAlertPresentException,
                                        ElementClickInterceptedException)
from abc import abstractmethod, ABCMeta
import os
import logging
import pyautogui
import pytesseract
import cv2
from info import *


""" Path to tesseract executable """
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


# close the chromedriver.exe & chrome.exe which runs in background
def close_():
    os.system('taskkill /f /im chromedriver.exe')
    os.system('taskkill /f /im chrome.exe')


# logging configuration
logging.basicConfig(filename='robot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# WEBSITE URLS
links = [
    'http://www.soodiran.com', 'https://www.shahr24.com/', 'http://digiagahi.com', 'https://persianagahi.com',
    'http://parsu.ir', 'https://agahi90.ir/', 'https://www.niaz118.com/framework/user/login',
    'http://www.decornama.com', 'http://www.adem.ir/fa/index.asp?p=Login', 'https://nasbeagahi.com/item/new',
    'https://agahiname.com/', 'https://agahiroz.com/%d9%88%d8%b1%d9%88%d8%af/', 'https://parstabligh.org/user_login/',
    'https://www.panikad.com/auth/login/', 'https://www.novintabligh.com/login.html', 'https://www.takro.net/',
    'https://my.niazerooz.com/membership', 'https://eforosh.com/', 'http://newagahi.ir/login_register.php',
    'https://71ap.ir/login/', 'https://otab.ir/auth',
    'https://www.agahichi.com/%D9%88%D8%B1%D9%88%D8%AF-%D8%B3%D8%A7%DB%8C%D8%AA.html', 'http://shetabe.ir/login',
    'http://iran-tejarat.com/LoginPage.aspx', 'http://sabzads.com/auth', 'http://www.tejaari.com/',
    'https://sellfree.ir/?d=login', 'https://googleagahi.com/auth', 'https://www.netmoj.ir/',
    'https://payameavval.net/login.aspx', 'http://xoonarg.com/', 'https://agahiaria.ir/auth',
    'http://darsanat.ir/login_register.php',
    'https://ruzandish.com/%d9%88%d8%b1%d9%88%d8%af/', 'https://100nama.com/sign-in',
    'https://niazmandyha.ir/login', 'https://www.2fanoos.com/auth',
    'https://www.2mihan.com/login/', 'https://3030l.net/auth', 'https://www.3ervice.com/%d9%88%d8%b1%d9%88%d8%af/',
    'https://www.rahnama118.com/framework/user/login', 'https://www.takniaz.com/framework/user/login',
    'https://www.novin-tejarat.com/framework/user/login', 'https://www.ptweb.ir/framework/user/login',
    'https://www.payamsara.com/framework/user/login', 'https://www.tablegh118.com/framework/user/login',
    'https://www.protabligh.com/framework/user/login', 'https://www.agahibartar.net/framework/user/login',
    'https://www.myniazmandi.com/framework/user/login', 'https://www.niazmandi-iran.com/framework/user/login', 
    'https://www.agahe118.com/framework/user/login', 'https://www.mytabligh.net/framework/user/login',
    'https://www.iran-agahi.com/framework/user/login', 'https://www.irantabligh.net/framework/user/login',
    'https://www.niaziran.net/framework/user/login', 'https://www.niaztehran.com/framework/user/login',
    'https://www.tehranagahi.net/framework/user/login', 'https://www.tehrantabligh.net/framework/user/login',
    'https://www.7010.ir/', 'http://7rang.ir/login', 'https://silverbookco.com/%D9%88%D8%B1%D9%88%D8%AF-2',
    'https://ads.zibashahr.com/user_login/', 'http://www.adsfarsi.com/', 'http://aftabe.com/%d9%88%d8%b1%d9%88%d8%af/',
    'https://www.agahi24.com/login', 'http://agahi2agahi.com/', 'http://www.agahi360.ir/account/login/',
    'http://www.abcagahi.ir/login', 'https://www.jarzadani.ir/index.php?r=site%2Flogin-reg',
    'http://jar24.ir/user/login', 'http://www.dasar.ir/', 'http://publik.ir/login_register.php',
    'http://hadafniaz.ir/login_register.php', 'http://peleha.ir/auth', 'https://pbazar.ir/login/',
    'http://pabi.ir/login', 'https://www.taaj.ir/?action=login', 'http://agahidon.ir/user/login',
    'http://agahiiran.ir/auth', 'https://agahi-kala.ir/user/login', 'https://agahimax.com/auth',
    'https://ariyads.com/auth', 'http://asreesfahan.com/login', 'http://bazarche96.com/auth',
    'https://bazarha.ir/%d9%88%d8%b1%d9%88%d8%af/', 'https://dararsh.com/login', 'https://fastniaz.com',
    'http://inagahi.com/', 'http://inokala.ir/auth', 'https://khafanbazar.ir/auth',
    'http://www.niazmandia.ir/panel/login', 'http://tabliqplus.ir/login_register.php', 
    'https://www.niazmandiha.net/login/',
    'https://noonerooz.com/%d9%88%d8%b1%d9%88%d8%af-%d8%a8%d9%87-%d8%ad%d8%b3%d8%a7%d8%a8'
    '-%da%a9%d8%a7%d8%b1%d8%a8%d8%b1%db%8c/', 'https://iranamir.com/ads/auth', 'http://nabzeroz.ir/auth',
    'https://www.hogre.ir/login', 'http://www.radtabligh.com/fa/index.asp?p=Login&m=Client',
    'http://aghayeagahi.ir/', 'https://jaraghe.net/my-account/',

]


# design class of our classes (Base Class)
class IPostAds(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, url, username, password):
        path = 'chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.username = username
        self.password = password
        self.driver.get(url)
        self.login()

        """ Information for login and load page"""

    """ Some province start with same name so __match & __search pass through this issue """
    @staticmethod
    def _match_(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 2:
            return True
        return False

    def _search_(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match_(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    """ In order to find groups & sub-groups that have 'main-group ->/» main-sub-group' pattern
        we re-define match and search to _match & _search
    """
    @staticmethod
    def _match(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2):
            return True
        return False

    def _search(self, group, sub_group, prefix, suffix, separate_by='', element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).split(separate_by)

                try:
                    if self._match(group, pattern_txt[0].strip()) and self._match(sub_group, pattern_txt[1].strip()):
                        pattern.click()
                        return element
                except IndexError:
                    pass

                element += 1
            except NoSuchElementException:
                loop = False

    """ Main match Function to match the string with string in dropdown boxes """
    @staticmethod
    def match(string, other):
        count = 0
        match_length = len(string)
        part = len(string.split(' '))
        for i, j in zip(string, other):
            if i == j:
                count += 1
        if count > ((match_length / 3) * 2) + 1 and part == 1:
            return True
        elif part > 1:
            if count > match_length - 4:
                return True
        return False

    """ Main search function to find string in a dropdown boxes and clicks it """
    def search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self.match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    """ Finding the specefic group & sub-group """
    def group_search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match_(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    @abstractmethod
    def login(self):
        """ Login method """

    @abstractmethod
    def post(self):
        """ Post our ads """

    def close(self):
        self.driver.quit()


class PostAd1(IPostAds):
    """ http://www.soodiran.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[2]/input')\
            .send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[4]/input')\
            .send_keys(self.password)

        # login button
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[5]/input').click()

        sleep(2)
        self.post()

    def post(self):
        # Enter to post ads page
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[3]/a').click()

        # Select Group
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/select').click()
        prefix = '/html/body/div/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/select/option['
        self.search(main_group, prefix, ']')

        # Select Sub Group
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/select').click()
        prefix = '/html/body/div/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/select/option['
        self.search(main_sub_group, prefix, ']')

        # Title
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[3]/td[2]/input')\
            .send_keys(title)

        # Description
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[4]/td[2]/textarea') \
            .send_keys(description)

        sleep(1)
        # Select Province
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[6]/td[2]/select').click()
        prefix = '/html/body/div/div[3]/div/div[2]/table/tbody/tr[6]/td[2]/select/option['
        self._search_(province, prefix, ']')

        # Select City
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[6]/td[4]/select').click()
        prefix = '/html/body/div/div[3]/div/div[2]/table/tbody/tr[6]/td[4]/select/option['
        self.search(city, prefix, ']')

        # Price
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[5]/td[4]/input')\
            .send_keys(price)

        # Address <optional>
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[7]/td[2]/input')\
            .send_keys(address)

        # Telephone <optional>
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[7]/td[4]/input')\
            .send_keys(phone)

        # submit
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="form"]/tbody/tr[11]/td[2]/input').click()


class PostAd2(IPostAds):
    """ https://www.shahr24.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_UserNameTBX"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_PasswordTbx"]').send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_LoginBtn"]').click()
        sleep(5)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/form/div[4]/header/div[1]/div/div[4]/a').click()

        sleep(2)
        # select main group
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/'
                                          'div[7]/div[2]/table/tbody/tr/td/select[1]').click()
        prefix = '/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/' \
                 'div[1]/div[7]/div[2]/table/tbody/tr/td/select[1]/option['
        self.search(main_group, prefix, ']')
        sleep(1)

        # select sub group
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/'
                                          'div[7]/div[2]/table/tbody/tr/td/div[2]/select').click()

        prefix = '/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/' \
                 'div[7]/div[2]/table/tbody/tr/td/div[2]/select/option['
        self.search(main_sub_group, prefix, ']')

        # title
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtTitle"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtBody"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtPrice"]').send_keys(price)

        # Keywords <optional>
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtKeywords"]').send_keys(
            keywords.replace('  ', '\n'))

        # Picture
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[7]'
                                          '/div[8]/table/tbody/tr[5]/td/div/div[2]/div/div[2]/input').send_keys(picture)

        # name
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtName"]').send_keys(name)

        # phone number
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtTel"]').send_keys(phone)

        # city
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[7]'
                                          '/div[11]/table/tbody/tr[4]/td/div[1]/button').click()

        prefix = '/html/body/form/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[7]/' \
                 'div[11]/table/tbody/tr[4]/td/div[1]/div/ul/li['
        self.search(city, prefix, ']/a')

        # address
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtAddress"]').send_keys(address)

        # submit
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_btnSave"]').click()


class PostAd3(IPostAds):
    """ http://digiagahi.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        # login btn
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()

        sleep(2)
        self.post()

    def post(self):
        # Goto to post page
        self.driver.find_element_by_xpath('/html/body/ul/div/li[2]/a').click()
        sleep(1)

        # Select group
        self.driver.find_element_by_id('main_group').click()
        prefix = '/html/body/div[4]/div/div/div[2]/form/table[1]/tbody/tr[1]/td[2]/select/option['
        self.search(main_group, prefix, ']')

        # Select sub group
        self.driver.find_element_by_id('sub_group').click()
        prefix = '/html/body/div[4]/div/div/div[2]/form/table[1]/tbody/tr[1]/td[4]/select/option['
        self.search(main_sub_group, prefix, ']')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys(description)

        # keyword
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords.replace('  ', '\n'))

        # website_link
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys(website_link)

        # price
        self.driver.find_element_by_xpath('//*[@id="adsprice"]').send_keys(price)

        # select province
        self.driver.find_element_by_id('ostan').click()
        prefix = '/html/body/div[4]/div/div/div[2]/form/table[1]/tbody/tr[6]/td[4]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # select city
        self.driver.find_element_by_id('Shahrestan').click()
        prefix = '/html/body/div[4]/div/div/div[2]/form/table[1]/tbody/tr[8]/td[4]/select/option['
        self.search(city, prefix, ']', element=2)

        # picture
        self.driver.find_element_by_xpath('//*[@id="image"]').send_keys(picture)

        # Home Phone
        self.driver.find_element_by_xpath('//*[@id="tel"]').send_keys(home_phone)

        # Mobile phone
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)

        # submit
        self.driver.find_element_by_xpath('//*[@id="addads"]').click()


class PostAd4(IPostAds):
    """ https://persianagahi.com """
    """
    NOTICE: we can just post 3 FREE ads in this website per month
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # go to login page
        self.driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div/section/div/div/div/ul/li[6]/a').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="edit-pass"]').send_keys(self.password)

        # simple captcha
        captcha = str(self.driver.find_element_by_xpath('/html/body/div[4]/div/section/div/'
                                                        'section/form/div/div[3]/div').text)
        captcha = captcha.split()
        number_1 = int(captcha[3][1])
        number_2 = int(captcha[5])
        operator = captcha[4]

        if operator == '+':
            number_1 += number_2
        else:
            number_1 -= number_2
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="edit-captcha-response"]').send_keys(number_1)

        # login
        self.driver.find_element_by_xpath('//*[@id="edit-submit"]').click()

        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('//*[@id="block-block-10"]/p[2]/span[1]/a').click()
        sleep(1)

        # title
        self.driver.find_element_by_xpath('//*[@id="edit-title"]').send_keys(title)

        # group
        self.driver.find_element_by_id('edit-taxonomy-catalog-und-hierarchical-select-selects-0').click()
        prefix = '/html/body/div[4]/div/section/div/section[2]/form/div/div[2]/div/div/div[1]/div/select/option['
        self.search(main_group, prefix, ']', element=2)
        sleep(10)

        # sub group
        self.driver.find_element_by_name('taxonomy_catalog[und][hierarchical_select][selects][1]').click()
        prefix = '/html/body/div[4]/div/section/div/section[2]/form/div/div[2]/div/div/div[1]/div/select[2]/option['
        self.search(main_sub_group, prefix, ']')

        # picture
        self.driver.find_element_by_xpath('//*[@id="edit-uc-product-image-und-0-upload"]').send_keys(picture)

        # description
        iframe = self.driver.find_element_by_xpath('/html/body/div[4]/div/section/div/section[2]/form/div/div[4]/'
                                                   'div/div/div[2]/div/div[1]/div/div/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html').send_keys(description)
        self.driver.switch_to.default_content()
        sleep(1)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="edit-field-tags-und"]').send_keys(keywords.replace('  ', '\n'))

        # address
        self.driver.find_element_by_xpath('//*[@id="edit-field-address-und-0-value"]').send_keys(address)

        # name
        self.driver.find_element_by_xpath('//*[@id="edit-field-name-und-0-value"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="edit-field-tel-und-0-value"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="edit-field-email-und-0-email"]').send_keys(email)

        # website address
        self.driver.find_element_by_xpath('//*[@id="edit-field-website-und-0-url"]').send_keys(website_link)

        # website title <up until 128 character>
        self.driver.find_element_by_xpath('/html/body/div[4]/div/section/div/section[2]/form/div/'
                                          'div[10]/div/div/div/div[1]/div/input').send_keys(website_title)

        # price
        self.driver.find_element_by_xpath('//*[@id="edit-field-price-und-0-amount"]').send_keys(price)

        # submit
        self.driver.find_element_by_xpath('//*[@id="edit-submit"]').click()


class PostAd5(IPostAds):
    """ http://parsu.ir """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('//*[@id="login_open"]').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        sleep(1)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/'
                                          'div[2]/form/div[3]/div[2]/button').click()

        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/a').click()
        sleep(2)

        # title
        self.driver.find_element_by_xpath('//*[@id="titlefa_IR"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="descriptionfa_IR"]').send_keys(description)
        sleep(1)

        # group
        self.driver.find_element_by_id('select_1').click()
        prefix = '/html/body/div[2]/div[4]/div[1]/div/div/div/form/fieldset/div[1]/div/select[1]/option['
        self.search(main_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        self.driver.find_element_by_id('select_2').click()
        prefix = '/html/body/div[2]/div[4]/div[1]/div/div/div/form/fieldset/div[1]/div/select[2]/option['
        self.search(main_sub_group, prefix, ']', element=2)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div/form/fieldset/div[3]'
                                          '/div[1]/div/div/div/div[3]/input').send_keys(picture)

        # province
        self.driver.find_element_by_id('regionId').click()
        prefix = '/html/body/div[2]/div[4]/div[1]/div/div/div/form/fieldset/div[5]/div[2]/div/select/option['
        self._search_(province, prefix, ']', element=2)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="s_tags"]').send_keys(keywords.replace('  ', '\n'))

        # phone
        self.driver.find_element_by_xpath('//*[@id="meta_phone"]').send_keys(phone)

        # click the radio button
        self.driver.find_element_by_xpath('//*[@id="terms_box"]').click()
        sleep(1.3)

        # submit
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div/'
                                          'form/fieldset/div[6]/div/button').click()


class PostAd6(IPostAds):
    """ https://agahi90.ir/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/form/div[2]/header/div/div[1]/div/ul[2]/li[1]/a').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="mainContent_TextBox1"]').send_keys(self.username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="mainContent_TextBox2"]').send_keys(self.password)

        # captcha
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtValidate"]').click()
        sleep(13)

        # login button
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainContent_Button1"]').click()

        sleep(2)
        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/'
                                              'div/div[2]/div[1]/div/div[1]/div[1]/a').click()

        except NoSuchElementException:
            self.login()
        sleep(2)

        # select group & sub-group
        self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/div/div/'
                                          'div[1]/div[2]/div[1]/div/div[1]').click()
        sleep(2)
        prefix = '/html/body/form/div[2]/section/section/div/div/div[2]' \
                 '/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div['

        self._search(main_group, main_sub_group, prefix, ']', separate_by='»')

        # select province & city
        self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/div/'
                                          'div/div[1]/div[2]/div[2]/div/div[1]').click()

        prefix = '/html/body/form/div[2]/section/section/div/div/div[2]/' \
                 'div/div/div[1]/div[2]/div[2]/div/div[2]/div/div['
        sleep(2)
        self._search(province, city, prefix, ']', separate_by='»')

        # title
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtOnvan"]').send_keys(title)

        # short description
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtDesciption"]').send_keys(short_description)

        # description
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtText"]').send_keys(description)
        sleep(1)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtKeyWord"]').send_keys(keywords)

        # website link
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtLink"]').send_keys(website_link)

        # price
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtPrice"]').send_keys(price)
        sleep(1)

        # picture
        self.driver.find_element_by_xpath('//*[@id="mainContent_FileUpload1"]').send_keys(picture)

        # Address
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtAddress"]').send_keys(address)

        # submit
        self.driver.find_element_by_xpath('//*[@id="mainContent_Button1"]').click()
        sleep(2)


class PostAd7(IPostAds):
    """ https://www.niaz118.com/framework/user/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    """ In order to inherit from this class ads page take information and pass them through the post method """
    def ads_page(self):
        """ Page is the webpage that ads is submitted """
        page = 'https://www.niaz118.com/ads/addprop'
        group = niaz118_group
        sub_group = niaz118_sub_group
        return page, group, sub_group, province, 'nds'

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(self.password)
        sleep(1)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/'
                                          'div/div[1]/div[1]/form/input[1]').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get(self.ads_page()[0])

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # click on sale button
        self.driver.find_element_by_xpath('//*[@id="reg2"]').click()

        # group
        sleep(1)
        prefix = '/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[1]/fieldset/div[2]/div[3]/select/option['
        self.group_search(str(self.ads_page()[1]), prefix, ']', element=2)
        sleep(2)

        # sub group
        prefix = '/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[1]/fieldset/div[2]/div[4]/div/' \
                 'select/option['
        self.group_search(str(self.ads_page()[2]), prefix, ']', element=2)

        # description
        self.driver.find_element_by_xpath('//*[@id="full_text"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[1]/form/'
                                          'div/div/div[1]/fieldset/div[2]/div[7]/input').send_keys(price)
        
        # picture
        self.driver.find_element_by_xpath('//*[@id="imgup1"]').send_keys(picture)

        # Address
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[1]/'
                                          'form/div/div/div[3]/fieldset/div[3]/input').send_keys(address)

        # province
        if self.ads_page()[4] == 'nds':
            prefix = '/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[3]/fieldset/div[4]/select/option['
            self.group_search(self.ads_page()[3], prefix, ']', element=2)
            sleep(2)

        else:
            prefix = '/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[3]/fieldset/div[4]/select/option['
            self._search_(self.ads_page()[3], prefix, ']', element=2)
            sleep(2)

        # phone
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[3]/'
                                              'fieldset/div[6]/input').clear()

            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div[3]/'
                                              'fieldset/div[6]/input').send_keys(phone)
        except NoSuchElementException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/'
                                          'form/div/div/table/tbody/tr/td[1]/input').click()


class PostAd8(IPostAds):
    """ http://www.decornama.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/'
                                          'div/div[1]/div[1]/div/div/ul/li[1]/a').click()
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="btn-register"]').click()

        sleep(5)
        self.post()

    def post(self):
        self.driver.get('https://decornama.com/?component=member&action=new_ads')

        # title
        self.driver.find_element_by_xpath('//*[@id="inputTitle"]').send_keys(title)

        # short description
        self.driver.find_element_by_xpath('//*[@id="inputBrief_description"]').send_keys(short_description)

        # description
        self.driver.find_element_by_xpath('//*[@id="inputDescription"]').send_keys(description)

        # Home phone
        self.driver.find_element_by_xpath('//*[@id="inputPhone2"]').send_keys(home_phone)

        # Address
        self.driver.find_element_by_xpath('//*[@id="inputAddress"]').send_keys(address)

        # website link
        self.driver.find_element_by_xpath('//*[@id="inputWeb_site"]').send_keys(website_link)

        # Email Address
        self.driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(email)

        # group
        prefix = '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/div[11]/div/div/ul/li['
        self.search(decornama_group, prefix, ']/a')
        sleep(2)

        # sub-group
        prefix = '/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/div[11]/div/div/div/div[7]/p/label['
        self.search(decornama_sub_group, prefix, ']')

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/'
                                          'form/div[13]/div/input').send_keys(picture)
        sleep(2)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="btn-register"]').click()


class PostAd9(IPostAds):
    """ http://www.adem.ir/fa/index.asp?p=Login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login-box-user"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div/div/div[1]/div/div[2]/'
                                          'form/input[2]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div/div/div[1]/div/div[2]/form/'
                                          'input[4]').click()

        sleep(2)
        self.post()

    def post(self):
        self.driver.get('http://www.adem.ir/newads/7075')

        # group
        prefix = '/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[1]/select/option['
        self.search(adem_group, prefix, ']', element=2)

        # sub-group
        prefix = '/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/div[1]/select/option['
        self.search(adem_sub_group, prefix, ']')

        # title
        self.driver.find_element_by_xpath('//*[@id="txtTitle"]').send_keys(title)

        # description
        element = self.driver.find_element_by_xpath('//*[@id="cke_contents_text"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click()
        actions.send_keys(description)
        actions.perform()
        sleep(2)

        # picture
        pictures = picture.split('\\')
        pic_path = pictures[0] + "\\fakepath\\" + pictures[-1]
        self.driver.find_element_by_xpath('//*[@id="Pictures"]').send_keys(pic_path)

        # name
        self.driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(name)
        
        # phone
        self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/'
                                          'div[6]/input').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/'
                                          'div[8]/input').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/'
                                          'div[9]/input').send_keys(website_link)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/'
                                          'div[2]/div[10]/textarea').send_keys(keywords.replace('  ', ','))

        # province
        prefix = '/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/div[12]/select/option['
        self._search_(province, prefix, ']', element=2)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/fieldset/div/form/div[2]/'
                                          'div[14]/input').click()


class PostAd10(IPostAds):
    """ https://nasbeagahi.com/item/new """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        """ No login required """
        self.post()

    def post(self):
        # group
        prefix = '/html/body/div[2]/div/div/form/div[1]/div/div/div/select/option['
        self.search(nasbeagahi_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        prefix = '/html/body/div[2]/div/div/form/div[1]/div/div/div/select[2]/option['
        self.search(nasbeagahi_sub_group, prefix, ']', element=2)
        sleep(1)

        # sub sub-group
        if nasbeagahi_sub_sub_group:
            prefix = '/html/body/div[2]/div/div/form/div[1]/div/div/div/select[3]/option['
            self.search(nasbeagahi_sub_sub_group, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="titlefa_IR"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="descriptionfa_IR"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div[1]/div[4]/div/'
                                          'div[2]/input').send_keys(picture)

        # province
        prefix = '/html/body/div[2]/div/div/form/div[2]/div[1]/div[7]/div[1]/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div/div/form/div[2]/div[1]/div[7]/div[2]/div/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="atr_10"]').send_keys(phone)

        # website link
        self.driver.find_element_by_xpath('//*[@id="atr_11"]').send_keys(website_link)

        # name
        self.driver.find_element_by_xpath('//*[@id="contactName"]').send_keys(name)
        
        # email
        self.driver.find_element_by_xpath('//*[@id="contactEmail"]').send_keys(email)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div[1]/div[10]/div/'
                                          'input').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_tag"]').send_keys(keywords.replace('  ', '\n'))

        # submit buttons
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div[3]/div/button').click()


class PostAd11(IPostAds):
    """ https://agahiname.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/form/div[2]/div/div/a[1]').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox1"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox2"]').send_keys(self.password)

        """ Captcha should entered manually """
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBoxCaptcha"]').click()
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]').click()
        sleep(1)

        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/form/div[3]/div/a[2]').click()
            self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_RepeaterPlans_ButtonSubmit_0"]').click()

        except NoSuchElementException:
            logging.error("Captcha Error")
            self.login()

        # group
        self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList1').click()
        prefix = '/html/body/form/div[7]/div[2]/div/div/div[1]/select/option['
        self.search(agahinama_group, prefix, ']', element=2)
        sleep(3)

        # sub group
        self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList2').click()
        prefix = '/html/body/form/div[7]/div[2]/div/div/div[2]/select/option['
        self.search(agahinama_sub_group, prefix, ']', element=2)
        sleep(1)

        # city
        self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList3').click()
        prefix = '/html/body/form/div[7]/div[2]/div/div/div[3]/select/option['
        self.search(city, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox1"]').send_keys(title)

        # address
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox9"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox6"]').send_keys(phone)

        # Email
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox7"]').send_keys(email)

        # description
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox11"]').send_keys(description)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]').click()
        sleep(2)

        # picture
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_FileUpload1"]').send_keys(picture)

        # submit picture
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]').click()

        # navigate to ads page
        self.driver.find_element_by_xpath('//*[@id="divsignout"]/a[2]').click()


class PostAd12(IPostAds):
    """ https://agahiroz.com/%d9%88%d8%b1%d9%88%d8%af/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/header/div/div/div/nav/ul/li[1]/a').click()

        # group
        self.driver.find_element_by_id('ad_cat_id').click()
        prefix = '/html/body/div[1]/div/div[3]/div[2]/div/main/div/div/div/div[2]/' \
                 'form/table/tbody/tr[2]/td[2]/div/div/select/option['
        self.search(agahirooz_group, prefix, ']', element=2)

        # first submit button
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="getcat"]').click()

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # province & city
        self.driver.find_element_by_css_selector('#list_cp_street > input:nth-child(2)').send_keys(
            province + ' - ' + city)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords)

        try:
            # description
            self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

            # Email
            self.driver.find_element_by_xpath('//*[@id="cp_register_email"]').send_keys(email)
            sleep(1)

            self.driver.find_element_by_id('list_image-input')

            # picture
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/'
                                              'main/div/div/div/div[2]/form/div[11]/p[3]/a').click()
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/main/div/div/div/'
                                              'div[2]/form/div[11]/div/div[2]/ul/li[3]/div/input').send_keys(picture)
            sleep(1)

        except NoSuchElementException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)

        try:
            # first submit button
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/main/'
                                              'div/div/div/div[2]/form/input[4]').click()
            sleep(5)
        except ElementNotInteractableException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/main/'
                                          'div/div/div/div[2]/form/p[2]/input[2]').click()
        sleep(1)

        # show the ads
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/'
                                              'div/main/div/div/div/div[2]/div/a').click()
        except NoSuchElementException:
            pass


class PostAd13(IPostAds):
    """ https://parstabligh.org/user_login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/artical/div[5]/'
                                          'div/div[3]/div/form/div[1]/div[2]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/artical/div[5]/div/div[3]/'
                                          'div/form/div[2]/div[2]/input').send_keys(self.password)

        # captcha
        captcha_txt = str(self.driver.find_element_by_xpath('/html/body/artical/div[5]/div/'
                                                            'div[3]/div/form/div[3]/div[1]/label').text)

        persian_number = {
            'یک': 1,
            'دو': 2,
            'سه': 3,
            'چهار': 4,
            'پنج': 5,
            'شش': 6,
            'هفت': 7,
            'هشت': 8,
            'نه': 9,
            'ده': 10,
            'یازده': 11,
            'دوازده': 12,
        }
        captcha_txt = captcha_txt.split()
        number = captcha_txt[2][:2]
        alpha_num = captcha_txt[0]
        captcha = persian_number[alpha_num] + int(number)
        self.driver.find_element_by_xpath('//*[@id="cc"]').send_keys(captcha)
        sleep(2)

        # login button
        self.driver.find_element_by_xpath('//*[@id="submitbtn"]').click()
        sleep(2)
        self.post()

    """ For choosing the right group two method 'match' and 'search' needed to be overwritten
        match() -> math_group()
        search() -> search_group()
    """
    @staticmethod
    def match_group(string, other):
        count = 0
        match_length = len(string)
        part = len(string.split(' '))
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) and part == 1:
            return True
        elif part > 1:
            if count > match_length - 3:
                return True
        return False

    def search_group(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text)
                if self.match_group(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        self.driver.find_element_by_xpath('/html/body/artical/div[2]/div[2]/a').click()

        # name
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/div/div[2]/div[2]/input').send_keys(phone)

        # website link
        self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/div/div[3]/div[2]/input')\
            .send_keys(website_link)

        # province
        self.driver.find_element_by_id('item75_select_1').click()
        prefix = '/html/body/artical/div[6]/form/div/div[4]/div[2]/select[1]/option['
        self._search_(province, prefix, ']', element=3)
        sleep(2)

        # city
        self.driver.find_element_by_id('item73_select_1').click()
        prefix = '/html/body/artical/div[6]/form/div/div[4]/div[2]/select[2]/option['
        self._search_(city, prefix, ']', element=2)

        # select free ads option
        Select(self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/'
                                                 'div/div[6]/div[3]/select')).select_by_visible_text('آگهی رایگان')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # group
        self.driver.find_element_by_id('catID').click()
        prefix = '/html/body/artical/div[6]/form/div/div[9]/select/option['
        self.search_group(parstabligh_group, prefix, ']', element=2)

        # description
        self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/div/textarea').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('//*[@id="file"]').send_keys(picture)
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()


class PostAd14(IPostAds):
    """ https://www.panikad.com/auth/login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="Username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(self.password)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[2]/form/div[1]/div/input').click()
        # CAPTCHA delay time
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[2]/form/p[5]/button').click()

        self.post()

    def post(self):
        self.driver.get('https://www.panikad.com/auth/ad/add/')

        # title
        self.driver.find_element_by_xpath('//*[@id="Title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="NoticeData"]').send_keys(description)

        # group
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/'
                                          'div[3]/form/div[2]/div[2]/div/select').click()
        prefix = '/html/body/div[1]/div/div/div/div/div[1]/div[3]/form/div[2]/div[2]/div/select/option['
        self.search(panikad_group, prefix, ']', element=2)
        sleep(1)

        # sub group
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/'
                                          'div[3]/form/div[2]/div[3]/div/select').click()
        prefix = '/html/body/div[1]/div/div/div/div/div[1]/div[3]/form/div[2]/div[3]/div/select/option['
        self.search(panikad_sub_group, prefix, ']')

        # province
        self.driver.find_element_by_id('States').click()
        prefix = '/html/body/div[1]/div/div/div/div/div[1]/div[3]/form/div[2]/div[4]/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(1)

        # city
        self.driver.find_element_by_id('Cities').click()
        prefix = '/html/body/div[1]/div/div/div/div/div[1]/div[3]/form/div[2]/div[5]/div/select/option['
        self.search(city, prefix, ']', element=2)

        # short description
        self.driver.find_element_by_xpath('//*[@id="Description"]').send_keys(short_description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags-selectized"]').send_keys(keywords)

        # price
        self.driver.find_element_by_xpath('//*[@id="ProductPrice"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/'
                                          'div[3]/form/div[2]/div[7]/div/input').send_keys(picture)

        # address
        self.driver.find_element_by_xpath('//*[@id="Address"]').clear()
        self.driver.find_element_by_xpath('//*[@id="Address"]').send_keys(address)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[3]/form/div[3]/div'
                                          '/button').click()


class PostAd15(IPostAds):
    """ https://www.novintabligh.com/login.html """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[4]/td[2]/input')\
            .send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[6]/td[2]/input')\
            .send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[8]/th/input').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.get('https://www.novintabligh.com/user.php?DPT=U2')

        # group
        try:
            self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/'
                                              'tr/td[1]/table/tbody/tr[1]/td/table[1]/tbody/'
                                              'tr/td/table/tbody/tr[4]/td[2]/select').click()
            prefix = '/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table[1]/tbody/tr/' \
                     'td/table/tbody/tr[4]/td[2]/select/option['
            self._search(main_group, main_sub_group, prefix, ']', separate_by='»', element=2)
        except NoSuchElementException:
            self.post()

        # title
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/'
                                          'table/tbody/tr[1]/td/table[1]/tbody/tr/td/table/tbody/'
                                          'tr[6]/td[2]/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/'
                                          'tr/td[1]/table/tbody/tr[1]/td/table[1]/tbody/tr/'
                                          'td/table/tbody/tr[8]/td[2]/textarea').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/'
                                          'table/tbody/tr[1]/td/table[1]/tbody/tr/td/table/tbody/tr[10]/'
                                          'td/table/tbody/tr/td[2]/input').send_keys(keywords)
        sleep(2)

        # scroll down
        phone_element = '/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/' \
                        'td/table[1]/tbody/tr/td/table/tbody/tr[19]/td[2]/input'

        try:
            self.driver.execute_script('arguments[0].scrollIntoView(true);', phone_element)
            sleep(1)
        except UnexpectedAlertPresentException:
            pass

        # phone
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/'
                                          'tbody/tr[1]/td/table[1]/tbody/tr/td/table/'
                                          'tbody/tr[19]/td[2]/input').send_keys(phone)

        # price
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/'
                                          'table/tbody/tr[1]/td/table[1]/tbody/tr/td/table/'
                                          'tbody/tr[22]/td[2]/input').send_keys(price)

        # address
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/'
                                          'table/tbody/tr[1]/td/table[1]/tbody/tr/td/table/tbody/'
                                          'tr[25]/td[2]/input').send_keys(address)

        # city
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/'
                                          'td/table[1]/tbody/tr/td/table/tbody/tr[16]/td[4]/select').click()
        prefix = '/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/' \
                 'table[1]/tbody/tr/td/table/tbody/tr[16]/td[4]/select/option['
        self.search(city, prefix, ']', element=2)

        # period
        Select(self.driver.find_element_by_xpath('//*[@id="PLANPERIOD"]')).select_by_visible_text('یک ماه')

        # type of ads
        Select(self.driver.find_element_by_xpath('//*[@id="PLANTYPE"]')).select_by_visible_text('معمولی')

        # picture
        self.driver.find_element_by_xpath('//*[@id="userfile1"]').send_keys(picture)
        sleep(3)

        # submit button
        try:
            self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/'
                                              'td[1]/table/tbody/tr[1]/td/table[1]/tbody/tr/td/'
                                              'table/tbody/tr[33]/th/input').click()

            self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/'
                                              'td[1]/table/tbody/tr[1]/td/table[1]/tbody/tr/td/'
                                              'table/tbody/tr[33]/th/input').click()
        except NoSuchElementException:
            pass


class PostAd16(IPostAds):
    """ https://www.takro.net/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[2]/div[1]/div[2]/form/input[2]').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[2]/div[1]/div[2]/ul/li[1]/a').click()

        # group
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[1]/'
                                          'div/div[2]/form/div/div[1]/div/select').click()
        prefix = '/html/body/div/div[4]/div/section[1]/div/div[2]/form/div/div[1]/div/select/option['
        self._search(main_group, main_sub_group, prefix, ']', separate_by='»', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="text"]').send_keys(description)

        # phone
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[1]/'
                                          'div/div[2]/form/div/div[5]/div/input').send_keys(phone)
        sleep(2)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="_keywords"]').send_keys(keywords)
        sleep(1)

        # price <تومان>
        try:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)
        except UnexpectedAlertPresentException:
            pass

        # ads type
        Select(self.driver.find_element_by_xpath('//*[@id="type"]')).select_by_visible_text('رایگان')

        # Address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # picture
        self.driver.find_element_by_xpath('//*[@id="photo1"]').send_keys(picture)
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[1]/'
                                          'div/div[2]/form/div/div[15]/button').click()


class PostAd17(IPostAds):
    """ https://my.niazerooz.com/membership """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    @staticmethod
    def check_for_integer(alpha):
        try:
            int(alpha)
            return True
        except ValueError:
            return False

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="EmailOrMobile"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(self.password)

        # captcha
        with open('index.jpg', 'wb') as img_file:
            img_file.write(self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/'
                                                             'div/form/div/div[1]/div[2]/div/img').screenshot_as_png)
        img = cv2.imread('index.jpg')
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        captcha = pytesseract.image_to_string(dst)
        captcha_value = "".join(filter(self.check_for_integer, captcha))
        sleep(4)

        container = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div/div[1]/div[2]')
        container.find_element_by_tag_name('input').send_keys(captcha_value)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/button').click()

        sleep(2)
        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/a').click()
        except NoSuchElementException:
            self.driver.refresh()
            self.login()

        # group
        self.driver.find_element_by_xpath('//*[@id="categorySelector"]').click()
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(my_niazerooz_group +
                                                                                 ' > ' +
                                                                                 my_niazerooz_sub_group)
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(Keys.RETURN)

        # province
        self.driver.find_element_by_xpath('//*[@id="regionSelector"]').click()
        sleep(2)
        prefix = '/html/body/div[2]/div[2]/form/div/div[5]/div[2]/div/div[2]/div/div/a['
        self._search_(province, prefix, ']')
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div[2]/form/div/div[5]/div[2]/div/div[2]/div/div/a['
        self.search(city, prefix, ']', element=3)

        # title
        self.driver.find_element_by_xpath('//*[@id="Subject"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="Description"]').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="moreInfotxt"]/div[1]/input').send_keys(keywords)

        # Address
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[15]/div[2]/input').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[16]/div[2]/div/input').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="Email"]').send_keys(email)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[20]/div[2]').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(3)

        # submit
        self.driver.find_element_by_xpath('//*[@id="btnSaveAdv"]').click()


class PostAd18(IPostAds):
    """ https://eforosh.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/ul/'
                                          'form[2]/table/tbody/tr[1]/td[2]/p/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/ul/'
                                          'form[2]/table/tbody/tr[2]/td[2]/p/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/'
                                          'ul/form[2]/table/tbody/tr[3]/td/p/input').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/ul/li[1]/a[2]').click()

        # title
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                          'ul/table/tbody/tr[1]/td[2]/p/input').send_keys(title)

        # group
        self.driver.find_element_by_id('subcatid').click()
        prefix = '/html/body/div/div[4]/form/div[2]/div[2]/ul/table/tbody/tr[2]/td[2]/p/select/option['
        self._search(main_group, main_sub_group, prefix, ']', separate_by='->', element=2)

        # description
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                          'ul/table/tbody/tr[3]/td[2]/p/textarea').send_keys(description)

        # picture
        iframe = self.driver.find_element_by_id('uploadframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/div/span/form/input[3]').send_keys(picture)
        self.driver.switch_to.default_content()

        # price
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/'
                                          'div[2]/ul/table/tbody/tr[8]/td[2]/p/input').send_keys(price)

        # Address
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/'
                                          'div[2]/ul/table/tbody/tr[9]/td[2]/p/input').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                          'ul/table/tbody/tr[7]/td[4]/p/input').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords.replace('  ', '\n'))

        # province
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                          'ul/table/tbody/tr[8]/td[4]/p/select').click()
        prefix = '/html/body/div/div[4]/form/div[2]/div[2]/ul/table/tbody/tr[8]/td[4]/p/select/option['
        self.search(province, prefix, ']')

        # submit button
        self.driver.find_element_by_xpath('//*[@id="b1"]').click()


class PostAd19(IPostAds):
    """ http://newagahi.ir/login_register.php """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        sleep(3)
        # close pop up
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/button').click()

        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[1]/input').send_keys(self.username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/'
                                          'section[1]/section/div[2]/form/div[4]/button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('http://newagahi.ir/add_estate.php')
        sleep(3)

        # close pop up
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/button').click()

        # title
        sleep(3)
        self.driver.find_element_by_css_selector('#frm_title').send_keys(title)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[5]/input').send_keys(phone)

        # group & sub-group
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[6]/div[1]/button').click()
        prefix = '/html/body/div[5]/section/div/div/div[2]/div/div[4]/form/div/div[6]/div[1]/ul/li['
        self._search(newagahi_group, newagahi_sub_group, prefix, ']/a', element=2, separate_by=' -- ')
        sleep(2)

        # select type of ads
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[7]/div/button').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div/'
                                          'div[4]/form/div/div[7]/div/ul/li[2]/a').click()

        # province
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[9]/div/button').click()

        prefix = '/html/body/div[5]/section/div/div/div[2]/div/div[4]/form/div/div[9]/div/ul/li['
        self._search_(province, prefix, ']/a')
        sleep(3)

        # city
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[10]/div/button').click()

        prefix = '/html/body/div[5]/section/div/div/div[2]/div/div[4]/form/div/div[10]/div/ul/li['
        self.search(city, prefix, ']/a')
        sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="step1_submit"]').click()
        sleep(3)

        # close pop up
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/button').click()

        # description
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div/'
                                          'div[4]/form/div/div[5]/div/div[6]').send_keys(description)

        # keywords
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[7]/div/input').send_keys(
            keywords.replace('  ', '\n'))

        # price
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/'
                                          'div[2]/div/div[4]/form/div/div[9]/input').send_keys(price)

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[13]/button').click()

        # close pop up
        try:
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/button').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/button').click()

        # picture
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[9]/div/span/input').send_keys(picture)

        # third submit button
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/div/form/div/div[8]/button').click()
        sleep(2)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[5]/button').click()


class PostAd20(IPostAds):
    """ https://71ap.ir/login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)
        sleep(2)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(3)
        self.post()

    def post(self):
        self.driver.get('https://71ap.ir/create-advertising/')
        sleep(2)

        # group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/' \
                 'div/div/select/option['
        self.search(ap_group, prefix, ']', element=2)
        sleep(4)

        # sub group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/' \
                 'div/div[2]/select/option['
        self.search(ap_sub_group, prefix, ']', element=2)
        sleep(3)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/'
                                          'div/div[2]/form/table/tbody/tr[3]/td/div/input').click()

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_mobile"]').send_keys(phone)

        # province
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[1]/div/div[1]/div[6]/span/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)

        # description
        self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/'
                                          'div[2]/form/div[2]/div[2]/div/div[1]/div/p[3]/a').click()

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[2]/div/div[1]/div/div/div[3]/ul/li[1]/div/input').send_keys(picture)

        # ads package
        Select(self.driver.find_element_by_id('ad_pack_id')).select_by_visible_text('بسته 10 روزه رایگان')

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/'
                                          'div/div/div/div[2]/form/input[3]').click()
        sleep(4)
        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/'
                                          'div/div/div/div[2]/form/p[2]/input[2]').click()


class PostAd21(IPostAds):
    """ https://otab.ir/auth *** captcha ***"""
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # delay time for captcha enter & switch into captcha input field
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(10)

        # login button
        self.driver.find_element_by_xpath('/html/body/section/div/div/section[1]/'
                                          'section/div[2]/form/div[5]/div[3]/button').click()

        self.post()

    def post(self):
        try:
            self.driver.get('https://otab.ir/new')
            sleep(2)
        except NoSuchElementException:
            logging.error('Captcha didn\'t entered or is incorrect - https://otab.ir/auth')
            self.login()

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/'
                                          'div/div/div/div[3]/div/span[2]/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(main_group, prefix, ']', element=2)
        sleep(3)

        # sub group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                          'div/div[3]/div/div[1]/span/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(main_sub_group, prefix, ']', element=2)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[7]/input').send_keys(picture)

        # type of ad
        Select(self.driver.find_element_by_id('frm_plan_type')).select_by_visible_text('آگهی رایگان')
        sleep(5)

        # price
        self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)
        sleep(2)

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/'
                                          'div/div/div/div[11]/div/span[2]/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[12]/div/span[2]/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # keyword
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                          'div/div[16]/div/span/span[1]/span/ul/li/input').send_keys(
            keywords.replace('  ', '\n'))

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submit_item"]').click()


class PostAd22(IPostAds):
    """ https://www.agahichi.com/%D9%88%D8%B1%D9%88%D8%AF-%D8%B3%D8%A7%DB%8C%D8%AA.html """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/'
                                          'div/section/section/div/form/input[2]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div/'
                                          'section/section/div/form/input[3]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/'
                                          'div/section/section/div/form/div[2]/input').click()

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div/section/div[2]/'
                                          'div/section/section/div/ul/li[1]/a').click()
        sleep(2)

        # group
        prefix = '/html/body/div/div[1]/section/div/div/section/section/div/div[1]/ul[2]/li/div[1]/select/option['
        self.search(agahichi_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        prefix = '/html/body/div/div[1]/section/div/div/section/section/div/div[1]/ul[2]/li/div[2]/select/option['
        self.search(agahichi_sub_group, prefix, ']', element=2)
        sleep(2)

        # submit group & sub group
        self.driver.find_element_by_xpath('//*[@id="next_step"]').click()
        sleep(2)

        # type of ads
        Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/div/div[2]/'
                                                 'div[2]/div[2]/select')).select_by_visible_text('آگهی رایگان (رایگان)')
        sleep(2)

        # title
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/'
                                          'div/div[2]/div[4]/div[2]/form/div/div[1]/div/div/div[1]/'
                                          'div[2]/input').send_keys(title)
        sleep(4)

        # description
        add_description = True
        try:
            iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/div/'
                                                       'div[2]/div[4]/div[2]/form/div/div[1]/div/div/div[2]/div[2]/'
                                                       'div/div/div/iframe')
            self.driver.switch_to.frame(iframe)
            self.driver.find_element_by_xpath('/html/body').send_keys(description)
            self.driver.switch_to.default_content()
            sleep(2)
        except NoSuchElementException:
            add_description = False
            pass

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/'
                                          'div/div[2]/div[4]/div[2]/form/div/div[1]/div/div/div[4]/'
                                          'div[2]/span/input[1]').send_keys(phone[:4])
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/'
                                          'div/div[2]/div[4]/div[2]/form/div/div[1]/div/div/div[4]/'
                                          'div[2]/span/input[2]').send_keys(phone[4:])
        sleep(1)

        # price
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/div/'
                                          'div[2]/div[4]/div[2]/form/div/div[2]/div/div/div[2]/div[2]/'
                                          'input[1]').send_keys(price)
        sleep(1)

        # province
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/'
                                          'section/div/div[2]/div[4]/div[2]/form/div/div[3]/'
                                          'div/div[2]/div[2]/div[2]/select').click()
        prefix = '/html/body/div[1]/div[1]/section/div/div/section/section/div/div[2]/div[4]/div[2]/' \
                 'form/div/div[3]/div/div[2]/div[2]/div[2]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/'
                                          'section/div/div[2]/div[4]/div[2]/form/div/div[3]/'
                                          'div/div[2]/div[3]/div[2]/select').click()
        prefix = '/html/body/div[1]/div[1]/section/div/div/section/section/div/div[2]/div[4]/div[2]/form/div' \
                 '/div[3]/div/div[2]/div[3]/div[2]/select/option['
        self.search(city, prefix, ']', element=2)
        sleep(2)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/div/'
                                          'div[2]/div[4]/div[3]/div/div[2]/form/div[1]/input').send_keys(picture)
        sleep(2)

        if not add_description:
            iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/section/div/'
                                                       'div[2]/div[4]/div[2]/form/div/div[1]/div/div/div[2]/div[2]/'
                                                       'div/div/div/iframe')
            self.driver.switch_to.frame(iframe)
            self.driver.find_element_by_xpath('/html/body').send_keys(description)
            self.driver.switch_to.default_content()

        # submit button
        for i in range(2):
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/'
                                                  'section/section/div/div[2]/div[4]/div[4]/input').click()
                sleep(2)
            except NoSuchElementException:
                pass


class PostAd23(IPostAds):
    """ http://shetabe.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # captcha
        with open('index.jpg', 'wb') as img_file:
            img_file.write(self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/form/'
                                                             'table/tbody/tr[4]/td[2]/img').screenshot_as_png)
        sleep(1)
        img = cv2.imread('index.jpg')
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        captcha = pytesseract.image_to_string(dst)

        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="capcha"]').send_keys(captcha.replace('.', ''))

        # login button
        try:
            self.driver.find_element_by_xpath('//*[@id="sub"]').click()
            sleep(3)
        except ElementNotInteractableException:
            pass
        self.post()

    @staticmethod
    def __match(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 1:
            return True
        return False

    def __search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self.__match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        try:
            sleep(3)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/div[2]/div/div[1]/a').click()
        except NoSuchElementException:
            self.login()

        # type of ads
        try:
            Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[3]/'
                                                     'td[2]/select')).select_by_visible_text('رایگان تصویری')
        except NoSuchElementException:
            pass

        # group
        prefix = '/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[6]/td[2]/select/option['
        self.search(shetab_group, prefix, ']')
        sleep(3)

        # sub group
        prefix = '/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[6]/td[2]/span[1]/select/option['
        self.search(shetab_sub_group, prefix, ']', element=2)
        sleep(3)

        # sub sub-group
        try:
            prefix = '/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[6]/td[2]/span[2]/select/option['
            self.search(shetab_sub_sub_group, prefix, ']', element=2)
            sleep(2)
        except NoSuchElementException:
            pass

        # province
        prefix = '/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[7]/td[2]/select/option['
        self.__search(province, prefix, ']', element=2)
        sleep(3)

        # city
        prefix = '/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[7]/td[2]/span/select/option['
        self.search(city, prefix, ']', element=2)
        sleep(2)

        # phone
        self.driver.find_element_by_xpath('//*[@id="tell"]').send_keys(phone)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords.replace(' ', '،'))

        # source
        try:
            Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                     'table/tbody/tr[12]/td[2]/select')).select_by_visible_text('عمومی')
        except UnexpectedAlertPresentException:
            pass

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('//*[@id="pic"]').send_keys(picture)
        sleep(1)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # description
        self.driver.find_element_by_xpath('//*[@id="describtion"]').send_keys(description)
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="sub"]').click()


class PostAd24(IPostAds):
    """ http://iran-tejarat.com/LoginPage.aspx """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="UserNameTextbox"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="PassTextbox"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="AddButton"]').click()
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a').click()

        # group
        try:
            select_group = Select(self.driver.find_element_by_xpath('//*[@id="MainCatDropdown"]'))
            select_group.select_by_visible_text(main_group)
            sleep(2)
        except NoSuchElementException:
            prefix = '/html/body/form/div[4]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/div[1]/select/option['
            self.search(main_group, prefix, ']')
            sleep(2)

        # sub group
        try:
            select_sub_group = Select(self.driver.find_element_by_xpath('//*[@id="SubCategoryDropdown"]'))
            select_sub_group.select_by_visible_text(main_sub_group)
        except NoSuchElementException:
            prefix = '/html/body/form/div[4]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/select/option['
            self.search(main_sub_group, prefix, ']')
            sleep(2)

        # title
        self.driver.find_element_by_xpath('//*[@id="TitleTextbox"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="DetailTextbox"]').send_keys(description)

        # province
        try:
            select_province = Select(self.driver.find_element_by_xpath('//*[@id="StateDropdown"]'))
            select_province.select_by_visible_text(province)
        except NoSuchElementException:
            prefix = '/html/body/form/div[4]/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[1]/select/option['
            self.search(province, prefix, ']')

        # city
        self.driver.find_element_by_xpath('//*[@id="CityTextbox"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="txtAddress"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/'
                                          'div[2]/div[6]/div[5]/div[1]/div/input').send_keys(phone)

        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # submit button
        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/span[2]/input').click()
        sleep(7)

        # picture
        self.driver.find_element_by_xpath('//*[@id="UploadPicFile1"]').send_keys(picture)

        # final submit button
        for i in range(2):  # if picture didn't fit in
            try:
                self.driver.find_element_by_xpath('//*[@id="btnSubmitPicture"]').click()
                sleep(2)
            except ElementClickInterceptedException:
                pass


class PostAd25(IPostAds):
    """ http://sabzads.com/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(12)   # delay time for entering captcha

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[5]/div[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('http://sabzads.com/new')
        sleep(3)

        # title
        try:
            self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/header/div/nav/div[1]/div[3]/a').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # email
        try:
            self.driver.find_element_by_xpath('//*[@id="register_param"]').send_keys(email)
        except NoSuchElementException:
            pass

        # group
        try:
            select_group = Select(self.driver.find_element_by_xpath('//*[@id="select-category"]'))
            select_group.select_by_visible_text(other_group)

        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div/div/'
                                              'div/div[2]/div/span[2]/span[1]/span').click()
            prefix = '/html/body/span/span/span[2]/ul/li['
            self.search(other_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        try:
            select_sub_group = Select(self.driver.find_element_by_xpath('//*[@id="select-subcategory"]'))
            select_sub_group.select_by_visible_text(other_sub_group)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div/div/div/'
                                              'div[2]/div/div[1]/span/span[1]/span').click()
            prefix = '/html/body/span/span/span[2]/ul/li['
            self.search(other_sub_group, prefix, ']', element=2)
        sleep(2)

        # sub sub-group
        if other_sub_sub_group:
            try:
                default_choice = 'متفرقه'
                select_sub_sub_group = Select(self.driver.find_element_by_xpath('/html/body/section/div/'
                                                                                'div/div/form/div[2]'
                                                                                '/div/div/div/div[2]/'
                                                                                'div/div[2]/select'))
                try:
                    select_sub_sub_group.select_by_visible_text(default_choice)
                except NoSuchElementException:
                    select_sub_sub_group.select_by_visible_text(other_sub_sub_group)

            except NoSuchElementException:
                prefix = '/html/body/section/div/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/select/option['
                self.search(other_sub_sub_group, prefix, ']', element=2)
        sleep(2)

        # type ads
        Select(self.driver.find_element_by_xpath('//*[@id="frm_plan_type"]')).select_by_visible_text('آگهی رایگان')

        # picture
        self.driver.find_element_by_xpath('/html/body/div[7]/input').send_keys(picture)
        sleep(2)

        # price
        self.driver.find_element_by_id('price').send_keys(price)

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)

        # province
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div/div/div/'
                                              'div[10]/div/span[2]/span[1]/span/span[1]').click()
            sleep(2)
            prefix = '/html/body/span/span/span[2]/ul/li['
            self._search_(province, prefix, ']', element=2)
        except NoSuchElementException:
            pass
        sleep(2)

        # city
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div/div/'
                                              'div/div[11]/div/span[2]/span[1]/span/span[1]').click()
            sleep(2)
            prefix = '/html/body/span/span/span[2]/ul/li['
            self.search(city, prefix, ']', element=2)

        except NoSuchElementException:
            pass

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div/div/div/'
                                          'div[14]/div/span/span[1]/span/ul/li/input').send_keys(
            keywords.replace(' ', '\n'))

        # submit button
        for i in range(2):
            try:
                self.driver.find_element_by_xpath('//*[@id="submit_item"]').click()
                sleep(2)
            except NoSuchElementException:
                pass


class PostAd26(IPostAds):
    """ http://www.tejaari.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Navigate to login page
        self.driver.find_element_by_xpath('/html/body/div[2]/header/nav/div[2]/div[3]/a').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/'
                                          'div[2]/form/div/div/label[1]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/'
                                          'form/div/div/label[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[2]/a').click()
        sleep(4)
        self.post()

    def post(self):
        self.driver.get('http://www.tejaari.com/Advertisement/adnew')
        sleep(3)

        # ads type
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                              'form/div/div[1]/label[1]/div[2]/span').click()
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/div/'
                                              'div[1]/label[1]/div[2]/ul/li[2]').click()
            sleep(2)
        except NoSuchElementException:
            pass

        # period
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[1]/label[2]/div[2]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/'
                                          'div/div[1]/label[2]/div[2]/ul/li[2]').click()

        # group
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[2]/label[1]/div[1]').click()
        sleep(3)

        prefix = '/html/body/div[2]/div[7]/div/div/div[1]/form/div/div[2]/label[1]/div[2]/div[2]/ul/li['
        self.search(tejjari_group, prefix, ']')
        sleep(2)

        # sub group
        prefix = '/html/body/div[2]/div[7]/div/div/div[1]/form/div/div[2]/label[1]/div[2]/div[2]/ul/li['
        self.search(tejjari_sub_group, prefix, ']')
        sleep(2)

        # sub sub-group
        if tejjari_sub_sub_group:
            prefix = '/html/body/div[2]/div[7]/div/div/div[1]/form/div/div[2]/label[1]/div[2]/div[2]/ul/li['
            self.search(tejjari_sub_sub_group, prefix, ']')
            sleep(2)

        # sub sub sub-group
        if tejjari_sub_sub_sub_group:
            prefix = '/html/body/div[2]/div[7]/div/div/div[1]/form/div/div[2]/label[1]/div[2]/div[2]/ul/li['
            self.search(tejjari_sub_sub_sub_group, prefix, ']')
        sleep(2)

        # title
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/'
                                          'div[1]/form/div/div[2]/label[2]/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/'
                                          'div[1]/form/div/div[2]/label[3]/textarea').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[2]/label[4]/div/div[1]/input').send_keys(
            keywords.replace(' ', '\n'))

        # picture
        self.driver.find_element_by_xpath('//*[@id="imgInp"]').send_keys(picture)

        # name
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[3]/label[1]/input').send_keys(name)

        # province
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/div/div[3]/label[2]/a').click()
        sleep(2)
        prefix = '/html/body/div[2]/div[3]/div/div[2]/div[1]/ul/li['
        self._search_(province, prefix, ']/span')
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/ul['
        self.search(city, prefix, ']/li/span')

        # address
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[3]/label[3]/input').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/'
                                          'div/div[3]/label[4]/div/div[1]/input').send_keys(phone + '\n')

        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/'
                                          'div/div[3]/label[5]/div/div[1]/input').send_keys(phone + '\n')

        # email
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/'
                                          'form/div/div[3]/label[7]/input').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/'
                                          'div[1]/form/div/div[3]/label[8]/input').send_keys(website_link)
        sleep(1)

        # close alert
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]').click()
            sleep(2)
        except NoSuchElementException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div[1]/form/div/input').click()


class PostAd27(IPostAds):
    """ https://sellfree.ir/?d=login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="darkoobusername"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="darkoobpassword"]').send_keys(self.password)

        # click the checkbox
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/input').click()

        # login button
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        self.post()

    def post(self):
        self.driver.get('https://sellfree.ir/?d=darsubmit')

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-categoryselect-container"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(main_group)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.RETURN)

        # title
        self.driver.find_element_by_xpath('//*[@id="darkoobtitle"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="darkoobdescid"]').send_keys(description)

        # phone
        information = self.driver.find_element_by_css_selector('#togglecontact')
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        actions = ActionChains(self.driver)
        actions.move_to_element(information)
        actions.click().perform()

        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="darkoobtel"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="darkoobmail"]').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="darkoobwebsite"]').send_keys(website_link)

        # country
        sleep(1)
        self.driver.execute_script("document.getElementById('select2-countryselect-container').scrollIntoView();")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/form/'
                                          'div[2]/div[10]/div[5]/div/span/span[1]/span').click()

        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('ایران')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.RETURN)

        # province
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/form/div[2]/'
                                          'div[10]/div[6]/div/span/span[1]/span').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(province)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.RETURN)

        # city
        self.driver.find_element_by_xpath('//*[@id="select2-cityselect-container"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(city + ' ')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.RETURN)

        # address
        self.driver.find_element_by_xpath('//*[@id="khiaban"]').send_keys(address)

        # price
        self.driver.find_element_by_xpath('//*[@id="togglepricesection"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="darkoobprice"]').send_keys(price)

        # submit button
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/form/div[2]/div[16]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()


class PostAd28(IPostAds):
    """ https://googleagahi.com/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # captcha time delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[5]/div[3]/button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://googleagahi.com/new')
        self.driver.maximize_window()

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # email
        try:
            self.driver.find_element_by_xpath('//*[@id="register_param"]').send_keys(email)
        except NoSuchElementException:
            pass

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-select-category-container"]').click()
        sleep(1)

        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(other_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        self.driver.find_element_by_xpath('//*[@id="select2-select-subcategory-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(other_sub_group, prefix, ']', element=2)
        sleep(2)

        # some sub groups have other sub groups
        try:
            self.driver.find_element_by_xpath('//*[@id="select2-select-subsidiary-container"]').click()
            sleep(1)
            if other_sub_sub_group:
                try:
                    default_choice = 'متفرقه'
                    prefix = '/html/body/span/span/span[2]/ul/li['
                    self.search(default_choice, prefix, ']', element=2)

                except NoSuchElementException:
                    self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                                      'div/div[2]/div/div[2]/span/span[1]/span/span[1]').click()

                    prefix = '/html/body/span/span/span[2]/ul/li['
                    self.search(other_sub_sub_group, prefix, ']', element=2)
            sleep(2)
        except NoSuchElementException:
            pass

        # price
        try:
            self.driver.find_element_by_id('price').send_keys(price)
        except NoSuchElementException:
            pass

        # picture
        self.driver.find_element_by_xpath('/html/body/div[10]/input').send_keys(picture)
        sleep(5)

        # ads type
        self.driver.find_element_by_xpath('//*[@id="select2-frm_plan_type-container"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        sleep(2)

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                          'div/div[10]/div/span[2]/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                          'div/div[11]/div/span[2]/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/'
                                          'div/div[15]/div/span/span[1]/span/ul/li/input').send_keys(
            keywords.replace('  ', '\n'))

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 2);')
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd29(IPostAds):
    """ https://www.netmoj.ir/ *** captcha ***"""
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[1]/li[12]/a').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtusr"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_passtxt"]').send_keys(self.password)

        # captcha delay
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_kalameamnyatitxt"]').click()
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_voroodbtn"]').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.maximize_window()
        self.driver.get("https://www.netmoj.ir/%D8%AB%D8%A8%D8%AA-"
                        "%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86-%D8"
                        "%A2%DA%AF%D9%87%DB%8C")
        sleep(2)

        # title
        self.driver.find_element_by_xpath('//*[@id="title_agahi"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="description_agahi"]').send_keys(description)

        # name
        self.driver.find_element_by_xpath('//*[@id="flname_user"]').clear()
        self.driver.find_element_by_xpath('//*[@id="flname_user"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="mobile_user"]').clear()
        self.driver.find_element_by_xpath('//*[@id="mobile_user"]').send_keys(phone)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div/form/div[4]/div[2]/div/input[1]').send_keys(picture)
        sleep(1)

        # group
        self.driver.find_element_by_xpath('//*[@id="select_cat"]').click()
        sleep(2)

        prefix = '/html/body/div[1]/div/form/div[4]/div[1]/div[1]/div/div/ul/li['
        first_list_element = self.search(netmoj_group, prefix, ']')
        sleep(1)

        # sub_group
        prefix = '/html/body/div[1]/div/form/div[4]/div[1]/div[1]/div/div/ul/li[' + str(first_list_element) + ']/ul/li['
        second_list_element = self.search(netmoj_sub_group, prefix, ']/a')
        sleep(2)

        if netmoj_sub_sub_group:
            prefix = '/html/body/div[1]/div/form/div[4]/div[1]/div[1]/div/div/ul/li[' + str(first_list_element) + \
                     ']/ul/li[' + str(second_list_element) + ']/ul/li['
            self.search(netmoj_sub_sub_group, prefix, ']/a')
        sleep(2)

        # price
        try:
            self.driver.find_element_by_xpath('//*[@id="price_agahi"]').send_keys(price)
        except ElementNotInteractableException:
            pass

        # province
        self.driver.find_element_by_xpath('//*[@id="select_ostan"]').click()
        sleep(2)
        prefix = '/html/body/div[1]/div/form/div[4]/div[1]/div[3]/div/div/ul/li['
        province_id = self._search_(province, prefix, ']/a')

        # city
        prefix = '/html/body/div[1]/div/form/div[4]/div[1]/div[3]/div/div/ul/li[' + str(province_id) + ']/ul/li['
        self.search(city, prefix, ']/a')
        sleep(2)

        # ads period
        self.driver.find_element_by_xpath('//*[@id="select_type_agahi2"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/form/div[4]/div[1]/div[4]/div/div/ul/li[1]/a').click()

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[1]/div/form/div[4]/div[1]/input[6]').send_keys(website_link)
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/form/div[4]/div[2]/p/a').click()


class PostAd30(IPostAds):
    """ https://payameavval.net/login.aspx """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1'
                                          '_Login1_UserName"]').send_keys(self.username)
        
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1'
                                          '_Login1_Password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Login1_LoginButton"]').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.get('https://payameavval.net/users/AddNotice.aspx')

        # title
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtTitle"]').send_keys(title)

        # group
        prefix = '/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/' \
                 'div[5]/div[1]/div/div[1]/div/select/option['
        self.search(main_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        prefix = '/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/' \
                 'div[5]/div[2]/div/div[1]/div/select/option['
        self.search(main_sub_group, prefix, ']', element=2)
        sleep(2)

        # ads period
        Select(self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_cboNoticeTime"]'))\
            .select_by_visible_text('یک ماه')

        # province
        prefix = '/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/' \
                 'div[2]/div[9]/div[1]/div/div/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/' \
                 'div[2]/div[9]/div[2]/div/div/div/select/option['
        self.search(city, prefix, ']', element=2)
        sleep(2)

        # description
        iframe = self.driver.find_element_by_xpath('/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/'
                                                   'div[3]/div/div/div[1]/div/div/div/div/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p').send_keys(description)
        sleep(2)
        self.driver.switch_to.default_content()

        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtDesc"]').send_keys(description)

        # phone
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPhone"]').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtAddress"]').send_keys(address)

        # email
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtEmail"]').send_keys(email)

        # price
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPrice"]').send_keys(price)

        # picture
        # we need to switch between 2 windows
        windows_before = self.driver.window_handles[0]  # main window

        self.driver.find_element_by_xpath('/html/body/div/form/div[3]/div[2]/div/div/div[2]/div[3]/div[9]/'
                                          'div[2]/div[1]/div/button[1]').click()
        sleep(2)
        windows_after = self.driver.window_handles[1]  # picture window
        self.driver.switch_to.window(windows_after)

        self.driver.find_element_by_xpath('//*[@id="file"]').send_keys(picture)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="btnCrop"]').click()
        sleep(1)
        self.driver.switch_to.window(windows_before)
        sleep(2)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtKey"]').send_keys(
            keywords.replace('  ', '\n'))

        # submit button
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnSave"]').click()


class PostAd31(IPostAds):
    """ http://xoonarg.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('//*[@id="nasim_logpop"]').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/form/input[1]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/form/input[2]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/form/input[3]').click()
        sleep(2)

        self.post()

    def _search(self, group, sub_group, prefix, suffix, separate_by='', element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).split(separate_by)

                try:
                    if self._match(sub_group, pattern_txt[0].strip()):
                        pattern.click()
                        return element
                except IndexError:
                    pass

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        self.driver.get('http://xoonarg.com/%d8%a7%db%8c%d8%ac%d8%a7%d8%af-%d8%a2%da%af%d9%87%db%8c/')

        # group
        prefix = '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/li[2]/div[2]/div/select/option['
        self.search(xoonrang_group, prefix, ']', element=2)
        sleep(3)

        # sub group
        prefix = '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/li[2]/div[2]/div[2]/select/option['
        self._search('', xoonrang_sub_group, prefix, ']', element=2, separate_by='-')
        sleep(3)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/'
                                          'div/div[2]/form/ol/li[2]/div[3]/input').click()
        sleep(2)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # province
        prefix = '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/span/li[4]/select/option['
        self.search(province, prefix, ']', element=2)

        # city
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').send_keys(city)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/'
                                          'div/div[2]/form/ol/span/li[8]/input').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/'
                                          'div/div[2]/form/ol/span/li[9]/input').send_keys(email)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords)

        # description
        iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/'
                                                   'ol/span/li[11]/div[2]/div[2]/div[2]/div/div[2]/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p').send_keys(description)
        sleep(2)
        self.driver.switch_to.default_content()

        # second Email input
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/'
                                          'div/div[2]/form/ol/span/li[12]/input').send_keys(email)
        sleep(2)

        # picture
        self.driver.find_element_by_css_selector('#app-attachment-upload-container > div.app-attachment-info'
                                                 ' > p.small.upload-flash-bypass > a').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#upload_1 > input.fileupload').send_keys(picture)

        # second submit button
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/p/input').click()
        sleep(5)

        # final submit button
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/'
                                          'div[1]/div/div[2]/form/p[2]/input[2]').click()
        sleep(4)

        # show the ad
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/button').click()


class PostAd32(IPostAds):
    """ https://agahiaria.ir/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[1]/div/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[2]/div/input').send_keys(self.password)
        
        # captcha delay
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[4]/div/input').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[5]/div[3]/button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://agahiaria.ir/new')

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[2]/div/span[2]/span[1]/span/span[1]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(main_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div'
                                          '/div/div[2]/div/div[1]/span/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(main_sub_group, prefix, ']', element=2)
        sleep(2)

        try:
            # phone
            self.driver.find_element_by_xpath('//*[@id="register_param"]').send_keys(phone)
        except NoSuchElementException:
            pass

        # price
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/'
                                          'div/div/div/div[6]/div/div[1]/input').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[9]/input').send_keys(picture)
        sleep(3)

        # ads type
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[3]/div/span[2]/span[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        sleep(2)

        # description
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/'
                                          'div/div/div/div[7]/div/textarea').send_keys(description)
        sleep(2)

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[10]/div/span[2]/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[11]/div/span[2]/span[1]/span').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)

        # phone
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/'
                                          'div[1]/div/div/div/div[12]/div/input').send_keys(phone)

        try:
            # keywords
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/'
                                              'div[14]/div/span/span[1]/span/ul/li/input').send_keys(
                keywords.replace('  ', '\n'))

        except ElementNotInteractableException:
            pass

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd33(IPostAds):
    """ http://darsanat.ir/login_register.php """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[4]/button').click()
        sleep(3)
        self.post()

    def post(self):
        self.driver.get('http://darsanat.ir/new')

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # group & sub-group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/'
                                          'div[3]/form/div/div[6]/div[1]/button').click()
        sleep(2)
        prefix = '/html/body/section/div/div/div/div/div[3]/form/div/div[6]/div[1]/ul/li['
        self._search(darsanat_group, darsanat_sub_group, prefix, ']/a/span', element=2, separate_by=' -- ')

        # ads type
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div[3]/form/'
                                          'div/div[7]/div/button/span[1]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div[3]/form/'
                                          'div/div[7]/div/ul/li[2]/a/span').click()

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/'
                                          'div[3]/form/div/div[9]/div/button').click()
        prefix = '/html/body/section/div/div/div/div/div[3]/form/div/div[9]/div/ul/li['
        sleep(1)
        self._search_(province, prefix, ']/a/span', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/'
                                          'div[3]/form/div/div[10]/div/button').click()
        sleep(1)
        prefix = '/html/body/section/div/div/div/div/div[3]/form/div/div[10]/div/ul/li['
        self.search(city, prefix, ']/a/span', element=2)
        sleep(2)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="step1_submit"]').click()
        sleep(5)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)
        sleep(2)

        # description
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div[3]/form/div/div[1]/'
                                          'div/div[7]/div/div[6]/p').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div[3]/form/div/div[1]/'
                                          'div/div[9]/div/input').send_keys(
            keywords.replace('  ', '\n'))

        # picture
        self.driver.find_element_by_xpath('/html/body/div[6]/input').send_keys(picture)
        sleep(4)

        # second submit button
        self.driver.find_element_by_xpath('//*[@id="step2_submit"]').click()
        sleep(4)

        # final submit button
        self.driver.find_element_by_xpath('//*[@id="payment_submit"]').click()


class PostAd34(IPostAds):
    """ https://ruzandish.com/%d9%88%d8%b1%d9%88%d8%af/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)
        path = 'chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(executable_path=path, options=options)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/article/div/div/div/form/fieldset/'
                                          'label[1]/input').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/article/div/div/div/form/fieldset/'
                                          'label[2]/input').send_keys(self.password)
        # login button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/article/div/div/div/form/'
                                          'fieldset/input[2]').click()
        sleep(4)
        self.post()

    @staticmethod
    def _match(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 1:
            return True
        return False

    def search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        self.driver.get('https://ruzandish.com/%d8%a7%db%8c%d8%ac%d8%a7%d8%af-%d8%a2%da%af%d9%87%db%8c/')

        # group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/div/' \
                 'select/option['
        self.search(ruzandish_group, prefix, ']')
        sleep(3)
        
        # sub-group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/div[2]/' \
                 'select/option['
        self.search(ruzandish_sub_group, prefix, ']')
        sleep(3)

        # sub sub-group
        if ruzandish_sub_sub_group:
            prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/div[3]/' \
                     'select/option['
            self.search(ruzandish_sub_sub_group, prefix, ']', element=2)
            sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/'
                                          'table/tbody/tr[3]/td/div/input').click()
        sleep(5)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_mobile"]').send_keys(phone)

        # Registration Email
        try:
            self.driver.find_element_by_xpath('//*[@id="cp_register_email"]').send_keys(email)
        except NoSuchElementException:
            pass

        # email
        self.driver.find_element_by_xpath('//*[@id="cp_mail"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_mail"]').send_keys(email)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-cp_state-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']')
        sleep(2)

        # city
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/div/div[1]/div[6]/' \
                 'select/option['
        self.search(city, prefix, ']', element=2)
        sleep(2)

        # keywords
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
        #                                   'div[1]/div/div[1]/div[12]/span/span[1]/span/ul/li/input').click()
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
        #                                   'div[1]/div/div[1]/div[12]/span/span[1]/span/ul/li/input').send_keys(
        #     keywords.replace('  ', '\n'))

        # description
        self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_phone"]').send_keys(phone)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[2]/div/div[1]/div/p[3]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[2]/'
                                          'div/div[1]/div/div/div[3]/ul/li[1]/div/input').send_keys(picture)
        sleep(5)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/input[3]').click()
        sleep(6)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/p[2]/'
                                          'input[2]').click()
        sleep(5)


class PostAd35(IPostAds):
    """ https://100nama.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('/html/body/section/div[1]/div/'
                                          'div/div/div[2]/form/div[1]/div/input').send_keys(self.username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/section/div[1]/div/'
                                          'div/div/div[2]/form/div[2]/div/input').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div/div[2]/form/div[4]/div/button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://100nama.com/user/submit-ad')

        # group
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/'
                                          'div[2]/div/div[1]/div[1]/div/div/button').click()
        sleep(1)
        prefix = '/html/body/section/div[4]/div/div/div[2]/ul/li['
        sub_group_id = self.search(nama_group, prefix, ']/a')
        sleep(2)

        # sub group
        prefix = '/html/body/section/div[4]/div/div/div[2]/ul/li[' + str(sub_group_id) + ']/ul/li['
        sub_sub_group_id = self.search(nama_sub_group, prefix, ']/a')
        sleep(2)

        # sub sub-group
        if nama_sub_sub_group:
            prefix = '/html/body/section/div[4]/div/div/div[2]/ul/li[' + str(sub_group_id) + ']/ul/li[' + \
                     str(sub_sub_group_id) + ']/ul/li['
            self.search(nama_sub_sub_group, prefix, ']/a')
            sleep(2)

        # title
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/'
                                          'div[1]/div[2]/div/div[1]/div[3]/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/'
                                          'div[2]/div/div[1]/div[4]/textarea').send_keys(description)

        # phone
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/'
                                          'div[2]/div/div[1]/div[7]/div/input').clear()
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/'
                                          'div[1]/div[2]/div/div[1]/div[7]/div/input').send_keys(phone)

        # ads type
        try:
            self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/'
                                              'div[2]/div/div[1]/div[8]/div/select/option[3]').click()
        except ElementNotInteractableException:
            pass

        # city
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/div[2]/'
                                          'div/div[1]/div[9]/div/span/span[1]/span').click()

        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']')

        # picture
        self.driver.find_element_by_xpath('/html/body/section/form/div[1]/div/div/div[1]/div[2]/div/div[2]/'
                                          'div[1]/div/div[2]/button').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="agree_terms"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="activate-step-2"]').click()
        sleep(3)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/section/form/div[2]/div/div/div/div[2]/button').click()


class PostAd36(IPostAds):
    """ https://niazmandyha.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div/form/fieldset/div[4]/div/'
                                          'button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://niazmandyha.ir/newAd')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # group
        prefix = '/html/body/main/div/div[2]/div/div/div/form/div[3]/select/option['
        self.search(agahimax_group, prefix, ']', element=2)
        sleep(2)

        # price
        self.driver.find_element_by_xpath('//*[@id="cost"]').send_keys(price)

        # description
        iframe = self.driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/form/div[5]/div/'
                                                   'div/div/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p').send_keys(description)
        sleep(1)
        self.driver.switch_to.default_content()

        # province
        prefix = '/html/body/main/div/div[2]/div/div/div/form/div[8]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/main/div/div[2]/div/div/div/form/div[9]/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # keywords
        self.driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/form/div[13]/div/input').send_keys(
            keywords.replace('  ', '\n'))

        # picture
        self.driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/form/div[16]/label').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)
        
        # first submit button
        self.driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/form/div[18]/button').click()
        sleep(5)

        # final submit button
        self.driver.find_element_by_xpath('//*[@id="continueBtn"]').click()
        sleep(2)
        pyautogui.press('enter')


class PostAd37(IPostAds):
    """ https://www.2fanoos.com/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/'
                                          'div[2]/form/div[5]/div[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('https://www.2fanoos.com/new')

        # maximize the window
        self.driver.maximize_window()

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[2]/'
                                          'div/span[2]/span[1]/span/span[1]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(fanoos_group, prefix, ']', element=2)
        sleep(2)

        # sub group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[2]/'
                                          'div/div[1]/span/span[1]/span/span[1]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(fanoos_sub_group, prefix, ']', element=2)
        sleep(2)

        # ads type
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[3]/div/span[2]/'
                                          'span[1]/span/span[1]').click()
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()

        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div[1]/div/div[2]/'
                                              'div[1]/div/input').send_keys(email)
        except NoSuchElementException:
            pass

        # picture
        self.driver.find_element_by_xpath('/html/body/div[8]/input').send_keys(picture)
        sleep(2)

        # price
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/'
                                          'div/div/div[6]/div/div[1]/input').send_keys(price)
        
        # description
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/'
                                          'div[7]/div/textarea').send_keys(description)

        # website_link
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/'
                                          'div[8]/div/input').send_keys(website_link)

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[10]/div/'
                                          'span[2]/span[1]/span/span[1]').click()

        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[11]/div/'
                                          'span[2]/span[1]/span/span[1]').click()

        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[12]/'
                                          'div/input').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[14]/div/span/'
                                          'span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd38(IPostAds):
    """ https://www.2mihan.com/login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/section/div/div/'
                                          'div[1]/div/form/div[1]/input').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/section/div/div/div[1]/'
                                          'div/form/div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="sb_login_submit"]').click()
        sleep(6)
        self.post()

    def post(self):
        self.driver.get('https://www.2mihan.com/post-ad/')

        # title
        self.driver.find_element_by_xpath('//*[@id="ad_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-ad_cat-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(mihan_group, prefix, ']')
        sleep(6)

        # sub group
        self.driver.find_element_by_xpath('//*[@id="select2-ad_cat_sub-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(mihan_sub_group, prefix, ']')
        sleep(6)

        if mihan_sub_sub_group:
            try:
                self.driver.find_element_by_xpath('//*[@id="select2-ad_cat_sub_sub-container"]').click()
                prefix = '/html/body/span/span/span[2]/ul/li['
                self.search(mihan_sub_sub_group, prefix, ']')
                sleep(2)
            except NoSuchElementException:
                pass

        # country
        try:
            self.driver.find_element_by_xpath('//*[@id="select2-ad_country-container"]').click()
        except ElementNotInteractableException:
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="select2-ad_country-container"]').click()

        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        sleep(5)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-ad_country_states-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']')
        sleep(5)

        # city
        self.driver.find_element_by_xpath('//*[@id="select2-ad_country_cities-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']')
        sleep(4)

        # address
        self.driver.find_element_by_xpath('//*[@id="sb_user_address"]').send_keys(address)

        # description
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div/div/form/div[1]/'
                                          'div[2]/div/div[2]/div/div[3]').send_keys(description)
        sleep(1)

        # ads type
        self.driver.find_element_by_xpath('//*[@id="select2-buy_sell-container"]').click()
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[4]').click()

        # price
        self.driver.find_element_by_xpath('//*[@id="ad_price"]').send_keys(price)

        # picture
        try:
            self.driver.find_element_by_xpath('//*[@id="dropzone"]').click()
            sleep(2)
            pyautogui.write(f'{picture}')
            sleep(1)
            pyautogui.press("enter")
            sleep(2)

        except ElementNotInteractableException:
            pass

        # keywords
        try:
            self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div/section/div/div/div/form/div[1]/'
                                              'div[2]/div/div[3]/div/div[9]/div/div/div[1]/input').send_keys(
                keywords.replace('  ', ','))
        except NoSuchElementException:
            pass

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div/div/form/div[1]/'
                                          'div[2]/div/div[3]/div/div[8]/div/input').send_keys(website_link)

        # submit button
        element = self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div/div/form/'
                                                    'div[2]/div/div/div[12]/div/button')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


class PostAd39(IPostAds):
    """ https://3030l.net/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[1]/div/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[2]/'
                                          'div/input').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[4]/'
                                          'div/input').click()
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[5]/'
                                          'div[3]/button').click()
        self.driver.maximize_window()
        self.post()

    def post(self):
        self.driver.get('https://3030l.net/new')

        # title
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[1]/div/'
                                          'input').send_keys(title)

        # closing the ads
        try:
            self.driver.find_element_by_xpath('/html/body/div[14]/div[2]/svg').click()
            sleep(2)
        except NoSuchElementException:
            pass

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-select-category-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(cicil_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        self.driver.find_element_by_xpath('//*[@id="select2-select-subcategory-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(cicil_sub_group, prefix, ']', element=2)
        sleep(2)

        if cicil_sub_sub_group:
            self.driver.find_element_by_xpath('//*[@id="select2-select-subsidiary-container"]').click()
            prefix = '/html/body/span/span/span[2]/ul/li['
            self.search(cicil_sub_sub_group, prefix, ']', element=2)
            sleep(2)

        # ads type
        self.driver.find_element_by_xpath('//*[@id="select2-frm_plan_type-container"]').click()
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        sleep(3)

        # price
        try:
            self.driver.find_element_by_id('price').send_keys(price)
        except NoSuchElementException:
            self.driver.find_element_by_id('frm_price').send_keys(price)

        # description
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[7]/div/'
                                          'textarea').send_keys(description)

        # picture
        try:
            self.driver.find_element_by_xpath('/html/body/div[10]/input').send_keys(picture)
        except NoSuchElementException:
            pass

        # email or phone <this field appear if we don't login>
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div[1]/div/div[2]/div[1]/div/'
                                              'input').send_keys(email)
        except NoSuchElementException:
            pass

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-state_id-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(5)

        # phone
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[12]/div/'
                                          'input').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[14]/div/span/'
                                          'span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))
        sleep(6)

        # city
        self.driver.find_element_by_xpath('//*[@id="select2-city_id-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)
        sleep(2)

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd40(IPostAds):
    """ https://www.3ervice.com/%d9%88%d8%b1%d9%88%d8%af/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(1)
        self.post()

    def post(self):
        self.driver.get('https://www.3ervice.com/%d8%a7%db%8c%d8%ac%d8%a7%d8%af-%d8%a2%da%af%d9%87%db%8c/')

        # group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/' \
                 'div/select/option['
        self.search(service_group, prefix, ']', element=2)
        sleep(5)

        # sub group
        prefix = '/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/div[2]/' \
                 'select/option['
        self.search(service_sub_group, prefix, ']', element=2)
        sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="getcat"]').click()
        sleep(4)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-cp_state-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="select2-cp_state-container"]').click()

        # address
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/'
                                          'div/div[1]/div[4]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/'
                                          'div/div[1]/div[4]/input').send_keys(address)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[2]/'
                                          'div/div[1]/div/p[3]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[2]/'
                                          'div/div[1]/div/div/div[3]/ul/li[1]/div/input').send_keys(picture)

        # description
        self.driver.find_element_by_xpath('//*[@id="post_content"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/'
                                          'div/div[1]/div[6]/span/span[1]/span/ul/li/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/'
                                          'div/div[1]/div[6]/span/span[1]/span/ul/li/input').send_keys(
            keywords.replace('  ', '\n'))

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[1]/div/div[1]/div[8]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[1]/div/div[1]/div[8]/input').send_keys(phone)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/div/'
                                          'div[1]/div[9]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/div/'
                                          'div[1]/div[9]/input').send_keys(website_link)
        sleep(2)

        # scroll down
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/'
                                                    'form/input[3]')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click(on_element=element)
        action.perform()
        sleep(2)

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/input[3]').click()
        sleep(5)

        # third submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/form/p[2]/input[2]')\
            .click()
        sleep(5)

        # show ads
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/button').click()
        except NoSuchElementException:
            pass


""" 
    PostAd7 has the same page with the classes 41-58
    PostAd47 & PostAd45 have special search method that will be inherited in other classes
"""


class PostAd41(PostAd7):
    """ https://www.rahnama118.com/framework/user/login """
    def group_search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def ads_page(self):
        page = 'https://www.rahnama118.com/ads/addprop'
        group = rahnama_group
        sub_group = rahnama_sub_group
        return page, group, sub_group, province, ''


class PostAd42(PostAd7):
    """ https://www.takniaz.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.takniaz.com/ads/addprop'
        group = takniz_group
        sub_group = takniz_sub_group
        return page, group, sub_group, takniz_province, 'nds'


class PostAd43(PostAd7):
    """ https://www.novin-tejarat.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.novin-tejarat.com/ads/addprop'
        group = novin_tejarat_group
        sub_group = novin_tejarat_sub_group
        return page, group, sub_group, province, ''


class PostAd44(PostAd7):
    """ https://www.ptweb.ir/framework/user/login """
    def ads_page(self):
        page = 'https://www.ptweb.ir/ads/addprop'
        group = ptweb_group
        sub_group = ptweb_sub_group
        return page, group, sub_group, province, 'nds'


class PostAd45(PostAd7):
    """ https://www.payamsara.com/framework/user/login """
    @staticmethod
    def _match_(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2):
            return True
        return False

    def group_search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match_(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def ads_page(self):
        page = 'https://www.payamsara.com/ads/addprop'
        group = payamsara_group
        sub_group = payamsara_sub_group
        return page, group, sub_group, province, 'nds'


class PostAd46(PostAd45):
    """ https://www.tablegh118.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.tablegh118.com/ads/addprop'
        group = tablegh118_group
        sub_group = tablegh118_sub_group
        return page, group, sub_group, province, ''


class PostAd47(PostAd7):
    """ https://www.protabligh.com/framework/user/login """
    @staticmethod
    def _match_(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 1:
            return True
        return False

    def group_search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match_(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def ads_page(self):
        page = 'https://www.protabligh.com/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd48(PostAd47):
    """ https://www.agahibartar.net/framework/user/login """
    def ads_page(self):
        page = 'https://www.agahibartar.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd49(PostAd47):
    """ https://www.myniazmandi.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.myniazmandi.com/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd50(PostAd45):
    # TODO: need to fix some bug in province choice
    """ https://www.niazmandi-iran.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.niazmandi-iran.com/ads/addprop'
        group = niazmandi_iran_group
        sub_group = niazmandi_iran_sub_group
        return page, group, sub_group, province, ''


class PostAd51(PostAd7):
    """ https://www.agahe118.com/framework/user/login """

    @staticmethod
    def _match_(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break
        m = 0
        if count > ((match_length / 3) * 2) + 1:
            m += 1
            return True

        if count > ((match_length / 3) * 2) and m == 0:
            return True

        return False

    def ads_page(self):
        page = 'https://www.agahe118.com/ads/addprop'
        group = agahe118_group
        sub_group = agahe118_sub_group
        return page, group, sub_group, province, ''


class PostAd52(PostAd47):
    """ https://www.mytabligh.net/framework/user/login """
    def ads_page(self):
        page = 'https://www.mytabligh.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd53(PostAd47):
    """ https://www.iran-agahi.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.iran-agahi.com/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd54(PostAd47):
    """ https://www.irantabligh.net/framework/user/login """
    def ads_page(self):
        page = 'https://www.irantabligh.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd55(PostAd47):
    """ https://www.niaziran.net/framework/user/login """
    def ads_page(self):
        page = 'https://www.niaziran.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd56(PostAd47):
    """ https://www.niaztehran.com/framework/user/login """
    def ads_page(self):
        page = 'https://www.niaztehran.com/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd57(PostAd47):
    """ https://www.tehranagahi.net/framework/user/login """
    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(self.password)
        sleep(1)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # close the some window
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/a').click()

        except NoSuchElementException:
            pass

        except ElementNotInteractableException:
            pass

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/'
                                          'div/div[1]/div[1]/form/input[1]').click()
        sleep(2)
        self.post()

    def ads_page(self):
        page = 'https://www.tehranagahi.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


class PostAd58(PostAd47):
    """ https://www.tehrantabligh.net/framework/user/login """
    def ads_page(self):
        page = 'https://www.tehrantabligh.net/ads/addprop'
        group = protabligh_group
        sub_group = protabligh_sub_group
        return page, group, sub_group, province, ''


""" Finish of inherited classes from PostAd7 """


class PostAd59(IPostAds):
    """ https://www.7010.ir/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="userpanel-trigger"]').click()
        sleep(4)

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="Text4"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="Password3"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="Button3"]').click()
        self.post()

    def post(self):
        self.driver.get('https://www.7010.ir/add/')

        # category
        prefix = '/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/label[1]/select/option['
        self.search(category_7010, prefix, ']', element=2)

        # province
        prefix = '/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[1]/label[1]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(1)

        # city
        prefix = '/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[1]/label[2]/select/option['
        self.search(city, prefix, ']')

        # group
        prefix = '/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[3]/label[1]/select/option['
        self.search(group_7010, prefix, ']', element=2)
        sleep(4)

        # sub-group
        prefix = '/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[3]/label[2]/select/option['
        self.group_search(sub_group_7010, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/label[4]/'
                                          'textarea').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[11]/div/'
                                          'label[1]/input').send_keys(picture)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[5]/div[1]/div/div/div/div/form/div[11]/div/'
                                          'label[2]/textarea').send_keys(keywords.replace('  ', '\n'))

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="uSite"]').clear()
        self.driver.find_element_by_xpath('//*[@id="uSite"]').send_keys(website_link)

        # phone
        self.driver.find_element_by_xpath('//*[@id="tel"]').clear()
        self.driver.find_element_by_xpath('//*[@id="tel"]').send_keys(phone)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submitBut"]').click()
        sleep(5)


class PostAd60(IPostAds):
    """ http://7rang.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').\
            send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').\
            send_keys(self.password)

        # captcha
        with open('index.jpg', 'wb') as img_file:
            img_file.write(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/'
                                                             'form/table/tbody/tr[4]/td[2]/img').screenshot_as_png)
        img = cv2.imread('index.jpg')
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        sleep(1)
        captcha = pytesseract.image_to_string(dst)
        self.driver.find_element_by_xpath('//*[@id="capcha"]').send_keys(captcha)

        # login button
        try:
            self.driver.find_element_by_xpath('//*[@id="sub"]').click()
        except ElementNotInteractableException:
            pass

        self.post()

    def post(self):
        self.driver.get('http://7rang.ir/newads')

        # ads type
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[3]/'
                                              'td[2]/select/option[3]').click()
        except NoSuchElementException:
            self.login()

        """
        1 - There is an pop-up on this page, in order to close we need to pass some part 2 times to submit the post
        2 - Each part that we pass we need to handle the exception because the pop-up can appear anywhere
        """

        # group
        prefix = '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/select/option['
        self.search(rang7_group, prefix, ']', element=2)
        sleep(3)

        # sub-group
        prefix = '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/span/select/option['
        self.search(rang7_sub_group, prefix, ']', element=2)

        # province
        prefix = '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/'
                                          'tr[9]/td[2]/input').send_keys(phone)

        # title
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[11]/'
                                          'td[2]/input').send_keys(title)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[12]/'
                                          'td[2]/input').send_keys(keywords.replace('  ', ','))

        # description
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[17]/'
                                              'td[2]/textarea').send_keys(description)

        except UnexpectedAlertPresentException:
            pass

        # price
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/'
                                              'tr[14]/td[2]/input').send_keys(price)
            sleep(1)
        except UnexpectedAlertPresentException:
            pass

        # picture
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[15]/'
                                              'td[2]/input').send_keys(picture)
            sleep(1)
        except UnexpectedAlertPresentException:
            pass

        # address
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[16]/'
                                              'td[2]/textarea').send_keys(address)
        except UnexpectedAlertPresentException:
            pass

        # description
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[17]/'
                'td[2]/textarea').send_keys(description)

        except UnexpectedAlertPresentException:
            pass

        # picture
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[15]/'
                'td[2]/input').send_keys(picture)
            sleep(1)
        except UnexpectedAlertPresentException:
            pass

        # submit button
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/form/table/tbody/tr[19]/'
                                              'td/input[2]').click()
        except UnexpectedAlertPresentException:
            pass


class PostAd61(IPostAds):
    """ https://silverbookco.com/%D9%88%D8%B1%D9%88%D8%AF-2 """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):

        # Enter username
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[2]/div/main/'
                                          'div[1]/form/fieldset/div[1]/div[2]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[2]/div/main/'
                                          'div[1]/form/fieldset/div[2]/div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[2]/div/main/div[1]/'
                                          'form/fieldset/div[4]/div/button').click()

        self.post()

    def post(self):
        self.driver.get('https://silverbookco.com/adad')

        # title
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                          'form/div[1]/div[2]/div[2]/div[1]/input').send_keys(title)

        # group
        prefix = '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/div[1]/div[2]/' \
                 'div[3]/div[1]/select/option['
        self.search(silverbook_group, prefix, ']', element=2)
        sleep(4)

        # sub-group
        try:
            prefix = '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/div[1]/div[2]/div[3]/' \
                     'div[1]/div[2]/select/option['
            self.search(silverbook_sub_group, prefix, ']', element=2)
        except NoSuchElementException:
            pass
        sleep(4)

        # sub sub-group
        try:
            prefix = '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/div[1]/div[2]/div[3]/' \
                     'div[1]/div[2]/div[2]/select/option['
            self.search(silverbook_sub_sub_group, prefix, ']', element=2)
        except NoSuchElementException:
            pass
        sleep(2)

        # navigation
        try:
            element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/'
                                                        'main/div/div/form/div[1]/div[2]/div[4]/div[1]/div[4]/div[1]/'
                                                        'input')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            sleep(2)
        except NoSuchElementException:
            pass

        # phone
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                              'form/div[1]/div[2]/div[4]/div[1]/div[7]/div[1]/input').send_keys(phone)
        except NoSuchElementException:
            pass

        # province
        prefix = '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/div[1]/div[2]/' \
                 'div[5]/div[1]/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(3)

        # city
        prefix = '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/div[1]/div[2]/div[5]/' \
                 'div[1]/div[2]/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                          'form/div[1]/div[2]/div[6]/div[1]/input').send_keys(address)

        # short description
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/'
                                          'div[1]/div[2]/div[12]/div[1]/textarea').send_keys(short_description)

        # description
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                          'form/div[1]/div[2]/div[13]/div[1]/textarea').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/'
                                          'div[1]/div[2]/div[14]/div[1]/textarea').send_keys(
            keywords.replace('  ', '\n'))

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                          'form/div[1]/div[2]/div[15]/div[1]/textarea').send_keys(phone)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/'
                                          'div[1]/div[2]/div[16]/div/div[1]/input').send_keys(phone)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/'
                                          'form/div[1]/div[2]/div[17]/div[1]/input').send_keys(website_link)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/main/div/div/form/'
                                          'div[2]/div[2]/div[4]/div/div[1]/div/div/div[2]/table[2]/tbody/tr/td[1]/'
                                          'div[1]/a[1]').click()
        sleep(3)
        pyautogui.write(picture)
        pyautogui.press('Enter')
        sleep(1)

        # submit button
        for i in range(3):
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/'
                                                  'div/main/div/div/form/div[5]/button[1]').click()
                sleep(2)
            except NoSuchElementException:
                pass


class PostAd62(IPostAds):
    """ https://ads.zibashahr.com/user_login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        self.post()

    def post(self):
        self.driver.get('https://ads.zibashahr.com/create-listing/')

        # group
        prefix = '/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/li[2]/div[2]/div/select/option['
        self.search(zibashahr_group, prefix, ']', element=2)
        sleep(3)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/'
                                          'li[2]/div[3]/input').click()
        sleep(4)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # address
        self.driver.find_element_by_xpath('//*[@id="cp_street"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_street"]').send_keys(address)

        # city
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').send_keys(city)

        # province
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/span/'
                                          'li[6]/a').click()
        sleep(1)
        prefix = '/html/body/ul[1]/li['
        self._search_(province, prefix, ']/a', element=2)
        sleep(1)

        # market target
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/span/'
                                          'li[7]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/ul[2]/li[2]/a').click()
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_zipcode"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_zipcode"]').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').clear()
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords.replace('  ', ','))

        try:
            # description
            self.driver.find_element_by_xpath('//*[@id="post_content"]').clear()
            self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

            # picture
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/span/'
                                              'li[12]/div[1]/div[3]/p[2]/a').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/ol/'
                                              'span/li[12]/div[1]/div[2]/ul/li/input[1]').send_keys(picture)

            # second submit button
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/'
                                              'form/ol/p/input').click()
            sleep(5)

        except NoSuchElementException:
            pass

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/p[2]/'
                                          'input[2]').click()


class PostAd63(IPostAds):
    """ http://www.adsfarsi.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ctl00_user1_EdtEamil"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ctl00_user1_EdtPassword"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="ctl00_user1_BtnLogin"]').click()

        self.post()

    def post(self):
        self.driver.get('http://www.adsfarsi.com/userpanel/advertisementnew.aspx?TypeRate=free')

        # group
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_CmbParentGroup"]').click()
        prefix = '/html/body/form/div[4]/div[2]/center/div[5]/div/div[1]/table/tbody/tr[1]/td[2]/select/option['
        self.search(adsfarsi_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/form/div[4]/div[2]/center/div[5]/div/div[1]/table/tbody/tr[2]/td[2]/select/option['
        self.search(adsfarsi_sub_group, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtTitle"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtSummary"]').send_keys(description)

        # keywords
        keyword = keywords.split('  ')
        counter = 1
        for i in range(6):
            keyword_element = '//*[@id="ctl00_Content_EdtKeyW' + str(counter) + 'NOSAVEHF"]'
            self.driver.find_element_by_xpath(keyword_element).send_keys(keyword[i])
            counter += 1
            sleep(1)

        # city
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtCity"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtAddress"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtMobile"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtEmail"]').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_EdtLinkWeb"]').send_keys(website_link)

        # ads period
        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[2]/center/div[5]/div/div[1]/table/tbody/'
                                          'tr[16]/td[2]/select/option[3]').click()

        # picture
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_FileUploadPic"]').send_keys(picture)
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="ctl00_Content_ibtn_Reg"]').click()


class PostAd64(IPostAds):
    """ http://aftabe.com/%d9%88%d8%b1%d9%88%d8%af/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        
        self.post()

    def post(self):
        self.driver.get('http://aftabe.com/%d8%a7%db%8c%d8%ac%d8%a7%d8%af-%d8%a2%da%af%d9%87%db%8c/')

        # group
        prefix = '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/li[2]/div[2]/div/select/option['
        self.search(aftabeh_group, prefix, ']', element=2)
        sleep(5)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # first submit button <next button>
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/li[2]/'
                                          'div[3]/input').click()
        sleep(3)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # country
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/'
                                          'form/ol/span/li[4]/select/option[106]').click()

        # province
        prefix = '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/span/li[5]/select/option['
        self._search_(province, prefix, ']', element=2)

        # city
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="cp_street"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_street"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_phonenumber"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_phonenumber"]').send_keys(phone)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').clear()
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords.replace('  ', ', '))

        # description
        try:
            self.driver.find_element_by_xpath('//*[@id="post_content"]').clear()
            self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)
        except NoSuchElementException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # picture
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/span/'
                                              'li[14]/div[1]/div[3]/p[2]/a').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/ol/span/'
                                              'li[14]/div[1]/div[2]/ul/li[1]/input[1]').send_keys(picture)
        except NoSuchElementException:
            pass

        # second submit button
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/'
                                              'form/ol/p/input').click()
            sleep(3)
        except NoSuchElementException:
            pass

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/form/p[2]/'
                                          'input[2]').click()
        sleep(4)


class PostAd65(IPostAds):
    """ https://www.agahi24.com/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        
        self.post()

    def post(self):
        self.driver.get('https://www.agahi24.com/create-listing')

        # group
        prefix = '/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/li[2]/div[2]/div/select/option['
        self.search(agahi24_group, prefix, ']', element=2)
        sleep(4)

        # sub-group
        prefix = '/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/li[2]/div[2]/div[2]/select/option['
        self.search(agahi24_sub_group, prefix, ']', element=2)
        sleep(4)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="getcat"]').click()
        sleep(4)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords.replace('  ', ','))

        # name
        self.driver.find_element_by_xpath('//*[@id="cp_name"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_mobile"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="cp_email"]').send_keys(email)

        # province
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/li[10]/a').click()
        prefix = '/html/body/ul/li['
        self._search_(province, prefix, ']/a', element=2)

        # city
        self.driver.find_element_by_xpath('//*[@id="cp_city"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="cp_street"]').send_keys(address)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/li[14]/'
                                          'div[1]/div[3]/p[2]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/li[14]/'
                                          'div[1]/div[2]/ul/li[1]/input[1]').send_keys(picture)

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/ol/p/input').click()
        sleep(5)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/p[2]/input[2]').click()


class PostAd66(IPostAds):
    """ http://agahi2agahi.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[1]/div[2]/form/table/tbody/'
                                          'tr[2]/td[2]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[1]/div[2]/form/table/tbody/'
                                          'tr[3]/td[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[1]/div[2]/form/table/tbody/'
                                          'tr[4]/td/input').click()
        self.post()

    def post(self):
        self.driver.get('http://agahi2agahi.com/0/advertisementpocketimage_new.html')

        # package
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[1]/td[2]/'
                                          'select/option[2]').click()

        # group & sub-group
        prefix = '/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td/' \
                 'table[2]/tbody/tr/td[3]/form/table/tbody/tr[2]/td[2]/select/option['

        self._search(agahi2agahi_group, agahi2agahi_sub_group, prefix, ']', separate_by='-->')

        # show communication form
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[3]/td[2]/'
                                          'select/option[2]').click()

        # name
        try:
            self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/'
                                              'div[1]/table/tbody/tr/td[1]/table/tbody/tr/td/'
                                              'table[2]/tbody/tr/td[3]/form/table/tbody/tr[5]/td[2]/input[1]')\
                .send_keys(english_name)

        except UnexpectedAlertPresentException:
            pass

        # phone
        try:
            self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/'
                                              'td[1]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/'
                                              'tr[6]/td[2]/input').send_keys(phone)
        except UnexpectedAlertPresentException:
            for i in range(2):
                pyautogui.press('enter')
            self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/'
                                              'td[1]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/'
                                              'tr[6]/td[2]/input').send_keys(phone)

        # price
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[8]/td[2]/'
                                          'input').send_keys(price)

        # province
        prefix = '/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td/' \
                 'table[2]/tbody/tr/td[3]/form/table/tbody/tr[9]/td[2]/select/option['

        self._search_(province, prefix, ']')

        # city
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[10]/td[2]/'
                                          'input').send_keys(city)

        # address
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[11]/td[2]/'
                                          'textarea').send_keys(address)

        # title
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[12]/td[2]/'
                                          'input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[14]/td[2]/'
                                          'textarea').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[15]/td[2]/'
                                          'input').send_keys(picture)

        # submit button
        self.driver.find_element_by_xpath('/html/body/center[1]/table[3]/tbody/tr/td[3]/div[1]/table/tbody/tr/td[1]/'
                                          'table/tbody/tr/td/table[2]/tbody/tr/td[3]/form/table/tbody/tr[17]/td[2]/'
                                          'button').click()


class PostAd67(IPostAds):
    """ http://www.agahi360.ir/account/login/ *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div/div[2]/form/table/tbody/'
                                          'tr[1]/td[2]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div/div[2]/form/table/tbody/'
                                          'tr[2]/td[2]/input').send_keys(self.password)
        sleep(1)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div/div[2]/form/'
                                          'table/tbody/tr[3]/td[2]/input').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div/div[2]/form/table/tbody/'
                                          'tr[4]/td/div/input').click()

        self.post()

    def post(self):
        self.driver.get('http://www.agahi360.ir/new/')

        # group
        prefix = '/html/body/div[2]/div[4]/div[3]/form/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/select[1]/option['
        sub_group_id = self.search(agahi360_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[2]/div[4]/div[3]/form/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/select['\
                 + str(sub_group_id) + ']/option['

        self.group_search(agahi360_sub_group, prefix, ']', element=2)
        sleep(1)

        # title
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/form/div[2]/div/div[2]/table/'
                                              'tbody/tr[2]/td[2]/input').send_keys(title)
        except NoSuchElementException:
            self.login()

        # description
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/form/div[2]/div/div[2]/table/tbody/tr[3]/'
                                          'td/textarea').send_keys(description)

        # first submit button
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/form/div[2]/div/div[2]/table/tbody/'
                                              'tr[4]/td/div/input').click()
        except NoSuchElementException:
            pass

        # price
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[2]/div[1]/div[2]/table/tbody/'
                                          'tr/td[2]/input').send_keys(price)

        # picture
        img = cv2.imread(picture)
        img = cv2.resize(img, (256, 256), fx=1, fy=1)
        cv2.imwrite('resized_image.jpg', img)

        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[2]/div[2]/div[2]/'
                                          'div[2]/input').send_keys(os.getcwd() + '\\resized_image.jpg')
        sleep(2)

        # keywords
        keyword = keywords.split('  ')
        td_counter = 1
        tr_counter = 1
        for i in range(6):
            keyword_path = '/html/body/div[2]/div[4]/div[4]/form/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[' \
                           + str(tr_counter) + ']/td[' + str(td_counter) + ']/input'
            self.driver.find_element_by_xpath(keyword_path).send_keys(keyword[i])
            td_counter += 1
            if td_counter > 3:
                td_counter = 1
                tr_counter += 1

            if tr_counter == 2:
                break

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[2]/div[4]/div[2]/div[2]/table/'
                                          'tbody/tr/td[1]/textarea').send_keys(keywords.replace('  ', '\n'))

        # name
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/'
                                          'tr[1]/td[2]/input').send_keys(name)

        # email
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/'
                                          'tr[2]/td[2]/input').send_keys(email)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/'
                                          'tr[3]/td[2]/input').send_keys(phone)

        # website-link
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/'
                                          'tr[4]/td[2]/input').send_keys(website_link)

        # province
        prefix = '/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[2]/select[1]/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[2]/select[12]/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/form/div[1]/div[2]/div[2]/table/'
                                          'tbody/tr[6]/td[2]/input').send_keys(address)

        # final submit button
        self.driver.find_element_by_xpath('//*[@id="add-new-advertisement"]').click()


class PostAd68(IPostAds):
    """ http://www.abcagahi.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/form/fieldset/'
                                          'div[4]/div/button').click()

        self.post()

    def post(self):
        self.driver.get('http://www.abcagahi.ir/%D8%AB%D8%A8%D8%AA-%D8%A2%DA%AF%D9%87%DB%8C-'
                        '%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86')

        # title
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(title)

        # group
        prefix = '/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/' \
                 'select/option['

        self.search(abcagahi_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/' \
                 'div[2]/select/option['

        self.group_search(abcagahi_sub_group, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # period ads
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/form/div[1]/'
                                          'div[2]/div[5]/div[1]/div/select/option[1]').click()

        # short_description
        self.driver.find_element_by_xpath('//*[@id="intro_desc"]').send_keys(short_description)

        # description
        iframe = self.driver.find_element_by_xpath('//*[@id="description_ifr"]')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p').send_keys(description)
        self.driver.switch_to.default_content()

        # phone
        self.driver.find_element_by_xpath('//*[@id="contact"]').send_keys(phone)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="website"]').send_keys(website_link)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('//*[@id="uploader_browse"]').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(2)
        pyautogui.press('enter')
        sleep(3)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submit_button"]').click()


class PostAd69(IPostAds):
    """ https://www.jarzadani.ir/index.php?r=site%2Flogin-reg """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="loginform-username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="loginform-password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/form/div/div[3]/button').click()
        
        self.post()

    @staticmethod
    def _match(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 1:
            return True
        return False

    def _search_(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        self.driver.get('https://www.jarzadani.ir/index.php?r=ads%2Freg-step1')

        # group & sub-group
        self.driver.find_element_by_xpath('//*[@id="get-cats"]').click()
        iframe = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div[2]/iframe')
        self.driver.switch_to.frame(iframe)

        # group
        prefix = '/html/body/table/tbody/tr['
        self.search(jarzadani_group, prefix, ']/td[1]/a')
        sleep(2)

        # sub-group
        prefix = '/html/body/table/tbody/tr['
        self.search(jarzadani_sub_group, prefix, ']/td/a')
        sleep(3)

        self.driver.switch_to.default_content()

        # title
        self.driver.find_element_by_xpath('//*[@id="adsreg1-title"]').send_keys(title)

        # name
        self.driver.find_element_by_xpath('//*[@id="adsreg1-alias"]').send_keys(name)

        # price
        self.driver.find_element_by_xpath('//*[@id="adsreg1-price"]').send_keys(price)

        # description
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div/'
                                          'div[2]/div/p').send_keys(description)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/div[3]/button').click()
        sleep(4)

        # address
        self.driver.find_element_by_xpath('//*[@id="adsreg2-addr"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="adsreg2-mobile"]').send_keys(phone)

        # province
        prefix = '/html/body/div[4]/div/div[2]/form/div[1]/div[2]/div[3]/div[2]/div[1]/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # email
        self.driver.find_element_by_xpath('//*[@id="adsreg2-email"]').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="adsreg2-web_url"]').send_keys(website_link)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="adsreg2-keywords_tag"]').send_keys(keywords.replace('  ', '\n'))

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/div[3]/button').click()
        sleep(4)

        # picture
        self.driver.find_element_by_xpath('//*[@id="inputImage"]').send_keys(picture)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/div[2]/div[3]/div[1]/div/'
                                          'div[3]/div[2]/button').click()
        sleep(1)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/div[3]/button').click()


class PostAd70(IPostAds):
    """ http://jar24.ir/user/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/'
                                          'div/div/form/fieldset/button').click()

        self.post()

    def post(self):
        self.driver.get('http://jar24.ir/item/new')

        # group
        prefix = '/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[1]/div[2]/div/select[1]/option['
        self.search(jar24_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[1]/div[2]/div/select[2]/option['
        self.search(jar24_sub_group, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="titlefa_IR"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="descriptionfa_IR"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[2]/div[2]/'
                                          'div/div[2]/input').send_keys(picture)
        sleep(5)
        # province
        prefix = '/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[3]/div/div[1]/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(1)
        
        # city
        prefix = '/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[3]/div/div[2]/div/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[3]/div/div[4]/'
                                          'div/input').send_keys(address)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[4]/div[4]/'
                                          'div[1]/div[1]/input').send_keys(keywords.replace('  ', '\n'))

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/form/fieldset/div[6]/'
                                          'div/button').click()

        pyautogui.press('enter')


class PostAd71(IPostAds):
    """ http://www.dasar.ir/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="block_email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="block_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[4]/div[1]/div[3]/div[2]/div[2]/form/table/'
                                          'tbody/tr[4]/td/input').click()
        sleep(3)
        self.post()

    def post(self):
        self.driver.get('http://www.dasar.ir/fullmode/advertisement_new.html')

        # package ad
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/'
                                          'div[2]/div/form/fieldset[1]/table/tbody/tr[1]/td[2]/'
                                          'select/option[2]').click()

        # province
        prefix = '/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/div[2]/div/form/fieldset[1]/' \
                 'table/tbody/tr[2]/td[2]/select/option['

        self._search_(province, prefix, ']', element=2)

        # group & sub-group
        prefix = '/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/div[2]/div/form/fieldset[1]/' \
                 'table/tbody/tr[3]/td[2]/select/option['

        self._search(dasar_group, dasar_sub_group, prefix, ']', separate_by='-->')

        # picture
        self.driver.find_element_by_xpath('//*[@id="fileurl_mode_1"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="fileurl"]').send_keys(picture)
        
        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="note"]').send_keys(description)

        # name
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/'
                                          'div[2]/div/form/fieldset[3]/table/tbody/tr[1]/td[2]/input').send_keys(name)

        # email
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/'
                                          'div[2]/div/form/fieldset[3]/table/tbody/tr[2]/td[2]/input').send_keys(email)

        # price
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/'
                                          'div[2]/div/form/fieldset[3]/table/tbody/tr[6]/td[2]/input').send_keys(price)

        # address
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[1]/div/div[1]/div/div/div/'
                                          'div[2]/div/form/fieldset[3]/table/tbody/tr[8]/'
                                          'td[2]/textarea').send_keys(address)
        # submit button
        self.driver.find_element_by_xpath('//*[@id="button_form"]').click()


class PostAd72(IPostAds):
    """ http://publik.ir/login_register.php """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    """ this function is for inheriting for PostAd73 """
    @staticmethod
    def page_info():
        group = publik_group
        sub_group = publik_sub_group
        page = 'http://publik.ir/add_estate.php'
        group_sub_group_button = '/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[6]/div[1]/button'
        return group, sub_group, page, group_sub_group_button

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[1]/input').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[2]/'
                                          'input').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[4]/'
                                          'button').click()

        self.post()

    def post(self):
        self.driver.get(self.page_info()[2])

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # group & sub-group
        self.driver.find_element_by_xpath(self.page_info()[3]).click()

        sleep(1)
        prefix = '/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[6]/div[1]/ul/li['
        self._search(self.page_info()[0], self.page_info()[1], prefix, ']/a/span', separate_by=' -- ')
        sleep(2)

        # ads type
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[7]/div/'
                                          'button').click()
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[7]/div/ul/'
                                          'li[2]/a').click()

        # province
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[9]/div/'
                                          'button').click()
        prefix = '/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[9]/div/ul/li['
        self._search_(province, prefix, ']/a/span', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[10]/div/'
                                          'button').click()
        prefix = '/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[10]/div/ul/li['
        self.search(city, prefix, ']/a/span', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="step1_submit"]').click()
        sleep(3)

        # description
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[5]/div/'
                                          'div[6]/p').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[7]/div/'
                                          'input').send_keys(keywords.replace('  ', '\n'))

        # price
        self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        # second submit button
        self.driver.find_element_by_xpath('//*[@id="step2_submit"]').click()
        sleep(3)

        # picture
        self.driver.find_element_by_css_selector('span.btn').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="image_upload_submit"]').click()
        sleep(3)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 2);')
        sleep(1)

        # # third submit button
        try:
            self.driver.find_element_by_xpath('//*[@id="step3_submit"]').click()
            sleep(4)
        except ElementClickInterceptedException:
            self.driver.find_element_by_xpath('//*[@id="step3_submit"]').click()
            sleep(4)

        # # final submit button
        self.driver.find_element_by_xpath('//*[@id="payment_submit"]').click()


class PostAd73(PostAd72):
    """ http://hadafniaz.ir/login_register.php """
    @staticmethod
    def page_info():
        group = hadafniaz_group
        sub_group = hadafniaz_sub_group
        page = 'http://hadafniaz.ir/add_estate.php'
        group_sub_group_button = '/html/body/section[1]/div/div/div[2]/div/div[3]/form/div/div[6]/div[1]/button'
        return group, sub_group, page, group_sub_group_button

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/'
                                          'form/div[1]/input').send_keys(self.username)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/'
                                          'form/div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[4]/button').click()

        self.post()


class PostAd74(IPostAds):
    """ http://peleha.ir/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/div[5]/'
                                          'div[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('http://peleha.ir/new')

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-select-category-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(peleha_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[2]/div/div[1]/'
                                          'span/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(peleha_sub_group, prefix, ']', element=2)
        sleep(2)

        # email or phone
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[2]/div[1]/div/div[2]/div[1]/'
                                              'div/input').send_keys(email)
        except NoSuchElementException:
            pass

        # price
        try:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)
        except NoSuchElementException:
            self.driver.find_element_by_id('frm_price').send_keys(price)

        # ad type
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[3]/div/'
                                          'span[2]/span[1]/span/span[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()

        # picture
        self.driver.find_element_by_xpath('/html/body/div[9]/input').send_keys(picture)

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').click()
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)

        # province
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[10]/'
                                          'div/span[2]/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[11]/div/'
                                          'span[2]/span[1]/span/span[1]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="frm_email"]').send_keys(email)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[14]/div/'
                                          'span/span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd75(IPostAds):
    """ https://pbazar.ir/login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="sb_reg_email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/section/div/div/div[1]/div/form/'
                                          'div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="sb_login_submit"]').click()
        sleep(3)
        self.post()

    def post(self):
        self.driver.get('https://pbazar.ir/post-ad/')

        # title
        self.driver.find_element_by_xpath('//*[@id="ad_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-ad_cat-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(pbazar_group, prefix, ']')
        sleep(7)

        # sub-group
        self.driver.find_element_by_xpath('//*[@id="select2-ad_cat_sub-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(pbazar_sub_group, prefix, ']')
        sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div[3]/div/div/form/div/'
                                          'nav[2]/div[1]/button[2]').click()
        sleep(2)

        # price
        self.driver.find_element_by_xpath('//*[@id="select2-ad_price_type-container"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[1]').click()

        self.driver.find_element_by_xpath('//*[@id="ad_price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div[3]/div/div/form/div/div/'
                                          'div[2]/div[4]/div/div').click()
        sleep(2)
        pyautogui.write(f'{pbazar_picture}')
        sleep(1)
        pyautogui.press('enter')

        # description
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div[3]/div/div/form/div/'
                                          'div/div[2]/div[5]/div/div/div[3]').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_tag"]').send_keys(keywords.replace('  ', '\n'))

        # ads type
        self.driver.find_element_by_xpath('//*[@id="select2-type-container"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[3]').click()

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div[3]/div/div/form/div/'
                                          'nav[2]/div[1]/button[2]').click()
        sleep(3)

        # name
        self.driver.find_element_by_xpath('//*[@id="step-2"]/div[1]/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="step-2"]/div[1]/div[1]/input').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="adforest_contact_number"]').clear()
        self.driver.find_element_by_xpath('//*[@id="adforest_contact_number"]').send_keys(phone)

        # country
        self.driver.find_element_by_xpath('//*[@id="select2-ad_country-container"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        sleep(4)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-ad_country_states-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']')
        sleep(7)

        # city
        self.driver.find_element_by_xpath('//*[@id="select2-ad_country_cities-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']')
        sleep(5)

        # address
        self.driver.find_element_by_xpath('//*[@id="sb_user_address"]').send_keys(address)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div/section/div/div[3]/div/div/form/div/'
                                          'nav[2]/div[2]/button').click()


class PostAd76(IPostAds):
    """ http://pabi.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="capcha"]').click()
        sleep(13)

        # login button
        try:
            self.driver.find_element_by_xpath('//*[@id="sub"]').click()
        except ElementNotInteractableException:
            pass

        sleep(2)
        self.post()

    def post(self):
        self.driver.get('http://pabi.ir/newads')

        # ads type
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/'
                                              'select/option[5]').click()
        except NoSuchElementException:
            self.login()

        # group & sub-group
        prefix = '/html/body/div[1]/div[5]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/select/option['
        self._search(pabi_group, pabi_sub_group, prefix, ']', separate_by='->')
        sleep(2)

        # province & city
        prefix = '/html/body/div[1]/div[5]/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/select/option['
        self._search(province, city, prefix, ']', separate_by='->', element=2)

        # name
        self.driver.find_element_by_xpath('//*[@id="fullname"]').click()
        self.driver.find_element_by_xpath('//*[@id="fullname"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="tell"]').send_keys(phone)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords.replace('  ', ','))

        # price
        try:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)
        except UnexpectedAlertPresentException:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # description
        self.driver.find_element_by_xpath('//*[@id="describtion"]').send_keys(description)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="sub"]').click()


class PostAd77(IPostAds):
    """ https://www.taaj.ir/?action=login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/form/table/tbody/tr[1]/td[2]/'
                                          'input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/form/table/tbody/tr[2]/td[2]/'
                                          'input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/form/table/tbody/tr[3]/td[2]/input').click()

        self.post()

    def post(self):
        self.driver.get('https://www.taaj.ir/?action=user&do=add')

        # group & sub-group
        prefix = '/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/tbody/tr[1]/td/select/option['
        self._search(taaj_group, taaj_sub_group, prefix, ']', separate_by='-->')
        sleep(2)

        # title
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[2]/td/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[3]/td/textarea').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[4]/td/input').send_keys(picture)
        sleep(2)

        # name
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[6]/td/input[1]').clear()

        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[6]/td/input[1]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[6]/td/input[2]').send_keys(phone)

        # province
        prefix = '/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/tbody/tr[7]/td/select/option['
        self._search('ایران', province, prefix, ']', separate_by='-->')
        sleep(2)

        # price
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[7]/td/input').send_keys(price)

        # address
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/table/'
                                          'tbody/tr[8]/td/input').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/'
                                          'table/tbody/tr[10]/td/input').send_keys(website_link)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/'
                                          'table/tbody/tr[11]/td/input').send_keys(keywords.replace('  ', '\n'))

        # first submit button
        try:
            self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset[1]/div/'
                                              'table/tbody/tr[14]/td/input').click()
        except NoSuchElementException:
            pass
        sleep(4)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset/form/table/'
                                          'tbody/tr/td/input').send_keys(picture)
        sleep(1)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div[2]/fieldset/form/input').click()


class PostAd78(IPostAds):
    """ http://agahidon.ir/user/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/form/fieldset/button').click()
        sleep(3)
        self.post()

    @staticmethod
    def page_info():
        page = 'http://agahidon.ir/item/new'
        group = '[' + agahidon_group + ']:'
        sub_group = agahidon_sub_group
        return page, group, sub_group, province, 'M'

    def post(self):
        self.driver.get(self.page_info()[0])

        # group
        prefix = '/html/body/div[2]/div/div/form/div[1]/div/div/div/select[1]/option['
        self.search(self.page_info()[1], prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[2]/div/div/form/div[1]/div/div/div/select[2]/option['
        self.search(self.page_info()[2], prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="titlefa_IR"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="descriptionfa_IR"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/'
                                          'input').send_keys(picture)

        # province
        prefix = '/html/body/div[2]/div/div/form/div[2]/div/div[6]/div[1]/div/select/option['
        if self.page_info()[4] == 'M':
            self._search_(self.page_info()[3], prefix, ']', element=2)

        else:
            self.search(self.page_info()[3], prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div/div/form/div[2]/div/div[6]/div[2]/div/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # phone
        try:
            self.driver.find_element_by_xpath('//*[@id="meta_tel"]').send_keys(phone)
        except NoSuchElementException:
            pass

        # website_link
        try:
            self.driver.find_element_by_xpath('//*[@id="meta_-"]').send_keys(website_link)
        except NoSuchElementException:
            pass

        # submit button
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/div[11]/div/button').click()
            sleep(1)

        except UnexpectedAlertPresentException:
            pyautogui.press('enter')

        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/div[10]/div/button').click()


class PostAd79(IPostAds):
    """ http://agahiiran.ir/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[5]/div[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('http://agahiiran.ir/new')

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-select-category-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(agahiiran_group, prefix, ']', element=2)
        sleep(2)
        
        # sub-group
        self.driver.find_element_by_xpath('//*[@id="select2-select-subcategory-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(agahiiran_sub_group, prefix, ']', element=2)
        sleep(2)

        # sub sub-group
        if agahiiran_sub_sub_group:
            try:
                self.driver.find_element_by_xpath('//*[@id="select2-select-subsidiary-container"]').click()
                prefix = '/html/body/span/span/span[2]/ul/li['
                self.search(agahiiran_sub_sub_group, prefix, ']', element=2)
                sleep(2)
            except NoSuchElementException:
                pass

        # price
        try:
            self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        except ElementNotInteractableException:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        sleep(2)
        
        # picture
        self.driver.find_element_by_xpath('/html/body/div[10]/input').send_keys(picture)

        # ad type
        self.driver.find_element_by_xpath('//*[@id="select2-frm_plan_type-container"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        sleep(3)
        
        # phone or email
        try:
            self.driver.find_element_by_xpath('//*[@id="register_param"]').send_keys(email)
        except NoSuchElementException:
            pass

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').click()
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-state_id-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)
        
        # city
        self.driver.find_element_by_xpath('//*[@id="submit-new-item"]/div[11]/div/span[2]/span[1]/span/span[2]').click()
        sleep(2)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="frm_email"]').send_keys(email)

        # keywords
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[14]/div/'
                                          'span/span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 2);')
        sleep(1)

        # submit button
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/button').click()


class PostAd80(PostAd78):
    """ https://agahi-kala.ir/user/login """
    @staticmethod
    def page_info():
        page = 'https://agahi-kala.ir/item/new'
        group = agahi_kala_group
        sub_group = agahi_kala_sub_group
        return page, group, sub_group, city, ''


class PostAd81(IPostAds):
    """ https://agahimax.com/auth *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[5]/div[3]/button').click()

        self.post()

    @staticmethod
    def page_info():
        return 'https://agahimax.com/new', agahimax_group, agahimax_sub_group, agahimax_sub_sub_group

    def post(self):
        self.driver.get(self.page_info()[0])
        self.driver.maximize_window()

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-select-category-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(self.page_info()[1], prefix, ']', element=2)
        sleep(2)

        # sub-group
        self.driver.find_element_by_xpath('//*[@id="select2-select-subcategory-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(self.page_info()[2], prefix, ']', element=2)
        sleep(2)

        # sub sub-group
        try:
            if self.page_info()[3]:
                try:
                    self.driver.find_element_by_xpath('//*[@id="select2-select-subsidiary-container"]').click()
                    prefix = '/html/body/span/span/span[2]/ul/li['
                    self.search(self.page_info()[3], prefix, ']', element=2)
                    sleep(2)
                except NoSuchElementException:
                    pass
        except IndexError:
            pass

        # price
        try:
            self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        except ElementNotInteractableException:
            self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        sleep(2)

        # picture
        try:
            self.driver.find_element_by_xpath('/html/body/div[8]/input').send_keys(picture)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/div[10]/input').send_keys(picture)

        # ad type
        self.driver.find_element_by_xpath('//*[@id="select2-frm_plan_type-container"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        sleep(5)

        # phone or email
        try:
            self.driver.find_element_by_xpath('//*[@id="register_param"]').send_keys(email)
        except NoSuchElementException:
            pass

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').click()
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-state_id-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        self.driver.find_element_by_xpath('//*[@id="submit-new-item"]/div[11]/div/span[2]/span[1]/span/span[2]').click()
        sleep(2)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(city, prefix, ']', element=2)
        sleep(1)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="frm_email"]').send_keys(email)

        # address
        try:
            self.driver.find_element_by_xpath('//*[@id="frm_address"]').click()
            self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)
        except NoSuchElementException:
            pass

        # keywords
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[15]/div/'
                                              'span/span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/div[1]/div/div/div/div[14]/div/'
                                              'span/span[1]/span/ul/li/input').send_keys(keywords.replace('  ', '\n'))

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # move to element
        element = self.driver.find_element_by_xpath('//*[@id="submit_item"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).double_click()
        actions.perform()

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submit_item"]').click()


class PostAd82(PostAd81):
    """ https://ariyads.com/auth *** captcha *** """
    def login(self):
        sleep(5)
        # close ads
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/button').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # CAPTCHA delay
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(13)

        # login button
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/section/div[2]/form/'
                                          'div[5]/div[3]/button').click()

        self.post()

    @staticmethod
    def page_info():
        return 'https://ariyads.com/new', agahimax_group, agahimax_sub_group, agahimax_sub_sub_group


class PostAd83(IPostAds):
    """ http://asreesfahan.com/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/button').click()
        
        self.post()

    def post(self):
        self.driver.get('http://asreesfahan.com/esfahanrequirements/new/%D8%AF%D8%B1%D8%AC-%D8%A2%DA%AF%D9%87%DB%8C'
                        '-%D8%AF%D8%B1-%D8%B3%D8%A7%DB%8C%D8%AA')

        # group
        prefix = '/html/body/div[2]/div/div[2]/div/form/section/div[2]/div[1]/div[2]/div/select/option['
        self.search(asreesfahan_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[2]/div/div[2]/div/form/section/div[2]/div[2]/div[2]/div/select/option['
        self.search(asreesfahan_sub_group, prefix, ']', element=2)
        sleep(2)

        # title
        self.driver.find_element_by_xpath('//*[@id="adv_title"]').send_keys(title)

        # description
        iframe = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/section/div[2]/div[4]/'
                                                   'div[2]/div/div/div/div/iframe')

        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p').send_keys(description)
        self.driver.switch_to.default_content()

        # name
        self.driver.find_element_by_xpath('//*[@id="order_name"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('//*[@id="order_address"]').send_keys(address)

        # picture
        img = cv2.imread(picture)
        img = cv2.resize(img, (600, 600), fx=1.1, fy=1.1)
        cv2.imwrite('resized_image.jpg', img)

        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/section/div[2]/div[9]/div[2]/'
                                          'div[1]/div/label').click()

        sleep(2)
        pyautogui.write(os.getcwd() + '\\resized_image.jpg')

        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/section/div[2]/div[12]/'
                                          'div/input').click()


class PostAd84(PostAd81):
    """ http://bazarche96.com/auth *** captcha ***"""
    @staticmethod
    def page_info():
        return 'http://bazarche96.com/new', bazarche96_group, bazarche96_sub_group, bazarche96_sub_sub_group


class PostAd85(IPostAds):
    """ https://bazarha.ir/%d9%88%d8%b1%d9%88%d8%af/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(self.username)
          
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://bazarha.ir/%d8%a7%db%8c%d8%ac%d8%a7%d8%af-%d8%a2%da%af%d9%87%db%8c/')

        # group
        prefix = '/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/' \
                 'tr[2]/td[2]/div/div[1]/select/option['
        self.search(bazarha_group + ' - 0 تومان', prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/' \
                 'div[2]/select/option['
        self.search(bazarha_sub_group + ' - 0 تومان', prefix, ']', element=2)
        sleep(2)

        # sub sub-group
        if bazarha_sub_sub_group:
            prefix = '/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/div/div[3]/' \
                     'select/option['
            self.search(bazarha_sub_sub_group + ' - 0 تومان', prefix, ']', element=2)
            sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="getcat"]').click()
        sleep(5)

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # phone
        self.driver.find_element_by_xpath('//*[@id="cp_mobile"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cp_mobile"]').send_keys(phone)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-cp_state-container"]').click()
        sleep(1)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/div/div[1]/div[7]/' \
                 'select/option['
        self.search(city, prefix, ']', element=2)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[1]/'
                                          'div/div[1]/div[15]/span/span[1]/span/ul/li/input').send_keys(
            keywords.replace('  ', '\n'))

        # description
        self.driver.find_element_by_xpath('//*[@id="post_content"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post_content"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[2]/'
                                          'div[2]/div/div[1]/div/p[3]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[2]/div[2]/'
                                          'div/div[1]/div/div/div[3]/ul/li[1]/div/input').send_keys(picture)

        # second submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/input[3]').click()
        sleep(5)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/p[2]/'
                                          'input[2]').click()


class PostAd86(IPostAds):
    """ https://dararsh.com/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # CAPTCHA
        with open('index.jpg', 'wb') as img_file:
            img_file.write(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[2]/form/table/'
                                                             'tbody/tr[4]/td[2]/img').screenshot_as_png)
        img = cv2.imread('index.jpg')
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        captcha = pytesseract.image_to_string(dst)
        self.driver.find_element_by_xpath('//*[@id="capcha"]').send_keys(captcha)

        # login button
        try:
            self.driver.find_element_by_xpath('//*[@id="sub"]').click()
        except ElementNotInteractableException:
            pass

        self.post()

    @staticmethod
    def _match_(string, other):
        count = 0
        match_length = len(string)
        for i in string:
            for j in other:
                if i == j and i != ' ':
                    count += 1
                    break

        if count > ((match_length / 3) * 2) + 1:
            return True
        return False

    def post(self):
        self.driver.get('https://dararsh.com/newads')

        # group
        try:
            prefix = '/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[2]/td[2]/select/option['
            self.search(dararsh_group, prefix, ']', element=2)
            sleep(2)

        except NoSuchElementException:
            self.login()

        # sub-group
        prefix = '/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[3]/td[2]/select/option['
        self.search(dararsh_sub_group, prefix, ']')
        sleep(1)

        # province
        prefix = '/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/select[1]/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/select[2]/option['
        self.search(city, prefix, ']')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="describtion"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[5]/'
                                          'td/table[2]/tbody/tr[2]/td[2]/input').send_keys(picture)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keych"]').send_keys(keywords.replace('  ', '\n'))

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # name
        self.driver.find_element_by_xpath('//*[@id="fullname"]').clear()
        self.driver.find_element_by_xpath('//*[@id="fullname"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="tell"]').send_keys(phone)

        # ad type
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/tr[9]/'
                                          'td[2]/select/option[4]').click()

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/form/table/tbody/'
                                          'tr[14]/td/input[2]').click()


class PostAd87(IPostAds):
    """ https://fastniaz.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        self.driver.find_element_by_xpath('/html/body/div[4]/header/div/div/div[2]/ul/li[2]/a').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/form/div[1]/'
                                          'input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/form/div[2]/'
                                          'input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/form/input[2]').click()
        sleep(4)
        self.post()

    def _search_option(self, group, sub_group, prefix, middle, suffix, separate_by='', element=1, other=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(other) + middle + str(element) + suffix)
                pattern_txt = str(pattern.text).split(separate_by)

                try:
                    if self._match(group, pattern_txt[0].strip()) and self._match(sub_group, pattern_txt[1].strip()):
                        pattern.click()
                        return element
                except IndexError:
                    pass

                element += 1
            except NoSuchElementException:
                element = 1
                other += 1
                if other == 12:
                    loop = False

    def post(self):
        self.driver.get('https://fastniaz.com/add-ads.html')

        # group & sub-group
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[1]/'
                                          'span/span[1]/span/ul/li/input').click()

        sleep(2)
        prefix = '/html/body/span/span/span/ul/li['
        middle = ']/ul/li['
        self._search_option(fastniaz_group, fastniaz_sub_group, prefix, middle, ']', separate_by=' : ')

        # title
        self.driver.find_element_by_xpath('//*[@id="fa_title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[2]/'
                                          'div/div[1]/div[2]/textarea').send_keys(description)

        # name
        self.driver.find_element_by_xpath('//*[@id="fa_full_name"]').send_keys(name)

        # address
        self.driver.find_element_by_xpath('//*[@id="fa_address"]').send_keys(address)

        # price
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/'
                                          'div/div[1]/div[1]/div/input').send_keys(price)

        # province
        prefix = '/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/div/div[1]/div[2]/div/' \
                 'select/option['
        self._search_(province, prefix, ']', element=2)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/'
                                          'div/div[1]/div[4]/div/input').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/'
                                          'div/div[1]/div[5]/div/input').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/'
                                          'div/div[1]/div[6]/div/input').send_keys(website_link)
        sleep(1)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/'
                                          'div[3]/ul/li[2]/a').click()

        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/'
                                          'div/div[2]/div/div/ul/li/input').send_keys(keywords.replace('  ', '\n'))

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/form/div[1]/'
                                          'div[4]/button[1]').click()
        sleep(5)

        # picture
        self.driver.find_element_by_xpath('//*[@id="ads_photos"]').send_keys(picture)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/div[1]/form/'
                                          'span[2]/div[2]/div[1]/button[1]').click()
        sleep(3)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[1]/div[1]/div/div/div[1]/form/'
                                          'div/button').click()


class PostAd88(IPostAds):
    """ http://inagahi.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[2]').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form/'
                                          'div[1]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form/'
                                          'div[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form/'
                                          'div[3]/input[2]').click()
        sleep(2)
        self.post()

    def search(self, string, prefix, suffix, element=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(element) + suffix)
                pattern_txt = str(pattern.text).strip()

                if self._match(string, pattern_txt):
                    pattern.click()
                    return element

                element += 1
            except NoSuchElementException:
                loop = False

    def post(self):
        self.driver.get('http://inagahi.com/newads')

        # group
        prefix = '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/table/tbody/tr[2]/td[2]/select/option['
        self.search(inagahi_group, prefix, ']', element=2)
        sleep(2)

        # sub-group
        prefix = '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/table/tbody/tr[3]/td[2]/select/option['
        self.search(inagahi_sub_group, prefix, ']')

        # city
        prefix = '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/table/tbody/tr[4]/td[2]/select/option['
        self.search(city, prefix, ']', element=2)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="describtion"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('//*[@id="pic"]').send_keys(picture)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keych"]').send_keys(keywords.replace('  ', '\n'))

        # address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('//*[@id="link"]').send_keys(website_link)

        # name
        self.driver.find_element_by_xpath('//*[@id="fullname"]').clear()
        self.driver.find_element_by_xpath('//*[@id="fullname"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="tell"]').send_keys(phone)

        # ad type
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/table/tbody/'
                                          'tr[17]/td[2]/select/option[3]').click()
        sleep(1)
        
        # submit button
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/table/tbody/'
                                          'tr[21]/td/input[2]').click()


class PostAd89(PostAd81):
    """ http://inokala.ir/auth *** captcha *** """
    @staticmethod
    def page_info():
        page = 'http://inokala.ir/new'
        group = agahimax_group
        sub_group = agahimax_sub_group
        sub_sub_group = agahimax_sub_sub_group
        return page, group, sub_group, sub_sub_group


class PostAd90(PostAd81):
    """ https://khafanbazar.ir/auth  *** captcha *** """
    @staticmethod
    def page_info():
        page = 'https://khafanbazar.ir/new'
        return page, agahimax_group, agahimax_sub_group, agahimax_sub_sub_group


class PostAd91(IPostAds):
    """ http://www.niazmandia.ir/panel/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[1]/'
                                          'td[2]/input').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[2]/'
                                          'td[2]/input').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/center/input').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('http://www.niazmandia.ir/panel/add-ads')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # group & sub-group
        prefix = '/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[2]/td[2]/select/option['
        self._search(niazmandia_group, niazmandia_sub_group, prefix, ']', separate_by=' -> ', element=2)

        # description
        self.driver.find_element_by_xpath('//*[@id="text"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[4]/'
                                          'td[2]/input').send_keys(picture)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[5]/'
                                          'td[2]/input').send_keys(phone)

        # price
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[6]/'
                                          'td[2]/input').send_keys(price)

        # province
        prefix = '/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[7]/td[2]/select/option['
        self.search(niazmandia_province, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[8]/'
                                          'td[2]/input').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[9]/td[2]/'
                                          'input').clear()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/table/tbody/tr[9]/td[2]/'
                                          'input').send_keys(website_link)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/center/input').click()


class PostAd92(IPostAds):
    """ http://tabliqplus.ir/login_register.php """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # close ads
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[1]/span').click()
        sleep(2)

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div/form/div/input').click()
        sleep(2)
        self.post()

    def _search_option(self, group, sub_group, prefix, middle, suffix, separate_by='', element=1, other=1):
        loop = True
        while loop:
            try:
                pattern = self.driver.find_element_by_xpath(prefix + str(other) + middle + str(element) + suffix)
                pattern_txt = str(pattern.text).split(separate_by)

                try:
                    if self._match(group, pattern_txt[0].strip()) and self._match(sub_group, pattern_txt[1].strip()):
                        pattern.click()
                        return element
                except IndexError:
                    pass

                element += 1
            except NoSuchElementException:
                element = 1
                other += 1
                if other == 12:
                    loop = False

    def post(self):
        self.driver.get('http://tabliqplus.ir/add_estate.php')

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').clear()
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # group & sub-group
        prefix = '/html/body/div[6]/div/div/div[3]/form/div/div[6]/div[1]/div/select/optgroup['
        self._search_option(tabliqplus_group, tabliqplus_sub_group, prefix, ']/option[', ']', separate_by=' -- ')
        sleep(3)

        # ad type
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/form/div/div[7]/div/div/select/'
                                          'option[2]').click()
        sleep(2)

        # province
        prefix = '/html/body/div[6]/div/div/div[3]/form/div/div[9]/div/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div[6]/div/div/div[3]/form/div/div[10]/div/div/select/option['
        self.search(city, prefix, ']', element=2)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="step1_submit"]').click()
        sleep(3)

        # description
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/form/div/div[5]/div/'
                                          'div[6]/p').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/form/div/div[7]/div/'
                                          'input').send_keys(keywords.replace('  ', '\n'))

        # price
        self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        # second submit button
        self.driver.find_element_by_xpath('//*[@id="step2_submit"]').click()
        sleep(2)

        # picture
        self.driver.find_element_by_css_selector('span.btn:nth-child(3)').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="image_upload_submit"]').click()
        sleep(3)

        # third submit button
        self.driver.find_element_by_xpath('//*[@id="step3_submit"]').click()
        sleep(2)

        # final submit button
        self.driver.find_element_by_xpath('//*[@id="payment_submit"]').click()


class PostAd93(IPostAds):
    """ https://www.niazmandiha.net/login/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/form/'
                                          'input[1]').send_keys(self.username)
        
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/form/'
                                          'input[2]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/form/input[4]').click()

        self.post()

    def post(self):
        self.driver.get('https://www.niazmandiha.net/?action=user&do=add')

        # group & sub-group
        prefix = '/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[1]/td/select/option['
        self._search(niazmandiha_net_group, niazmandiha_net_sub_group, prefix, ']', separate_by=' --> ', element=2)

        # title
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[2]/'
                                          'td/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/'
                                          'tr[3]/td/textarea').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/'
                                          'tr[4]/td/input').send_keys(picture)

        # name
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[5]/td/'
                                          'input').clear()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[5]/td/'
                                          'input').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody'
                                          '/tr[6]/td/input').send_keys(phone)

        # province
        prefix = '/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[8]/td/select/option['
        self._search('ایران', province, prefix, ']', separate_by=' --> ')

        # price
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[9]/'
                                          'td/input').send_keys(price)

        # address
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/'
                                          'tr[10]/td/input').send_keys(address)

        # email
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[11]/'
                                          'td/input').clear()

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[11]/'
                                          'td/input').send_keys(email)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[13]/'
                                          'td/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[13]/'
                                          'td/input').send_keys(website_link)

        # keywords
        keyword = keywords.split('  ')
        element = 1
        for i in range(5):
            try:
                keyword_path = '/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[14]/td/div/input[' + str(
                    element) + ']'
                self.driver.find_element_by_xpath(keyword_path).send_keys(keyword[i])
                sleep(1)
                element += 1
            except IndexError:
                pass

        # ad type
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/tbody/tr[16]/td/'
                                          'select/option[9]').click()

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/fieldset[1]/div/table/'
                                          'tbody/tr[17]/td/input').click()


class PostAd94(IPostAds):
    """ https://noonerooz.com/%d9%88%d8%b1%d9%88%d8%af-%d8%a8%d9%87-
        %d8%ad%d8%b3%d8%a7%d8%a8-%da%a9%d8%a7%d8%b1%d8%a8%d8%b1%db%8c/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/div/div[2]/div[1]/'
                                          'form/p[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('https://noonerooz.com/newad/')

        # group
        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[1]/div/div[2]/a['
        self.search(noonerooz_group, prefix, ']')
        sleep(2)

        # sub-group
        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[1]/div/div[2]/a['
        self.search(noonerooz_sub_group, prefix, ']')
        sleep(2)

        # title
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/div[4]/div[1]/div/input').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="details"]').send_keys(description)

        # province
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/section[2]/div/div[2]/div/div/button').click()

        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[2]/div[2]/section[2]/' \
                 'div/div[2]/div/div/div/div[2]/ul/li['
        self._search_(province, prefix, ']/a/span')
        sleep(4)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/section[3]/div/section/section[1]/div/div/div/'
                                          'input').send_keys(website_link)

        # phone
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/section[3]/div/section/section[3]/div/div/div/'
                                          'input').send_keys(phone)

        # picture
        self.driver.find_element_by_xpath('//*[@id="charsoogh-file-upload"]').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/button[1]').click()
        sleep(5)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/div[2]/'
                                          'div/button[1]').click()


class PostAd95(PostAd81):
    """ https://iranamir.com/ads/auth *** captcha *** """
    @staticmethod
    def page_info():
        page = 'https://iranamir.com/ads/new'
        return page, agahimax_group, agahimax_sub_group, agahimax_sub_sub_group


class PostAd96(PostAd81):
    """ http://nabzeroz.ir/auth  *** captcha *** """
    @staticmethod
    def page_info():
        page = 'http://nabzeroz.ir/new'
        return page, nabzeroz_group, nabzeroz_sub_group


class PostAd97(IPostAds):
    """ https://www.hogre.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
        
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[4]/button').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.get('https://www.hogre.ir/panel/ads/create')

        # title
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[1]/div/'
                                          'input').send_keys(title)

        # short_description
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[2]/div/'
                                          'textarea').send_keys(short_description)
        
        # description
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[3]/div/'
                                          'textarea').send_keys(description)

        # province
        self.driver.find_element_by_xpath('//*[@id="select2-state-container"]').click()
        sleep(2)
        prefix = '/html/body/span/span/span[2]/ul/li['
        self._search_(province, prefix, ']', element=2)
        sleep(2)

        # city
        prefix = '/html/body/div/main/div/div/div/div[2]/form/div[5]/div/select/option['
        self.search(city, prefix, ']', element=2)
        sleep(1)

        # group
        self.driver.find_element_by_xpath('//*[@id="select2-category-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(hogre_group, prefix, ']')
        sleep(2)
        
        # sub-group
        self.driver.find_element_by_xpath('//*[@id="select2-category2-container"]').click()
        prefix = '/html/body/span/span/span[2]/ul/li['
        self.search(hogre_sub_group, prefix, ']')
        sleep(2)

        # sub sub-group
        if hogre_sub_sub_group:
            self.driver.find_element_by_xpath('//*[@id="select2-category3-container"]').click()
            prefix = '/html/body/span/span/span[2]/ul/li['
            self.search(hogre_sub_sub_group, prefix, ']')
            sleep(2)

        # phone
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[9]/div/'
                                          'input').send_keys(phone)

        # picture
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[12]/label/span').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div/main/div/div/div/div[2]/form/div[13]/button').click()


class PostAd98(IPostAds):
    """ http://www.radtabligh.com/fa/index.asp?p=Login&m=Client *** captcha *** """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login-box-user"]').send_keys(self.username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/fieldset/div[4]/div[2]/'
                                          'form/input[2]').send_keys(self.password)

        # CAPTCHA delay
        try:
            self.driver.find_element_by_xpath('//*[@id="securityCode"]').click()
            sleep(13)
        except NoSuchElementException:
            pass

        # login button
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/fieldset/div[4]/div[2]/'
                                          'form/input[4]').click()
        
        self.post()

    def post(self):
        self.driver.get('http://www.radtabligh.com/newads/12809')

        # group
        prefix = '/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/table/tbody/tr[1]/td[2]/' \
                 'select/option['
        self.search(radtabligh_group, prefix, ']', element=2)
        sleep(4)

        # sub-group
        prefix = '/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/table/tbody/tr[2]/td[2]/p/' \
                 'select/option['
        self.search(radtabligh_sub_group, prefix, ']')

        # title
        self.driver.find_element_by_xpath('//*[@id="txtTitle"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="text"]').send_keys(description)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/'
                                          'table/tbody/tr[5]/td[2]/p/img').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # name
        self.driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/'
                                          'form/table/tbody/tr[6]/td[2]/input[2]').send_keys(phone)

        # price
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/'
                                          'table/tbody/tr[7]/td[2]/input[2]').send_keys(price)

        # address
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/'
                                          'table/tbody/tr[8]/td[2]/input').send_keys(address)

        # website_link
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/'
                                          'table/tbody/tr[9]/td[2]/input').send_keys(website_link)

        # keywords
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/'
                                          'form/table/tbody/tr[11]/td[2]/textarea').send_keys(
            keywords.replace('  ', ','))

        # province
        prefix = '/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/table/tbody/tr[12]/td[2]/' \
                 'select[2]/option['
        self._search_(province, prefix, ']', element=2)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/div[2]/fieldset[1]/div/form/'
                                          'table/tbody/tr[14]/td[2]/button').click()


class PostAd99(IPostAds):
    """ http://aghayeagahi.ir/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        self.driver.find_element_by_xpath('/html/body/section/nav/div/div/div/div/ul[2]/li[1]/a').click()
        sleep(3)

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="log_email"]').send_keys(self.username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="log_password"]').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[1]/div/div[5]/form/button').click()
        sleep(4)
        self.post()

    def post(self):
        self.driver.get('http://aghayeagahi.ir/submit-ads/')
        sleep(2)
        self.driver.get('http://aghayeagahi.ir/submit-ads/')

        # title
        self.driver.find_element_by_xpath('//*[@id="listing_title"]').send_keys(title)

        # group
        prefix = '/html/body/section[3]/div/div/div/form/div[2]/div[1]/div[2]/div/select/option['
        self.search(aghayeagahi_group, prefix, ']', element=2)
        sleep(5)

        # phone
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[2]/div[4]/div/div/'
                                          'div[1]/input').send_keys(phone)

        # description
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[4]/div/div[1]/div/'
                                          'div[1]/div[3]').send_keys(description)

        # email
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[4]/div/div[2]/div/'
                                          'div[1]/input').send_keys(email)

        # keywords
        try:
            self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[4]/div/'
                                              'div[3]/div/ul/li[2]').send_keys(keywords.replace('  ', ','))
        except ElementNotInteractableException:
            pass

        # picture
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[4]/div/div[4]/'
                                          'div[1]/div/div').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # address
        self.driver.find_element_by_xpath('//*[@id="address_location"]').send_keys(address)

        # country
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[5]/div/div[5]/div/'
                                          'select/option[2]').click()
        sleep(5)

        # province
        prefix = '/html/body/section[3]/div/div/div/form/div[5]/div/div[6]/div/select/option['
        self._search_(province, prefix, ']', element=2)
        sleep(5)

        # city
        prefix = '/html/body/section[3]/div/div/div/form/div[5]/div/div[7]/div/select/option['
        self.search(city, prefix, ']', element=2)
        sleep(5)

        # submit button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/form/div[5]/div/div[9]/'
                                          'div/button').click()


class PostAd100(IPostAds):
    """ https://jaraghe.net/my-account/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        # login button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/div/div[2]/div[1]/form/'
                                          'p[3]/button').click()

        self.post()

    def post(self):
        self.driver.get('https://jaraghe.net/newad/')

        # group
        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[1]/div/div[2]/a['
        self.search(jaraghe_group, prefix, ']')
        sleep(7)
        
        # sub-group
        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[1]/div/div[2]/a['
        self.search(jaraghe_sub_group, prefix, ']')
        sleep(7)

        # sub sub-group
        if jaraghe_sub_sub_group:
            prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[1]/div/div[2]/a['
            self.search(jaraghe_sub_sub_group, prefix, ']')
            sleep(6)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)
        
        # price
        self.driver.find_element_by_xpath('//*[@id="price_show"]').send_keys(price)

        # description
        self.driver.find_element_by_xpath('//*[@id="details"]').send_keys(description)

        # city
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/div[2]/'
                                          'div[2]/section[2]/div/div[2]/div/div/button').click()
        prefix = '/html/body/div/main/section/div/div/div/article/section/div/form/div[2]/div[2]/section[2]/div/' \
                 'div[2]/div/div/div/div[2]/ul/li['
        self.search(city, prefix, ']/a/span')
        sleep(4)

        # picture
        self.driver.find_element_by_xpath('//*[@id="charsoogh-file-upload"]').click()
        sleep(2)
        pyautogui.write(f'{picture}')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)

        # first submit button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/form/'
                                          'div[2]/div[2]/button[1]').click()
        sleep(7)

        # final submit button
        self.driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/article/section/div/'
                                          'div[2]/div/button[1]').click()
