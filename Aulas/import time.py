import time

i = 0
while i<258:
    #cast chr = de int para caracther // ord = caractere para int
    time.sleep(0.1)
    print(chr(i))
    print(ord(chr(i)))
    i+=1
