from robot import *
import logging

# TODO: take correct username & password for the PostAds that are diffrent

with open('info.txt', 'r', encoding='utf-8') as info:
    file = info.readlines()
    for line in file:
        line = line.split('=')
        if 'default_username' in line[0]:
            _username_ = line[1].strip()

        if 'default_password' in line[0]:
            _password_ = line[1].strip()


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
    [PostAd11, links[10]],
    [PostAd12, _username_, _password_, links[11]],
    [PostAd13, _username_, _password_, links[12]],
    [PostAd14, links[13]],
    [PostAd15, links[14]],
    [PostAd16, links[15]],
    [PostAd17, _username_, _password_, links[16]],
    [PostAd18, links[17]],
    [PostAd19, _username_, _password_, links[18]],
    [PostAd20, links[19]],
    # PostAd21 in RUN_CAPTCHA
    [PostAd22, _username_, _password_, links[21]],
    [PostAd23, links[22]],
    [PostAd24, links[23]],
    # PostAd25 in RUN_CAPTCHA
    [PostAd26, links[25]],
    [PostAd27, _username_, _password_, links[26]],
    # PostAd28 in RUN_CAPTCHA
    # PostAd29 in RUN_CAPTCHA
    [PostAd30, links[29]],
    [PostAd31, links[30]],
    [PostAd32, links[31]],
    [PostAd33, _username_, _password_, links[32]],
    [PostAd34, links[33]],
]

for post in posts:
    if len(post) == 2:
        try:
            _url_ = post[1]
            ad = post[0](_url_, _username_, _password_)
            sleep(2)
            ad.close()

        except Exception as e:
            print(e)
            logging.error(f"Failed at {post[1]}")

