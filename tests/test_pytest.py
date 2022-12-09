
'''
# o nome da pasta TEM QUE SER "tests" os nomes dos arquivos tem que
começar com "test_"
# caso queira ver exatamente o ponto use o termo "pytest -v"


O teste é formado por 3 etapas(GWT - AAA):

- Given - Dado
- Whnrn - Quando
- Then  - Então

- Arange
- Act
- Assert
====================

NOTA: toda vez que tiver um teste e seu erro NÂO for um "assert error"
siginifica que a estrutura do codigo está errada!

">" quando tem esse sinal ele indica onde está localizado o erro
"F" falhou
"x" falha esperada
"X" falha esperada, mas não falhou
"s" pulou (skiped)

pytest
-v      Mostra o nome dos testes executados
-s      Mostra as saídas no console
-k      "nome_dos_testes": filtra resultados
-x      Saida rápida

--pdb   Para debugar quando falhar

-m      Mostra os marks EX: pytest -v -m smoke
-rs     Mostra os textos contido nos skips

'''
from pytest import mark
from codigo.jogo import brincadeira


def test_para_saber_se_o_pytest_esta_funcionando():
    assert True


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1  # Dado
    esperado = 1  # Dado
    resultado = brincadeira(1)  # Quando
    assert resultado == esperado  # Então

    # Versão pequena
    assert brincadeira(1) == 1


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'


# @mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_guiabada():
    assert brincadeira(5) == 'goiabada'


# @mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_guiabada():
    assert brincadeira(10) == 'goiabada'


@mark.smoke
def test_quando_brincadeira_receber_20_entao_deve_retornar_guiabada():
    assert brincadeira(20) == 'goiabada'


@mark.skip(reason='pq ainda não implementei')
def test_quando_brincadeira_receber_menos_1_entao_deve_retornar_None():
    assert brincadeira(-1) == 'goiabada'


@mark.parametrizado1
@mark.parametrize('entrada', [5, 10, 20, 25, 35])
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == 'goiabada'


@mark.parametrizado2
@mark.parametrize('entrada, esperado', [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')])
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada, esperado):
    assert brincadeira(entrada) == esperado
