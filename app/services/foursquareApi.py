import requests

class FourSquareApi:
    apiKey = "fsq3MPNAzleYG/1CNuzhR1Ddr8+4Grit+GP8S5Gdhela7H4="
    header = {
        "accept": "application/json",
        "Authorization": apiKey
    }

    def __init__(self) -> None:
        pass

    def searchPlace(self, location: str) -> list:
        apiUrl = "https://api.foursquare.com/v3/places/search"
        params = {
            "categories": 19009,                            # looks for just hotels
            "fields": "fsq_id,categories,location,name",    # Only the required fields
            "near": location,                               # near the given location
        }
        response = requests.get(apiUrl, params=params, headers=self.header)
        response.encoding = 'unicode_escape'
        response = response.json()

        ret = []
        for x in response['results']:
            try:
                ret.append({
                    "fsq_id": x['fsq_id'],
                    "icon": x['categories'][0]['icon']['prefix'] + "120" + x['categories'][0]['icon']['suffix'],
                    "name": x['name'],
                    "address": x['location']['formatted_address'],
                })
            except KeyError:
                continue
            except Exception as e:
                print(e)

        return ret
            