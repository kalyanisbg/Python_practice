from collections import ChainMap

'''
1. Basic ChainMap Creation

Task: Create a ChainMap from two dictionaries. The first dictionary contains user information, and the second contains preferences. After creating the ChainMap, retrieve both the user information and preferences, and check how they are combined.

Example Input:
	•	user_info = {'name': 'John', 'age': 30}
	•	preferences = {'theme': 'dark', 'language': 'English'}

Expected Output:
	•	Combined ChainMap: {'name': 'John', 'age': 30, 'theme': 'dark', 'language': 'English'}
'''

def user_data(user_info, preferences):
    return dict(ChainMap(preferences, user_info))

# print(user_data({'name': 'John', 'age': 30}, {'theme': 'dark', 'language': 'English'}))

'''
2. Lookups in a ChainMap

Task: Given two dictionaries (defaults and user), create a ChainMap and try to look up values from the user dictionary. If a value is not found, check the fallback in the defaults dictionary.

Example Input:
	•	defaults = {‘theme’: ‘light’, ‘language’: ‘French’}
	•	user = {‘theme’: ‘dark’}

Expected Output:
	•	Theme: dark
	•	Language: French
'''

def lookup(defaults, user):
    output = ""
    for key, value in ChainMap(user, defaults).items():
        output += (f'{key.title()}: {value}\n')
    return output

# print(lookup({'theme': 'light', 'language': 'French'}, {'theme': 'dark'}))

'''
3. Adding a New Mapping to a ChainMap

Task: Create a ChainMap with two dictionaries, then add a new dictionary representing session data. Add this new dictionary to the ChainMap and perform lookups to see how the order of mappings affects the lookup.

Example Input:
    - global_settings = {'timezone': 'UTC', 'currency': 'USD'}
    - user_settings = {'timezone': 'PST'}
    - session_data = {'currency': 'EUR'}

Expected Output:
    - Global Settings: {'timezone': 'UTC', 'currency': 'USD'}
    - User Settings: {'timezone': 'PST'}
    - Session Data: {'currency': 'EUR'}

Perform a lookup for "currency" after adding the session data and observe the result.
'''

