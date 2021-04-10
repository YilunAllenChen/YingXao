#!/bin/bash
shopt -s extglob

str=$(ls -tr /var/lib/bluetooth | tail -1)
sudo chmod +777 /var/lib/bluetooth
sudo chmod +777 /var/lib/bluetooth/$str
sudo chmod +777 /var/lib/bluetooth/$str/cache
cd  /var/lib/bluetooth/$str
sudo rm -rfv /var/lib/bluetooth/$str/cache/*
sudo rm -rf !("cache"|"settings")
sudo bluetoothctl << EOF
discoverable on
pairable on
exit
