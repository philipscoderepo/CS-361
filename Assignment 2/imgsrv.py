import time

while True:
    time.sleep(1)
    service = open("image-service.txt", "r")
    num = service.read()
    service.close()
    if num.isdigit():
        service = open("image-service.txt", "w")
        service.write(f"C:\\Users\super\Documents\Dev\CS-361\Assignment 2\images\cat.{num}.jpg")
        service.close()

