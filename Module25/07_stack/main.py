
class Stack:

    def __init__(self):
        self.stack = []

    def add_item(self, item):
        self.stack.append(item)

    def delete_last_item(self):
        self.stack.pop()


my_stack = Stack()
my_stack.add_item(5)
my_stack.add_item(8)
my_stack.add_item(12)
my_stack.delete_last_item()
my_stack.add_item(15)
my_stack.add_item(18)
my_stack.delete_last_item()
print(my_stack.stack)


class TaskManager:

    def __init__(self):
        self.my_dict = dict()

    def new_task(self, string, number):
        if isinstance(string , str) and isinstance(number, int):
            value = string
            key = number
            if key not in self.my_dict:
                self.my_dict[key] = [value]
            else:
                self.my_dict[key].append(value)

    def del_item(self, string, number):
        if isinstance(string, str) and isinstance(number, int):
            for i_value in self.my_dict[number]:
                if i_value == string:
                    index = self.my_dict[number].index(i_value)
                    self.my_dict[number].pop(index)

    def del_duplicate(self):
        for key in self.my_dict:
            set(self.my_dict[key])

    def __str__(self):
        print(f'\nРезультат:')
        result = ''
        new_order = sorted(self.my_dict.keys())
        for i in new_order:
            result += f'{i} {"; ".join(value for value in self.my_dict[i])}\n'

        return result


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.new_task('погладить кота', 5)
print(manager)
manager.del_item('помыть посуду', 4)
print(manager)
