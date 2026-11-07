
class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Avoid adding the same friend more than once.
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        # Only add a person if they are not already in the network.
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} is already in the network.")

    def add_friendship(self, person1_name, person2_name):
        # Check that both people exist before connecting them.
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        # Prevent a person from becoming friends with themselves.
        if person1_name == person2_name:
            print("Friendship not created. A person cannot be their own friend.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add the friendship in both directions.
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person_name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person_name} is friends with: {', '.join(friend_names)}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    print("Adding people:")
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    print("\nCreating friendships:")
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    print("\nSocial network:")
    network.print_network()

    print("\nTesting a missing person:")
    network.add_friendship("Jordan", "Johnny")

    print("\nTesting a duplicate person:")
    network.add_person("Alex")

    print("\nTesting a duplicate friendship:")
    network.add_friendship("Alex", "Jordan")

    print("\nTesting a friendship with yourself:")
    network.add_friendship("Alex", "Alex")

    print("\nFinal social network:")
    network.print_network()
