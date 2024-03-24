from trex_stl_lib.api import *
from imix import STLImix  # Ensure this import is correct based on your IMIX profile setup

def generate_ul_traffic(client, port=1, dst_ip="10.0.1.2", rate="5mbps", duration=60):
    """
    Generates UL IMIX traffic on a specified port.

    :param client: The TRex STLClient instance.
    :param port: Port number to generate traffic on.
    :param dst_ip: Destination IP address for UL traffic.
    :param rate: Traffic rate (e.g., "5mbps").
    :param duration: Duration of the traffic generation in seconds.
    """
    # Instantiate the IMIX profile
    imix_profile = STLImix()

    # Get the IMIX streams for UL traffic
    ul_streams = imix_profile.get_streams(dst_ip=dst_ip)

    # Clear any existing streams and add new UL streams
    client.reset(ports=[port])
    client.add_streams(ul_streams, ports=[port])

    # Start UL traffic on the specified port with the given rate
    client.start(ports=[port], mult=rate)

    # Print status and wait for traffic to complete
    print("UL IMIX Traffic started on port {port}. Waiting {duration} seconds...")
    client.wait_on_traffic(ports=[port], timeout=duration)
    print("UL IMIX Traffic generation completed.")

def main():
    client = STLClient()
    try:
        client.connect()
        client.acquire(ports=[1], force=True)
        client.reset(ports=[1])

        # Generate uplink traffic
        generate_ul_traffic(client, port=1, dst_ip="10.0.1.2", rate="5mbps", duration=60)

    except STLError as e:
        print("Error encountered: {e}")
    finally:
        # Ensure cleanup actions are properly executed
        try:
            client.stop(ports=[1])
        except STLError as e:
            print("Error stopping traffic: {e}")
        try:
            client.release(ports=[1])
        except STLError as e:
            print("Error releasing ports: {e}")
        client.disconnect()

if __name__ == '__main__':
    main()
