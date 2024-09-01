from linkedin_api import Linkedin

# Authenticate using LinkedIn credentials
api = Linkedin('your_email@example.com', 'your_password')

# Search for engineers based on a keyword
search_results = api.search_people(keywords='Engineer', limit=10)

# Print details of the search results
for person in search_results:
    print(f"Name: {person['firstName']} {person['lastName']}")
    print(f"Occupation: {person['occupation']}")
    print(f"Location: {person['location']}")
    print(f"LinkedIn Profile: {person['publicIdentifier']}")
    print('-' * 30)

# You can further use the API to send connection requests or messages
