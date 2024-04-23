## create jira api token

https://id.atlassian.com/manage-profile/security/api-tokens

## find project ids

https://confluence.atlassian.com/jirakb/how-to-get-project-id-from-the-jira-user-interface-827341414.html

```
$ py get-jira-project-id.py 
Project ID: 10001
Project Name: NightVision
Project Key: NV

Project ID: 10004
Project Name: NV Sales
Project Key: NS
```

## create ticket

```
nightvision export sarif -s "33a32558-bd24-44f0-aafa-224468d4b7f5" --swagger-file backup-openapi-spec.yml
py sarif-to-jira.py
```