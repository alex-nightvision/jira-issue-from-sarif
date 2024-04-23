from jira import JIRA
import os
import json

# Jira server credentials
jira_url = 'https://nightvision.atlassian.net/'
username = 'alex@nightvision.net'
assignee_username = 'alex@nightvision.net'
api_token = os.environ['JIRA_API_TOKEN']
project_id = 10004
component_name = 'Readme Doc'

# Connect to Jira
jira = JIRA(basic_auth=(username, api_token), options={'server': jira_url})

# List all components available in the project
components = jira.project_components(str(project_id))
# get component matching name
component_id = [component.id for component in components if component.name == component_name][0]

# Check if component was found
if not component_id:
    raise ValueError("Component not found in Jira")

# Load SARIF data
sarif_file = 'results.sarif'
with open(sarif_file, 'r') as file:
    sarif_data = json.load(file)

# Iterate over findings in SARIF data
for run in sarif_data['runs']:
    for result in run['results']:
        rule_id = result['ruleId']
        description = next((rule['fullDescription']['text'] for rule in run['tool']['driver']['rules'] if rule['id'] == rule_id), "No description available.")

        # Issue details
        issue_dict = {
            'project': {'id': project_id},
            'summary': result['message']['text'],
            'description': description,
            'issuetype': {'name': 'Bug'},
            'components': [{'id': component_id}],
        }

        # only if issues cannot be unassigned
        if assignee_username:
            issue_dict['assignee'] = {'name': assignee_username}

        # Create the issue
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Issue created: {new_issue.key}")