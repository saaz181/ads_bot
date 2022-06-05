carved_out_keyword = {
"default_username": "",
"default_password": "",
"title": "",
"description": "",
"short_description": "",
"address": "",
"province": "",
"city": "",
"name": "",
"english-name": "",
"phone": "",
"home-phone": "",
"keywords": "",
"website-title": "",
"website_link": "",
"picture": "",
"price": "",
"email": "",
"71ap-username": "",
"71ap-password": "",
"niazerooz-username": "",
"niazerooz-password": "",
"sellfree-username": "",
"sellfree-password": "",
"zibashahr-username": "",
"zibashahr-password": "",
"most-username": "",
"most-password": "",
"main-group": "",
"main-sub-group": "",
"other-group": "",
"other-sub-group": "",
"other-sub-sub-group": "",
"my-niazerooz-group": "",
"my-niazerooz-sub-group": "",
"newagahi-group": "",
"newagahi-sub-group": "",
"decornama-group": "",
"decornama-sub-group": "",
"netmoj-group": "",
"netmoj-sub-group": "",
"netmoj-sub-sub-group": "",
"darsanat-group": "",
"darsanat-sub-group": "",
"niaz118-group": "",
"niaz118-sub-group": "",
"adem-group": "",
"adem-sub-group": "",
"nasbeagahi-group": "",
"nasbeagahi-sub-group": "",
"nasbeagahi-sub-sub-group": "",
"agahinama-group": "",
"agahinama-sub-group": "",
"agahirooz-group": "",
"parstabligh-group": "",
"panikad-group": "",
"panikad-sub-group": "",
"ap_group": "",
"ap_sub_group": "",
"agahichi-group": "",
"agahichi-sub-group": "",
"shetab-group": "",
"shetab-sub-group": "",
"shetab-sub-sub-group": "",
"tejjari-group": "",
"tejjari-sub-group": "",
"tejjari-sub-sub-group": "",
"tejjari-sub-sub-sub-group": "",
"xoonrang-group": "",
"xoonrang-sub-group": "",
"ruzandish-group": "",
"ruzandish-sub-group": "",
"ruzandish-sub-sub-group": "",
"nama-group": "",
"nama-sub-group": "",
"nama-sub-sub-group": "",
"eshareh-group": "",
"eshareh-sub-group": "",
"fanoos-group": "",
"fanoos-sub-group": "",
"mihan-group": "",
"mihan-sub-group": "",
"mihan-sub-sub-group": "",
"3030l-group": "",
"3030l-sub-group": "",
"3030l-sub-sub-group": "",
"service-group": "",
"service-sub-group": "",
"rahnama-group": "",
"rahnama-sub-group": "",
"takniz-group": "",
"takniz-sub-group": "",
"takniz-province": "",
"novin-tejarat-group": "",
"novin-tejarat-sub-group": "",
"ptweb-group": "",
"ptweb-sub-group": "",
"payamsara-group": "",
"payamsara-sub-group": "",
"tablegh118-group": "",
"tablegh118-sub-group": "",
"protabligh-group": "",
"protabligh-sub-group": "",
"niazmandi-iran-group": "",
"niazmandi-iran-sub-group": "",
"agahe118-group": "",
"agahe118-sub-group": "",
"category-7010": "",
"group-7010": "",
"sub-group-7010": "",
"rang7-group": "",
"rang7-sub-group": "",
"silverbook-group": "",
"silverbook-sub-group": "",
"silverbook-sub-sub-group": "",
"zibashahr-group": "",
"adsfarsi-group": "",
"adsfarsi-sub-group": "",
"aftabeh-group": "",
"agahi24-group": "",
"agahi24-sub-group": "",
"agahi2agahi-group": "",
"agahi2agahi-sub-group": "",
"agahi360-group": "",
"agahi360-sub-group": "",
"abcagahi-group": "",
"abcagahi-sub-group": "",
"jarzadani-group": "",
"jarzadani-sub-group": "",
"jar24-group": "",
"jar24-sub-group": "",
"dasar-group": "",
"dasar-sub-group": "",
"publik-group": "",
"publik-sub-group": "",
"hadafniaz-group": "",
"hadafniaz-sub-group": "",
"peleha-group": "",
"peleha-sub-group": "",
"pbazar-group": "",
"pbazar-sub-group": "",
"pbazar-picture": "",
"pabi-group": "",
"pabi-sub-group": "",
"taaj-group": "",
"taaj-sub-group": "",
"agahidon-group": "",
"agahidon-sub-group": "",
"agahiiran-group": "",
"agahiiran-sub-group": "",
"agahiiran-sub-sub-group": "",
"agahi-kala-group": "",
"agahi-kala-sub-group": "",
"agahimax-group": "",
"agahimax-sub-group": "",
"agahimax-sub-sub-group": "",
"asreesfahan-group": "",
"asreesfahan-sub-group": "",
"bazarche96-group": "",
"bazarche96-sub-group": "",
"bazarche96-sub-sub-group": "",
"bazarha-group": "",
"bazarha-sub-group": "",
"bazarha-sub-sub-group": "",
"bazarmajazi-group": "",
"bazarmajazi-sub-group": "",
"bazarmajazi-sub-sub-group": "",
"dararsh-group": "",
"dararsh-sub-group": "",
"fastniaz-group": "",
"fastniaz-sub-group": "",
"inagahi-group": "",
"inagahi-sub-group": "",
"niazmandia-group": "",
"niazmandia-sub-group": "",
"niazmandia-province": "",
"tabliqplus-group": "",
"tabliqplus-sub-group": "",
"niazmandiha-net-group": "",
"niazmandiha-net-sub-group": "",
"noonerooz-group": "",
"noonerooz-sub-group": "",
"nabzeroz-group": "",
"nabzeroz-sub-group": "",
"hogre-group": "",
"hogre-sub-group": "",
"hogre-sub-sub-group": "",
"radtabligh-group": "",
"radtabligh-sub-group": "",
"aghayeagahi-group": "",
"jaraghe-group": "",
"jaraghe-sub-group": "",
"jaraghe-sub-sub-group": "",
}


