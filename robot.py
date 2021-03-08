from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
from abc import abstractmethod, ABCMeta

logging.basicConfig(filename='robot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class IPostAds(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, url, username, password):
        PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(url)
        self.login()
        """ Information for login and load page"""

    @abstractmethod
    def login(self):
        """ Login method """

    @abstractmethod
    def post(self):
        """ Post our add """


class PostAds(IPostAds):
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


class PostAds2(IPostAds):
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
        sleep(5)

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
                print("Not Found")
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
                print("Not Found")
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

