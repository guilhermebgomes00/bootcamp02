import pytest
from src.app import ControladorMedicamentos


def test_adicionar_medicamento_sucesso():
    controlador = ControladorMedicamentos()
    resultado = controlador.adicionar_medicamento("Dipirona", "500mg", "08:00", "2x ao dia")
    assert len(controlador.listar_medicamentos()) == 1
    assert "sucesso" in resultado


def test_adicionar_medicamento_erro_campos_vazios():
    controlador = ControladorMedicamentos()
    with pytest.raises(ValueError):
        controlador.adicionar_medicamento("", "500mg", "08:00", "2x ao dia")


def test_adicionar_medicamento_erro_horario_invalido():
    controlador = ControladorMedicamentos()
    with pytest.raises(ValueError):
        controlador.adicionar_medicamento("Dipirona", "500mg", "25:00", "2x ao dia")


def test_marcar_medicamento_como_tomado():
    controlador = ControladorMedicamentos()
    controlador.adicionar_medicamento("Dipirona", "500mg", "08:00", "2x ao dia")
    resultado = controlador.marcar_como_tomado(0)
    assert resultado is True
    assert controlador.listar_medicamentos()[0]["tomado_hoje"] is True


def test_desmarcar_medicamento():
    controlador = ControladorMedicamentos()
    controlador.adicionar_medicamento("Dipirona", "500mg", "08:00", "2x ao dia")
    controlador.marcar_como_tomado(0)
    resultado = controlador.desmarcar_medicamento(0)
    assert resultado is True
    assert controlador.listar_medicamentos()[0]["tomado_hoje"] is False


def test_remover_medicamento():
    controlador = ControladorMedicamentos()
    controlador.adicionar_medicamento("Dipirona", "500mg", "08:00", "2x ao dia")
    resultado = controlador.remover_medicamento(0)
    assert len(controlador.listar_medicamentos()) == 0
    assert "removido" in resultado


def test_listar_medicamentos_vazio():
    controlador = ControladorMedicamentos()
    assert controlador.listar_medicamentos() == []


def test_resetar_dia():
    controlador = ControladorMedicamentos()
    controlador.adicionar_medicamento("Dipirona", "500mg", "08:00", "2x ao dia")
    controlador.adicionar_medicamento("Ibuprofeno", "200mg", "14:00", "3x ao dia")
    controlador.marcar_como_tomado(0)
    controlador.marcar_como_tomado(1)
    
    controlador.resetar_dia()
    
    for med in controlador.listar_medicamentos():
        assert med["tomado_hoje"] is False
