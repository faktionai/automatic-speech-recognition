import argparse
import requests
import json
import os
import time

parser = argparse.ArgumentParser(description='Upload file to speech recognition server.')
parser.add_argument('--file', type=str, required=True, help='Path to file')
parser.add_argument('--key', type=str, required=True, help='Authorization key')
parser.add_argument('--server', type=str, required=True, help='Server address')

args = parser.parse_args()

with open(args.file, 'rb') as f:
    r = requests.post(os.path.join(args.server, 'http/speech/upload'), files={'file': f},
                      params={'Authorization': args.key})

    if r.status_code == 200:
        json_object = json.loads(r.text)
        job_id = json_object['job_id']
        print(job_id)
        while True:
            r = requests.get(os.path.join(args.server, 'http/speech/transcription/{}'.format(job_id)),
                             params={'Authorization': args.key})
            if r.status_code == 200:
                json_object = json.loads(r.text)
                print(json_object["message"])
                if json_object["status"] == 2 and "transcription" in json_object:
                    print(json_object)
                    break
                elif json_object["status"] == 3:
                    print("Transcription failed")
            else:
                print("Something went wrong")
            time.sleep(1)
    elif r.status_code == 401:
        print('You are not authorized!')
    else:
        print('Something went wrong')