import requests
import argparse
import os
import json

parser = argparse.ArgumentParser(description='Request status of a job on speech recognition server.')
parser.add_argument('--key', type=str, required=True, help='Authorization key')
parser.add_argument('--server', type=str, required=True, help='Server address')
parser.add_argument('--job_id', type=str, required=False, help='Path to file')

args = parser.parse_args()

r = requests.get(os.path.join(args.server, 'http/speech/status/'),
                 params={'Authorization': args.key})


json_object = json.loads(r.text)
print(json_object["message"])