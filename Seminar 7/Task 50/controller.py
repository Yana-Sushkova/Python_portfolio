import view
import operation
import process
import log


def button_click():
    some_str = view.inp()
    some_tuple = process.processing(some_str)
    a, b, symbol = some_tuple[0], some_tuple[1], some_tuple[2]
    if symbol == "+":
        result= operation.summa(a,b)
    elif symbol == "-":
        result= operation.diff(a,b)
    elif symbol == "*":
        result= operation.mult(a,b)   
    else:
        result= operation.div(a,b)
    view.view_data(result)
    log.log_cash(some_str, result)
   