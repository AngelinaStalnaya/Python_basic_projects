class MyDict(dict):

    def __init__(self, dictionary):
        super().__init__()
        self.dict = dictionary

    def get(self, key):
        if isinstance(key, str):
            key = key.title()
        if key in self.dict:
            return self.dict[key]
        else:
            return 0


some_dict = {'Кошка': '-и, ж. 1. Хищное млекопитающее сем. кошачьих.',
             'Собака': '-и, ж. 1. Домашнее животное сем. псовых. ',
             'Петух': '-а, м. 1. Самец домашних кур и нек-рых куриных.',
             'Утка': '-и, ас. 1. Водоплавающая птица с широким клювом, короткой шеей и короткими, широко поставленными лапами.',
             'Синица': '-ы, ж. Небольшая пестрая птица отряда воробьиных.',
             'Воробей': '-бья, м. Маленькая птичка с серо-черным оперением.'}


my_dict = MyDict(some_dict)
print(my_dict.get('собака'))
print(my_dict.get('Воробей'))
print(my_dict.get(5))