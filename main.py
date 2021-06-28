import requests
import json
import csv

def get_customers():
    url = 'https://9b29f5d9ae93b429608bc6f8c4d490d6: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@not-mystore.myshopify.com/admin/api/2021-04/customers.json'
    infor_customers = json.loads(requests.get(url).text)
    fields = list(infor_customers['customers'][0].keys())
    fields.remove('addresses')
    fields.remove('default_address')
    data = infor_customers['customers']
    return fields, data
def write_csvfile():
    fields, data = get_customers()
    with open('customers.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for infor in data:
            del infor['addresses']
            del infor['default_address']
            writer.writerow(infor)

# get_customers()
write_csvfile()



