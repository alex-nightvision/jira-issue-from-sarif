from jira import JIRA
import os

# Jira server credentials
jira_url = 'https://nightvision.atlassian.net/'
username = 'alex@nightvision.net'
api_token = os.environ['JIRA_API_TOKEN']
project_id = 10004
component_name = 'Readme Doc'

# Connect to Jira
jira = JIRA(basic_auth=(username, api_token), options={'server': jira_url})

# List all components available in the project
components = jira.project_components(str(project_id))
# get component matching name
component_id = [component.id for component in components if component.name == component_name][0]

# Issue details
issue_dict = {
    'project': {'id': project_id},  # Replace 'PROJ' with your project key
    'summary': 'New issue created via API',
    'description': 'Here is a detailed description of the issue.',
    'issuetype': {'name': 'Bug'},  # You can change the issue type
    'components': [{'id': component_id}],  # Replace 'COMPONENT_ID' with the actual component ID
}

# Create the issue
new_issue = jira.create_issue(fields=issue_dict)
print(f"Issue created: {new_issue.key}")
