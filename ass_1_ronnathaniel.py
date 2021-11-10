
from typing import List, Dict


"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 9/22/2021
Title: Programming Assignment #1
"""


def is_valid_email(email: str) -> bool:
    parted = email.partition('@')
    return all(parted)

def get_unique_emails(emails: List[str]) -> Dict:
    unique_emails = set()
    for email in emails:
        if not is_valid_email(email):
            continue
        local, domain = email.split('@')
        if '+' in local:
            local = local.split('+', 1)[0]
        if '.' in local:
            local = local.replace('.', '')
        unique_emails.add('@'.join([local, domain]))

    amt = len(unique_emails)
    print('Total Unique Emails:', amt)
    return amt

if __name__ == '__main__':
    # Integration Tests

    # Total Unique: 3
    emails = [
        "a@leetcode.com",
        "b@leetcode.com",
        "c@leetcode.com"
    ]
    assert get_unique_emails(emails) == 3

    # Total Unique: 2
    emails = [
         "test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com",
         "testemail+james@lee.tcode.com"
    ]
    assert get_unique_emails(emails) == 2
