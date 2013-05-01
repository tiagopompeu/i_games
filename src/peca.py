"""
############################################################
Quarto - peca
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
class Peca:
    """Peca do jogo"""
    def __init__(self, gui, local, name):
        "local onde nasce, o nome da peca"
        self.gui, self.local, self.name = gui, local, name
    def escolhida(self, peca=None):
        "a peca escolhida move para a casa da base"
        self.local.escolhida(self)
    def move(self, casa):
        "a peca escolhida move para esta casa"
        self.local.sai(self)
        self.local = casa
