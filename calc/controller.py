import view
import operation
import logger

def button_click():
    choice = view.get_choise()
    value_a = view.get_value()
    value_b = view.get_value()
    # if choice:
    #     value_a = complex(value_a)
    #     value_b = complex(value_b)
    oper = view.get_operator()
    func = operation.dict_ar[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)
    logger.get_log(operation, result)