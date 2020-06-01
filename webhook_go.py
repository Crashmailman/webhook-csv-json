##Created By ADBY IT AND MEDIA SOLUTIONS
# 21/05/2020
# Open Source
# adam@adby.com.au

import pandas
import json
import requests
import configparser as cp
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

configParser = cp.RawConfigParser()

config = cp.ConfigParser()
config.read(dir_path + '/' + 'settings.ini')

# settings details
webhook = config.get('webhook', 'host')
csvfile = config.get('webhook', 'csvfile')

print("Converting CSV file to JSON file....")

df = pandas.read_csv(csvfile, index_col=False)
df.to_json(r'frzdata.json', orient='index')

print("Converting CSV file to JSON file.... Complete")

print("Sending Data to" + " " + webhook)

with open("FRZDATA.json", "rt") as block_f:
    data = json.load(block_f)


def post_to_slack(message):
    webhook_url = webhook
    slack_data = json.dumps({'blocks': message})
    response = requests.post(
        webhook_url, data=slack_data,
        headers={'Content-Type': 'application/json'}

    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


post_to_slack(data)
