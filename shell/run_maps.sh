#!/bin/bash

for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    nohup ../src/map.py --input_path="$file" &
done
