# https://github.com/Loucios/deque
# ID 54461346

from deque.deque import Deque


def main():
    try:
        commands_number = int(input())
        deque_max_size = int(input())
        commands = [input() for i in range(commands_number)]
    except ValueError as e:
        print(f'Wrong input {e}')
        return

    deque = Deque(deque_max_size)
    report = deque.execute_commands_and_generate_report(commands)

    print('\n'.join(report))


if __name__ == "__main__":
    main()
