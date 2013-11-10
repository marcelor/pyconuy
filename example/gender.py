#! /usr/bin/env python
import wave
import time
from os.path import (abspath, dirname, join)

from speaker import Speaker

path = dirname(abspath(__file__))

DATA_DIR = "%s/%s" % (path, 'data')

# Relative audio path to data dir
AUDIO_FILE = 'F-audio-sample.wav'

AUDIO_FILE_PATH = join(DATA_DIR, AUDIO_FILE)

frames_chunk = 80000

wav = wave.open(AUDIO_FILE_PATH, "r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = \
    wav.getparams()

# sampwidth holds bytes, let's get the bit count
bitdepth = sampwidth * 8

frames = wav.readframes(frames_chunk * nchannels)

wav.close()

data = {
        'audio_sequence': 1,
        'audio_samplerate': framerate,
        'audio_bitdepth': bitdepth,
        'audio_channels': nchannels,
        'audio_sent_frames': frames_chunk,
        'frames': frames,
}

api = Speaker()

print("Feeding %s audio frames to WS" % (frames_chunk))
response = api.issue_gender_recognition_task(**data)

print("Service replied with status code [%s]" % (response['status_code']))

result_in = response['new_result_in']
task_id = response['task_id']

print("Waiting %s secs to ask for response" % (result_in))

time.sleep(result_in)

data = {
    'task_id': task_id}

result = api.get_gender_recognition_result(**data)

print("Service replied with status code [%s]" % (result['status_code']))

print("Gender is: %s" % (result['gender']))
