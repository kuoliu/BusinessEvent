import urllib,random,re

ip_regex = re.compile("(([0-9]{1,3}\.){3}[0-9]{1,3})")

def public_ip():
    hosts = """http://www.whatismyip.com/
http://adresseip.com
http://www.aboutmyip.com/
http://www.ipchicken.com/
http://www.showmyip.com/
http://monip.net/
http://checkrealip.com/
http://ipcheck.rehbein.net/
http://checkmyip.com/
http://www.raffar.com/checkip/
http://www.thisip.org/
http://www.lawrencegoetz.com/programs/ipinfo/
http://www.mantacore.se/whoami/
http://www.edpsciences.org/htbin/ipaddress
http://mwburden.com/cgi-bin/getipadd

http://checkipaddress.com/
http://www.glowhost.com/support/your.ip.php
http://www.tanziars.com/
http://www.naumann-net.org/
http://www.godwiz.com/
http://checkip.eurodyndns.org/""".strip().split("\n")
    for i in range(3):
        host = random.choice(hosts)
        try:
            results = ip_regex.findall(urllib.urlopen(host).read(200000))
            if results:
                return results[0][0]
        except:
            pass
    return None