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

        if 'english-name' == line[0].strip():
            english_name = line[1].strip()

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

        if 'zibashahr-username' == line[0].strip():
            zibashahr_username = line[1].strip()

        if 'zibashahr-password' == line[0].strip():
            zibashahr_password = line[1].strip()

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

        if 'my-niazerooz-group' == line[0].strip():
            my_niazerooz_group = line[1].strip()

        if 'my-niazerooz-sub-group' == line[0].strip():
            my_niazerooz_sub_group = line[1].strip()

        if 'newagahi-group' == line[0].strip():
            newagahi_group = line[1].strip()

        if 'newagahi-sub-group' == line[0].strip():
            newagahi_sub_group = line[1].strip()

        if 'decornama-group' == line[0].strip():
            decornama_group = line[1].strip()

        if 'decornama-sub-group' == line[0].strip():
            decornama_sub_group = line[1].strip()

        if 'netmoj-group' in line[0]:
            netmoj_group = line[1].strip()

        if 'netmoj-sub-group' in line[0]:
            netmoj_sub_group = line[1].strip()

        if 'netmoj-sub-sub-group' in line[0]:
            netmoj_sub_sub_group = line[1].strip()

        if 'darsanat-group' == line[0].strip():
            darsanat_group = line[1].strip()

        if 'darsanat-sub-group' == line[0].strip():
            darsanat_sub_group = line[1].strip()

        if 'niaz118-group' in line[0]:
            niaz118_group = line[1].strip()

        if 'niaz118-sub-group' in line[0]:
            niaz118_sub_group = line[1].strip()

        if 'adem-group' == line[0].strip():
            adem_group = line[1].strip()

        if 'adem-sub-group' == line[0].strip():
            adem_sub_group = line[1].strip()

        if 'nasbeagahi-group' == line[0].strip():
            nasbeagahi_group = line[1].strip()

        if 'nasbeagahi-sub-group' == line[0].strip():
            nasbeagahi_sub_group = line[1].strip()

        if 'nasbeagahi-sub-sub-group' == line[0].strip():
            nasbeagahi_sub_sub_group = line[1].strip()

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

        if 'ruzandish-group' == line[0].strip():
            ruzandish_group = line[1].strip()

        if 'ruzandish-sub-group' == line[0].strip():
            ruzandish_sub_group = line[1].strip()

        if 'ruzandish-sub-sub-group' in line[0].strip():
            ruzandish_sub_sub_group = line[1].strip()

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

        if 'category-7010' in line[0]:
            category_7010 = line[1].strip()

        if 'group-7010' == line[0].strip():
            group_7010 = line[1].strip()

        if 'sub-group-7010' in line[0]:
            sub_group_7010 = line[1].strip()

        if 'rang7-group' == line[0].strip():
            rang7_group = line[1].strip()

        if 'rang7-sub-group' == line[0].strip():
            rang7_sub_group = line[1].strip()

        if 'silverbook-group' == line[0].strip():
            silverbook_group = line[1].strip()

        if 'silverbook-sub-group' == line[0].strip():
            silverbook_sub_group = line[1].strip()

        if 'silverbook-sub-sub-group' in line[0]:
            silverbook_sub_sub_group = line[1].strip()

        if 'zibashahr-group' == line[0].strip():
            zibashahr_group = line[1].strip()

        if 'adsfarsi-group' == line[0].strip():
            adsfarsi_group = line[1].strip()

        if 'adsfarsi-sub-group' in line[0]:
            adsfarsi_sub_group = line[1].strip()

        if 'aftabeh-group' == line[0].strip():
            aftabeh_group = line[1].strip()

        if 'agahi24-group' == line[0].strip():
            agahi24_group = line[1].strip()

        if 'agahi24-sub-group' == line[0].strip():
            agahi24_sub_group = line[1].strip()

        if 'agahi2agahi-group' == line[0].strip():
            agahi2agahi_group = line[1].strip()

        if 'agahi2agahi-sub-group' in line[0]:
            agahi2agahi_sub_group = line[1].strip()

        if 'agahi360-group' == line[0].strip():
            agahi360_group = line[1].strip()

        if 'agahi360-sub-group' == line[0].strip():
            agahi360_sub_group = line[1].strip()

        if 'abcagahi-group' == line[0].strip():
            abcagahi_group = line[1].strip()

        if 'abcagahi-sub-group' == line[0].strip():
            abcagahi_sub_group = line[1].strip()

        if 'jarzadani-group' == line[0].strip():
            jarzadani_group = line[1].strip()

        if 'jarzadani-sub-group' == line[0].strip():
            jarzadani_sub_group = line[1].strip()

        if 'jar24-group' == line[0].strip():
            jar24_group = line[1].strip()

        if 'jar24-sub-group' == line[0].strip():
            jar24_sub_group = line[1].strip()

        if 'dasar-group' == line[0].strip():
            dasar_group = line[1].strip()

        if 'dasar-sub-group' == line[0].strip():
            dasar_sub_group = line[1].strip()

        if 'publik-group' == line[0].strip():
            publik_group = line[1].strip()

        if 'publik-sub-group' == line[0].strip():
            publik_sub_group = line[1].strip()

        if 'hadafniaz-group' == line[0].strip():
            hadafniaz_group = line[1].strip()

        if 'hadafniaz-sub-group' == line[0].strip():
            hadafniaz_sub_group = line[1].strip()

        if 'peleha-group' == line[0].strip():
            peleha_group = line[1].strip()

        if 'peleha-sub-group' == line[0].strip():
            peleha_sub_group = line[1].strip()

        if 'pbazar-group' == line[0].strip():
            pbazar_group = line[1].strip()

        if 'pbazar-sub-group' == line[0].strip():
            pbazar_sub_group = line[1].strip()

        if 'pbazar-picture' == line[0].strip():
            pbazar_picture = line[1].strip()

        if 'pabi-group' == line[0].strip():
            pabi_group = line[1].strip()

        if 'pabi-sub-group' == line[0].strip():
            pabi_sub_group = line[1].strip()

        if 'taaj-group' == line[0].strip():
            taaj_group = line[1].strip()

        if 'taaj-sub-group' == line[0].strip():
            taaj_sub_group = line[1].strip()

        if 'agahidon-group' == line[0].strip():
            agahidon_group = line[1].strip()

        if 'agahidon-sub-group' == line[0].strip():
            agahidon_sub_group = line[1].strip()

        if 'agahiiran-group' == line[0].strip():
            agahiiran_group = line[1].strip()

        if 'agahiiran-sub-group' == line[0].strip():
            agahiiran_sub_group = line[1].strip()

        if 'agahiiran-sub-sub-group' == line[0].strip():
            agahiiran_sub_sub_group = line[1].strip()

        if 'agahi-kala-group' == line[0].strip():
            agahi_kala_group = line[1].strip()

        if 'agahi-kala-sub-group' == line[0].strip():
            agahi_kala_sub_group = line[1].strip()

        if 'agahimax-group' == line[0].strip():
            agahimax_group = line[1].strip()

        if 'agahimax-sub-group' == line[0].strip():
            agahimax_sub_group = line[1].strip()

        if 'agahimax-sub-sub-group' == line[0].strip():
            agahimax_sub_sub_group = line[1].strip()

        if 'asreesfahan-group' == line[0].strip():
            asreesfahan_group = line[1].strip()

        if 'asreesfahan-sub-group' == line[0].strip():
            asreesfahan_sub_group = line[1].strip()

        if 'bazarche96-group' == line[0].strip():
            bazarche96_group = line[1].strip()

        if 'bazarche96-sub-group' == line[0].strip():
            bazarche96_sub_group = line[1].strip()

        if 'bazarche96-sub-sub-group' == line[0].strip():
            bazarche96_sub_sub_group = line[1].strip()

        if 'bazarha-group' == line[0].strip():
            bazarha_group = line[1].strip()

        if 'bazarha-sub-group' == line[0].strip():
            bazarha_sub_group = line[1].strip()

        if 'bazarha-sub-sub-group' == line[0].strip():
            bazarha_sub_sub_group = line[1].strip()

        if 'bazarmajazi-group' == line[0].strip():
            bazarmajazi_group = line[1].strip()

        if 'bazarmajazi-sub-group' == line[0].strip():
            bazarmajazi_sub_group = line[1].strip()

        if 'bazarmajazi-sub-sub-group' == line[0].strip():
            bazarmajazi_sub_sub_group = line[1].strip()

        if 'dararsh-group' == line[0].strip():
            dararsh_group = line[1].strip()

        if 'dararsh-sub-group' == line[0].strip():
            dararsh_sub_group = line[1].strip()

        if 'fastniaz-group' == line[0].strip():
            fastniaz_group = line[1].strip()

        if 'fastniaz-sub-group' == line[0].strip():
            fastniaz_sub_group = line[1].strip()

        if 'inagahi-group' == line[0].strip():
            inagahi_group = line[1].strip()

        if 'inagahi-sub-group' == line[0].strip():
            inagahi_sub_group = line[1].strip()

        if 'niazmandia-group' == line[0].strip():
            niazmandia_group = line[1].strip()

        if 'niazmandia-sub-group' == line[0].strip():
            niazmandia_sub_group = line[1].strip()

        if 'niazmandia-province' == line[0].strip():
            niazmandia_province = line[1].strip()

        if 'tabliqplus-group' == line[0].strip():
            tabliqplus_group = line[1].strip()

        if 'tabliqplus-sub-group' == line[0].strip():
            tabliqplus_sub_group = line[1].strip()

        if 'niazmandiha-net-group' == line[0].strip():
            niazmandiha_net_group = line[1].strip()

        if 'niazmandiha-net-sub-group' == line[0].strip():
            niazmandiha_net_sub_group = line[1].strip()

        if 'noonerooz-group' == line[0].strip():
            noonerooz_group = line[1].strip()

        if 'noonerooz-sub-group' == line[0].strip():
            noonerooz_sub_group = line[1].strip()

        if 'nabzeroz-group' == line[0].strip():
            nabzeroz_group = line[1].strip()

        if 'nabzeroz-sub-group' == line[0].strip():
            nabzeroz_sub_group = line[1].strip()

        if 'hogre-group' == line[0].strip():
            hogre_group = line[1].strip()

        if 'hogre-sub-group' == line[0].strip():
            hogre_sub_group = line[1].strip()

        if 'hogre-sub-sub-group' == line[0].strip():
            hogre_sub_sub_group = line[1].strip()

        if 'radtabligh-group' == line[0].strip():
            radtabligh_group = line[1].strip()

        if 'radtabligh-sub-group' == line[0].strip():
            radtabligh_sub_group = line[1].strip()

        if 'aghayeagahi-group' == line[0].strip():
            aghayeagahi_group = line[1].strip()

        if 'jaraghe-group' == line[0].strip():
            jaraghe_group = line[1].strip()

        if 'jaraghe-sub-group' == line[0].strip():
            jaraghe_sub_group = line[1].strip()

        if 'jaraghe-sub-sub-group' == line[0].strip():
            jaraghe_sub_sub_group = line[1].strip()

