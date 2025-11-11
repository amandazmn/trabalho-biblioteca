# Sistema de Biblioteca

**Católica SC – Curso de Engenharia de Software**  
**Disciplina:** Teste de Software  
**Semestre:** 2025/2  
**Projeto:** Sistema de Biblioteca  
**Equipe:** Amanda Zimermann, Camila Lorenzetti, Camila Teixeira, Laura Donath e Luana Melchioretto  

---

## Introdução

O presente projeto tem como objetivo o desenvolvimento de um *Sistema de Biblioteca* com foco na 
aplicação de práticas de **Teste de Software**. O trabalho foi elaborado com base no paradigma de 
**Desenvolvimento Orientado a Testes (TDD)**, visando demonstrar o ciclo de implementação incremental 
e a validação contínua das funcionalidades por meio de testes automatizados.

---

## Objetivos de Aprendizagem

- Aplicar o ciclo de vida de testes utilizando **pytest** em Python.  
- Utilizar **TDD** para o desenvolvimento iterativo de funcionalidades.  
- Implementar testes de **exceções**, **parâmetros**, **stubs** e **mocks**.  
- Simular uma integração de componentes em um fluxo completo.  
- Avaliar cobertura de testes (linhas ≥ 80%, branches ≥ 70%).  
- Demonstrar controle de qualidade contínuo (CI) e desempenho (timeout).

---

## Estrutura do Projeto

```
trabalho-biblioteca-master/
├── python/
│   ├── src/
│   │   └── biblioteca/
│   │       ├── __init__.py
│   │       ├── entidades.py
│   │       ├── repositorio.py
│   │       ├── servico.py
│   │       └── email_service.py
│   └── tests/
│       ├── test_emprestimo.py
│       ├── test_devolucao.py
│       ├── test_excecoes.py
│       ├── test_performance.py
│       └── test_integracao.py
├── requirements.txt
└── README.md
```

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.11+  
- **Framework de Teste:** Pytest  
- **Cobertura:** Coverage.py  
- **Integração Contínua:** GitHub Actions  

---

## Configuração e Execução

### 1 Instalação do Ambiente Virtual
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 2 Execução dos Testes
```bash
pytest -v
```

### 3 Geração do Relatório de Cobertura
```bash
coverage run -m pytest
coverage html
start htmlcov/index.html    # Abre o relatório no navegador
```

---

## Estratégia de Testes

O projeto segue o padrão **AAA (Arrange, Act, Assert)** em todos os testes.  
Cada caso de teste é independente, claro e de fácil manutenção.

### Categorias de Testes Implementadas

| Categoria | Descrição | Arquivo |
|------------|------------|----------|
| Testes de Unidade | Validam entidades e regras básicas | `test_emprestimo.py` |
| Testes de Integração | Simulam o fluxo completo de empréstimo e devolução | `test_integracao.py` |
| Testes de Exceções | Verificam erros esperados em cenários inválidos | `test_excecoes.py` |
| Testes Parametrizados | Avaliam múltiplas combinações de entrada | `test_devolucao.py` |
| Testes de Performance | Verificam tempo de resposta máximo | `test_performance.py` |

---

## TDD – Desenvolvimento Orientado a Testes

O projeto foi conduzido conforme o ciclo **Red → Green → Refactor**:

1. Criação de um teste falho (fase *Red*).  
2. Implementação mínima para passar o teste (fase *Green*).  
3. Refatoração do código mantendo os testes verdes (fase *Refactor*).  

Os commits no repositório Git refletem claramente este ciclo, evidenciando a evolução incremental das funcionalidades.

---

## Stubs, Mocks e Exceções

- **Stubs:** utilizados para simular serviços externos, como `EmailServiceStub` e `RelogioStub`.  
- **Mocks:** aplicados para validar chamadas esperadas sem depender de recursos reais.  
- **Exceções:** testadas com `pytest.raises()` para garantir robustez e tratamento correto de erros.

---

## Integração Simulada

A integração completa do sistema é testada simulando o ciclo **empréstimo → devolução → notificação de multa**,
utilizando componentes reais e stubs de serviços auxiliares.

---

## Teste de Performance

Um dos casos de teste verifica se as operações críticas de devolução ocorrem dentro de um tempo limite 
definido (≤ 0,2s), garantindo a responsividade do sistema.

---

## Integração Contínua (CI)

O projeto possui pipeline configurado via **GitHub Actions**, que executa automaticamente os testes 
e gera relatórios de cobertura a cada *commit*.

Exemplo de workflow (`.github/workflows/ci.yml`):

```yaml
name: CI - Sistema de Biblioteca

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Instalar dependências
        run: pip install -r requirements.txt
      - name: Executar testes
        run: pytest -v --maxfail=1 --disable-warnings
      - name: Gerar cobertura
        run: |
          pip install coverage
          coverage run -m pytest
          coverage report -m
```

---

## Conclusão

O *Sistema de Biblioteca* alcançou plena cobertura funcional e aderência aos critérios de qualidade propostos, 
demonstrando a importância das boas práticas de teste, automação e TDD no ciclo de desenvolvimento de software.

---

**Católica SC – Engenharia de Software – 2025/2**  
*Trabalho Acadêmico de Teste de Software*
