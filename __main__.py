from Bot import *  # AddBot, ExitBot, SearchBot, RemoveBot, EditBot, SaveBot, LoadBot, CongratulateBot, VieweBot, ExitBot

if __name__ == "__main__":

    choice = {
        "add": AddBot,
        "search": SearchBot,
        "remove": RemoveBot,
        "edit": EditBot,
        "save": SaveBot,
        "load": LoadBot,
        "Congratulate": CongratulateBot,
        "view": ViewBot,
        "exit": ExitBot
    }

my_address_book = AddressBook()  # create AddressBook

while True:
    action = input("Choose an action: ").strip().lower()
    if action in choice:
        bot_instance = choice[action]()
        bot_instance.handle(my_address_book)
    else:
        print("Incorrect action")

# if action in choice:
#     choice[action].handle()
# else:
#     print("Incorrect action")
