pipeline_info = ("sales_pipeline", "alice", "2024-03-28", "completed")
coordinates = [(40.7128, 74.0060), (51.5074, 0.1278), (48.8566, 2.3522)]
Name = pipeline_info[0]
Owner = pipeline_info[1]
Date = pipeline_info[2]
Status = pipeline_info[3]
print(f"Name: {Name}\n"
      f"Owner: {Owner}\n"
      f"Date: {Date}\n"
      f"Status: {Status}\n"
      f"Total fields: {len(coordinates) + 1}"
)

try:
    pipeline_info[0] = "orders_pipeline"
except TypeError:
    print("Error: tuples are immutable - cannot be changed")

for coordinate in coordinates:
    lat = coordinate[0]
    lon = coordinate[1]
    print(f"lat: {lat} | lon: {lon}")
'''
Your script should:
1. Unpack pipeline_info into four separate variables and print each one
2. Print the number of items in pipeline_info
3. Try to change the first item of pipeline_info to "orders_pipeline"
   and print what error you get as a string
4. Loop over coordinates and unpack each tuple into lat and lon
   and print them

Expected output:
Name: sales_pipeline
Owner: alice
Date: 2024-03-28
Status: completed
Total fields: 4
Error: tuples are immutable - cannot be changed
Lat: 40.7128 | Lon: 74.006
Lat: 51.5074 | Lon: 0.1278
Lat: 48.8566 | Lon: 2.3522
'''