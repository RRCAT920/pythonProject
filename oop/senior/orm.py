# -*- coding: utf-8 -*-
class Field:

    def __init__(self, name: str, column_type: str):
        """

        :param name: 字段名
        :param column_type: 列类型
        """
        self.name = name
        self.column_type = column_type

    def __str__(self):
        """

        :return: 类名:字段名
        """
        return f'<{self.__class__.__name__}:{self.name}>'


class IntField(Field):

    def __init__(self, name: str):
        super().__init__(name, 'bigint')


class StringField(Field):

    def __init__(self, name: str):
        super().__init__(name, 'varchar(100)')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name != 'Model':
            print(f'Found model: {name}')
            mappings = dict()
            for key, val in attrs.items():
                if isinstance(val, Field):
                    print(f'Found mapping: {key} ===> {val}')
                    mappings[key] = val

            # 避免实例属性覆盖类属性
            for key in mappings:
                attrs.pop(key)

            attrs['__mappings__'] = mappings
            attrs['__table__'] = name.lower()

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' object has no attribute '{key}'")

    def __setattr__(self, key, val):
        self[key] = val

    def save(self) -> None:
        fields = []
        params = []
        args = []

        for key, val in self.__mappings__.items():
            fields.append(val.name)
            params.append('?')
            args.append(getattr(self, key))

        sql = f"insert into {self.__table__}({','.join(fields)}) values({','.join(params)})"
        print(f'SQL: {sql}')
        print(f'ARGS: {args}')