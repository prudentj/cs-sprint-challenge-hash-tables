#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Assuming you don't ever fly to the same city twice
    # Key in ticketsDict is the source
    ticketsDict = {}
    # Stores destination of tickets in order
    route = []
    # Adding tickets to tickets Dict
    for ticket in tickets:
        if ticket not in ticketsDict:
            # Assuming I will not get any repeat tickets
            ticketsDict[ticket.source] = ticket
    # Ticket I am holding
    ticketHolder = ticketsDict["NONE"]
    route.append(ticketHolder.destination)
    # Look at a destintion and see if I have a ticket that has that as a source
    while ticketHolder.destination != "NONE":
        ticketHolder = ticketsDict[ticketHolder.destination]
        route.append(ticketHolder.destination)
    return route
