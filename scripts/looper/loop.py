from subprocess import Popen
import serial
import time
import re
from serial import tools
from serial.tools import list_ports
import multiprocessing as mp

def timed_input(prompt):
    start = time.time()
    s = input(prompt)
    return s, time.time() - start

def play():
    while True:
        try:
            key = ser.readline().replace(" ", "")
            #print key

            if '0' in key:
                    a = Popen(['aplay', '../samples/CLAP1.wav'])
            elif '1' in key:
                    b = Popen(['aplay', '../samples/CLAV3.wav'])
            elif '2' in key:
                    c = Popen(['aplay', '../samples/HIHAT42(OPEN).wav'])
            elif '3' in key:
                    d = Popen(['aplay', '../samples/HIHAT43(CLSD).wav'])
            elif '4' in key:
                    e = Popen(['aplay', '../samples/Istanbul_Radiant_14_Hihat_Closed-13.wav'])
            elif '5' in key:
                    f = Popen(['aplay', '../samples/Istanbul_Radiant_14_Hihat_Open-13.wav'])
            elif '6' in key:
                    g = Popen(['aplay', '../samples/KICK18.wav'])
            elif '7' in key:
                    h = Popen(['aplay', '../samples/KICK77.wav'])
            elif '8' in key:
                    i = Popen(['aplay', '../samples/PERCUSSIONVARIOUS31.wav'])
            elif '9' in key:
                    j = Popen(['aplay', '../samples/PERCUSSIONVARIOUS32.wav'])
            elif 'A' in key:
                    k = Popen(['aplay', '../samples/ride4.wav'])
            elif 'F' in key:
                    l = Popen(['aplay', '../samples/SNARE91.wav'])
            elif 'C' in key:
                    m = Popen(['aplay', '../samples/S-Shh.wav'])
            elif 'D' in key:
                    n = Popen(['aplay', '../samples/TAM4.wav'])
            elif 'E' in key:
                    o = Popen(['aplay', '../samples/COWBELL9.wav'])
            elif 'B' in key:		
                    pass
                    # spawn seperate process
                    # process records actions              
                    # after F is pressed, record next keypress until another F keypress, play that pattern
            else:
                    pass
            
            return key

        except KeyboardInterrupt:
            print "[]--> Terminated by ^C"
            exit(0)

        except serial.serialutil.SerialException as e:
            print "[]--> Serial Exception Raised: Probably a disconnected arduino"
            print "[]--> Quitting"
            exit(0)
#records the loops played over the asynchronous function play()
def record():
    pass


if __name__ == '__main__':
	def main():
		#configure multiprocessing
                mp.set_start_method('spawn')
                #Configure Arduino Port
                #Check for arduino presence
		if list(serial.tools.list_ports.grep('/dev/ttyACM')) != "":
                    arduino_ports = list(serial.tools.list_ports.grep('/dev/ttyACM'))
                    print "[]-->Arduino detected at " , arduino_ports
                    port = re.findall(r'/dev/ttyACM.', str(arduino_ports))
                    l = str(port).strip("[']")
                    print "[]-->Selecting port" , l
                    ser = serial.Serial('%s' % l, 9600)

                    print "[]-->READY"
                    looper = Process(target=play)
                    looper.start()
                else:
                    print "[]-->There doesn't seem to be an arduino present. Check the connection?"

