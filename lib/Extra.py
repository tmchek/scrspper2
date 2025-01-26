from random import choice,randint
from dataclasses import dataclass


@dataclass
class ExtraPoleador:
    'extra ccs basados en un bin[:6]'
    @classmethod
    def __init__(self, bin = None):
        self.bin = bin
        self.extrapole = list()
        
        
    'Metodo para generar los factores de extra'
    @classmethod
    def extra_cards(self):
        for _ in range(3):
            
            self.numbers =  "".join(choice("0123456789") for _ in range(6))
            self.mes     = randint(1, 12)
    
            if self.mes <= 9:
                self.mes = '0{}'.format(self.mes)
    
            self.year    = randint(2024, 2032)
            self.extra   = '{}{}xxxx|{}|{}|rnd'.format(
                self.bin,
                self.numbers,
                self.mes,
                self.year,
            )

            self.extrapole.append(self.extra)
        
        return ( self.extrapole )
