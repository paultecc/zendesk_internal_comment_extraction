## Setup & Usage

### 1. Configure Credentials

Create a .env in the root folder and add the following credentials:

* SUBDOMAIN: Your subdomain only (ignore zendesk.com).
* EMAIL: Your Zendesk login email.
* TOKEN: Your API token.

### 2. Prepare Ticket List

Create a file named tickets.csv in the project folder. List your Ticket IDs one per line.

Important: Do not include a header row (don't put 'tickets' in the top row).

### 3. Generate Report

Run the script. A file named report.txt will be automatically created containing the internal comments from all listed tickets. Any errors should be raised as the script runs.
