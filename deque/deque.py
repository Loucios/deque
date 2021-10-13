class Deque:
    def __init__(self, n: int) -> None:
        self.queue, self.max_size = [None] * n, n
        self.head = self.tail = self.queue_size = 0

    @property
    def is_empty(self) -> bool:
        return self.queue_size == 0

    @property
    def is_full(self) -> bool:
        return self.queue_size == self.max_size

    def push_back(self, value: int) -> bool:
        if self.is_full:
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.queue_size += 1
        return True

    def push_front(self, value: int) -> bool:
        if self.is_full:
            return False

        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.queue_size += 1
        return True

    def pop_back(self) -> str:
        if self.is_empty:
            return 'error'

        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.queue_size -= 1
        return str(value)

    def pop_front(self) -> str:
        if self.is_empty:
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
        attribute_list = ['pop_front', 'pop_back', 'push_front', 'push_back']
        pop_list = ['pop_front', 'pop_back']
        push_list = ['push_front', 'push_back']

        for command in commands:
            for element in attribute_list:
                if element in command:
                    if element in pop_list:
                        attr = getattr(self, element)()
                        report.append(attr)
                    if element in push_list:
                        attr = getattr(self, element)(
                            int(command[len(element)+1:])
                        )
                        if not attr:
                            report.append('error')
        return report
