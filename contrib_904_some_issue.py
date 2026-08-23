"""Some Issue (fix for issue #904)"""

import requests
from typing import Optional

def fetch_random_cat_fact() -> Optional[str]:
    """
    Retrieve a random cat fact from the Cat Fact API.
    Returns the fact as a string, or None if the request fails.
    """
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("fact")
    except (requests.RequestException, ValueError):
        return None

