def find_number(start, end):
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            print(i)


def generate_square_dict(value):
    dict1 = {}
    for i in range(1, value + 1):
        dict1[i] = i * i
    print(dict1)


def convert_input_to_list_and_tuple(value):
    print(value.split(","), (value.split(",")))


if __name__ == "__main__":
    find_number(100, 200)
    generate_square_dict(8)
    convert_input_to_list_and_tuple("3,6,5,3,2,8")
