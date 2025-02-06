import requests


def get_epic_game():
    # call the api
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

    response = requests.get(url)

    # check if the response is successful
    if response.status_code == 200:
        # get the data from the response
        data = response.json()

        # initialize the current free game to none
        free_game_index = None
        # check which game in the array is the current free game
        for index, game in enumerate(data["data"]["Catalog"]["searchStore"]["elements"]):
            try:
                if len(game["promotions"]["promotionalOffers"]) > 0:
                    free_game_index = index
                    break
            except KeyError:
                pass

        if free_game_index is None:
            return "There are no free games available at the moment."

        # get the url of the current free game
        game_url = data["data"]["Catalog"]["searchStore"]["elements"][free_game_index]["urlSlug"]

        return {
            "game_name": data["data"]["Catalog"]["searchStore"]["elements"][free_game_index]["title"],
            "image_url": data["data"]["Catalog"]["searchStore"]["elements"][free_game_index]["keyImages"][0]["url"],
            "game_url": f"https://www.epicgames.com/store/en-US/p/{game_url}",
            "description": data["data"]["Catalog"]["searchStore"]["elements"][free_game_index]["description"],
            "promo_end_date": data["data"]["Catalog"]["searchStore"]["elements"][free_game_index]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
        }

    else:
        return "There is a problem with the Epic Games Store API. Please try again later."
