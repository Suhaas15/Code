import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

while True:
    game = input("Do you want to play a game of blackjack?: Type 'y' for yes and 'n' for no: ").lower()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if game=="y":
        print(logo)
        your_cards=[]
        comp_cards=[]

        comp_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))

        def your_play():
            your_count=sum(your_cards)
            print(f"Your cards: {your_cards}, current score: {your_count}")
            print(f"Computer's first card: {comp_cards}")
            more=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while more=="y":
                your_cards.append(random.choice(cards))
                your_count = sum(your_cards)
                if your_count>21:
                    return your_count
                print(f"Your cards: {your_cards}, current score: {your_count}")
                print(f"Computer's first card: {comp_cards}")
                more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            return your_count

        def comp_play():
            comp_cards.append(random.choice(cards))
            comp_count=sum(comp_cards)
            while comp_count<17:
                comp_cards.append(random.choice(cards))
                comp_count=sum(comp_cards)
            return comp_count

        def blackjack():
            count1=your_play()
            count2=comp_play()
            print(f"Your final hand: {your_cards}, final score: {count1}")
            print(f"Computer's final hand: {comp_cards}, final score: {count2}")
            if count1>21:
                if count2>21:
                    return "It's a draw!"
                else:
                    return "You lose!"
            elif count2>21:
                if count1>21:
                    return "It's a draw!"
                else:
                    return "You WIN!"
            elif count1>count2:
                return "You WIN!"
            elif count2>count1:
                return "You lose!"
            else:
                return "It's a draw!"

        print(blackjack())
    else:
        print("Sad to see you go.\nThanks for coming!!")
        break