from random import choice

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']
        self.__user = ''
        self.__computer = ''
        self.__game_result = ''


    def __get_user_item(self):
        while True:
            user_choice = input("Let's start the game, choose rock or paper or scissors! One, Two, Three and ...\n")
            for item in self.items:
                if item == user_choice:
                    self.__user = user_choice
                    return self.__user

    def __get_computer_item(self):
        self.__computer = choice(self.items)
        return self.__computer

      def __get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.__game_result = 'Draw'
            return self.__game_result
        if user_item == 'rock':
            if computer_item == 'scissors':
                self.__game_result = 'Win'
                return self.__game_result
            self.__game_result = 'Loss'
            return self.__game_result
        if user_item == 'paper':
            if computer_item == 'rock':
                self.__game_result = 'Win'
                return self.__game_result
            self.__game_result = 'Loss'
            return self.__game_result
        if computer_item == 'paper':
            self.__game_result = 'Win'
            return self.__game_result
        self.__game_result = 'Loss'
        return self.__game_result


    def play(self):
        self.__get_game_result(self.__get_user_item(), self.__get_computer_item())
        print(f"You selected {self.__user}. The computer selected {self.__computer}. It's a {self.__game_result}\n")
        return self.__game_result









