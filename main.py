import requests
from bs4 import BeautifulSoup
import time

print('enter skills u dont wanna join')
unwant=input("->")
print(f"filtering jobs which dont have:{unwant}")

def scrape ():
    getreq=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=machine+learning&txtLocation=mumbai&cboWorkExp1=1")       # requset for url to get inspect
    soup = BeautifulSoup(getreq.content,'lxml')    
    tags = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")     
    
    for tag in tags:
        post = tag.find('span',class_='sim-posted').span.text.replace(" ","")
        if 'few' in post:
            cmp = tag.find('h3',class_="joblist-comp-name").text.replace(" ","")
            skill= tag.find("span",class_="srp-skills").text.replace(" ","")
            loc = tag.find('li',class_="srp-walkin-dtl").span.text.replace(" ","")  
            link = tag.header.h2.a['href']                    
            if unwant not in skill:
                with open('job_details_upload/details.txt','w') as cr:
                    cr.write(f"company:{cmp.strip()}\n")
                    cr.write(f"skills:{skill.strip()}\n")
                    cr.write(loc.strip())
                    cr.write(f"\nmore info:{link}")

                    cr.write(" ")
                print('detail saved in details file!')

if __name__=='__main__':
    while True:
        scrape()
        print('waiting 10 minutes to get update....')
        time.sleep(600)

 print(f"""compny:{cmp}
 skills:{skill}
 time and location:{loc}""")
for refr in tags:
    words=refr.h3.text.split()[-1]    
    words=refr.h3.text[:100]
    print(words)

# to pint if needed

print(tags)
print(soup.prettify())
print(soup.get_text())
