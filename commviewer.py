import requests

from bs4 import BeautifulSoup, Comment
ascii_art = """
██████╗░██╗██╗░░░██╗░█████╗░░░░░░░░█████╗░░█████╗░███╗░░░███╗░░░░░░██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗███████╗██████╗░
██╔══██╗██║╚██╗░██╔╝██╔══██╗░░░░░░██╔══██╗██╔══██╗████╗░████║░░░░░░██║░░░██║██║██╔════╝░██║░░██╗░░██║██╔════╝██╔══██╗
██║░░██║██║░╚████╔╝░██║░░██║█████╗██║░░╚═╝██║░░██║██╔████╔██║█████╗╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝█████╗░░██████╔╝
██║░░██║██║░░╚██╔╝░░██║░░██║╚════╝██║░░██╗██║░░██║██║╚██╔╝██║╚════╝░╚████╔╝░██║██╔══╝░░░░████╔═████║░██╔══╝░░██╔══██╗
██████╔╝██║░░░██║░░░╚█████╔╝░░░░░░╚█████╔╝╚█████╔╝██║░╚═╝░██║░░░░░░░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░███████╗██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░░░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░░░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝
"""


print(ascii_art)

print("Note if you press Crtl + c : the code will break")

def fetch_page(url):
    """Fetch the HTML content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print("The URL provided is wrong: 404 Not Found")
            
        else:
            print(f"HTTP error occurred: {err}")

    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


    return response.text
def extract_comments(html):
    """Extract comments from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    comments = soup.findAll(string=lambda string: isinstance(string, Comment))
    return comments

def main(url):
    """Main function to fetch a webpage and print its comments."""
    html = fetch_page(url)
    comments = extract_comments(html)
    if comments:
        print(f"Comments found in {url}:")
        for comment in comments:
            print("comments are : ",comment)
    else:
        print(f"No comments found in {url}.")


def exit(key1):
    key1 = key1.strip()
    if ord(key1) == 49 :
        url = input("Enter the URL of the webpage: ")
        main(url)
        


if __name__ == '__main__':
    try :
        url = input("Enter the URL of the webpage: ")
        main(url)
        while True :
            key1 = input("Type  1 to continue Or Press ENTER to eixt  !   : ")
            exit(key1)
    except KeyboardInterrupt : 
        print("Exiting...")