def carve_out_words(word: str, string_1: str, string_2: str):
    if word in string_1:
        carved_out_keyword[word] = string_2


with open('info.txt', 'r', encoding='utf-8') as info:
    file = info.readlines()
    for line in file:
        line = line.split('=')

        if 'default_username' in line[0]:
            _username_ = line[1].strip()

        if 'default_password' in line[0]:
            _password_ = line[1].strip()

        else:
            if carved_out_keyword.get(line[0].strip()) is not None:
                carve_out_words(line[0].strip(), line[0].strip(), line[1].strip())


title = carved_out_keyword.get("title")
description = carved_out_keyword.get("description")
short_description = carved_out_keyword.get("short_description")
address = carved_out_keyword.get("address")
province = carved_out_keyword.get("province")
city = carved_out_keyword.get("city")
name = carved_out_keyword.get("name")
english_name = carved_out_keyword.get("english-name")
phone = carved_out_keyword.get("phone")
home_phone = carved_out_keyword.get("home-phone")
keywords = carved_out_keyword.get("keywords")
website_title = carved_out_keyword.get("website-title")
website_link = carved_out_keyword.get("website_link")
picture = carved_out_keyword.get("picture")
price = carved_out_keyword.get("price")
email = carved_out_keyword.get("email")
ap_username = carved_out_keyword.get("71ap-username")
ap_password = carved_out_keyword.get("71ap-password")
niazerooz_username = carved_out_keyword.get("niazerooz-username")
niazerooz_password = carved_out_keyword.get("niazerooz-password")
sellfree_username = carved_out_keyword.get("sellfree-username")
sellfree_password = carved_out_keyword.get("sellfree-password")
zibashahr_username = carved_out_keyword.get("zibashahr-username")
zibashahr_password = carved_out_keyword.get("zibashahr-password")
most_username = carved_out_keyword.get("most-username")
most_password = carved_out_keyword.get("most-password")
main_group = carved_out_keyword.get("main-group")
main_sub_group = carved_out_keyword.get("main-sub-group")
other_group = carved_out_keyword.get("other-group")
other_sub_group = carved_out_keyword.get("other-sub-group")
other_sub_sub_group = carved_out_keyword.get("other-sub-sub-group")
my_niazerooz_group = carved_out_keyword.get("my-niazerooz-group")
my_niazerooz_sub_group = carved_out_keyword.get("my-niazerooz-sub-group")
newagahi_group = carved_out_keyword.get("newagahi-group")
newagahi_sub_group = carved_out_keyword.get("newagahi-sub-group")
decornama_group = carved_out_keyword.get("decornama-group")
decornama_sub_group = carved_out_keyword.get("decornama-sub-group")
netmoj_group = carved_out_keyword.get("netmoj-group")
netmoj_sub_group = carved_out_keyword.get("netmoj-sub-group")
netmoj_sub_sub_group = carved_out_keyword.get("netmoj-sub-sub-group")
darsanat_group = carved_out_keyword.get("darsanat-group")
darsanat_sub_group = carved_out_keyword.get("darsanat-sub-group")
niaz118_group = carved_out_keyword.get("niaz118-group")
niaz118_sub_group = carved_out_keyword.get("niaz118-sub-group")
adem_group = carved_out_keyword.get("adem-group")
adem_sub_group = carved_out_keyword.get("adem-sub-group")
nasbeagahi_group = carved_out_keyword.get("nasbeagahi-group")
nasbeagahi_sub_group = carved_out_keyword.get("nasbeagahi-sub-group")
nasbeagahi_sub_sub_group = carved_out_keyword.get("nasbeagahi-sub-sub-group")
agahinama_group = carved_out_keyword.get("agahinama-group")
agahinama_sub_group = carved_out_keyword.get("agahinama-sub-group")
agahirooz_group = carved_out_keyword.get("agahirooz-group")
parstabligh_group = carved_out_keyword.get("parstabligh-group")
panikad_group = carved_out_keyword.get("panikad-group")
panikad_sub_group = carved_out_keyword.get("panikad-sub-group")
ap_group = carved_out_keyword.get("ap_group")
ap_sub_group = carved_out_keyword.get("ap_sub_group")
agahichi_group = carved_out_keyword.get("agahichi-group")
agahichi_sub_group = carved_out_keyword.get("agahichi-sub-group")
shetab_group = carved_out_keyword.get("shetab-group")
shetab_sub_group = carved_out_keyword.get("shetab-sub-group")
shetab_sub_sub_group = carved_out_keyword.get("shetab-sub-sub-group")
tejjari_group = carved_out_keyword.get("tejjari-group")
tejjari_sub_group = carved_out_keyword.get("tejjari-sub-group")
tejjari_sub_sub_group = carved_out_keyword.get("tejjari-sub-sub-group")
tejjari_sub_sub_sub_group = carved_out_keyword.get("tejjari-sub-sub-sub-group")
xoonrang_group = carved_out_keyword.get("xoonrang-group")
xoonrang_sub_group = carved_out_keyword.get("xoonrang-sub-group")
ruzandish_group = carved_out_keyword.get("ruzandish-group")
ruzandish_sub_group = carved_out_keyword.get("ruzandish-sub-group")
ruzandish_sub_sub_group = carved_out_keyword.get("ruzandish-sub-sub-group")
nama_group = carved_out_keyword.get("nama-group")
nama_sub_group = carved_out_keyword.get("nama-sub-group")
nama_sub_sub_group = carved_out_keyword.get("nama-sub-sub-group")
eshareh_group = carved_out_keyword.get("eshareh-group")
eshareh_sub_group = carved_out_keyword.get("eshareh-sub-group")
fanoos_group = carved_out_keyword.get("fanoos-group")
fanoos_sub_group = carved_out_keyword.get("fanoos-sub-group")
mihan_group = carved_out_keyword.get("mihan-group")
mihan_sub_group = carved_out_keyword.get("mihan-sub-group")
mihan_sub_sub_group = carved_out_keyword.get("mihan-sub-sub-group")
cicil_group = carved_out_keyword.get("3030l-group")
cicil_sub_group = carved_out_keyword.get("3030l-sub-group")
cicil_sub_sub_group = carved_out_keyword.get("3030l-sub-sub-group")
service_group = carved_out_keyword.get("service-group")
service_sub_group = carved_out_keyword.get("service-sub-group")
rahnama_group = carved_out_keyword.get("rahnama-group")
rahnama_sub_group = carved_out_keyword.get("rahnama-sub-group")
takniz_group = carved_out_keyword.get("takniz-group")
takniz_sub_group = carved_out_keyword.get("takniz-sub-group")
takniz_province = carved_out_keyword.get("takniz-province")
novin_tejarat_group = carved_out_keyword.get("novin-tejarat-group")
novin_tejarat_sub_group = carved_out_keyword.get("novin-tejarat-sub-group")
ptweb_group = carved_out_keyword.get("ptweb-group")
ptweb_sub_group = carved_out_keyword.get("ptweb-sub-group")
payamsara_group = carved_out_keyword.get("payamsara-group")
payamsara_sub_group = carved_out_keyword.get("payamsara-sub-group")
tablegh118_group = carved_out_keyword.get("tablegh118-group")
tablegh118_sub_group = carved_out_keyword.get("tablegh118-sub-group")
protabligh_group = carved_out_keyword.get("protabligh-group")
protabligh_sub_group = carved_out_keyword.get("protabligh-sub-group")
niazmandi_iran_group = carved_out_keyword.get("niazmandi-iran-group")
niazmandi_iran_sub_group = carved_out_keyword.get("niazmandi-iran-sub-group")
agahe118_group = carved_out_keyword.get("agahe118-group")
agahe118_sub_group = carved_out_keyword.get("agahe118-sub-group")
category_7010 = carved_out_keyword.get("category-7010")
group_7010 = carved_out_keyword.get("group-7010")
sub_group_7010 = carved_out_keyword.get("sub-group-7010")
rang7_group = carved_out_keyword.get("rang7-group")
rang7_sub_group = carved_out_keyword.get("rang7-sub-group")
silverbook_group = carved_out_keyword.get("silverbook-group")
silverbook_sub_group = carved_out_keyword.get("silverbook-sub-group")
silverbook_sub_sub_group = carved_out_keyword.get("silverbook-sub-sub-group")
zibashahr_group = carved_out_keyword.get("zibashahr-group")
adsfarsi_group = carved_out_keyword.get("adsfarsi-group")
adsfarsi_sub_group = carved_out_keyword.get("adsfarsi-sub-group")
aftabeh_group = carved_out_keyword.get("aftabeh-group")
agahi24_group = carved_out_keyword.get("agahi24-group")
agahi24_sub_group = carved_out_keyword.get("agahi24-sub-group")
agahi2agahi_group = carved_out_keyword.get("agahi2agahi-group")
agahi2agahi_sub_group = carved_out_keyword.get("agahi2agahi-sub-group")
agahi360_group = carved_out_keyword.get("agahi360-group")
agahi360_sub_group = carved_out_keyword.get("agahi360-sub-group")
abcagahi_group = carved_out_keyword.get("abcagahi-group")
abcagahi_sub_group = carved_out_keyword.get("abcagahi-sub-group")
jarzadani_group = carved_out_keyword.get("jarzadani-group")
jarzadani_sub_group = carved_out_keyword.get("jarzadani-sub-group")
jar24_group = carved_out_keyword.get("jar24-group")
jar24_sub_group = carved_out_keyword.get("jar24-sub-group")
dasar_group = carved_out_keyword.get("dasar-group")
dasar_sub_group = carved_out_keyword.get("dasar-sub-group")
publik_group = carved_out_keyword.get("publik-group")
publik_sub_group = carved_out_keyword.get("publik-sub-group")
hadafniaz_group = carved_out_keyword.get("hadafniaz-group")
hadafniaz_sub_group = carved_out_keyword.get("hadafniaz-sub-group")
peleha_group = carved_out_keyword.get("peleha-group")
peleha_sub_group = carved_out_keyword.get("peleha-sub-group")
pbazar_group = carved_out_keyword.get("pbazar-group")
pbazar_sub_group = carved_out_keyword.get("pbazar-sub-group")
pbazar_picture = carved_out_keyword.get("pbazar-picture")
pabi_group = carved_out_keyword.get("pabi-group")
pabi_sub_group = carved_out_keyword.get("pabi-sub-group")
taaj_group = carved_out_keyword.get("taaj-group")
taaj_sub_group = carved_out_keyword.get("taaj-sub-group")
agahidon_group = carved_out_keyword.get("agahidon-group")
agahidon_sub_group = carved_out_keyword.get("agahidon-sub-group")
agahiiran_group = carved_out_keyword.get("agahiiran-group")
agahiiran_sub_group = carved_out_keyword.get("agahiiran-sub-group")
agahiiran_sub_sub_group = carved_out_keyword.get("agahiiran-sub-sub-group")
agahi_kala_group = carved_out_keyword.get("agahi-kala-group")
agahi_kala_sub_group = carved_out_keyword.get("agahi-kala-sub-group")
agahimax_group = carved_out_keyword.get("agahimax-group")
agahimax_sub_group = carved_out_keyword.get("agahimax-sub-group")
agahimax_sub_sub_group = carved_out_keyword.get("agahimax-sub-sub-group")
asreesfahan_group = carved_out_keyword.get("asreesfahan-group")
asreesfahan_sub_group = carved_out_keyword.get("asreesfahan-sub-group")
bazarche96_group = carved_out_keyword.get("bazarche96-group")
bazarche96_sub_group = carved_out_keyword.get("bazarche96-sub-group")
bazarche96_sub_sub_group = carved_out_keyword.get("bazarche96-sub-sub-group")
bazarha_group = carved_out_keyword.get("bazarha-group")
bazarha_sub_group = carved_out_keyword.get("bazarha-sub-group")
bazarha_sub_sub_group = carved_out_keyword.get("bazarha-sub-sub-group")
bazarmajazi_group = carved_out_keyword.get("bazarmajazi-group")
bazarmajazi_sub_group = carved_out_keyword.get("bazarmajazi-sub-group")
bazarmajazi_sub_sub_group = carved_out_keyword.get("bazarmajazi-sub-sub-group")
dararsh_group = carved_out_keyword.get("dararsh-group")
dararsh_sub_group = carved_out_keyword.get("dararsh-sub-group")
fastniaz_group = carved_out_keyword.get("fastniaz-group")
fastniaz_sub_group = carved_out_keyword.get("fastniaz-sub-group")
inagahi_group = carved_out_keyword.get("inagahi-group")
inagahi_sub_group = carved_out_keyword.get("inagahi-sub-group")
niazmandia_group = carved_out_keyword.get("niazmandia-group")
niazmandia_sub_group = carved_out_keyword.get("niazmandia-sub-group")
niazmandia_province = carved_out_keyword.get("niazmandia-province")
tabliqplus_group = carved_out_keyword.get("tabliqplus-group")
tabliqplus_sub_group = carved_out_keyword.get("tabliqplus-sub-group")
niazmandiha_net_group = carved_out_keyword.get("niazmandiha-net-group")
niazmandiha_net_sub_group = carved_out_keyword.get("niazmandiha-net-sub-group")
noonerooz_group = carved_out_keyword.get("noonerooz-group")
noonerooz_sub_group = carved_out_keyword.get("noonerooz-sub-group")
nabzeroz_group = carved_out_keyword.get("nabzeroz-group")
nabzeroz_sub_group = carved_out_keyword.get("nabzeroz-sub-group")
hogre_group = carved_out_keyword.get("hogre-group")
hogre_sub_group = carved_out_keyword.get("hogre-sub-group")
hogre_sub_sub_group = carved_out_keyword.get("hogre-sub-sub-group")
radtabligh_group = carved_out_keyword.get("radtabligh-group")
radtabligh_sub_group = carved_out_keyword.get("radtabligh-sub-group")
aghayeagahi_group = carved_out_keyword.get("aghayeagahi-group")
jaraghe_group = carved_out_keyword.get("jaraghe-group")
jaraghe_sub_group = carved_out_keyword.get("jaraghe-sub-group")
jaraghe_sub_sub_group = carved_out_keyword.get("jaraghe-sub-sub-group")

