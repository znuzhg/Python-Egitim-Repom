import requests

def username_Kontrol(username):
    USERNAME_SITES = {
        # =======================
        # SOSYAL MEDYA
        # =======================
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "X": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "VK": f"https://vk.com/{username}",
        "OK": f"https://ok.ru/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "Bilibili": f"https://space.bilibili.com/{username}",

        # =======================
        # DEVELOPER / TECH
        # =======================
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "StackExchange": f"https://stackexchange.com/users/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "Codeforces": f"https://codeforces.com/profile/{username}",
        "Codepen": f"https://codepen.io/{username}",
        "Replit": f"https://replit.com/@{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "SourceForge": f"https://sourceforge.net/u/{username}",
        "Launchpad": f"https://launchpad.net/~{username}",
        "OpenHub": f"https://www.openhub.net/accounts/{username}",
        "DockerHub": f"https://hub.docker.com/u/{username}",
        "NPM": f"https://www.npmjs.com/~{username}",
        "PyPI": f"https://pypi.org/user/{username}",
        "RubyGems": f"https://rubygems.org/profiles/{username}",
        "Crates": f"https://crates.io/users/{username}",
        "HuggingFace": f"https://huggingface.co/{username}",

        # =======================
        # FORUM / İÇERİK
        # =======================
        "Quora": f"https://www.quora.com/profile/{username}",
        "Disqus": f"https://disqus.com/by/{username}/",
        "Patreon": f"https://www.patreon.com/{username}",
        "AboutMe": f"https://about.me/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Blogger": f"https://{username}.blogspot.com",
        "Flipboard": f"https://flipboard.com/@{username}",
        "Slideshare": f"https://www.slideshare.net/{username}",
        "Issuu": f"https://issuu.com/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",

        # =======================
        # ALIŞVERİŞ / MARKET
        # =======================
        "Amazon": f"https://www.amazon.com/gp/profile/{username}",
        "Ebay": f"https://www.ebay.com/usr/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "AliExpress": f"https://www.aliexpress.com/store/{username}",
        "Letgo": f"https://www.letgo.com/en-us/profile/{username}",
        "OfferUp": f"https://offerup.com/p/{username}",
        "Depop": f"https://www.depop.com/{username}",
        "Shopify": f"https://{username}.myshopify.com",

        # =======================
        # MÜZİK / PODCAST
        # =======================
        "Spotify": f"https://open.spotify.com/user/{username}",
        "LastFM": f"https://www.last.fm/user/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",
        "Audiomack": f"https://audiomack.com/{username}",

        # =======================
        # OYUN / DİJİTAL
        # =======================
        "Steam": f"https://steamcommunity.com/id/{username}",
        "EpicGames": f"https://www.epicgames.com/id/{username}",
        "BattleNet": f"https://battle.net/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Minecraft": f"https://api.mojang.com/users/profiles/minecraft/{username}",
        "Xbox": f"https://account.xbox.com/en-us/profile?gamertag={username}",
        "PlayStation": f"https://my.playstation.com/profile/{username}",
        "ItchIO": f"https://{username}.itch.io",
        "Speedrun": f"https://www.speedrun.com/users/{username}",

        # =======================
        # BÖLGESEL / DİĞER
        # =======================
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Upwork": f"https://www.upwork.com/freelancers/~{username}",
        "Freelancer": f"https://www.freelancer.com/u/{username}",
        "500px": f"https://500px.com/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        "Pastebin": f"https://pastebin.com/u/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Telegram": f"https://t.me/{username}",
        "BuyMeACoffee": f"https://www.buymeacoffee.com/{username}",
        "KoFi": f"https://ko-fi.com/{username}",
        "Unsplash": f"https://unsplash.com/@{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        "Academia": f"https://independent.academia.edu/{username}"
    }
    try:
        for key in USERNAME_SITES:
            response = requests.get(USERNAME_SITES[key],timeout=10)
            if response.status_code in [200,301,302]:
                print(f"[+] {USERNAME_SITES[key]} -> Bulundu")
            if response.status_code == 404:
                print(f"[-] {USERNAME_SITES[key]} -> Kullanıcı Bulunamadı")
            if response.status_code == 410:
                print(f"[-] {USERNAME_SITES[key]} -> Kullanıcı Silinmiş")
            if response.status_code in [999,403,429]:
                print(f"[-] Doğrulanamadı / WAF ---> {USERNAME_SITES[key]}")
            if response.status_code == 401:
                print(f"[-] Giriş Gerekli ---> {USERNAME_SITES[key]}")
            if response.status_code == 429:
                print(f"[-] Çok Fazla İstek Gönderildi ---> {USERNAME_SITES[key]}")
            if response.status_code in [500,502,503,504]:
                print(f"[-] Sunucu Hatası ---> {USERNAME_SITES[key]}")
    except ConnectionError:
        print(f"Siteye Ulaşılamadı")
    except:
        print("Tanımlanamayan Hata")


