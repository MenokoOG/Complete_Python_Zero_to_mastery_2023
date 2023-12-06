"""Testing lesson, Menoko OG, 11-2023"""


def do_stuff(num = 0):
    try:
        if num:
            return int(num) + 5
        else:
            return "_Please enter number_"
    except ValueError as err:
        return err
