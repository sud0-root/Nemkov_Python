# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов

import re
from collections import OrderedDict

with open('PZ_14/radio_stations.txt', 'r', encoding='utf-8') as file:
    data = file.read()

domains = re.findall(r'(?<=://)[^/:]+', data)
print("Домены из URL-адресов:")

order_domain = OrderedDict.fromkeys(domains)
for domain in order_domain:
    print(domain)