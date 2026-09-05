import requests
import datetime

print("--------------------------------------------------")
print("NASA ASTRONOMY PICTURE OF THE DAY")

while True:
    print()
    user_input = input("Enter a date to see the picture of that date\n(YYYY-MM-DD) or 'today', or 'q' to quit: ")

    if user_input.lower() == "q" or user_input.lower() == "quit":
        print("Exiting the program...")
        break

    if user_input == "today":
        user_input = datetime.datetime.today().strftime("%Y-%m-%d")

    url = f"https://api.nasa.gov/planetary/apod?date={user_input}&api_key=DEMO_KEY"

    response = requests.get(url)

    if response.status_code == 404:
        print("Error: Picture not found for this date.")
        continue
    else:
        data = response.json()

    print()
    print("--------------------------------------------------")
    print(f"Title: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Explanation: {data['explanation']}")
    print("--------------------------------------------------")
    print(f"HD URL: {data['hdurl']}")
    print("--------------------------------------------------")