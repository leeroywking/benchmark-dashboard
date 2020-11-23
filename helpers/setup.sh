#!/bin/bash
sudo yum update -y
sudo yum install python3 git gcc python3-devel -y
sudo pip3 install poetry

git clone https://github.com/leeroywking/benchmark-dashboard.git
cd benchmark-dashboard
poetry install
poetry run python main.py > output.json
