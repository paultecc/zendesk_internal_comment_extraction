import csv
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

subdomain = os.getenv("ZD_SUBDOMAIN")
email = os.getenv("ZD_EMAIL")
token = os.getenv("ZD_TOKEN")

auth = (f"{email}/token", token)
base_url = f"https://{subdomain}.zendesk.com/api/v2"


def load_tickets(file_path):
    ticket_ids = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            ticket_ids.append(row[0].strip())
    return ticket_ids


def get_comments(ticket_id):
    url = f"{base_url}/tickets/{ticket_id}/comments.json"
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        comments = response.json().get("comments", [])
        return comments

    elif response.status_code == 429:
        print(f"API rate limit hit. Pausing for 30 seconds at {ticket_id}")
        time.sleep(30)
        return get_comments(ticket_id)

    else:
        print(f"Skpping ticket {ticket_id}: Error {response.status_code}")
        return []


if __name__ == "__main__":
    tickets = load_tickets("tickets.csv")

    report = "Internal Ticket Comments\n"

    if tickets:
        for ids in tickets:
            print(f"Processing ticket #{ids}.")
            comments = get_comments(ids)

            # Internal Comment only filter
            internal_comments = [c for c in comments if c["public"] is False]
            if not internal_comments:
                continue

            report += f"Ticket #{ids}:\n"
            report += f"https://{subdomain}.zendesk.com/tickets/{ids}\n"
            report += "-" * 20 + "\n"

            for note in internal_comments:
                date_short = note["created_at"].split("T")[0]

                report += f"Date: {date_short} | Author: {note['author_id']}\n"
                report += f"Body: {note['body']}\n"
                report += "\n"

            report += "\n"

        with open("report.txt", "w", encoding="utf-8") as f:
            f.write(report)

        print("Export complete")
