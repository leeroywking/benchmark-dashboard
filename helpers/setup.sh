#!/bin/bash
sudo yum update -y
sudo yum install python3 git -y
sudo pip3 install poetry

git clone https://github.com/leeroywking/benchmark-dashboard.git
cd benchmark-dashboard
poetry install