def IP_BilgiToplama(ip):
    url = f"https://ipapi.co/{ip}/json/"
    try:
        response = requests.get(url=url,timeout=8)
        if response.status_code == 429:
            print("Çok Fazla İstek Atıldı Geçici Engelleme")
        elif response.status_code == 408:
            print("Api Cevap vermiyor veya İnternet yavaş")
        elif response.status_code == 200:
            response = response.json()
            print(f"\n--- 🔹 TEMEL IP BİLGİLERİ ---\n"
                  f"Sorgulanan IP  : {ip}\n"
                  f"Network        : {response['network']}\n"
                  f"IP Versiyonu   : {response['version']}\n"
                  f"\n--- 📍 COĞRAFİ KONUM ---\n"
                  f"Şehir          : {response['city']}\n"
                  f"İl / Bölge     : {response['region']}\n"
                  f"İl Plaka Kodu  : {response['region_code']}\n"
                  f"Posta Kodu     : {response['postal']}\n"
                  f"Enlem          : {response['latitude']}\n"
                  f"Boylam         : {response['longitude']}\n"
                  f"Saat Dilimi    : {response['timezone']}\n"
                  f"UTC Farkı      : {response['utc_offset']}\n"
                  f"\n--- 🌐 ÜLKE BİLGİLERİ ---\n"
                  f"Ülke Kodu      : {response['country']}\n"
                  f"Ülke Adı       : {response['country_name']}\n"
                  f"Ülke Başkent   : {response['country_capital']}\n"
                  f"Ülke Kodu      : {response['country_code']}\n"
                  f"Kıta Kodu      : {response['continent_code']}\n"
                  f"AB Üyesi mi ?  : {response['in_eu']}\n"
                  f"\n--- 📞 TELEKOMÜNİKASYON & PARA ---\n"
                  f"Telefon Kodu   : {response['country_calling_code']}\n"
                  f"Para Birimi    : {response['currency']}\n"
                  f"Konuşulan Dil  : {response['languages']}\n"
                  f"\n--- 🧮 DEMOGRAFİK / GENEL VERİ ---\n"
                  f"Ülke Yüzölçümü : {response['country_area']}\n"
                  f"Ülke Nüfusu    : {response['country_population']}\n"
                  f"\n--- 🛜 AĞ & İNTERNET SAĞLAYICI ---\n"
                  f"ISS/ Ağ Bloğu  : {response['asn']}\n"
                  f"ISP/ Firma Adı : {response['org']}\n"
                  )
        else:
            print("Api Hatası !")
    except:
        print("Tanımlanamayan bir hata oluştu !")
def E_Mail_Kontrol(email):
    api= f"https://leakcheck.net/api/public?check={email}"
    try:
        response = requests.get(api,timeout=10)
        if response.status_code != 200:
            print(f"Api Hatası: {response.status_code}")
            return
        data = response.json()
        print("\n--- E-POSTA SIZINTI KONTROLÜ ---\n"
              f"E-posta {email}\n"
              f"Sızıntı Sayısı: {data.get('found', 0)}")
        sources = data.get("sources",[])
        if not sources:
            print("Kaynak Bulunamadı")
            return
        print("\nBulunduğu Platformlar\n")
        for kaynak in sources:
            print(f"- {kaynak.get('name', 'Bilinmiyor')} ({kaynak.get('date', 'Tarih yok')})")
    except requests.exceptions.RequestException:
        print("Bağlantı hatası oluştu.")

menu_ekrani = ("""
========================================
    🕵️ OSINT TERMINAL TOOL
========================================
[1] Kullanıcı Adı Kontrolü
[2] IP Bilgi Toplama
[3] E-Posta Sızıntı Kontrolü
[0] Çıkış
========================================
""")

def menu():

    while True:
        try:
            print(menu_ekrani)
            sec = int(input("İşlem: "))
            if sec == 0:
                print("Program Kapatıldı.")
                break

            elif sec == 1:
                username = str(input("Kullanıcı Adı [deneme123]: "))
                username_Kontrol(username=username)
            elif sec == 2:
                ip = str(input("IP Giriniz [172.217.17.110]: "))
                IP_BilgiToplama(ip=ip)
            elif sec == 3:
                e_mail = str(input("E-mail Giriniz [deneme@gmail.com]: "))
                E_Mail_Kontrol(email=e_mail)
            else:
                print("Geçersiz seçim, tekrar deneyin.")
        except ValueError:
            print("Lütfen Değeri Doğru Giriniz !")
menu()

