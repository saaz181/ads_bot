from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import logging
from abc import abstractmethod, ABCMeta
import sys


# Convert String to class object
def str_to_class(class_name):
    return getattr(sys.modules[__name__], class_name)


# logging configuration
logging.basicConfig(filename='robot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# WEBSITE URLS
links = [
    'http://www.soodiran.com', 'https://www.shahr24.com/', 'http://digiagahi.com', 'https://persianagahi.com',
    'http://parsu.ir', 'https://agahi90.ir/', 'https://www.niaz118.com/', 'http://www.decornama.com',
    'http://www.tehran-tejarat.com', 'https://vista.ir/ads/', 'https://agahiname.com/',
    'https://agahiroz.com/%d9%88%d8%b1%d9%88%d8%af/', 'https://parstabligh.org/user_login/',
    'https://www.panikad.com/auth/login/', 'https://www.novintabligh.com/login.html', 'https://www.takro.net/',
    'https://my.niazerooz.com/membership', 'https://eforosh.com/', 'http://newagahi.ir/login_register.php',
    'https://71ap.ir/login/', 'https://otab.ir/auth',
    'https://www.agahichi.com/%D9%88%D8%B1%D9%88%D8%AF-%D8%B3%D8%A7%DB%8C%D8%AA.html', 'http://shetabe.ir/login',

]


# design class of our classes
class IPostAds(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, url, username, password):
        PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(PATH)
        self.username = username
        self.password = password
        self.driver.get(url)
        self.login()

        """ Information for login and load page"""

    @staticmethod
    def match(string, other):
        count = 0
        match_length = len(string)
        partion = len(string.split(' '))
        for i, j in zip(string, other):
            if i == j:
                count += 1
        if count > ((match_length / 3) * 2) and partion == 1:
            return True
        elif partion > 1:
            if count > match_length - 3:
                return True
        return False

    @abstractmethod
    def login(self):
        """ Login method """

    @abstractmethod
    def post(self):
        """ Post our ads """


class PostAd1(IPostAds):
    """ http://www.soodiran.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[2]/input')\
            .send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[4]/input')\
            .send_keys(password)

        # login button
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/form/div[5]/input').click()

        sleep(2)
        self.post()

    def post(self):
        # Enter to post ads page
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[3]/a').click()

        """ INFO """
        group = 'آموزش'
        sub_group = 'آموزش زبان'
        title = 'اموزشگاه زبان'
        description = 'some content'  # TODO: add picture field
        province = 'خراسان رضوی'
        city = 'مشهد'
        price = '5000'
        address = 'مشهد-خیابان فلان'
        phone = '055615151'

        # Select Group
        select_group = Select(self.driver.find_element_by_name('group'))
        select_group.select_by_value(group)

        # Select Sub Group
        sleep(1)
        select_sub_group = Select(self.driver.find_element_by_name('subgroup'))
        select_sub_group.select_by_value(sub_group)

        # Title
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[3]/td[2]/input')\
            .send_keys(title)

        # Description
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/table/tbody/tr[4]/td[2]/textarea') \
            .send_keys(description)

        sleep(1)
        # Select Province
        select_province = Select(self.driver.find_element_by_name('ostan'))
        select_province.select_by_value(province)

        # Select City
        sleep(1)
        select_city = Select(self.driver.find_element_by_name('city'))
        select_city.select_by_value(city)

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
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_UserNameTBX"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_PasswordTbx"]').send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ClubMenu_UC1_LoginBtn"]').click()
        sleep(5)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/form/div[4]/header/div[1]/div/div[4]/a').click()

        """ INFO """
        main_group = 'کامپیوتر'
        group = 'طراحی سایت'
        title = 'برنامه نویسی'
        description = 'برنامه تحت وب'
        price = '20000'
        discount_price = ''     # <optional>
        keywords = 'خوب'           # <optional>
        picture = r'C:/Users/Sabalan/Pictures/index.jpg'
        name = 'علی'
        phone = '09156455409'
        city = 'مشهد'
        address = 'ابوذر غفاری'

        sleep(2)
        # select main group
        select_group = Select(self.driver.find_element_by_id('Body1PlaceHolder_MianDDCategory'))
        select_group.select_by_visible_text(main_group)
        sleep(1)

        # select sub group
        select_sub_group = Select(self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_BackupDropDownList1"]'))
        select_sub_group.select_by_visible_text(group)

        # title
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtTitle"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtBody"]').send_keys(description)

        # price
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtPrice"]').send_keys(price)

        # discount price is <optional>
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtOffer"]').clear()
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtOffer"]').send_keys(discount_price)

        # Keywords <optional>
        self.driver.find_element_by_xpath('//*[@id="Body1PlaceHolder_txtKeywords"]').send_keys(keywords)

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
        element_number = 1

        while True:
            select_city = self.driver.find_element_by_css_selector('ul.dropdown-menu:nth-child(1) > '
                                                                   'li:nth-child(' + str(element_number) + ')')
            if select_city.text == city:
                select_city.click()
                break
            if element_number > 70:
                print("City Not Found!")
                break
            element_number += 1

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
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        # login btn
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()

        sleep(2)
        self.post()

    def post(self):
        # Goto to post page
        self.driver.find_element_by_xpath('/html/body/ul/div/li[2]/a').click()
        sleep(1)

        """ INFO """
        group = 'اینترنت'
        sub_group = 'اخبار و رسانه'
        title = 'اینترنت خوبه'
        description = 'اینترنت پرسرعت'
        keywords = 'من-تو-او'
        website_link = ''  # <optional>
        price = '20000'
        province = 'آذربایجان غربی'
        city = 'ارومیه'
        picture = r'C:/Users/Sabalan/Pictures/index.jpg'
        home_phone = '09525155151'
        mobile_phone = '3545444354'

        # Select group
        select_group = Select(self.driver.find_element_by_id('main_group'))
        select_group.select_by_visible_text(group)

        # Select sub group
        select_sub_group = Select(self.driver.find_element_by_id('sub_group'))
        select_sub_group.select_by_value(sub_group)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys(description)

        # Keyword <optional>
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords)

        # website_link <optional>
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys(website_link)

        # price
        self.driver.find_element_by_xpath('//*[@id="adsprice"]').send_keys(price)

        # Select Province
        select_province = Select(self.driver.find_element_by_id('ostan'))
        select_province.select_by_visible_text(province)
        sleep(1)

        # Select city
        select_city = Select(self.driver.find_element_by_id('Shahrestan'))
        select_city.select_by_value(city)

        # picture
        self.driver.find_element_by_xpath('//*[@id="image"]').send_keys(picture)

        # Home Phone
        self.driver.find_element_by_xpath('//*[@id="tel"]').send_keys(home_phone)

        # Mobile phone
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(mobile_phone)

        # submit
        self.driver.find_element_by_xpath('//*[@id="addads"]').click()


class PostAd4(IPostAds):
    """ https://persianagahi.com """
    """
    NOTICE: we can just post 3 FREE ads in this website per month
    """
    def __init__(self, url ,username, password):
        super().__init__(url, username, password)

    def login(self):
        # go to login page
        self.driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div/section/div/div/div/ul/li[6]/a').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys(username)
        # Enter password
        self.driver.find_element_by_xpath('//*[@id="edit-pass"]').send_keys(password)

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

        """ INFO """
        title = 'کامپیوتر'
        group = 'کامپيوتر و اینترنت'
        sub_group = 'خرید و فروش لپ تاپ'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'  # min size is : 250x250 px
        description = 'بهترین لپتاپ'
        keywords = 'لپتاپ-کامپبوتر-pc'
        address = 'خیابان فلان-کوچه فلان'
        name = 'علی'
        phone = '09156654545'
        email = 'saliaz.mg326@gmail.com'
        website_address = 'https://example.com'  # <optional>
        website_title = 'example'    # <optional>
        price = '200000'

        # title
        self.driver.find_element_by_xpath('//*[@id="edit-title"]').send_keys(title)

        # group
        select_group = Select(self.driver.find_element_by_id('edit-taxonomy-catalog-und-hierarchical-select-selects-0'))
        select_group.select_by_visible_text(group)
        sleep(8)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_name('taxonomy_catalog[und][hierarchical_select]'
                                                                   '[selects][1]'))
        select_sub_group.select_by_visible_text(sub_group)

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
        self.driver.find_element_by_xpath('//*[@id="edit-field-tags-und"]').send_keys(keywords)

        # address
        self.driver.find_element_by_xpath('//*[@id="edit-field-address-und-0-value"]').send_keys(address)

        # name
        self.driver.find_element_by_xpath('//*[@id="edit-field-name-und-0-value"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('//*[@id="edit-field-tel-und-0-value"]').send_keys(phone)

        # email
        self.driver.find_element_by_xpath('//*[@id="edit-field-email-und-0-email"]').send_keys(email)

        # website address
        self.driver.find_element_by_xpath('//*[@id="edit-field-website-und-0-url"]').send_keys(website_address)

        # website title <up until 128 character>
        self.driver.find_element_by_xpath('//*[@id="edit-field-website-und-0-title"]').send_keys(website_title)

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
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        sleep(1)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/'
                                          'div[2]/form/div[3]/div[2]/button').click()

        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/a').click()
        sleep(2)

        """ INFO """
        title = 'دو چیزی'
        description = 'چقد خوب و عالی'
        group = 'کامپیوتر'
        sub_group = 'لپ تاپ'
        picture = r'C:/Users/Sabalan/Pictures/index.jpg'
        province = 'خراسان رضوی'
        keywords = 'خبی یبی خیب'
        phone = '464541254512'

        # title
        self.driver.find_element_by_xpath('//*[@id="titlefa_IR"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="descriptionfa_IR"]').send_keys(description)
        sleep(1)

        # group
        select_group = Select(self.driver.find_element_by_id('select_1'))
        select_group.select_by_visible_text(group)
        sleep(1)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('select_2'))
        select_sub_group.select_by_visible_text(sub_group)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div/form/fieldset/div[3]'
                                          '/div[1]/div/div/div/div[3]/input').send_keys(picture)

        # province
        select_province = Select(self.driver.find_element_by_id('regionId'))
        select_province.select_by_visible_text(province)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="s_tags"]').send_keys(keywords)

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
        from PIL import Image
        import pytesseract

        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/form/div[2]/header/div/div[1]/div/ul[2]/li[1]/a').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="mainContent_TextBox1"]').send_keys(username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="mainContent_TextBox2"]').send_keys(password)

        # captcha
        with open('index.jpg', 'wb') as file:
            file.write(self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div/div/'
                                                         'div[1]/div/div[1]/div[1]/div/img').screenshot_as_png)
        sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        captcha = pytesseract.image_to_string(Image.open('index.jpg'))

        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContent_txtValidate"]').send_keys(captcha)

        # login button
        try:
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="mainContent_Button1"]').click()

        except NoSuchElementException:
            pass

        sleep(2)
        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/'
                                              'div/div[2]/div[1]/div/div[1]/div[1]/a').click()

        except NoSuchElementException:
            self.login()
        sleep(1)

        """ INFO """
        group = 'كامپيـوتر'
        sub_group = 'خدمات اينترنت و شبكه'

        province = 'آذربایجان شرقی'
        city = 'آذرشهر'

        title = 'sdfsdf'
        short_description = 'fsdfsf'
        description = 'sdfsdf'
        keywords = 'fsdfsf'
        website_link = 'http://example.com'
        price = 'fsdfsfs'
        picture = r'C:\Users\Sabalan\Pictures\nature.jpg'
        address = 'خیابان فلان-پلاک1111'

        # select group & sub-group
        self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/div/div/'
                                          'div[1]/div[2]/div[1]/div/div[1]').click()
        sleep(1)

        element = 1
        loop = True
        while loop:
            try:
                group_txt = str(self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/'
                                                              'div/div/div[1]/div[2]/div[1]/div/div[2]/div/div['
                                                              + str(element) + ']').text)
                group_txt = group_txt.split()
                if group_txt[0] == group and " ".join(group_txt[2:]) == sub_group:
                    self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/'
                                                      'div/div/div[1]/div[2]/div[1]/div/div[2]/div/div['
                                                      + str(element) + ']').click()
                    loop = False

                element += 1

            except NoSuchElementException:
                logging.error("Not Found - https://agahi90.ir/ ")
                loop = False

        # select province & city

        self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/div[2]/div/'
                                          'div/div[1]/div[2]/div[2]/div/div[1]').click()
        sleep(2)
        element = 1
        loop = True
        while loop:
            try:
                city_txt = str(self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/'
                                                                 'div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/'
                                                                 'div/div[' + str(element) + ']').text)

                try:
                    city_txt = city_txt.split("»")
                    if city_txt[0].strip() == province and city_txt[1].strip() == city:
                        self.driver.find_element_by_xpath('/html/body/form/div[2]/section/section/div/div/'
                                                          'div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/'
                                                          'div/div[' + str(element) + ']').click()
                        loop = False
                except IndexError:
                    pass

                element += 1

            except NoSuchElementException:
                logging.error("Not Found - https://agahi90.ir/ ")
                loop = False

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
    """ https://www.niaz118.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/ul/li[3]/a').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

        # login buttin
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]'
                                          '/div/div[1]/div[1]/form/input[1]').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/ul/li[2]/a').click()
        sleep(1)

        """ INFO """
        title = 'سلام چه خبر چیکار میکتی بسیبسیبسیب'
        group = 'كامپيـوتری'
        sub_group = 'گرافيك كامپيوتري'
        description = 'یشسیشسیشسیسسسسسسسسسسسسسسسسسسیسشیشسیشسیشسشسیشسیشسیشسیشسیشسیشسیشسیشسیسشیشیسشیشسیشسیشیشسسیشسیشسیسشییسیییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییییی'
        price = '2323232323'
        picture = r'C:/Users/Sabalan/Pictures/index.jpg'
        address = 'asdasdasdsdasdadadsadas'
        province = 'آذربايجان شرقي'

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # click on sale button
        self.driver.find_element_by_xpath('//*[@id="reg2"]').click()

        # group
        select_group = Select(self.driver.find_element_by_id('MainType'))
        select_group.select_by_visible_text(group)
        sleep(1)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('SubType'))
        select_sub_group.select_by_visible_text(sub_group)

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
        select_province = Select(self.driver.find_element_by_name('state'))
        select_province.select_by_visible_text(province)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/'
                                          'div[1]/form/div/table/tbody/tr/td[1]/input').click()


class PostAd8(IPostAds):
    """ http://www.decornama.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/'
                                          'div/div[1]/div[1]/div/div/ul/li[1]/a').click()
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="btn-register"]').click()

        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/'
                                          'div/div[1]/div/div/div/ul/li[3]/a').click()

        """ INFO """
        # TODO: add list of items that we can pick
        title = 'dasd'
        short_description = 'dasdadadadaasd'
        description = 'adsasdasdasdasdasdasdasdasdsad'
        home_phone = '123213132'
        address = 'dasdasdasdasdasda'
        website_link = 'dasdsadaadad'  # <optional>
        email_address = 'dasdsadasdhhkjk'  # <optional>
        keywords = 'gsdg'       # <optional>
        group = 'ژئوتکنیک'
        sub_group = 'اجرای میکروپایل'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

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
        self.driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(email_address)

        # Keywords
        self.driver.find_element_by_xpath('//*[@id="inputKeyword1"]').send_keys(keywords)

        # select group
        element = 1
        loop = True
        while loop:
            try:
                group_txt = str(self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/div/'
                                                                  'div[2]/div/div/form/div[11]/div/div/ul/li['
                                                                  + str(element) + ']/a').text)
                group_txt = group_txt.split()
                if " ".join(group_txt[1:]) == group.strip():
                    self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/div/'
                                                      'div[2]/div/div/form/div[11]/div/div/ul/li['
                                                      + str(element) + ']/a').click()
                    loop = False
                element += 1

            except NoSuchElementException:
                loop = False

        # select sub group
        sleep(2)
        element = 1
        loop = True
        while loop:
            try:
                sub_group_txt = str(
                    self.driver.find_element_by_css_selector('#tab2000 > p:nth-child(1) >'
                                                             ' label:nth-child(' + str(element) + ')').text)

                if sub_group_txt == sub_group:
                    self.driver.find_element_by_css_selector('#tab2000 > p:nth-child(1) >'
                                                             ' label:nth-child(' + str(element) +
                                                             ') > input:nth-child(1)').click()
                    loop = False

                element += 1

            except NoSuchElementException:
                element += 1

        # select picture
        self.driver.find_element_by_xpath('//*[@id="inputImage"]').send_keys(picture)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="btn-register"]').click()


