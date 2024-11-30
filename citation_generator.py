# variables
# Get user inputs
author_name = input("Enter the author's name (e.g., 'Last Name, First Initial'): ")
art_date = input("Enter the date of the article (e.g., '2024, April 15'): ")
title = input("Enter the title of the work (e.g., 'This is an Example'): ")
source = input("Enter the title of the source (e.g., 'Google'): ")
url = input("Enter the URL of the article (e.g., 'https://google.com'): ")

# Generate citation in APA 7th Edition format
citation = f"{author_name}. ({art_date}). {title}. {source}. {url}"
print(citation)





