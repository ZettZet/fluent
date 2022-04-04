from fluent import fluent


@fluent()
class Meta:
    locale: str = None
    port: int

    #  You may want to add typehint (but it will also mark as a warning)
    def set_locale(self, locale: str) -> 'Meta':
        self.locale = locale

    #  All return statements will be ignored
    #  (but IDE still thinks, that method returns string, i.e. it will suggest str hints)
    def set_port(self, port: int):
        self.port = port
        return 'ignored'

    #  not affected
    def __inner_func(self):
        ...

    #  not affected
    def __str__(self):
        return f'{self.__class__.__name__}[{self.locale=}, {self.port=}]'


if __name__ == '__main__':
    meta = Meta().set_port(3).set_locale('RU')
    print(meta)  # Meta[self.locale='RU', self.port=3]
