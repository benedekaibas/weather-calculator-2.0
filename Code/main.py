#we are using the BeautifulSoup library for this project
import requests
from bs4 import BeautifulSoup

print("This is a program that provides information for you based on your request of location.")


def Main():

    users_input = str(input("Enter the name of the city: "))
    
    url = "https://www.google.com/search?q="+"weather"+ users_input
    #news = "https://www.google.com/search?q="+"news"+ users_input
    html = requests.get(url).content
    
    soup = BeautifulSoup(html, "html.parser")
    print(html)




















if __name__ == "__main__":
    Main()