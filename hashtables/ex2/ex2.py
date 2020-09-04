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

    #NOTE tickets = array of Ticket(s)
    route = [None] * length

    locations = {}

    # hash keys as start location and destinations as values
    for ticket in tickets:
        locations[ticket.source] = ticket.destination
        

    # return locations

    # start destination?
    start_destination = locations["NONE"]

    # for key in locations: 

    for i in range(length):
        route[i] = start_destination

        start_destination = locations[start_destination]


    return route




def test_short_case(self):
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")
    tickets = [ticket_1, ticket_2, ticket_3]
    expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets, 3)

    return result

print(test_short_case(""))