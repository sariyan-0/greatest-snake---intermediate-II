############################# MODULE REQUESTS #############################
#
# -------------------------------------------------------------------------
import requests
import re
# responce = requests.get()
# responce = requests.post()
# responce = requests.put()
# responce = requests.patch()
# responce = requests.delete()

response = requests.get("https://mftplus.com")
st_code = response.status_code
json = response.json
# print(st_code)
html_data = response.text
# print(html_data)
result = re.findall(r"Python", html_data)
print(result)
if len (result)> 0:
    print("There are",len(result), " python courses in the site")