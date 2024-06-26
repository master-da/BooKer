import requests

class ServiceProvider:
    provider_id = ''
    name = ''
    address = ''
    phone = ''
    email = ''
    services = ''

class Service:
    service_id = ''
    provider_id = ''
    type = ''
    description = ''
    price = ''
    availability = ''

    def get_details(self):
        return FourSquareApi().getService(self.service_id)

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
        response.encoding = 'utf-8'
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
    
    def getService(self, service_id) -> ServiceProvider:
        apiUrl = "https://api.foursquare.com/v3/places/search"
        params = {
            "near": service_id,                               # near the given location
            "categories": 19009,                            # looks for just hotels
            "fields": "fsq_id,categories,location,name",    # Only the required fields
        }
        try:
            response = response.get(apiUrl, params=params, headers=self.header)
            response.encoding = 'utf-8'
            response = response.json()

            serviceProvider = ServiceProvider()
            serviceProvider.provider_id = response['fsq_id']
            serviceProvider.name = response['name']
            serviceProvider.address = response['location']['formatted_address']
            serviceProvider.phone = response['tel']
            serviceProvider.email = response['email']
            serviceProvider.services = response['categories']

            return serviceProvider
        except:
            return None

    def getPlaceNameBasic(self, fsq_id: str) -> str:
        apiUrl = "https://api.foursquare.com/v3/places/" + fsq_id
        params = {
            "fields": "name,location",    # Only the required fields
        }
        response = requests.get(apiUrl, params=params, headers=self.header)
        response.encoding = 'utf-8'
        response = response.json()

        return response

            
    def getPlaceDetails(self, fsq_id: str) -> dict:
        # https://api.foursquare.com/v3/places/4c6238d358810f4795db061e?fields=photos%2Ctips%2Ctel%2Cemail%2Cwebsite%2Csocial_media
        apiUrl = "https://api.foursquare.com/v3/places/" + fsq_id
        params = {
            "fields": "name,photos,tips,tel,email,social_media", #website,    # Only the required fields
        }
        response = requests.get(apiUrl, params=params, headers=self.header)
        response.encoding = 'utf-8'
        response = response.json()

        # print(response)

        ret = {
            "name": "",
            "photos": [],
            "tips": [],
            "tel": "",
            "email": "",
            # "website": "",
            "social_media": {},
        }

        try: ret['name'] = response['name']
        except Exception as e: ret['name'] = ''

        try:
            for photo in response['photos']:
                ret['photos'].append(photo['prefix'] + "original" + photo['suffix'])
        except Exception as e:
            print(e)

        try:
            for tip in response['tips']:
                ret['tips'].append(tip['text'])
        except Exception as e:
            print(e)

        try: ret['tel'] = response['tel']
        except Exception as e: ret['tel'] = ''

        try: ret['email'] = response['email']
        except Exception as e: ret['email'] = ''

        # try: ret['website'] = response['website']
        # except Exception as e: ret['website'] = ''

        try: ret['social_media'] = response['social_media']
        except Exception as e: ret['social_media'] = ''

        # print(ret)

        return ret
    
