
from sys import maxsize
class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    #как будет выглядеть объект при выводе : идентификатор и имя
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    #сравнение объектов логически по именам безусловно и идентификаторам, если они определены
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # вычислять по группе ключ используемой для сравнения

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize  # максим. целое число
