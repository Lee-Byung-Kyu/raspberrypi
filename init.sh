# mosquitto Broker init
FILE="/var/run/mosquitto" 
if [ ! -e $FILE ];then
	sudo mkdir /var/run/mosquitto/
fi

sudo chown mosquitto: /var/run/mosquitto
sudo mosquitto -c /etc/mosquitto/mosquitto.conf --deamon

sudo python3 /home/pi/Desktop/raspberrypi/main.py
# mosquitto subscriber init (for test)
#mosquitto_sub -h 192.168.0.11 -t /test
