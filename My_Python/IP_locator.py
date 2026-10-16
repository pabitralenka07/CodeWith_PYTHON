import requests


# Function to get location from IP
def get_location(ip_address):

    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if data["status"] == "success":

            print(f"\nIP Address: {ip_address}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP Code: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")

        else:
            print("Error:", data["message"])

    else:
        print("Failed to connect to the API.")


# Take IP input from user
ip = input("\nEnter an IP address: ")

get_location(ip)
