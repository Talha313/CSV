# import os
# # print (os.system('pwd'))
# # print(os.system('pwd'))
# # for ali, dirs, files in os.walk("."):
# #     for filename in files:
#
# # import os
# # print("pwd=" + os.getcwd())
# # import os
# for talha, dirs, files in os.walk('./'):
#      for file in files:
#         print (file)

import requests

proxies = {
    'http': 'http://104.140.211.192:3128',
    'https': 'http://206.214.93.246:3128',
}
response=requests.get('http://grubhub.com', proxies=proxies)
#response = requests.get('http://pakwheels.com')
print(response.text)

