import requests


class ExerciseManager(object):
    """Exercise Manager."""

    api_endpoints = {
        "GET_BODYPARTS": "exercises/bodyPartList",
        "GET_TARGET_MUSCLES": "exercises/targetList",
        "GET_EQUIPMENTS": "exercises/equipmentList",
        "GET_EXERCISES": "exercises",
    }

    def __init__(self):
        """Initialize Exercise Manager."""
        super(ExerciseManager, self).__init__()
        self.access_key = 'a768cf273bmshb1731bcc0995349p1c4d76jsn6782eb4812e6'
        self.host = 'exercisedb.p.rapidapi.com'
        self.base_url = 'https://exercisedb.p.rapidapi.com/'
    
    def get_bodyparts(self):
        """Get body parts."""
        url = self.base_url+self.api_endpoints["GET_BODYPARTS"]
        print(url)
        headers = {
            'X-RapidAPI-Host': self.host,
            'X-RapidAPI-Key': self.access_key,
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def get_target_muscles(self):
        """Get target muscles."""
        url = self.base_url+self.api_endpoints["GET_TARGET_MUSCLES"]
        print(url)
        headers = {
            'X-RapidAPI-Host': self.host,
            'X-RapidAPI-Key': self.access_key,
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def get_equipments(self):
        """Get equipments."""
        url = self.base_url+self.api_endpoints["GET_EQUIPMENTS"]
        print(url)
        headers = {
            'X-RapidAPI-Host': self.host,
            'X-RapidAPI-Key': self.access_key,
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def get_exercises(self):
        """Get exercises."""
        url = self.base_url+self.api_endpoints["GET_EXERCISES"]
        print(url)
        headers = {
            'X-RapidAPI-Host': self.host,
            'X-RapidAPI-Key': self.access_key,
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()