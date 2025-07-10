bids = {}
dicision = ""
condition = True
highest_bid = 0
highest_bidder = ""
while condition:
    print("\n" * 100)
    print(
        '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    )
    key = input("What's your name?\n")
    value = int(input("What's your bid?\n"))
    bids[key] = value
    dicision = input("Are there any other bidders?\n")
    if dicision == "no":
        condition = False

for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key

print("The Highest Bidder is: " + highest_bidder + f" \nBid: {highest_bid}")
