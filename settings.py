import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = int(os.environ.get('MIN_PRICE', 1500))

# The maximum rent you want to pay per month.
MAX_PRICE = int(os.environ.get('MAX_PRICE', 2000))

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = os.environ.get('CRAIGSLIST_SITE', 'sfbay')

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = os.environ.get('AREAS', ["eby", "sfc", "sby", "nby"])

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
DEFAULT_BOXES = {
    "adams_point": [
        [37.80789, -122.25000],
        [37.81589,	-122.26081],
    ],
    "piedmont": [
        [37.82240, -122.24768],
        [37.83237, -122.25386],
    ],
    "rockridge": [
        [37.83826, -122.24073],
        [37.84680, -122.25944],
    ],
    "berkeley": [
        [37.86226, -122.25043],
        [37.86781, -122.26502],
    ],
    "north_berkeley": [
        [37.86425, -122.26330],
        [37.87655, -122.28974],
    ],
    "pac_heights": [
        [37.79124, -122.42381],
        [37.79850, -122.44784],
    ],
    "lower_pac_heights": [
        [37.78554, -122.42878],
        [37.78873, -122.44544],
    ],
    "haight": [
        [37.77059, -122.42688],
        [37.77086, -122.45401],
    ],
    "sunset": [
        [37.75451, -122.46422],
        [37.76258, -122.50825],
    ],
    "richmond": [
        [37.77188, -122.47263],
        [37.78029, -122.51005],
    ],
    "presidio": [
        [37.77805, -122.43959],
        [37.78829, -122.47151],
    ]
}

BOXES = os.environ.get('BOXES', DEFAULT_BOXES)

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
DEFAULT_NEIGHBORHOODS = ["berkeley north", "berkeley", "rockridge", "adams point", "oakland lake merritt",
                         "cow hollow", "piedmont", "pac hts", "pacific heights", "lower haight", "inner sunset",
                         "outer sunset", "presidio", "palo alto", "richmond / seacliff", "haight ashbury", "alameda",
                         "twin peaks", "noe valley", "bernal heights", "glen park", "sunset", "mission district",
                         "potrero hill", "dogpatch"]

NEIGHBORHOODS = os.environ.get('NEIGHBORHOODS', DEFAULT_NEIGHBORHOODS)

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = int(os.environ.get('MAX_TRANSIT_DIST', 2))  # Kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
DEFAULT_TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur_bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758]
}

TRANSIT_STATIONS = os.environ.get('DEFAULT_TRANSIT_STATIONS', DEFAULT_TRANSIT_STATIONS)

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = os.environ.get('CRAIGLIST_HOUSING_SECTION', 'apa')

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = int(os.environ.get('SLEEP_INTERVAL', 20 * 60))  # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL', '#housing')

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass