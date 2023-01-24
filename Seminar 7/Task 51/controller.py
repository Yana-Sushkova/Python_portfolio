import view
import process
import log


def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'поиск':  # Метод lower () — это строковый метод, который возвращает новую строку полностью в нижнем регистре
        sern = view.inp_import()
        res_search = process.search(sern)
        # print(res_search)
        # Функция isinstance() в Python используется для проверки, является ли объект экземпляром указанного класса или нет.
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
        view.view_export()
    log.log_cash(rezhim)
