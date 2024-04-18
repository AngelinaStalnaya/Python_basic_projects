from collections import Counter


if __name__ == '__main__':
    def can_be_poly(string: str) -> bool:
        '''
        Функция определения возможности создания палиндрома из переданной в нее строки
        :param string: любая строка
        :return: bool (True или False)
        '''
        letters_count = Counter(string)
        result = list(filter(lambda num: num % 2 != 0, letters_count.values()))
        if len(result) == 1:
            return True
        return False

    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))

