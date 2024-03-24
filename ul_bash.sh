#start TRex in interactive mode
./t-rex-64 -i &

# Wait for TRex to initialize
sleep 8

# Execute the Python script
python /var/trex/v2.41/stl/ul_traffic.py

# Optionally, add any cleanup commands here

