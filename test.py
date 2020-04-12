import requests
from bs4 import BeautifulSoup

try:
    p = int(input('ch7ale men page bghiti tjib :' ))
except:
    print('mefhetekch dekhel ar9ame lay7fdek')
    p = int(input('ch7ale men page bghiti tjib :' ))



url = 'https://www.akoam.net/cat/156/%D8%A7%D9%84%D8%A3%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D9%84%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D8%A9'
headers={"User-Agent":"Mozilla/5.0  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
s = requests.Session()
s.headers.update(headers)
r = s.get(url)
soup = BeautifulSoup(r.content,"lxml")


def websc():
    for div in soup.find_all('div',class_='subject_box'):
        a = div.find('a')
        surl= a['href']
        r2 = s.get(surl)
        soup2 = BeautifulSoup(r2.content,"lxml")
        for div2 in soup2.find_all('div',class_='sub_desc sub_extra_desc'):
            a2 = div2.find('a')
            url2= a2['href']
            r3 = s.get(url2)
            soup3 = BeautifulSoup(r3.content,"lxml")
            a3 = soup3.find('a',class_="link-btn link-download d-flex align-items-center px-3")
            url3= a3['href']
            r4 = s.get(url3)
            soup4 = BeautifulSoup(r4.content,"lxml")
            a4 = soup4.find('a',class_="download-link")
            url4 = a4['href']
            try:
                r5 = s.get(url4)
                soup5 = BeautifulSoup(r5.content,"lxml")
                a5 = soup5.find('a',class_="font-size-16 text-muted")
                url5 = a5['href']
                text = open('fileidm.txt','a+')
                text.write(url5+'\r\n')
                text.close()
                print(url5)
            except:
                print('hade  lien majabouch ')
                continue
            
websc()
if p >= 1:
    p = p-1
    for i in range(p):
        A = soup.find('a',class_='next') 
        url=A['href']
        text = open('fileidm.txt','a+')
        text.write('next page''\r\n')
        text.close()
        websc()




        
    
    


    