# Faktion Automatic Speech Recognition API
This repository contains some examples on how to query the Faktion Automatic Speech Recognition API.
Faktion has developed his own properietary speech recognition models voor Flemish.

## API docs

The API docs can be found over here: https://api.speech.faktion.com/docs/

## Request Access
To request an API key, get more information or a demo, contact `info@faktion.com`.


## Examples
An example on how to transcribe a file can be found at `python/transcribe_file.py`.

```
python transcribe_file.py --file YOUR_FILE --key YOUR_KEY --server https://api.speech.faktion.com
```
Similarly `python/request_status.py` and `python/cancel_job.py` allow you to respectively request the status of 
the job and to cancel a job.

For additional functionality, check the docs.

## [Flemish] Automatische Vlaamse Spraakherkenning
Bij Faktion hebben we samen met Chatlayer.ai onze eigen Vlaamse spraakherkenningstechnologie ontwikkeld. Dit laat ons toe automatisch gesproken 
Vlaamse taal om te zetten naar tekst. Deze technologie kan onder meer ingezet worden in callcenters, 
automatische ondertiteling of het automatisch omzetten van interviews.