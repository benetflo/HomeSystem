import time
import board
import wifi
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT

def connect_to_mqtt(mqtt_broker, mqtt_port): # paramters will be sent from main
    try:
        pool = socketpool.SocketPool(wifi.radio)
        mqtt_client = MQTT.MQTT(
            broker=mqtt_broker,
            port=mqtt_port,
            socket_pool=pool
        )
        mqtt_client.connect()
        return mqtt_client
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def publish_msg(mqtt_client,topic, msg):
    mqtt_client.publish(topic, msg)
