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

        if 'province' == line[0].strip():
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
            picture = r'' + line[1].strip()

        if 'price' in line[0]:
            price = line[1].strip()

        if 'email' in line[0]:
            email = line[1].strip()

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

        if 'tejjari-group' == line[0].strip():
            tejjari_group = line[1].strip()

        if 'tejjari-sub-group' == line[0].strip():
            tejjari_sub_group = line[1].strip()

        if 'tejjari-sub-sub-group' == line[0].strip():
            tejjari_sub_sub_group = line[1].strip()

        if 'tejjari-sub-sub-sub-group' in line[0]:
            tejjari_sub_sub_sub_group = line[1].strip()

        if 'xoonrang-group' == line[0].strip():
            xoonrang_group = line[1].strip()

        if 'xoonrang-sub-group' in line[0]:
            xoonrang_sub_group = line[1].strip()

        if 'jarchi-group' == line[0].strip():
            jarchi_group = line[1].strip()

        if 'jarchi-sub-group' == line[0].strip():
            jarchi_sub_group = line[1].strip()

        if 'jarchi-sub-sub-group' in line[0].strip():
            jarchi_sub_sub_group = line[1].strip()

        if 'nama-group' == line[0].strip():
            nama_group = line[1].strip()

        if 'nama-sub-group' == line[0].strip():
            nama_sub_group = line[1].strip()

        if 'nama-sub-sub-group' in line[0]:
            nama_sub_sub_group = line[1].strip()

        if 'eshareh-group' == line[0].strip():
            eshareh_group = line[1].strip()

        if 'eshareh-sub-group' in line[0]:
            eshareh_sub_group = line[1].strip()

        if 'fanoos-group' == line[0].strip():
            fanoos_group = line[1].strip()

        if 'fanoos-sub-group' in line[0]:
            fanoos_sub_group = line[1].strip()

        if 'mihan-group' == line[0].strip():
            mihan_group = line[1].strip()

        if 'mihan-sub-group' == line[0].strip():
            mihan_sub_group = line[1].strip()

        if 'mihan-sub-sub-group' in line[0]:
            mihan_sub_sub_group = line[1].strip()

        if '3030l-group' == line[0].strip():
            cicil_group = line[1].strip()

        if '3030l-sub-group' == line[0].strip():
            cicil_sub_group = line[1].strip()

        if '3030l-sub-sub-group' in line[0]:
            cicil_sub_sub_group = line[1].strip()

        if 'service-group' == line[0].strip():
            service_group = line[1].strip()

        if 'service-sub-group' == line[0].strip():
            service_sub_group = line[1].strip()

        if 'rahnama-group' == line[0].strip():
            rahnama_group = line[1].strip()

        if 'rahnama-sub-group' in line[0]:
            rahnama_sub_group = line[1].strip()

        if 'takniz-group' == line[0].strip():
            takniz_group = line[1].strip()

        if 'takniz-sub-group' == line[0].strip():
            takniz_sub_group = line[1].strip()

        if 'takniz-province' in line[0]:
            takniz_province = line[1].strip()

        if 'novin-tejarat-group' == line[0].strip():
            novin_tajarat_group = line[1].strip()

        if 'novin-tejarat-sub-group' in line[0]:
            novin_tajarat_sub_group = line[1].strip()

        if 'ptweb-group' == line[0].strip():
            ptweb_group = line[1].strip()

        if 'ptweb-sub-group' in line[0]:
            ptweb_sub_group = line[1].strip()

        if 'payamsara-group' == line[0].strip():
            payamsara_group = line[1].strip()

        if 'payamsara-sub-group' in line[0]:
            payamsara_sub_group = line[1].strip()

        if 'tablegh118-group' == line[0].strip():
            tablegh118_group = line[1].strip()

        if 'tablegh118-sub-group' in line[0]:
            tablegh118_sub_group = line[1].strip()

        if 'protabligh-group' == line[0].strip():
            protabligh_group = line[1].strip()

        if 'protabligh-sub-group' in line[0]:
            protabligh_sub_group = line[1].strip()

        if 'niazmandi-iran-group' == line[0].strip():
            niazmandi_iran_group = line[1].strip()

        if 'niazmandi-iran-sub-group' in line[0]:
            niazmandi_iran_sub_group = line[1].strip()

        if 'agahe118-group' == line[0].strip():
            agahe118_group = line[1].strip()

        if 'agahe118-sub-group' == line[0].strip():
            agahe118_sub_group = line[1].strip()
