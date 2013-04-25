"""
############################################################
Quarto - Tabuleiro
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
import unittest
from tabuleiro import Tabuleiro

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.tabuleiro = Tabuleiro()

    def test_criar(self):
        # cria um tabuleiro
        self.tabuleiro.cria()
        self.assertEqual(len(self.tabuleiro.casas), 16)

if __name__ == '__main__':
    unittest.main()


