# -*- coding: utf-8 -*-


class Global_dict:
    global _global_dict
    _global_dict = {}
    print('global初始化')

    @staticmethod
    def set_value(name, value):
        _global_dict[name] = value

    @staticmethod
    def get_value(name, defValue=''):
        try:
            return _global_dict[name]
        except KeyError:
            return defValue
