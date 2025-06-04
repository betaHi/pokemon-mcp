import requests
from fastmcp import FastMCP

mcp = FastMCP("get-pokemon")

def main():
    mcp.run(transport='stdio')

@mcp.tool()
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data["name"],
                "id": data["id"],
                "height": f"{data['height'] / 10} meters",
                "weight": f"{data['weight'] / 10} kg",
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]]
            }
        else:
            return {
                "error": f"Request failed with status code: {response.status_code}"
            }
    except requests.exceptions.RequestException as e:
        return {
            "error": f"Request exception: {str(e)}"
        }

if __name__ == "__main__":
    main()
