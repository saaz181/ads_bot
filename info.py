with open('info.txt', 'r', encoding='utf-8') as info:
    file = info.readlines()
    for line in file:
        line = line.split('=')
        if 'default_username' in line[0]:
            _username_ = line[1].strip()

        if 'default_password' in line[0]:
            _password_ = line[1].strip()

        if 'title' == line[0].strip():
            title = line[1].strip()

        if 'description' == line[0].strip():
            description = line[1].strip()

        if 'short_description' in line[0]:
            short_description = line[1].strip()

        if 'address' in line[0]:
            address = line[1].strip()

        if 'province' in line[0]:
            province = line[1].strip()

        if 'city' in line[0]:
            city = line[1].strip()

        if 'name' == line[0].strip():
            name = line[1].strip()

        if 'phone' == line[0].strip():
            phone = line[1].strip()

        if 'home-phone' in line[0]:
            home_phone = line[1].strip()

        if 'keywords' in line[0]:
            keywords = line[1] + '  '

        if 'website-title' in line[0]:
            website_title = line[1].strip()

        if 'website_link' in line[0]:
            website_link = line[1].strip()

        if 'picture' in line[0]:
            picture = line[1].strip()

        if 'price' in line[0]:
            price = line[1].strip()

        if 'email' in line[0]:
            email = line[1].strip()

        if 'main-group' in line[0]:
            main_group = line[1].strip()

        if 'main-sub-group' in line[0]:
            main_sub_group = line[1].strip()

        if 'other-group' in line[0]:
            other_group = line[1].strip()

        if 'other-sub-group' in line[0]:
            other_sub_group = line[1].strip()

        if 'other-sub-sub-group' in line[0]:
            other_sub_sub_group = line[1].strip()

        if 'netmoj-group' in line[0]:
            netmoj_group = line[1].strip()

        if 'netmoj-sub-group' in line[0]:
            netmoj_sub_group = line[1].strip()

        if 'netmoj-sub-sub-group' in line[0]:
            netmoj_sub_sub_group = line[1].strip()

        if 'niaz118-group' in line[0]:
            niaz118_group = line[1].strip()

        if 'niaz118-sub-group' in line[0]:
            niaz118_sub_group = line[1].strip()

        if 'tehran-tejarat-group' in line[0]:
            tehran_tejarat_group = line[1].strip()

        if 'tehran-tejarat-sub-group' in line[0]:
            tehran_tejarat_sub_group = line[1].strip()

        if 'vista-group' in line[0]:
            vista_group = line[1].strip()

        if 'vista-sub-group' in line[0]:
            vista_sub_group = line[1].strip()

        if 'agahinama-group' in line[0]:
            agahinama_group = line[1].strip()

        if 'agahinama-sub-group' in line[0]:
            agahinama_sub_group = line[1].strip()

        if 'agahirooz-group' in line[0]:
            agahirooz_group = line[1].strip()

        if 'parstabligh-group' in line[0]:
            parstabligh_group = line[1].strip()

        if '71ap-username' in line[0]:
            ap_username = line[1].strip()

        if '71ap-password' in line[0]:
            ap_password = line[1].strip()

        if 'niazerooz-username' in line[0]:
            niazerooz_username = line[1].strip()

        if 'niazerooz-password' in line[0]:
            niazerooz_password = line[1].strip()

        if 'sellfree-username' in line[0]:
            sellfree_username = line[1].strip()

        if 'sellfree-password' in line[0]:
            sellfree_password = line[1].strip()

        if 'most-username' in line[0]:
            most_username = line[1].strip()

        if 'most-password' in line[0]:
            most_password = line[1].strip()

        if 'panikad-group' in line[0]:
            panikad_group = line[1].strip()

        if 'panikad-sub-group' in line[0]:
            panikad_sub_group = line[1].strip()

        if 'ap_group' in line[0]:
            ap_group = line[1].strip()

        if 'ap_sub_group' in line[0]:
            ap_sub_group = line[1].strip()

        if 'agahichi-group' in line[0]:
            agahichi_group = line[1].strip()

        if 'agahichi-sub-group' in line[0]:
            agahichi_sub_group = line[1].strip()

        if 'shetab-group' == line[0].strip():
            shetab_group = line[1].strip()

        if 'shetab-sub-group' == line[0].strip():
            shetab_sub_group = line[1].strip()

        if 'shetab-sub-sub-group' in line[0]:
            shetab_sub_sub_group = line[1].strip()

