⚠️⚠️**Internal Project - customer data in commit history**⚠️⚠️

## Setup & Usage

### 1. Configure Credentials

Create a file named .env in the root folder and add the following:

* ZD_SUBDOMAIN: Your subdomain only (e.g., if it's company.zendesk.com, just use company).
* ZD_EMAIL: Your Zendesk login email.
* ZD_TOKEN: Your generated API token.

### 2. Prepare Ticket List

Create a file named tickets.csv in the project folder. List your Ticket IDs one per line.

Important: Do not include a header row (e.g., don't put "Ticket ID" at the top).

### 3. Generate Report

Run the script. A file named report.txt will be automatically created containing the internal comments from all listed tickets.
