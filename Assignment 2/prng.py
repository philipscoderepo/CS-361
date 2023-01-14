import time
import random

while True:
    time.sleep(1)
    service = open("prng-service.txt", "r")
    run = service.read()
    service.close()
    if run == "run":
        service = open("prng-service.txt", "w")
        service.write(f"{random.randint(1, 100)}")
        service.close()
