#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    hashmap = dict()
    route = [None] * length

    for i in range(0, length):
        current = tickets[i]
        hashmap[current.source] = current.destination

    # set first flight in arr to flight w/ source "NONE"
    route[0] = hashmap['NONE']
    route[1] = hashmap[route[0]]

    if length > 2:
        for i in range(2, length):
            # the `i`th location in the route can be found by checking the hash
            # table for the `i-1`th location
            route[i] = hashmap[route[i - 1]]

    return route



if __name__ == "__main__":
    arrays = []

    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    print(reconstruct_trip(tickets, 3))
