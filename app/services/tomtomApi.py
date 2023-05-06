import requests

class TomTomApi:

    baseURL = "api.tomtom.com"
    versionNumber = 2
    responseExtension = "json"
    key = "Zv3rzY1MK31CEvRgZR4w8DmEFgqAAaWX"
    
    payload = {
        "key": key
    }

    def __init__(self) -> None:
        pass

    def geoCoding(self, location) -> dict:
        apiReqUrl = f'https://{self.baseURL}/search/{self.versionNumber}/geocode/{location}.{self.responseExtension}'

        payload = self.payload | {"limit": 1}

        try:
            result = requests.get(apiReqUrl, params=payload)
            result = result.json()
            return result['results'][0]['position']
        except Exception as e:
            print(e)
            return {}
        
    def findHotel(self, location):
        geoCode = self.geoCoding(location)
        apiReqUrl = f'https://{self.baseURL}/search/{self.versionNumber}/nearbySearch/.{self.responseExtension}'
        payload = self.payload | geoCode | {
            "radius": 4000, # 4km radius
            "categorySet": "7314002,7314007,7314004,7314003,7314006,7314005,7314008"
        }

        try:
            assert 'lat' in payload and 'lon' in payload

            result = requests.get(apiReqUrl, params=payload)
            result = result.json()
            print(result['results'])
            # return result['results']
        except Exception as e:
            print(e)
            # return {}

thing = TomTomApi()
# thing.geoCoding("London, UK")
thing.findHotel("Dhaka, Bangladesh")