class PostAd9(IPostAds):
    """ http://www.tehran-tejarat.com """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/header/div[1]/div/div[3]/a[2]').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_Uc_'
                                          'LoginUsers_TextBoxUsername"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_Uc_LoginUsers_TextBoxPass"]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_Uc_LoginUsers_ButtonLogin"]').click()

        sleep(1)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/header/div[1]/div/div[2]/div/a').click()

        """ INFO """
        title = 'dasdas'
        group = 'کامپیوتر'
        sub_group = 'برنامه نويسي'
        description = 'adasdasdasdasdaddadd'
        keywords = 'afdsfsdfdfsdf'
        province = 'اردبيل'
        city = 'مشهد'
        address = 'شسیشسیشیشیشسی'
        phone = '094512154512'
        website_link = 'https://example.com'  # <optional>
        price = '200000'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # title
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtTitle"]').send_keys(title)

        # group
        select_group = Select(self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_DropDownListCategory"]'))
        select_group.select_by_visible_text(group)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_'
                                                                    'DropDownListSubCategory"]'))
        select_sub_group.select_by_visible_text(sub_group)

        # description
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtDescription"]').send_keys(description)

        # keyword
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtKeyWords"]').send_keys(keywords)

        # province
        select_province = Select(self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_DropDownListOstan"]'))
        select_province.select_by_visible_text(province)

        # city
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtCity"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtAddress"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtPhone"]').send_keys(phone)

        # website link
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtWebSite"]').send_keys(website_link)

        # price
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_TxtPrice"]').send_keys(price)

        # first submit button
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_BtnSabt"]').click()
        sleep(1)

        # picture
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_FileUpload1"]').send_keys(picture)

        # final submit button
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentAsli_BtnSabt"]').click()


class PostAd10(IPostAds):
    """ https://vista.ir/ads/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div/a').click()

        # Enter username
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div[2]/div[1]/div/'
                                          'div[1]/div[2]/div/form/div/div[1]/div/input').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div[2]/div[1]'
                                          '/div/div[1]/div[2]/div/form/div/div[2]/div/input').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div[2]/div[1]/'
                                          'div/div[1]/div[2]/div/form/div/div[3]/button').click()

        sleep(1)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div[2]/form/button').click()

        """ INFO """
        group = 'کامپیوتر'
        sub_group = 'خدمات شبکه'
        title = 'یسبسیب'
        keywords = 'بسیبسببسیبب'
        description = 'سیبسیبسبیبسیببسیبسیب'
        city = 'تهران'
        address = 'بیسبسیبسبسبسبیبب'
        phone = '125454104'
        website_link = ''
        email = 'saliaz.@gmail.com'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_id('cats'))
        select_group.select_by_visible_text(group)
        sleep(1)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('subcats'))
        select_sub_group.select_by_visible_text(sub_group)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="area"]').send_keys(keywords)

        # description
        self.driver.find_element_by_xpath('//*[@id="desc"]').send_keys(description)

        # city
        select_city = Select(self.driver.find_element_by_name('city'))
        select_city.select_by_visible_text(city)

        # Address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(phone)

        # website link
        self.driver.find_element_by_xpath('//*[@id="website"]').send_keys(website_link)

        # email
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)

        # picture
        self.driver.find_element_by_xpath('//*[@id="File"]').send_keys(picture)

        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

        # submit radio button
        self.driver.find_element_by_id('check').click()
        sleep(1)

        # submit buttons
        self.driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div/div[2]/form/button').click()


class PostAd11(IPostAds):
    """ https://agahiname.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # navigate to login page
        self.driver.find_element_by_xpath('/html/body/form/div[2]/div/div/a[1]').click()

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox1"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TextBox2"]').send_keys(password)

        """ Captcha should entered manually """
        sleep(10)

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

        """ INFO """
        group = 'املاک'
        sub_group = 'اجاره اتاق'
        city = 'اراک'
        title = 'سیبسیبسیبب'
        address = 'سیبسیبیسبسبسبسی'
        phone = '09123214569'
        email = 'saliaz.mg326@gmail.com'
        description = 'شسیشسیسبمنیسبئینردیبتردتسبسیبیسب'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList1'))
        select_group.select_by_visible_text(group)
        sleep(2)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList2'))
        select_sub_group.select_by_visible_text(sub_group)

        # city
        select_city = Select(self.driver.find_element_by_id('ContentPlaceHolder1_DropDownList3'))
        select_city.select_by_visible_text(city)

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
    """ https://agahiroz.com/%d9%88%d8%b1%d9%88%d8%af/
        username: saaz
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/header/div/div/div/nav/ul/li[1]/a').click()

        """ INFO """
        group = 'اجاره خودرو'
        title = 'adsadad'
        price = '25000'
        province_city = 'خراسان رضوی - مشهد'
        keywords = 'سبسیبسیببب'
        description = 'بیسبسیبسبسبیسبیسبسببیسبسیسیبسبی'
        email = 'saliaz.mg326@gmail.com'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_id('ad_cat_id'))
        select_group.select_by_visible_text(group)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="getcat"]').click()

        # title
        self.driver.find_element_by_xpath('//*[@id="post_title"]').send_keys(title)

        # price
        self.driver.find_element_by_xpath('//*[@id="cp_price"]').send_keys(price)

        # province & city
        self.driver.find_element_by_css_selector('#list_cp_street > input:nth-child(2)').send_keys(province_city)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags_input"]').send_keys(keywords)

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
        # scroll down
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(5)

        # first submit button   TODO: fixing the submit button
        self.driver.find_element_by_id('step1').click()
        sleep(2)

        # final submit button
        self.driver.find_element_by_id('step2').click()
        sleep(2)

        # show the ads
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/'
                                          'div/main/div/div/div/div[2]/div/a').click()


class PostAd13(IPostAds):
    """ https://parstabligh.org/user_login/
        username: saaz
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/artical/div[5]/'
                                          'div/div[3]/div/form/div[1]/div[2]/input').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/artical/div[5]/div/div[3]/'
                                          'div/form/div[2]/div[2]/input').send_keys(password)

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
            'نه': 9
        }
        captcha_txt = captcha_txt.split()
        number = captcha_txt[2][:2]
        alpha_num = captcha_txt[0]
        captcha = persian_number[alpha_num] + int(number)
        self.driver.find_element_by_xpath('//*[@id="cc"]').send_keys(captcha)

        # login button
        self.driver.find_element_by_xpath('//*[@id="submitbtn"]').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/artical/div[2]/div[2]/a').click()

        """ INFO """
        name = 'علی'
        phone = '09151232321'
        website_link = 'https://example.com'
        province = 'خراسان رضوی'
        city = 'مشهد'
        title = 'یبسبسسیسبیس'
        group = '   ' + 'خدمات آرایشی'
        description = 'یسیسیسیسیسیسسیسیسیسی'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # name
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(name)

        # phone
        self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/div/div[2]/div[2]/input').send_keys(phone)

        # website link
        self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/div/div[3]/div[2]/input').send_keys(website_link)

        # province
        select_province = Select(self.driver.find_element_by_id('item75_select_1'))
        select_province.select_by_visible_text(province)

        # city
        select_city = Select(self.driver.find_element_by_id('item73_select_1'))
        select_city.select_by_visible_text(city)

        # select free ads option
        Select(self.driver.find_element_by_xpath('/html/body/artical/div[6]/form/'
                                                 'div/div[6]/div[3]/select')).select_by_visible_text('آگهی رایگان')

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # group
        select_group = Select(self.driver.find_element_by_id('catID'))
        select_group.select_by_visible_text(group)

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
        self.driver.find_element_by_xpath('//*[@id="Username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(password)

        # CAPTCHA delay time
        sleep(12)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/form/fieldset/div[5]/div/button').click()

        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/header/div[3]/a').click()
            sleep(4)

        except NoSuchElementException:
            logging.error("Captcha didn't entered correctly - https://www.panikad.com/auth/login/ ")

        """ INFO """
        title = 'لیبلیللبیلیلیبلیلبلی'
        description = 'بیسبسبیسبیبسیبسبیبیسب'
        short_description = 'خهشیتشهیتسهخبیخرخشبتح'
        keywords = 'خهیتشخهستیشسهخیتیتهسشیخهشیش'
        price = '232323'
        group = 'کامپیوتر'
        sub_group = 'برنامه نویسی'
        province = 'خراسان رضوی'
        city = 'مشهد'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'
        address = 'شسیسشیسششسشیشسیشیشسی'

        # title
        self.driver.find_element_by_xpath('//*[@id="Title"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="NoticeData"]').send_keys(description)

        # short description
        self.driver.find_element_by_xpath('//*[@id="Description"]').send_keys(short_description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="tags-selectized"]').send_keys(keywords)

        # price
        self.driver.find_element_by_xpath('//*[@id="ProductPrice"]').send_keys(price)

        # group
        select_group = Select(self.driver.find_element_by_id('Cats'))
        select_group.select_by_visible_text(group)
        sleep(1)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('SubCats'))
        select_sub_group.select_by_visible_text(sub_group)

        # province
        select_province = Select(self.driver.find_element_by_id('States'))
        select_province.select_by_visible_text(province)
        sleep(1)

        # city
        select_city = Select(self.driver.find_element_by_id('Cities'))
        select_city.select_by_visible_text(city)

        # picture
        self.driver.find_element_by_xpath('//*[@id="imgup"]').send_keys(picture)

        # address
        self.driver.find_element_by_xpath('//*[@id="Address"]').clear()
        self.driver.find_element_by_xpath('//*[@id="Address"]').send_keys(address)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/form/div[2]/div[9]/button').click()


