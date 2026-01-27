#smth
from app.commands.command_parser import command_parser
from app.orchestra import orchestra
def main():
    print("Some app is ready to use:")
    is_running = True


    while is_running:
        input_command = input()
        is_running = orchestra(command_parser(input_command))

        


if __name__ == "__main__":
    main()