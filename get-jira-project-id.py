import requests, os

# Replace these variables with your actual data
jira_url = 'https://nightvision.atlassian.net'
api_token = os.environ['JIRA_API_TOKEN']
email = 'alex@nightvision.net'


# Set up basic authentication
auth = requests.auth.HTTPBasicAuth(email, api_token)

# Set up the headers
headers = {
   "Accept": "application/json"
}

# Make a request to get project information
response = requests.request(
   "GET",
   f"{jira_url}/rest/api/3/project/",
   headers=headers,
   auth=auth
)

# Parse the response
project_data = response.json()

# Print the project ID
for project in project_data:
   print("Project ID:", project.get('id'))
   print("Project Name:", project.get('name'))
   print("Project Key:", project.get('key'))
   print()
