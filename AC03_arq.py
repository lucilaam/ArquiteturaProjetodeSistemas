from unittest import TestCase, main
import abc
import unittest

class Calculadora (object):
    def calcular (self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica ()
        operacao= operacaoFabrica.CriarOperacao(operador)
        if (operacao == None):
            return 0
        else:
            return operacao.executar(valor1, valor2)

class OperacaoFabrica (object):
    def CriarOperacao(self, operador):
        if (operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return Subtracao()
        elif (operador == "divisao"):
            return Divisao()
        elif (operador == "multiplicacao"):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2 


class testa(TestCase):
    def teste_soma(self):
        self.assertEqual (Calculadora().calcular(7,1, "soma"), 8)
        print("Soma ok!")

    def teste_divisao(self):
        self.assertEqual (Calculadora().calcular(2,2, "divisao"), 1)
        print("Divisao ok!")

    def teste_subtracao(self):
        self.assertEqual (Calculadora().calcular(100,10, "subtracao"), 90)
        print("Subtracao ok!")
  
    def teste_multiplicacao(self):
        self.assertEqual (Calculadora().calcular(10,5, "multiplicacao"), 50)
        print("Multiplicacao ok!")

    
    
if __name__ == '__main__':
    main()
