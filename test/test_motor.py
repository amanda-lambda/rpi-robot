import time
import explorerhat

explorerhat.motor.one.forwards()
time.sleep(5)
explorerhat.motor.one.stop() 

explorerhat.motor.two.forwards()
time.sleep(5)
explorerhat.motor.two.stop() 