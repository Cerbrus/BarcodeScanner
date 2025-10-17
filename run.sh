#!/bin/bash

docker compose up -d --build
sudo python apps/input-listener/listener.py