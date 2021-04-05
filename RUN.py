from robot import *
import logging
from info import (_username_, _password_,
                  ap_username, ap_password,
                  niazerooz_username, niazerooz_password,
                  sellfree_username, sellfree_password,
                  most_username, most_password
                  )

posts = [
    [PostAd1, links[0]],
    [PostAd2, links[1]],
    [PostAd3, links[2]],
    [PostAd4, links[3]],
    [PostAd5, links[4]],
    [PostAd6, links[5]],
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
    [PostAd32, links[31]],
    [PostAd34, links[33]],
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
]


# For websites which have same username & password #
for post in posts:
    try:
        _url_ = post[1]
        ad = post[0](_url_, _username_, _password_)
        sleep(2)
        ad.close()
    except Exception as error:
        print(error)
        logging.error(f"Failed at {post[1]}")


# For websites which have different username & password #
for post in different_user_pass_posts:
    try:
        _url_ = post[3]
        ad = post[0](_url_, post[1], post[2])
        sleep(2)
        ad.close()
    except Exception as error:
        print(error)
        logging.error(f"Failed at {post[3]}")