class PostAd15(IPostAds):
    """ https://www.novintabligh.com/login.html """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[4]/td[2]/input').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[6]/td[2]/input').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[8]/th/input').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/'
                                          'tr[1]/td/table/tbody/tr[1]/td/div/div[1]/a').click()

        """ INFO """
        group = 'كامپيـوتر'
        sub_group = 'گرافيك كامپيوتري'
        title = 'سیبسیسبیسب'
        description = 'بسیبییبخنرهیتسهتبصثب'
        keywords = 'بیسبسببسبسبیبب'
        phone = '09151233212'
        price = '2000'
        address = 'بیسبسبسیبمخنیحخسنر'
        city = '  مشهد'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/'
                                                                'tr/td[1]/table/tbody/tr[1]/td/table[1]/tbody/'
                                                                'tr/td/table/tbody/tr[4]/td[2]/select'))

        select_group.select_by_visible_text(group + " » " + sub_group)

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
        select_city = Select(self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/'
                                                               'tr/td[1]/table/tbody/tr[1]/td/table[1]/tbody/tr/'
                                                               'td/table/tbody/tr[16]/td[4]/select'))
        try:
            select_city.select_by_visible_text(city)

        except NoSuchElementException:
            select_city.select_by_visible_text("  " + city)

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
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[2]/div[1]/div[2]/form/input[2]').click()
        sleep(2)

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[2]/div[1]/div[2]/ul/li[1]/a').click()

        """ INFO """
        group = 'آموزش'
        sub_group = 'كامپيوتر'
        title = 'سیبسبیبسیسیبب'
        description = 'سیبسیبسیبسیببیب'
        keywords = 'بسیبیسیسبسیبب'
        phone = '09121233212'
        price = '20120'
        address = 'بسیبسبیبیبسیبسبیب'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_id('g'))
        select_group.select_by_visible_text(f'{group}   »\u200c   {sub_group}')

        # title
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="text"]').send_keys(description)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="_keywords"]').send_keys(keywords)

        # phone
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(phone)

        # price <تومان>
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)

        # ads type
        Select(self.driver.find_element_by_xpath('//*[@id="type"]')).select_by_visible_text('رایگان')

        # Address
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(address)

        # picture
        self.driver.find_element_by_xpath('//*[@id="photo1"]').send_keys(picture)

        # submit button
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/section[1]/'
                                          'div/div[2]/form/div/div[15]/button').click()


