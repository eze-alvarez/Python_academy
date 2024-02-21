# publicas => pueden ser leidos sin un getter - metodos
# _privadas => pueden ser leidos con un getter - atributos



class Auto():
    def desplazamiento(self):
        print('me desplazo en 4 ruedas')


class Moto():
    def desplazamiento(self):
        print('me desplazo en 2 ruedas')





class libro:
    def __init__(self, _editorial, _generoLiterario):
            self._editorial = _editorial
            self._generoLiterario = _generoLiterario


