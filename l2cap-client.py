import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

target_name = "My Phone"
target_address = None
flag=0
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print(" %s - %s" % (addr, name))

#target_name = input("Enter the target name of the device")
target_address = input("Enter the target address of the device")

'''
nearby_devices2 = bluetooth.discover_devices()
for bdaddr in nearby_devices2:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        flag=1
    break

if flag==1:
    print ("found target bluetooth device with address: \n ", target_address)
else:
    print ("could not find target bluetooth device nearby: \n")
'''

bd_addr = target_address
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
