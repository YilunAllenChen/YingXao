## In the terminal, run following commands 
sudo apt-get update   
sudo apt-get upgrade   
sudo pip3 install --upgrade setuptools   
pip3 install adafruit-circuitpython-dht   
sudo apt-get install libgpiod2

## How to select the data pin in the DHT22 python file
change    
dhtDevice = adafruit_dht.DHT22(board.D4)   
to   
dhtDevice = adafruit_dht.DHT22(board.Dxx)   
"the number in the D4 or Dxx means the GPIOxx"

## Wire Connection
V+to 3.3v   
V- to ground   
data to GPIO21
