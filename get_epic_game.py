import requests


def get_epic_game():
    # call the api
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

    response = requests.get(url)

    # check if the response is successful
    if response.status_code == 200:
        # get the data from the response
        data = response.json()

        # get the current free game
        current_free_game = data["data"]["Catalog"]["searchStore"]["elements"][0]["title"]

        # get the image of the current free game
        image_url = data["data"]["Catalog"]["searchStore"]["elements"][0]["keyImages"][0]["url"]

        # get the url of the current free game
        game_url = data["data"]["Catalog"]["searchStore"]["elements"][0]["urlSlug"]

        return {
            "game_name": current_free_game,
            "image_url": image_url
            "game_url": f"https://www.epicgames.com/store/en-US/p/{game_url}"
        }

    else:
        return "Failed to get the current free game"