class PostAd17(IPostAds):
    """ https://my.niazerooz.com/membership
        username: 09156455409
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def check_for_integer(self, alpha):
        try:
            int(alpha)
            return True
        except ValueError:
            return False

    def login(self):
        import pytesseract
        import cv2

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="EmailOrMobile"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(password)

        # captcha
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        with open('index.jpg', 'wb') as file:
            file.write(self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/'
                                                         'div/form/div/div[1]/div[2]/div/img').screenshot_as_png)
        img = cv2.imread('index.jpg')
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        captcha = pytesseract.image_to_string(dst)
        captcha_value = "".join(filter(self.check_for_integer, captcha))
        sleep(6)

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
            logging.error("captcha couldn't solve - https://my.niazerooz.com/membership ")
            self.driver.refresh()
            self.login()

        """ INFO """
        group = ''
        sub_groups = ''
        province = ''
        city = ''
        title = ''
        description = ''
        keywords = ''
        address = ''
        phone = ''
        email = ''
        picture = r''

        # group
        self.driver.find_element_by_xpath('//*[@id="categorySelector"]').click()
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(group + ' > ' + sub_groups)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath('//*[@id="groupSelectBox"]').send_keys(Keys.RETURN)

        # province
        self.driver.find_element_by_xpath('//*[@id="regionSelector"]').click()
        sleep(2)
        element = 1
        loop = True
        while loop:
            try:
                province_txt = str(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/'
                                                                     'div[5]/div[2]/div/div[2]/div/div/a['
                                                                     + str(element) + ']').text)
                if province_txt == province:
                    self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/'
                                                                     'div[5]/div[2]/div/div[2]/div/div/a['
                                                                     + str(element) + ']').click()
                    loop = False

                element += 1
            except NoSuchElementException:
                loop = False

        element = 3
        loop = True
        while loop:
            try:
                city_txt = str(self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div/"
                                                                 "div[5]/div[2]/div/div[2]/div/div/a["
                                                                 + str(element) + "]").text)

                if city_txt == city:
                    self.driver.find_element_by_xpath("html/body/div[2]/div[2]/form/div/"
                                                      "div[5]/div[2]/div/div[2]/div/div/a["
                                                      + str(element) + "]").click()
                    loop = False
                element += 1
            except NoSuchElementException:
                loop = False

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

        # picture TODO: make picture input

        # submit
        self.driver.find_element_by_xpath('//*[@id="btnSaveAdv"]').click()


class PostAd18(IPostAds):
    """ https://eforosh.com/ """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/ul/'
                                          'form[2]/table/tbody/tr[1]/td[2]/p/input').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/ul/'
                                          'form[2]/table/tbody/tr[2]/td[2]/p/input').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/a/div[1]/'
                                          'ul/form[2]/table/tbody/tr[3]/td/p/input').click()
        sleep(2)
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/ul/li[1]/a[2]').click()

        """ INFO """
        title = 'asdassadadsdasds'
        group = 'كامپيوتر'
        sub_group = 'خرید کامپیوتر'
        description = 'sdsfsdfsdfsdfsdfsdfsdfsfdfsfd'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'
        price = '20000'
        address = 'adadasdasdadadasdasdsa'
        phone = '09151233212'
        keywords = 'dasdadsadasdadasdasdsadsad'
        province = 'تهران'

        # title
        self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                          'ul/table/tbody/tr[1]/td[2]/p/input').send_keys(title)

        # group
        select_group_and_sub_group = Select(self.driver.find_element_by_id('subcatid'))
        select_group_and_sub_group.select_by_visible_text(group + ' -> ' + sub_group)

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
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords)

        # province
        try:
            select_province = Select(self.driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[2]/'
                                                                       'ul/table/tbody/tr[8]/td[4]/p/select'))
            select_province.select_by_visible_text(province)
        except NoSuchElementException:
            pass

        # submit button
        self.driver.find_element_by_xpath('//*[@id="b1"]').click()


