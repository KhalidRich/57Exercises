# printing_quotes.py

def main():
    print(format_quotes())

    mo_quote = {"quote": "Your word is your bond.", "author": "Michelle Obama"}
    mt_quote = {"quote": "Your word is your bond.", "author": "Mich- I mean Melania Trump"}
    
    single_quote = format_quotes([mo_quote])
    print(single_quote)

    double_quote = format_quotes([mo_quote, mt_quote])
    print(double_quote)

def format_quotes(quotes=[]):
    if len(quotes) == 0:
        return "There are no quotes here."

    superquote = ""
    for quote in quotes:
        superquote += quote['author'] + " says, \"" + quote['quote'] + "\" "
    return superquote

if __name__ == "__main__":
    main()
