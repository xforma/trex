from trex_stl_lib.api import *
from time import sleep
import imix

# Initialize the client
client = STLClient()

try:
    # Connect to TRex
    client.connect()

    # Acquire port 0, force acquisition if the port is already taken
    client.acquire(ports=[0], force=True)

    # Remove any existing streams on the port
    client.remove_all_streams(ports=[0])

    # Prepare the traffic profile from imix.py
    traffic_profile = imix.STLImix()
    streams = traffic_profile.get_streams()

    # Add the streams to the client
    client.add_streams(streams, ports=[0])

    # Start the transmission at 50 Mbps
    client.start(ports=[0], mult="50mbps")

    # Run for 30 seconds
    sleep(30)

    # Update the rate to 100 Mbps without stopping the traffic
    client.update(ports=[0], mult="100mbps")

    # Run for additional 30 seconds
    sleep(30)

except STLError as e:
    print("An error occurred: {}".format(e))
finally:
    # Ensure the ports are stopped and released properly
    try:
        client.stop(ports=[0])
        client.release(ports=[0])
    except STLError as e:
        print("Error in cleanup: {}".format(e))

    # Disconnect the client
    client.disconnect()
