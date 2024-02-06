#!/usr/bin/env bash

set -e

rm -rf data
mkdir data
wget https://www.kaggle.com/competitions/50160/leaderboard/download/public -O ./data/public.zip
cd ./data
unzip public.zip 
rm -rf public.zip
cd ..
source env/bin/activate
ls data | xargs -I{} python upload.py data/{}
rm -rf data
rm tables.txt