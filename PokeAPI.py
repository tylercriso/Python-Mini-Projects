import requests


while True:
    user_input = input("Enter a Pokémon name: ")

    if user_input.lower() == "q" or user_input.lower() == "quit":
        print("Exiting the program...")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{user_input}"


    response = requests.get(url)


    if response.status_code == 404:
        print("Error: Pokémon not found.")
        continue
    else:
        data = response.json()

    pid = data["id"]
    pname = data["name"]
    pbase_experience = data["base_experience"]
    pheight = data["height"]
    pweight = data["weight"]

    print(f"ID: {pid}")
    print(f"Name: {pname}")
    print(f"Base Experience: {pbase_experience}")
    print(f"Height: {pheight}")
    print(f"Weight: {pweight}")
