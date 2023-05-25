#Build an application that extracts phone number, email and link from a website. 
#This application should run as an executable file and should ask for the file name, 
#extract email etc also store the extracted email in a file separ

import re
import requests
from bs4 import BeautifulSoup
import os
import sys


def executable():
    url = input("Enter the website URL: ")
    filename = input("Enter the filename to save the emails: ")

    if not url.startswith("http://") and not url.startswith("https://"):
        print("Please enter a valid website URL.")
        return executable()

    if not filename.endswith(".txt"):
        print("Please enter a valid filename.")
        return executable()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    phone_numbers = re.findall(r'\+?\d{10}(?:\s+\d{3}-\d{3}-\d{4})?\b', soup.get_text())
    emails = re.findall(r"[A-Za-z0-9%_+-.]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z:;*$#]{2,6}",soup.get_text())
    links = [link.get('href') for link in soup.find_all('a', href=True)]

    print("Phone Numbers:")
    print(phone_numbers)
    print("Emails:")
    print(emails)
    print("Links:")
    print(links)

    with open(os.path.join(sys.path[0], "exmails.txt"), 'w') as c2file:
        for email in emails:
            c2file.write(email + '\n')

    print(f"Emails saved to '{filename}'.")
    input("Press Enter to exit...")

if __name__ == '__main__':
   executable() 


   