class PostAd19(IPostAds):
    """ http://newagahi.ir/login_register.php
        username: saaz
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        sleep(3)
        # close pop up
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/button').click()

        # Enter username
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[1]/input').send_keys(username)
        sleep(1)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/section[1]/'
                                          'section/div[2]/form/div[2]/input').send_keys(password)

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

        """ INFO """
        title = 'dlsd,skmf'
        phone = '09121233212'
        group = 'کامپیوتر و اینترنت'
        sub_group = 'برنامه نویسی'
        province = 'خراسان رضوی'
        city = 'مشهد'
        description = 'sdsfdsfsdjfhksjdkfshksduhfkshkjdkjsfjkdshfjkshdfsdkjfhskdjhfksjdnfkjfpfp[pqefksdojvsdncjbwfjbdkjsnjdshnfljsdisdjlkfjlsdjfsfsdfsdfsdfsddsffsf'
        keywords = 'adasdd\ndsfsdf\nsdfsdff\n'
        price = '20000'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

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
        element = 2
        loop = True
        while loop:
            try:
                group_txt = str(self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div/'
                                                                  'div[4]/form/div/div[6]/div[1]/ul/li['
                                                                  + str(element) + ' ]/a').text)
                group_txt = group_txt.split(' -- ')
                if group_txt[0] == group and group_txt[1] == sub_group:
                    self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div/'
                                                      'div[4]/form/div/div[6]/div[1]/ul/li['
                                                      + str(element) + ' ]/a').click()
                    loop = False
                element += 1
            
            except NoSuchElementException:
                loop = False

        # select type of ads
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[7]/div/button').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div/'
                                          'div[4]/form/div/div[7]/div/ul/li[2]/a').click()

        # province
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[9]/div/button').click()

        loop = True
        element = 1
        while loop:
            try:
                province_txt = str(self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                                                     'div/div[4]/form/div/div[9]/div/ul/li['
                                                                     + str(element) + ']/a').text)
                if province_txt == province:
                    self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                                      'div/div[4]/form/div/div[9]/div/ul/li['
                                                      + str(element) + ']/a').click()
                    loop = False
                element += 1
            
            except NoSuchElementException:
                loop = False
        sleep(2)

        # city
        self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                          'div/div[4]/form/div/div[10]/div/button').click()

        loop = True
        element = 1
        while loop:
            try:
                city_txt = str(self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                                              'div/div[4]/form/div/div[10]/div/ul/li['
                                                              + str(element) + ']/a').text)
                if city_txt == city:
                    self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/'
                                                      'div/div[4]/form/div/div[10]/div/ul/li['
                                                      + str(element) + ']/a').click()
                    loop = False
                element += 1
            except NoSuchElementException:
                loop = False

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
                                          'div/div[4]/form/div/div[7]/div/input').send_keys(keywords)

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
    """ https://71ap.ir/login/
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(password)
        sleep(2)

        # login button
        self.driver.find_element_by_xpath('//*[@id="login"]').click()

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[3]/ul/li/a').click()

        """ INFO """
        group = 'رایانه'
        sub_group = 'برنامه نویسی'
        title = 'dsfsdfsdfdfds'
        price = '20301'
        phone = '09121233212'
        province = 'خراسان رضوی'
        description = 'خهیتریهختبهخسیتبخسیهبتیسخبهتسخسهبتسیحیسزجحزنسیمئزمنیدسرینسدبخهثصبئنیسمئزنمیسدبهیسبهسیئزنیسئدبندیسندبئسیخمنب'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_id('ad_cat_id'))
        select_group.select_by_visible_text(group)
        sleep(2)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_css_selector('#catlvl1 > select:nth-child(1)'))
        select_sub_group.select_by_visible_text(sub_group)
        sleep(2)

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
        select_province = Select(self.driver.find_element_by_xpath('//*[@id="cp_state"]'))
        select_province.select_by_visible_text(province)

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
    """ https://otab.ir/auth """
    def __init__(self, url, username, password):
        super().__init__(url ,username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('//*[@id="frm_username"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="frm_password"]').send_keys(password)

        # delay time for captcha enter & switch into captcha input field
        self.driver.find_element_by_xpath('//*[@id="login_captcha_input"]').click()
        sleep(10)

        # login button
        self.driver.find_element_by_xpath('/html/body/section/div/div/section[1]/'
                                          'section/div[2]/form/div[5]/div[3]/button').click()

        self.post()

    def post(self):
        try:
            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/div/a').click()
            sleep(2)
        except NoSuchElementException:
            logging.error('Captcha didn\'t entered or is incorrect - https://otab.ir/auth')
            self.login()

        """ INFO """
        title = 'dsfsdfsdfsf'
        group = 'کامپیوتر و اینترنت'
        sub_group = 'برنامه نویسی'
        description = 'سیسحبنیسبخسهیبتسخهیبتسیهخبتسیخهبتیخب'
        price = '2000'
        province = 'خراسان رضوی'
        city = 'شاندیز'
        phone = '09121233212'
        address = 'dasdasdasasadsadsadasdsadsadsadsadasdsadssd'
        keyword = '' + '\n' + '' + '\n' + '' + '\n'  # TODO: fix the keywords
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # title
        self.driver.find_element_by_xpath('//*[@id="frm_title"]').send_keys(title)

        # group
        select_group = Select(self.driver.find_element_by_id('select-category'))
        select_group.select_by_visible_text(group)
        sleep(3)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_id('select-subcategory'))
        select_sub_group.select_by_visible_text(sub_group)

        # picture
        self.driver.find_element_by_xpath('/html/body/div[7]/input').send_keys(picture)

        # type of ad
        Select(self.driver.find_element_by_id('frm_plan_type')).select_by_visible_text('آگهی رایگان')
        sleep(2)

        # price
        self.driver.find_element_by_xpath('//*[@id="frm_price"]').send_keys(price)

        # description
        self.driver.find_element_by_xpath('//*[@id="frm_description"]').send_keys(description)
        sleep(2)

        # province
        select_province = Select(self.driver.find_element_by_id('state_id'))
        select_province.select_by_visible_text(province)
        sleep(2)

        # city
        select_city = Select(self.driver.find_element_by_id('city_id'))
        select_city.select_by_visible_text(city)

        # phone
        self.driver.find_element_by_xpath('//*[@id="frm_tel"]').send_keys(phone)

        # address
        self.driver.find_element_by_xpath('//*[@id="frm_address"]').send_keys(address)

        # keyword
        select_keywords = Select(self.driver.find_element_by_id('frm_keywords'))

        # submit button
        self.driver.find_element_by_xpath('//*[@id="submit_item"]').click()


