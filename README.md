+# Controlador de Medicamentos para Idosos

## Descrição do Problema

Idosos frequentemente enfrentam dificuldades em manter o controle de seus medicamentos, horários de ingestão e dosagens. A falta de um sistema organizado pode resultar em esquecimento de doses, ingestão duplicada ou não conformidade com o tratamento prescrito, comprometendo a saúde e o bem-estar.

## Proposta da Solução

O Controlador de Medicamentos para Idosos é uma aplicação de interface de linha de comando (CLI) que permite ao usuário gerenciar seus medicamentos de forma estruturada e intuitiva. A solução foca na simplicidade e na eficácia, permitindo o registro de medicamentos, definição de horários e dosagens, além de controle de ingestão diária.

## Público-Alvo

Idosos, cuidadores, familiares e profissionais de saúde que necessitam de uma ferramenta leve e direta para organizar e acompanhar a medicação diária de forma segura e confiável.

## Funcionalidades Principais

* Adição de medicamentos com especificação de nome, dosagem, horário e frequência de ingestão.
* Listagem completa de todos os medicamentos cadastrados com seus respectivos status.
* Marcação de medicamentos como tomados para acompanhamento diário.
* Desmarcação de medicamentos caso tenha havido erro no registro.
* Remoção de medicamentos da lista de controle.
* Visualização de próximos horários de medicamentos a serem tomados.
* Visualização de medicamentos que ficaram atrasados.
* Resetar o dia para iniciar novo ciclo de controle.
* Validação de dados para garantir que horários sejam válidos.
* Registro de data e hora da última ingestão de cada medicamento.

## Tecnologias Utilizadas

* Linguagem de Programação: Python 3.11+
* Framework de Testes: Pytest
* Análise Estática (Linting): Ruff
* Integração Contínua (CI): GitHub Actions

## Instruções de Instalação

1. Realize o clone do repositório:
   ```bash
   git clone https:https://github.com/guilhermebgomes00/bootcamp02.git
   cd medicamentos_idosos
   ```
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: .\venv\Scripts\activate
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Instruções de Execução

Para iniciar a aplicação interativa, utilize o comando:

```bash
python src/app.py
```

## Instruções para Rodar os Testes

Para executar a suite de testes automatizados, utilize o comando:

```bash
python -m pytest
```

## Instruções para Rodar o Lint

Para executar a análise estática de código e verificar a qualidade do mesmo, utilize o comando:

```bash
ruff check src/ tests/
```

## Exemplo de Uso

```
==================================================
   CONTROLE DE MEDICAMENTOS PARA IDOSOS
==================================================
1. Adicionar Medicamento
2. Listar Medicamentos
3. Marcar Medicamento como Tomado
4. Desmarcar Medicamento
5. Remover Medicamento
6. Ver Próximos Horários
7. Ver Medicamentos Atrasados
8. Resetar Dia
9. Sair

Escolha uma opção: 1
Nome do medicamento: Dipirona
Dosagem (ex: 500mg, 1 comprimido): 500mg
Horário (HH:MM, ex: 08:00): 08:00
Frequência (ex: 2x ao dia, 3x ao dia): 2x ao dia
✅ Medicamento 'Dipirona' adicionado com sucesso!
```

## Versão Atual

1.0.0

## Autor

Guilherme Oliveira 

## Link do Repositório Público

https://github.com/guilhermebgomes00/bootcamp02.git
