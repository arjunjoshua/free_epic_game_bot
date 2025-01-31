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
        current_free_game = None
        # check which game in the array is the current free game
        for index, game in enumerate(data["data"]["Catalog"]["searchStore"]["elements"]):
            try:
                if len(game["promotions"]["promotionalOffers"]) > 0:
                    current_free_game = index
                    break
            except KeyError:
                pass

        if current_free_game is None:
            return None

        # get the url of the current free game
        game_url = data["data"]["Catalog"]["searchStore"]["elements"][current_free_game]["urlSlug"]

        return {
            "game_name": data["data"]["Catalog"]["searchStore"]["elements"][current_free_game]["title"],
            "image_url": data["data"]["Catalog"]["searchStore"]["elements"][current_free_game]["keyImages"][0]["url"],
            "game_url": f"https://www.epicgames.com/store/en-US/p/{game_url}",
            "description": data["data"]["Catalog"]["searchStore"]["elements"][current_free_game]["description"],
            "promo_end_date": data["data"]["Catalog"]["searchStore"]["elements"][current_free_game]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
        }

    else:
        return None
