#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    element = []
    result_count = 0
    for i in range(0, list_length):
        try:
            result_count = my_list_1[i] / my_list_2[i]
        except TypeError:
            result_count = 0
            print("wrong type")
        except ZeroDivisionError:
            result_count = 0
            print("division by 0")
        except IndexError:
            result_count = 0
            print("out of range")
        finally:
            pass
        element.append(result_count)
    return element
