"""
############################################################
Quarto - Casa
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
class Casa:
    """Casa onde se coloca pecas"""
    def __init__(self, gui, local, name):
        "local onde nasce, o nome da casa"
        self.gui, self.local, self.name = gui, local, name
        self.sai(None)
    def _casa_vazia(self, peca):
        "a peca escolhida move para esta casa"
        self.peca = peca
        self.peca.move(self)
        self._estado_corrente = lambda *a: None
    def escolhida(self, peca):
        "a peca escolhida age segundo o estado corrente"
        self._estado_corrente(peca)
    def sai(self, peca):
        "a peca escolhida sai daqui"
        self.peca = None
        self._estado_corrente = self._casa_vazia
