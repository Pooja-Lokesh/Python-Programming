import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url= "http://quotes.toscrape.com"

def read_quotes(filename) :
    with open(filename, "r") as file :
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes) :
    quote = choice(quotes)
    remaining_guesses = 4
    print("here is a quote :")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses != 0:
        guess = input(f"who said this quote? guesses remaining : {remaining_guesses}")
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT")
            break
        remaining_guesses -= 1
        
        if  remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint : the author was born in {birth_place} on {birth_date}")
        
        elif remaining_guesses == 2:
            print(f"Here's the hint : the author first name starts with {quote['author'][0]} ")
        
        elif remaining_guesses == 1 :
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here's a hint : the author's last name starts with {last_initial}")
        
        else :
            print(f"You ran out of quesses. The answer was {quote['author']} ")

    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input("Would you like to play again (y/n) ?")
    if again.lower() in ('yes','y') :
        print("OK YOU PLAY AGAIN")
        return start_game()
    else:
        print("OK, GOODBYE!")


quotes = read_quotes("quotes.csv")
start_game(quotes)
