from game import Game


def get_user_menu_choice():
    menu = input("\nMenu:\n(1) Play a new game\n(2) Show scores\n(0) Exit\n")
    answers = ['1', '2', '0']
    if menu not in answers:
        get_user_menu_choice()
    else:
        return menu


def print_results(results):
    if len(results) == 0:
        print(f"You haven't played yet")
    else:
        for result, number in results.items():
            print(f"{result}: {number}")


def main():
    results = {}
    while True:
        a = get_user_menu_choice()
        if a == '0':
            break
        elif a == '1':
            game = Game()
            game_result = game.play()
            results[game_result] = results.get(game_result, 0) + 1
        elif a == '2':
            print_results(results)
    print('Thank you for playing')

main()
