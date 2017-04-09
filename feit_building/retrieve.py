import requests


class Data():
    """Used to provide a means to access data from the UTS eif api."""

    @staticmethod
    def retrieve(startDate, endDate, family, unit):
        """Performs a post request to the UTS eif api."""

        payload = {
            'rFromDate': startDate,
            'rToDate': endDate,
            'rFamily': family,
            'rSensor': unit,
        }

        r = requests.post('http://eif-research.feit.uts.edu.au/api/json/', params=payload)

        if(r.status_code == 200):
            return (True, r.json())
        else:
            return (False, {})
