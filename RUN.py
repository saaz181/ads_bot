import time
from robot import *
import logging
from selenium.common.exceptions import NoSuchWindowException
from info import (_username_, _password_, most_username, most_password,
                  ap_username, ap_password, niazerooz_username,
                  niazerooz_password, sellfree_username,
                  sellfree_password, zibashahr_username, zibashahr_password)

start_time = time.time()

posts = [
    [PostAd1, links[0]],
    [PostAd2, links[1]],
    [PostAd3, links[2]],
    [PostAd4, links[3]],
    [PostAd5, links[4]],
    [PostAd7, links[6]],
    [PostAd8, links[7]],
    [PostAd9, links[8]],
    [PostAd10, links[9]],
    # PostAd11 in RUN_CAPTCHA
    # PostAd14 in RUN_CAPTCHA
    [PostAd15, links[14]],
    [PostAd16, links[15]],
    [PostAd18, links[17]],
    # PostAd21 in RUN_CAPTCHA
    [PostAd23, links[22]],
    [PostAd24, links[23]],
    # PostAd25 in RUN_CAPTCHA
    [PostAd26, links[25]],
    # PostAd28 in RUN_CAPTCHA
    # PostAd29 in RUN_CAPTCHA
    [PostAd30, links[29]],
    [PostAd31, links[30]],
    # PostAd32 in RUN_CAPTCHA
    [PostAd34, links[33]],
    # PostAd37 in RUN_CAPTCHA
    [PostAd38, links[37]],
    [PostAd40, links[39]],
    [PostAd41, links[40]],
    [PostAd42, links[41]],
    [PostAd43, links[42]],
    [PostAd44, links[43]],
    [PostAd45, links[44]],
    [PostAd46, links[45]],
    [PostAd47, links[46]],
    [PostAd48, links[47]],
    [PostAd49, links[48]],
    [PostAd50, links[49]],
    [PostAd51, links[50]],
    [PostAd52, links[51]],
    [PostAd53, links[52]],
    [PostAd54, links[53]],
    [PostAd55, links[54]],
    [PostAd56, links[55]],
    [PostAd57, links[56]],
    [PostAd58, links[57]],
    [PostAd59, links[58]],
    [PostAd60, links[59]],
    [PostAd63, links[62]],
    [PostAd64, links[63]],
    [PostAd65, links[64]],
    [PostAd66, links[65]],
    [PostAd70, links[69]],
    [PostAd71, links[70]],
    [PostAd75, links[74]],
    [PostAd77, links[76]],
    [PostAd78, links[77]],
    [PostAd80, links[79]],
    [PostAd83, links[82]],
    [PostAd85, links[84]],
    [PostAd86, links[85]],
    [PostAd87, links[86]],
    [PostAd88, links[87]],
    [PostAd91, links[90]],
    [PostAd93, links[92]],
    [PostAd94, links[93]],
    [PostAd97, links[96]],
    [PostAd99, links[98]],
    [PostAd100, links[99]],
]

different_user_pass_posts = [
    [PostAd12, most_username, most_password, links[11]],
    [PostAd13, most_username, most_password, links[12]],
    [PostAd17, niazerooz_username, niazerooz_password, links[16]],
    [PostAd19, most_username, most_password, links[18]],
    [PostAd20, ap_username, ap_password, links[19]],
    [PostAd22, most_username, most_password, links[21]],
    [PostAd27, sellfree_username, sellfree_password, links[26]],
    [PostAd33, most_username, most_password, links[32]],
    [PostAd35, most_username, most_password, links[34]],
    [PostAd36, most_username, most_password, links[35]],
    [PostAd61, most_username, most_password, links[60]],
    [PostAd62, zibashahr_username, zibashahr_password, links[61]],
    [PostAd68, most_username, most_password, links[67]],
    [PostAd69, most_username, most_password, links[68]],
    [PostAd72, most_username, most_password, links[71]],
    [PostAd73, most_username, most_password, links[72]],
    [PostAd92, most_username, most_password, links[91]],
]

# For websites which have same username & password #
for post in posts:
    try:
        _url_ = post[1]
        ad = post[0](_url_, _username_, _password_)
        sleep(5)
        # ad.close()

    except NoSuchWindowException:
        pass

    except Exception as error:
        logging.error(f"{error} at {post[1]}")

# For websites which have different username & password #
for post in different_user_pass_posts:
    try:
        _url_ = post[3]
        ad = post[0](_url_, post[1], post[2])
        sleep(2)
        # ad.close()

    except Exception as error:
        logging.error(f"{error} at {post[3]}")

# close_()

print("\n\n--- %s seconds ---" % (time.time() - start_time))
