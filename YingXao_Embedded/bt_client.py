
import bluetooth

bd_addr = "dc:a6:32:ab:be:29"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()