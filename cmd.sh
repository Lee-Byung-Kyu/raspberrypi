# mosquitto Broker init
sudo mkdir /var/run/mosquitto/
sudo chown mosquitto: /var/run/mosquitto
sudo mosquitto -c /etc/mosquitto/mosquitto.conf

# mosquitto subscriber init (for test)
mosquitto_sub -h 192.168.0.11 -t /test
