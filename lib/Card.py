from re import search


class FindsCard:
    "Busqueda de cards en un text"
    @classmethod
    def __init__(self):
        pass
    
    @classmethod
    def finds_cards(self, Texto = None):
        self.texto  = Texto
        self.cadena = r'(\d{15,16})+?[^0-9]+?(\d{1,2})[\D]*?(\d{2,4})[^0-9]+?(\d{3,4})'
        try:
            self.cardinfo = search(
                self.cadena, 
                self.texto
            )

            self.cc, self.mes, self.ano, self.cvv = self.cardinfo.groups()
            self.cc = self.cc.replace("-", "").replace(" ", "")

            return [
                self.cc, 
                self.mes, 
                self.ano, 
                self.cvv,
                ]
        
        except:
            ...