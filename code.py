from modules import led_light, mqtt_func, temp_sensor, uv_sensor # import helper functions from modules
import time

# BROKER INFO
broker = "IP TO BROKER"
port = 1883

# TOPICS
topic1 = "sensor/temperature"
topic2 = "sensor/lux"
topic3 = "sensor/light"
topic4 = "sensor/uvi"
topic5 = "sensor/uvs"

# MAIN LOOP - 5 MINUTES INTERVAL
while 1:

  # CREATE VARIABLES WITH SENSOR VALUES AS STRINGS. "N/A" IF NO VALUE FROM SENSOR - CHECK HARDWARE.
  temp = str(temp_sensor.get_temperature()) or "N/A"
  lux = str(uv_sensor.get_lux()) or "N/A"
  light = str(uv_sensor.get_light()) or "N/A"
  uvi = str(uv_sensor.get_uvi()) or "N/A"
  uvs = str(uv_sensor.get_uvs()) or "N/A"
  
  try:
    # CONNECT TO CLIENT EVERY 5 MIN
    client = mqtt_func.connect_to_mqtt(broker, port)

    # PUBLISH TO TOPICS
    mqtt_func.publish_msg(client, topic1, temp)
    mqtt_func.publish_msg(client, topic2, lux)
    mqtt_func.publish_msg(client, topic3, light)
    mqtt_func.publish_msg(client, topic4, uvi)
    mqtt_func.publish_msg(client, topic5, uvs)

    # GREEN LED IS ON FOR 2,5 MINUTES
    led_light.led_on()
    time.sleep(150)
    # GREEN LED IS OFF FOR 2,5 MINUTES 
    led_light.led_off()
    time.sleep(150)
  # SIMPLE ERROR CHECK
  except Exception as e:
    print(f"ERROR: {e}")
    
