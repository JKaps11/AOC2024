import requests

# Create a session object
session = requests.Session()

# Generate a unique session ID (if needed)
session_id = "53616c7465645f5ff1cc36642816608561294178461eb44fa45a6381647f9401eda6882c2edaca7af8603ec71f76d5434eb1e57b01e47551a2e03022c8db06db"

headers = {'User-Agent': 'github.com/{$userName}/{$repository} by {$email}'}

# Add the session ID to the headers
session.headers.update({"Session-ID": session_id})

# Make a request using the session
response = session.get("https://adventofcode.com/2024/day/1/input")

# Print the response
print(response.text)