class PostAd22(IPostAds):
    """ https://www.agahichi.com/%D9%88%D8%B1%D9%88%D8%AF-%D8%B3%D8%A7%DB%8C%D8%AA.html
        username: saaz
    """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        # Enter username
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/'
                                          'div/section/section/div/form/input[2]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div/'
                                          'section/section/div/form/input[3]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/div/'
                                          'div/section/section/div/form/div[2]/input').click()

        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div/div/section/div[2]/'
                                          'div/section/section/div/ul/li[1]/a').click()
        sleep(2)

        """ INFO """
        group = 'کامپیوتر و اینترنت'
        sub_group = 'اینترنت'
        title = 'یبسبسبسیبسب'
        description = 'جبهیسبخهسدیبخهسدیسهدبسهدیسهبدیسهبدیسهسیتدبیستبدسهیتدبینستدبیسندبیسندبسیدبنتسیدبسینتدبسینبدیسبنتدسینبدسیسیدبسینتبسیبنتی'
        phone = '09121233212'
        price = '20000'
        province = 'خراسان رضوی'
        city = 'مشهد'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        select_group = Select(self.driver.find_element_by_xpath('/html/body/div/div[1]/section/div/div/'
                                                                'section/section/div/div[1]/ul[2]/li/div/select'))
        select_group.select_by_visible_text(group)
        sleep(2)

        # sub group
        select_sub_group = Select(self.driver.find_element_by_xpath('/html/body/div/div[1]/section/div/div/section/'
                                                                    'section/div/div[1]/ul[2]/li/div[2]/select'))
        select_sub_group.select_by_visible_text(sub_group)
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
        select_province = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/'
                                                                   'section/div/div[2]/div[4]/div[2]/form/div/div[3]/'
                                                                   'div/div[2]/div[2]/div[2]/select'))
        select_province.select_by_visible_text(province)
        sleep(2)

        # city
        select_city = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/section/'
                                                               'section/div/div[2]/div[4]/div[2]/form/div/div[3]/'
                                                               'div/div[2]/div[3]/div[2]/select'))
        select_city.select_by_visible_text(city)
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
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/'
                                              'section/section/div/div[2]/div[4]/div[4]/input').click()
            sleep(2)


