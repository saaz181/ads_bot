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
        [PostAd37, links[36]],
        [PostAd39, links[38]],
        [PostAd67, links[66]],
        [PostAd74, links[73]],
        [PostAd79, links[78]],
        [PostAd81, links[80]],
        [PostAd82, links[81]],
        [PostAd84, links[83]],
        [PostAd89, links[88]],
        [PostAd90, links[89]],
        [PostAd95, links[94]],
        [PostAd96, links[95]],
        [PostAd98, links[97]]
    ]

for website in link:
    _url_ = website[1]
    try:
        ad = website[0](_url_, _username_, _password_)
        sleep(1)
        ad.close()

    except Exception as error:
        print(error)
        logging.error(f'Failed at {website[1]}')

    except FileNotFoundError:
        pass

close_()
