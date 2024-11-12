import requests

URL = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Using the variable URL without quotes
response = requests.get(URL)

if response.status_code == 200: 
    pull_requests = response.json()
    pr_creators = {}

    for pull in pull_requests:
        creator = pull['user']['login']
        
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Correct indentation and syntax for print statements
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():  # Parentheses needed for .items()
        print(f"{creator}: {count} PR(s)")
else:
    # Correct syntax for else and print statement
    print(f"Failed to fetch data. Status code: {response.status_code}")
