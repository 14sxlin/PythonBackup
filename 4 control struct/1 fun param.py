if __name__ == '__main__':
    options = dict(option=True, go="Beijing")

    print(options)  # {'option': True, 'go': 'Beijing'}

    def print_op(**kwargs):
        print("{} {}".format("option",options["option"]))

    print_op(**options)
