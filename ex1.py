import json

# Create a JSON file with the following content:
donne = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}
with open("data.json", "w") as file:
    json.dump(donne, file)
    print("File data.json is created with success.")

# Read the “data.json” file and display its initial content
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Add new key 
data["langage"] = "Python"

# Save the modified dictionary in “data.json” file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
    print("\n the key 'langage' is added.")

# Show contents of “data.json” file after editing
with open("data.json", "r") as file:
    modified_data = json.load(file)
    print("\nAfter the modification :")
    print(modified_data)

data["langue"] = "arabe"

with open("data.json","w") as file:
    json.dump(data, file)

with open("data.json","r") as file:
    x=json.load(file)
    print(x)