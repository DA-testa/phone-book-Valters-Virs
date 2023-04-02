# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Phonebook:
    size = 1000
    multiplier = 13

    def __init__(self):
        self.array = [None] * self.size

    def get_hash(self, key):
        hash = (key * self.multiplier) % self.size

        return hash
    
    def add(self, number, name):
        hash = self.get_hash(number)

        self.array[hash] = name

    def delete(self, number):
        hash = self.get_hash(number)

        self.array[hash] = None

    def find(self, number):
        hash = self.get_hash(number)

        if self.array[hash] == None:
            return 'not found'
        
        return self.array[hash]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = []
    contacts = Phonebook()
    for cur_query in queries:
        if cur_query.type == 'add':
            # # if we already have contact with such number,
            # # we should rewrite contact's name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else: # otherwise, just add it
            #     contacts.append(cur_query)

            contacts.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break

            contacts.delete(cur_query.number)
        else:
            # response = 'not found'
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            # result.append(response)

            result.append(contacts.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

