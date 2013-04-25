"""
############################################################
Quarto - Principal - Base
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
class Quarto:
    """Base do jogo com tabuleiro e duas maos."""
    def __init__(self, gui):
        """Constroi as partes do Jogo. """
        self.build_base(gui)
        #self.build_tabuleiro(gui)
        #self.build_mao(gui)
        
    def build_base(self,gui):
        """docs here"""
        self.base = gui.svg.rect(x=10, y= 10, width=800, height=600, fill='green')
        gui <= self.base
    #: TODO - put all the rest

def main(gui):
  print('Quarto 0.1.0')
  quarto = Quarto(gui)


