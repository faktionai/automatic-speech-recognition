#!/usr/bin/env python3
import argparse
import requests
import json
import os

parser = argparse.ArgumentParser(description='Cancel a job on speech recognition server.')
parser.add_argument('--key', type=str, required=True, help='Authorization key')
parser.add_argument('--server', type=str, required=True, help='Server address')
parser.add_argument('--job_id', type=str, required=True, help='Path to file')

args = parser.parse_args()

data={'status': 4} # see docs for all statuses

r = requests.put(os.path.join(args.server, 'http/speech/transcription/{}'.format(args.job_id)),
                 params={'Authorization': args.key}, data=json.dumps(data), headers={'Content-Type': 'application/json'})
json_object = json.loads(r.text)
print(json_object['message'])