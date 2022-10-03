from interface import get_choice, get_dict, get_element, get_result
from add_record import add_record
from search_record import get_search
from logg import get_log


def push_rocked():
    operator_num = get_choice()
    if operator_num == 1:
        new_dict = get_dict()
        add_record(new_dict)
        get_log(operator_num)
        get_result()
    elif operator_num == 2:
        new_dict = {}
        get_element()
        get_search(new_dict)
        get_log(operator_num)
        get_result()


