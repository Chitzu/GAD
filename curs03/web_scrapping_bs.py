from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import ExcelWriter

request_page = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
# print(request_page)
link = BeautifulSoup(request_page.text, 'html.parser')
# print(link)

dataset , header_list= [], []
main = link.find_all('div', attrs={'id' : 'contentDiv'})
# print(main)

for obj in main:
    for table_index in obj.find_all('table'):
        # print(table_index)
        for table_trs in table_index.find_all('tr'):
            # print(table_trs)
            td_list = []
            if table_trs.find_all('th'):
                header_list = [x.get_text() for x in table_trs.find_all('th')]
                # for header_data in table_trs.find_all('th'):     # echivalent cu linia de mai sus
                #     header_list.append((header_data.get_text()))
            for index, td in enumerate(table_trs.find_all('td')):
                # print(index,td)
                if index == 0 :
                    td_list.append(td.get_text())
                elif td.get_text() != '':
                    td_list.append(float(td.get_text().replace(',', '.')))
                # print(td_list)
            dataset.append(td_list)
del dataset[0]
print(dataset)

df = pd.DataFrame(dataset, columns=header_list, index=range(1, 11))
print(df)
df.to_excel('CursBNR.xlsx', header=header_list, sheet_name='CursBNR')
# with ExcelWriter('CursBNR.xls') as writer:
#     df.to_excel(writer, index=False)
