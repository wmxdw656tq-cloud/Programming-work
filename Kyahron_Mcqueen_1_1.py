 #Ask the user how many tickets they want
def ask_tickets(remaining_tickets):
    tickets = int(input("How many tickets would you like to buy (1 to 4)? "))

    # Check if the request is valid
    if tickets < 1 or tickets > 4:
        print("You can only buy between 1 and 4 tickets.")
        return 0

    if tickets > remaining_tickets:
        print("Not enough tickets remaining.")
        return 0

    return tickets


# selling tickets
def sell_tickets():
    remaining_tickets = 10
    buyers = 0  

    # Loop until all tickets are sold
    while remaining_tickets > 0:
        print("\nTickets remaining:", remaining_tickets)

        tickets_bought = ask_tickets(remaining_tickets)

        # If the purchase is valid
        if tickets_bought > 0:
            remaining_tickets = remaining_tickets - tickets_bought
            buyers = buyers + 1

            print("Purchase successful!")
            print("Tickets left:", remaining_tickets)

    # All tickets sold
    print("\nAll tickets have been sold.")
    print("Total number of buyers:", buyers)


# Start the program
sell_tickets()
