# -*- coding: utf-8 -*-

import json


class ACL():
    """
    Access Control List (ACL)
    """
    def check(self, ip):
        """
        проверка наличия разрешения для доступа для указанного IP
        ! если IP в списке не найдено, значит доступ для IP запрещен
        """
        acl = self._load_file()
        # проверяем наличия ключа в массиве
        # если ключа нет, то завершаем функцию с запретом
        try:
            acl[ip]
        except KeyError:
            return False

        # если для указанного ip определено значение allow возвращаем значение True,
        # если deny, то False
        if acl[ip] == "allow":
            return True
        else:
            return False

    def _load_file(self):
        """
        считывает json-файл со списком разрешенных или запрещенных ip
        """
        with open('acl.json') as acl_file:
            acl = json.load(acl_file)

        return acl