from bs4 import BeautifulSoup
import requests
from datetime import date,datetime
import re


def consultantNoWorkDays():
    no_work_days=[]
    url=f'http://www.consultant.ru/law/ref/calendar/proizvodstvennye/{date.today().year}/'
    response=requests.get(url)
    if response.status_code == 200:
        consultant_html=response.text
        soup = BeautifulSoup(consultant_html, 'html.parser')
        searchResult_block = soup.findAll('table', {'class':'cal'})
    
        if searchResult_block!=None:
            for index, block in enumerate(searchResult_block):
                for weekend in block.find_all('td', class_='weekend'):
                    day=re.findall(r'\d+', weekend.get_text())[0]
                    no_work_days.append(datetime.strptime(f'{day}.{index+1}.{date.today().year}', '%d.%m.%Y').date())
    return {'days_count': len(no_work_days), 'days': no_work_days}

print(date.today() in consultantNoWorkDays()['days'])
