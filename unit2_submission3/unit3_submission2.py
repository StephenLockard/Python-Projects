class DVD:

    # Constructor
    def __init__(self, title, dvd_type, cost):
        self.title = title
        self.dvd_type = dvd_type
        self.cost = cost

        # Return self._title instance variable

    def get_title(self):
        return self.title

    # newTitle
    def set_title(self, new_title):
        self.title = new_title

    # Return self.type instance variable
    def get_type(self):
        return self.dvd_type

    # Return self.cost instance variable
    def get_cost(self):
        return self.cost

    # Change the self._cost instance variable
    def set_cost(self, new_cost):
        self.cost = new_cost

    # Change the self.dvd_type instance variable. This includes verifying the dvd_type specified will match valid_types
    def set_type(self, new_dvd_type):
        valid_types = ['Game', 'Movie', 'Software']
        while True:
            self.dvd_Type = input('Please enter one of: (Game, Movie, Software)')
            if self.dvd_type() not in valid_types:
                print('Incorrect type, please enter from the following choices: '
                      '(Game, Movie, Software)')
                continue
            else:
                self.dvd_type = new_dvd_type
            break

    # define valid types that user can enter
    @staticmethod
    def list_valid_dvd_types():
        print("We only accept: 'Game', 'Movie', 'Software' as types")

    # output title,dvd_type, and cost
    def display_dvd_information(self):
        for obj in self:
            print(obj.title)
            print(obj.dvd_type)
            print(obj.cost)

    # Calculate average cost and output
    def display_total_and_average_costs(self):
        add = 0
        for obj in self:
            add += obj.cost
        print(obj.cost)
        avg = add / len(self)
        print('Average cost: ', avg)

    # Allow user to change dvd title, type, and cost
    def change_dvd(self):
        # Show Current title and allow user to update
        print('DVD Title is', self.title)
        input_one = input('Do you want to change title(y/n):')
        if input_one in ['y', 'Y']:
            title = input('Please enter a title:')
            self.title = title
        else:
            pass

        # Show current type and allow user to update type
        print('DVD type is ', self.dvd_type)
        input_two = input('Do you want to change type (y/n): ')
        if input_two in ['y', 'Y']:
            valid_types = ['Game', 'Movie', 'Software']
            while True:
                dvd_type = input('Please enter valid type: (Game, Movie, Software)')
                if dvd_type.title() not in valid_types:
                    print('Incorrect type, please enter from the following choices: '
                          '(Game, Movie, Software)')
                    continue
                else:
                    self.type = dvd_type
                break
            else:
                pass
        # Show current cost and allow user to update it
        print('DVD cost is ', self.cost)
        in3 = input('Do you want to change cost (y/n):')
        if in3 in ['y', 'Y']:
            cost = int(input('Please enter the cost: '))
            self.cost = cost
        else:
            pass


def main():
    # Create empty list
    list = []

    # Variables for adding to the list
    dvd1 = DVD('Madden 2019', 'Game', 60)
    dvd2 = DVD('Quicken 2019', 'Software', 55)
    dvd3 = DVD('Batman', 'Movie', 15)

    # Add data to list
    list.append(dvd1)
    list.append(dvd2)
    list.append(dvd3)
    print('All of the DVD information')

    # Display all dvd info
    DVD.display_dvd_information(list)

    # Display total cost and average of the cost
    DVD.display_total_and_average_costs(list)

    # Allow user to update list
    DVD.change_dvd(dvd1)
    DVD.change_dvd(dvd2)
    DVD.change_dvd(dvd3)

    # Declare new list
    list = []

    # Add updated information to list
    list.append(dvd1)
    list.append(dvd2)
    list.append(dvd3)

    # Display updated information list
    DVD.display_dvd_information(list)

    # Display updated total cost and average
    DVD.display_total_and_average_costs(list)


main()

