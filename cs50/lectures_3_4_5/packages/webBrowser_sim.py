# Install requests package to make API calls
#---------- REQUEST ---------------
# Request impersonates a web browser
import requests
#--- JSON ------ shipped with pyth
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

if len(sys.argv) == 2:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

# print(response.json())
# ---- using json package to clean up output
# print(json.dumps(response.json(), indent=2))

object_list = response.json()
# - results used in loop is taken from APPLE RESPONSE
for result in object_list["results"]:
    # - trackName is taken fron returned APPLE RESPONSE
    print(result["trackName"])

