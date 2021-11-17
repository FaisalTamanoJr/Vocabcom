from bs4 import BeautifulSoup
import sys
import requests


def main():
    # The commands in the program
    commands = {
            "define":
            "searches for the short definition of that word",
            "long-define":
            "searches for the long definition of that word",
            }

    # Create a list for their keys and their values
    command_keys = []
    command_values = []
    for command in commands.items():
        command_keys.append(command[0])
        command_values.append(command[1])

    # Let the user provide one word
    if len(sys.argv) == 2 or len(sys.argv) == 3:

        if sys.argv[1] == "define":
            Definition("short")

        elif sys.argv[1] == "long-define":
            Definition("long")

        else:
            print("Usage: vocabcom <command> [arguments]" +
                  "\n\nThe commands are:\n")
            for i in range(len(commands)):
                print("\t" + command_keys[i] + "\t\t" + command_values[i])

    # If the user does not provide a word or provides
    # too much words tell them how to properly use the program
    else:
        print("Usage: vocabcom <command> [arguments] \n\nThe commands are:\n")
        for i in range(len(commands)):
            print("\t" + command_keys[i] + "\t\t" + command_values[i])


def Definition(length):
    if len(sys.argv) == 3:
        # The dictionary link to use
        dictionary = "https://www.vocabulary.com/dictionary/"
        url = dictionary + sys.argv[2]

        # Send an http request to get the html file from the url
        url = requests.get(url).text

        # Parse it
        soup = BeautifulSoup(url, "html.parser")

        if length == "short":
            # Look for the short definition and print it
            short_definition = soup.find_all("p", class_="short")

            # If it exists
            if short_definition:
                for short in short_definition:
                    print(short.text)

            # If the definition cannot be found
            else:
                print(f'The {length} definition of the word cannot be found')

        else:
            # Look for the long definition and print it
            long_definition = soup.find_all("p", class_="long")

            # If it exists
            if long_definition:
                for long in long_definition:
                    print(long.text)

            # If the definition cannot be found
            else:
                print(f'The {length} definition of the word cannot be found')

    else:
        print("Usage: vobacom define <word>")


if __name__ == "__main__":
    exit(main())
