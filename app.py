from gardener import Gardener
import time

system = Gardener()
system.set_led(True)
time.sleep(3)
system.set_led(False)
time.sleep(3)
system.set_led(True)
time.sleep(3)
system.set_led(False)
