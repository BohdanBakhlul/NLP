import re
from urllib import request

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

for month, day in zip(months, days):
    for d in range(1, day):
        response = request.urlopen('https://en.wikipedia.org/wiki/' + month + '_' + str(d))
        page_source = response.read().decode('utf-8')
        data = re.findall(r"<li>.*</li>", page_source)[0]
        print(month + ' ' + str(d) + '  ' + re.sub("<[^>]*>|(\&\#8211\;)", "", data))
