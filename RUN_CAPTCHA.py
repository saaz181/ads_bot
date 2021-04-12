from robot import *
from info import _username_, _password_
import logging

link = [
        [PostAd11, links[10]],
        [PostAd14, links[13]],
        [PostAd21, links[20]],
        [PostAd25, links[24]],
        [PostAd28, links[27]],
        [PostAd29, links[28]],
        [PostAd32, links[31]],
    ]

for website in link:
    _url = website[1]
    try:
        ad = website[0](_url, _username_, _password_)
        sleep(1)
        ad.close()
    except Exception as e:
        print(e)
        logging.error(f'Failed at {website[1]}')
    except FileNotFoundError:
        pass

close_()
