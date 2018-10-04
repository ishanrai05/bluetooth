import bluetooth

target_name = "My Phone"
target_address = None
flag=0
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print(" %s - %s" % (addr, name))

#target_name = input("Enter the target name of the device")
target_address = input("Enter the target address of the device")
bd_addr = target_address

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
