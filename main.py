import gspread
import json
import os
cred = {
  "type": "service_account",
  "project_id": "sheet-update-359009",
  "private_key_id": "e191c42887c3c2fea30dd28d47ea1bf98ac0d5f4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCtxvp9CGuJJqR/\nX03xHRKgTa68m6l3Wp62RQGQTnXYv/sS0KkcY5o7f9EbUfiDwh/Cgxf6lbiAoRkQ\n2e2AIVrxwMdWZOe+rbXLMp9B140gyoOh6N9Zv7dhxp2yjJnaCDpA4LqEWyfPAUdo\nxJvtn6yqTHpMNzaK9hBBk803LBDBT134/p2Q7YSkCN9vmjzUHc8G/rTqqdGpc41j\ntJI4XM5ufPeWOg6evRkc95fVSVPdPzgO3pA6gNNN8olM5Lhb1fUYJamvvcxfjz2a\nVygQKwcDrvEdOVzP5UoSYOPz661rs4A52wQLYwjVgCCKc31+gWGV/vnIRRuZi5gK\nWd29yup7AgMBAAECggEAGqMRyaadF9nU2d1Zoig1rwgZTQ8t69NNLrKR1HU3uoYQ\nTfMEE7ZExvKxsoFfGZCLs7zKfn5YA1zY7cH/QLuxfWBybbtr4R4uwTs85CfOmdnQ\n/Dl+OvtDIyQBui5edZL7SESU8oLSgvg24kf41XS7T84HP7WFkR659oNZr9JRAysO\n5n4Qh9xW2PQBRSPq4OOik4EcPujwdtkhyAt39nskfglz1bkh0cwb0rBHnXsiEeRN\nxE49HrZUYSSP2jkgN+sRBwys8CHwvPXDlibpPlV6DPN8Es/q0+6yQosDUiOinkIu\n6EO2dUjznjNTWJb8BpdESezJvJ37CH4TGN9DdJcXSQKBgQDaQxuhn2H7ELaZZ3KF\nOQVQqMN73YOb3onHpQyPtEAXjeJWxpIbXji9Jn78drN6mUsG9zFh50GPVD4uo1dL\nEJJoda4xxpTL4KOkz+jIJ5GPsuiJSl0+OPtnBHF64n7PwtUAvyrafh37Ncs7sOIm\nNLzpEYnwGAXmHgSETtaZqulrVQKBgQDL0thu76Ds9EPNOi7nMnsWHpklFrNuS5Tw\nOt2X3CFCdq2xdLs4D0JOjhiYB1pSZ8zAdv5cZpyZ6UCH/HWwv37z/BmjVM5cJ4hb\nsQ/wcgov9X77mqkCLdkoAcxMJhXJN0sucDuH5Gv6SVGNp9Li2xWqJ5WbJayVxele\nj+9gR4QejwKBgE9z2G4oZ/GOLvp+9uhaTn4DQU4o4AzwoLVFduIlGqO4aalvFabS\n0NLCXb2ntEQv42kAuUBLf8keQJiXq2JPAQz3sda61FW3S7rmWHXsOYfW9+FqabEJ\n6zKgInM6WjFlWkawUHhDKsTU20u6Y0jHL/GkCdOV2yfey4Qicupzlg8VAoGARKhV\nd6kIkEkHvc3nlsGObLkJ5VBsSK71EKcDle/01Cqd/7TOi+e38jYzWqK/bhrBAeQT\ncpSuE7pannQQQOWAojc9e6NJkAlRCXHvaJNBkz4i9CX44F8JU0ynwM7jb9BMZuwv\nYWs0ZC7mZc0uYHRkK9kBsC1UoW71WYEqpUfx3UkCgYAV1QH9FaqfN1/Arhh4+9KZ\nsW/FsZa/s0CI9Y8xPJxJHLXyzRPUgtpVjyfTdkaCvKF/bHR0LmgRhq20sk8gu/Es\nEuX1fvjc8SOj01MdwDfubrYFrxq/9y84lu3MWsFNBEC01yq6mjrjXHaaLNHzbrYh\nuCX62YTy4o9jASoFyODuTA==\n-----END PRIVATE KEY-----\n",
  "client_email": "pythonscript@sheet-update-359009.iam.gserviceaccount.com",
  "client_id": "113961874482314261104",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pythonscript%40sheet-update-359009.iam.gserviceaccount.com"
}
#path = r'C:\\Users\\ashvi\\Executable'
#file = 'sample.json'
#json_object = json.dumps(credentials, indent=4)
 
#Writing to sample.json
#with open(os.path.join(path, file), "w") as outfile:
    #outfile.write(json_object)

gc = gspread.service_account_from_dict(cred)

sh = gc.open_by_key('1BtBIYP0LEmbpat0e5BLLdy8DX_BBB70ztYvSHHZR7rY')
worksheet = sh.sheet1

res = worksheet.get_all_records()
print(res)
with open("output.json", "w") as outfile:
    outfile.write(str(res))
#file2 = 'output.json'
#json_object = json.dumps(res, indent=4)
#with open(os.path.join(path, file2), "w") as outfile:
    #outfile.write(json_object)