class PostAd23(IPostAds):
    """ http://shetabe.ir/login """
    def __init__(self, url, username, password):
        super().__init__(url, username, password)

    def login(self):
        import cv2
        import pytesseract

        # Enter username
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

        # captcha
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        with open('index.jpg', 'wb') as file:
            file.write(self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/form/'
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

    def post(self):
        try:
            sleep(3)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/div[2]/div/div[1]/a').click()
        except NoSuchElementException:
            logging.error("Captcha didn't entered correctly - http://shetabe.ir/login ")
            self.login()

        """ INFO """
        group = 'کامپیوتر و اینترنت'
        sub_group = 'کامپیوتر'
        province = 'خراسان رضوی'
        city = 'مشهد'
        phone = '09121233212'
        title = 'شسیشسیشسشیشی'
        keywords = 'یشسیشیشسی،بیسبسیب،بسیبسبی'
        price = '20000'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'
        address = 'شسیشسیشیشییشیشیسیشسیس'
        description = 'یسشیسشیشیشسیشسیشیشسیشیسشییسشیس'

        # type of ads
        try:
            Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[3]/'
                                                     'td[2]/select')).select_by_visible_text('رایگان تصویری')
        except NoSuchElementException:
            pass

        try:
            # group
            select_group = Select(self.driver.find_element_by_id('cat'))
            select_group.select_by_visible_text(group)
            sleep(2)

        except NoSuchElementException:
            element = 1
            loop = True
            while loop:
                try:
                    group_txt = str(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                                      'table/tbody/tr[6]/td[2]/select/option['
                                                                      + str(element) + ']').text)

                    if self.match(group, group_txt):
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                          'table/tbody/tr[6]/td[2]/select/option['
                                                          + str(element) + ']').click()
                        loop = False
                    element += 1
                except NoSuchElementException:
                    loop = False

        # sub group
        select_sub_group = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/'
                                                                    'tbody/tr[6]/td[2]/span[1]/select'))
        select_sub_group.select_by_visible_text(sub_group)

        # province
        try:
            select_province = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                                       'table/tbody/tr[7]/td[2]/select'))
            select_province.select_by_visible_text(province)
            sleep(2)
        except NoSuchElementException:
            loop = True
            element = 1
            while loop:
                try:
                    select_province = str(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                                            'table/tbody/tr[7]/td[2]/select/option['
                                                                            + str(element) + ']').text)
                    if self.match(province, select_province):
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                          'table/tbody/tr[7]/td[2]/select/option['
                                                          + str(element) + ']').click()
                        loop = False
                        sleep(2)
                    element += 1
                except NoSuchElementException:
                    loop = False
                    sleep(2)

        # city
        try:
            select_city = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/'
                                                                   'form/table/tbody/tr[7]/td[2]/span/select'))
            select_city.select_by_visible_text(city)
        except NoSuchElementException:
            loop = True
            element = 1
            while loop:
                try:
                    select_city_txt = str(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/'
                                                                         'form/table/tbody/tr[7]/td[2]/span/'
                                                                         'select/option[' + str(element) + ']').text)
                    if self.match(city, select_city_txt):
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/'
                                                          'form/table/tbody/tr[7]/td[2]/span/'
                                                          'select/option[' + str(element) + ']').click()
                        loop = False
                    element += 1
                except NoSuchElementException:
                    loop = False

        # phone
        self.driver.find_element_by_xpath('//*[@id="tell"]').send_keys(phone)

        # title
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)

        # keywords
        self.driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(keywords.replace(' ', '،'))

        # source
        Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/'
                                                 'table/tbody/tr[12]/td[2]/select')).select_by_visible_text('عمومی')

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
        self.driver.find_element_by_xpath('//*[@id="UserNameTextbox"]').send_keys(username)

        # Enter password
        self.driver.find_element_by_xpath('//*[@id="PassTextbox"]').send_keys(password)

        # login button
        self.driver.find_element_by_xpath('//*[@id="AddButton"]').click()
        self.post()

    def post(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a').click()

        """ INFO """
        group = 'کامپیوتر'
        sub_group = 'برنامه نویسی'
        title = 'یسیسبیسب'
        description = 'بیسبسیبسبمدیسندبنسیدبنیتبدینتبینب'
        province = 'خراسان رضوی'
        city = 'مشهد'
        address = 'یبخهیسخهبتسیدبستدبیسنتدبستیندبسینتدنستب'
        phone = '09121233212'
        picture = r'C:/Users/Sabalan/Pictures/nature.jpg'

        # group
        try:
            select_group = Select(self.driver.find_element_by_xpath('//*[@id="MainCatDropdown"]'))
            select_group.select_by_visible_text(group)

        except NoSuchElementException:
            loop = True
            element = 1
            while loop:
                try:
                    group_txt = str(self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/'
                                                                      'div/div[2]/div[3]/div[1]/div[1]/select/option['
                                                                      + str(element) + ']').text)

                    if self.match(group, group_txt):
                        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/'
                                                          'div/div[2]/div[3]/div[1]/div[1]/select/option['
                                                          + str(element) + ']').click()
                        loop = False
                    element += 1
                except NoSuchElementException:
                    loop = False

        # sub group
        try:
            select_sub_group = Select(self.driver.find_element_by_xpath('//*[@id="SubCategoryDropdown"]'))
            select_sub_group.select_by_visible_text(sub_group)
        except NoSuchElementException:
            loop = True
            element = 1
            while loop:
                try:
                    sub_group_txt = str(self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/div'
                                                                          '[2]/div[3]/div[2]/div[1]/select/option['
                                                                          + str(element) + ']').text)
                    if self.match(sub_group, sub_group_txt):
                        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/div'
                                                          '[2]/div[3]/div[2]/div[1]/select/option['
                                                          + str(element) + ']').click()
                        loop = False
                    element += 1
                except NoSuchElementException:
                    loop = False

        # title
        self.driver.find_element_by_xpath('//*[@id="TitleTextbox"]').send_keys(title)

        # description
        self.driver.find_element_by_xpath('//*[@id="DetailTextbox"]').send_keys(description)

        # province
        try:
            select_province = Select(self.driver.find_element_by_xpath('//*[@id="StateDropdown"]'))
            select_province.select_by_visible_text(province)
        except NoSuchElementException:
            loop = True
            element = 1
            while loop:
                try:
                    province_txt = str(self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/'
                                                                         'div[2]/div[6]/div[1]/div[1]/select/option['
                                                                         + str(element) + ']').text)
                    if self.match(province, province_txt):
                        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/'
                                                          'div[2]/div[6]/div[1]/div[1]/select/option['
                                                          + str(element) + ']').click()
                        loop = False
                    element += 1
                except NoSuchElementException:
                    loop = False

        # city
        self.driver.find_element_by_xpath('//*[@id="CityTextbox"]').send_keys(city)

        # address
        self.driver.find_element_by_xpath('//*[@id="txtAddress"]').send_keys(address)

        # phone
        self.driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/div/'
                                          'div[2]/div[6]/div[5]/div[1]/div/input').send_keys(phone)

        # submit button
        self.driver.find_element_by_xpath('//*[@id="AddButton"]').click()
        sleep(5)

        # picture
        self.driver.find_element_by_xpath('//*[@id="UploadPicFile1"]').send_keys(picture)

        # final submit button
        for i in range(2):  # if picture didn't fit in
            self.driver.find_element_by_xpath('//*[@id="btnSubmitPicture"]').click()
            sleep(2)


url = ''
username = ''
password = ''

# ad = PostAd24(url, username, password)

# TODO: make this more efficient
'''         RUN ALL CLASSES
for index, url in enumerate(links):
    ad = str_to_class(f"PostAd{index + 1}")
    if index + 1 == 12 or index + 1 == 13:  username = 'saaz'
    else:  username = ''    

    try:
        ad(url, username, password)
    except NoSuchElementException:
        logging.error(f"{url} - Failed")
'''


