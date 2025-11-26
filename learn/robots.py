import urllib.robotparser

def cek_izin_scrape(url_target):
    rp = urllib.robotparser.RobotFileParser()
    
    # 1. Set lokasi robots.txt
    robots_url = "https://kuronime.moe/robots.txt" 
    rp.set_url(robots_url)
    
    try:
        # 2. Baca file robots.txt
        rp.read()
        
        # 3. Cek apakah User-agent kita (*) boleh mengambil URL target
        izin = rp.can_fetch("*", url_target)
        
        if izin:
            print(f"Diizinkan: Anda BOLEH scrape {url_target}")
        else:
            print(f"Dilarang: robots.txt MELARANG akses ke {url_target}")
            
    except Exception as e:
        print(f"Gagal membaca robots.txt: {e}")

# Contoh penggunaan
cek_izin_scrape("https://kuronime.moe/anime/judul-anime-tertentu/")