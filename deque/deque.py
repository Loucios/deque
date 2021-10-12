class Deque:
    def __init__(self, n: int) -> None:
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def is_empty(self) -> bool:
        return self.queue_size == 0

    def is_full(self) -> bool:
        return self.queue_size == self.max_size

    def push_back(self, value: int) -> bool:
        if self.is_full():
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.queue_size += 1
        return True

    def push_front(self, value: int) -> bool:
        if self.is_full():
            return False

        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.queue_size += 1
        return True

    def pop_back(self) -> str:
        if self.is_empty():
            return 'error'

        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.queue_size -= 1
        return str(value)

    def pop_front(self) -> str:
        if self.is_empty():
            return 'error'

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return str(value)

    def execute_commands_and_generate_report(
        self, commands: 'list[str]'
    ) -> 'list[str]':

        report = []

        for command in commands:
            if 'pop_front' in command:
                report.append(self.pop_front())
            if 'pop_back' in command:
                report.append(self.pop_back())
            if 'push_front' in command and not self.push_front(
                int(command[11:])
            ):
                report.append('error')
            if 'push_back' in command and not self.push_back(
                int(command[10:])
            ):
                report.append('error')

        return report
