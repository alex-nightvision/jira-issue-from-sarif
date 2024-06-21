---

# NightVision Integration Repository

This repository contains scripts and configurations to interact with Jira and manage project vulnerabilities using NightVision SARIF reports.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Usage](#usage)
    - [Create Jira API Token](#create-jira-api-token)
    - [Find Jira Project IDs](#find-jira-project-ids)
    - [Create Tickets from SARIF](#create-tickets-from-sarif)
5. [License](#license)

## Overview

This repository automates the process of creating Jira tickets based on vulnerabilities found by NightVision. It includes scripts to fetch Jira project IDs, convert SARIF reports to Jira issues, and a sample OpenAPI specification.

## Prerequisites

- Python 3.x
- Jira account and API token
- NightVision account

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages:**
   ```sh
   pip install requests jira
   ```

3. **Set environment variables:**
   ```sh
   export JIRA_API_TOKEN='your_jira_api_token'
   ```

## Usage

### Create Jira API Token

1. Go to [Jira API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Create a new API token and copy it.

### Find Jira Project IDs

1. Run the following command to get Jira project IDs:
   ```sh
   python get-jira-project-id.py
   ```
   Example output:
   ```
   Project ID: 10001
   Project Name: NightVision
   Project Key: NV

   Project ID: 10004
   Project Name: NV Sales
   Project Key: NS
   ```

### Create Tickets from SARIF

1. Export NightVision SARIF report:
   ```sh
   nightvision export sarif -s "33a32558-bd24-44f0-aafa-224468d4b7f5" --swagger-file backup-openapi-spec.yml
   ```

2. Create Jira tickets from the SARIF report:
   ```sh
   python sarif-to-jira.py
   ```
