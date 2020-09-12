#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}

    # Setting up list for route
    route = [None] * length  # len of length

    # iterating thru the ticket in all tickets
    for ticket in tickets:
        # setting source in my dictionary
        cache[ticket.source] = ticket.destination  # to the destination
    next = cache["NONE"]  # resetting my dictionary

    for r in range(0, length):  # iterating thru the range (over the length)
        # set route flight to dictionary
        route[r] = next
        # set the next destination to the dictionary
        next = cache[next]

    return route
