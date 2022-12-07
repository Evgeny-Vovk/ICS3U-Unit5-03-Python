# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit5-02.py File, learning functions with parameters in python.


def convert_to_mark(mark_as_level):

    match mark_as_level:
        case "4+":
            mark_as_grade = 97
        case "4":
            mark_as_grade = 90
        case "4-":
            mark_as_grade = 83
        case "3+":
            mark_as_grade = 78
        case "3":
            mark_as_grade = 74
        case "3-":
            mark_as_grade = 71
        case "2+":
            mark_as_grade = 68
        case "2":
            mark_as_grade = 64
        case "2-":
            mark_as_grade = 61
        case "1+":
            mark_as_grade = 58
        case "1":
            mark_as_grade = 54
        case "1-":
            mark_as_grade = 51
        case "R":
            mark_as_grade = 30
        case "NE":
            mark_as_grade = 0
        case _:
            mark_as_grade = -1
    return mark_as_grade


def main():

    mark_as_level = input("Enter the mark that you got as a level(4+, 3-, 2, R, NE): ")
    convert_to_mark(mark_as_level)

    mark_as_grade = convert_to_mark(mark_as_level)

    print("")
    if mark_as_grade <= 100 and mark_as_grade >= 0:
        print("You got a mark of {0}%.".format(mark_as_grade))
    else:
        print("Please input a valid mark.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
