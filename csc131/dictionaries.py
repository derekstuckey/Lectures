import string


def get_personal_data() -> dict:
    """
    :return: Returns a dictionary of personal information
    """
    personal_data = {"name": "Derek", "a_role": "Student"}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)         # will always give back a blank dict
    initialized_dict = dict([('name', 'Derek'), ('a_role', 'joker')])       # dict constructor
    print(initialized_dict)
    simple_init_dict = dict(name='Derek', a_role='student')                 # dict constructor
    print(simple_init_dict)
    simple_init_dict['a_role'] = "joker" # changes value associated with key
    print(simple_init_dict)
    my_comprehension = {x: x**2 for x in range(5)}      # dict comprehension
    print(my_comprehension)

    s = "little,".translate({ord(i): None for i in string.punctuation})         # print our the string withought the punctuation
    print(s)

    return 0


if __name__ == '__main__':
    main()
