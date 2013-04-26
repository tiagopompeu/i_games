"""
############################################################
Quarto - Peca
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
from peca import Peca

class TestPeca(unittest.TestCase):

    def setUp(self):
        self.peca = Peca(self,15)

    def test_local(self):
        # ve se a peca esta no local
        self.assertEqual(self.peca.local, self)
    def test_combina(self):
        # ve se a peca combina com outras
        self.assertTrue(self.peca.combina([Peca(self,7)]))

if __name__ == '__main__':
    unittest.main()
