from robot import *
import logging

link = [
        [PostAd21, links[20]],
        [PostAd25, links[24]],
        [PostAd28, links[27]],
        [PostAd29, links[28]]
    ]

with open('info.txt', 'r', encoding='utf-8') as info:
    file = info.readlines()
    for line in file:
        line = line.split('=')
        if 'default_username' in line[0]:
            _username = line[1].strip()

        if 'default_password' in line[0]:
            _password = line[1].strip()


for website in link:
    _url = website[1]
    try:
        ad = website[0](_url, _username, _password)
        sleep(1)
        ad.close()
    except Exception as e:
        print(e)
        logging.error(f'Failed at {website[1]}')
    except FileNotFoundError:
        pass
