# Sistema de Biblioteca

**Católica SC – Curso de Engenharia de Software**  
**Disciplina:** Teste de Software  
**Semestre:** 2025/2  
**Projeto:** Sistema de Biblioteca  
**Equipe:** Amanda Zimermann, Camila Lorenzetti, Camila Teixeira, Laura Donath e Luana Melchioretto  

---

## Introdução

O presente projeto tem como objetivo o desenvolvimento de um *Sistema de Biblioteca* 
com suporte a *empréstimo de livros, devoluções, cálculo de multas e envio de notificações por e-mail*.  
O código é modular, extensível e totalmente coberto por testes automatizados.

---

## Objetivos de Aprendizagem

* Simular as operações de uma biblioteca digital:
  - Cadastro e controle de *usuários, **livros* e *empréstimos*.
  - Cálculo de *multas* para devoluções em atraso.
  - Emissão de *faturas* e envio de *notificações por e-mail*.
* Servir como exemplo de:
  - *Boas práticas de design orientado a objetos*.
  - *Testes automatizados com Pytest*.
  - *Integração Contínua (CI)* via GitHub Actions.


---

## Estrutura do Projeto


```plaintext
python/
├── src/
│   └── biblioteca/
│       ├── modelos.py              # Define entidades: Livro, Usuário, Empréstimo
│       ├── repositorio.py          # Repositório em memória para persistência
│       ├── servico.py              # Lógica principal: empréstimos, devoluções, multas
│       ├── fatura_service.py       # Geração de faturas por atraso
│       ├── email_service.py        # Simula envio de notificações por e-mail
│       ├── relogio.py              # Abstração para controle de datas (testabilidade)
│       └── __init__.py
├── tests/                          # Testes unitários e de integração
│   ├── test_emprestimo.py
│   ├── test_devolucao_email_multa.py
│   ├── test_fatura.py
│   ├── test_modelos_repositorio.py
│   └── ...
├── requirements.txt
└── pytest.ini
```



---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.11+  
- **Framework de Teste:** Pytest  
- **Cobertura:** Coverage.py  
- **Integração Contínua:** GitHub Actions  

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

## Regras de Negócio

### Empréstimos
- Um *usuário* pode pegar livros emprestados até seu *limite máximo*.
- Um *livro* só pode ser emprestado se estiver *disponível*.
- Ao emprestar:
  - O livro passa a ter disponivel = False.
  - É criado um registro de Emprestimo com a data atual.
- O prazo padrão de devolução é de *7 dias*.

### Devoluções
- O usuário deve devolver o livro dentro do prazo.
- Ao devolver:
  - O livro volta a ficar disponível.
  - Se houver atraso, é calculada uma *multa*.

### Multas
- Multa diária padrão: *R$ 2,00 por dia de atraso*.
- Multa calculada em servico.calcular_multa().
- O cálculo é feito com base na diferença entre data_devolucao e data_emprestimo.

### Faturas e E-mails
- O módulo fatura_service.py gera uma *fatura* com o valor total devido.
- O módulo email_service.py envia um *e-mail automático* ao usuário:
  - Aviso de devolução.
  - Notificação de multa (se aplicável).

---

## Componentes Técnicos

| Componente | Responsabilidade Principal |
|-------------|-----------------------------|
| modelos.py | Define classes Livro, Usuario, Emprestimo, Fatura. |
| repositorio.py | Armazena entidades em memória (pode ser substituído por banco de dados). |
| servico.py | Implementa regras de negócio: empréstimo, devolução e cálculo de multa. |
| email_service.py | Envia notificações simuladas. |
| fatura_service.py | Gera faturas baseadas em atrasos. |
| relogio.py | Fornece abstração para data atual (facilita testes determinísticos). |

---

## Testes Automatizados

Os testes cobrem *todas as regras de negócio* do sistema.

### Estrutura de Testes
- *Unitários*: Validam comportamento isolado (empréstimo, multa, e-mail).
- *Integração*: Simulam fluxos completos de empréstimo → devolução → fatura.
- *Performance e Exceções*: Testam limites e validação de erros.

### Framework
- [Pytest](https://docs.pytest.org/)
- Configuração: pytest.ini
- Execução:
  bash
  pytest -v
    

### Cobertura

A suíte de testes cobre praticamente 100% dos módulos principais (servico.py, fatura_service.py, repositorio.py, etc.), 
conforme indicado pelo uso intensivo de asserts e mocks nos testes.

---
## Integração Contínua (CI)

O projeto utiliza GitHub Actions para CI/CD automatizado:

- Local do workflow: .github/workflows/ci.yml
- Ações executadas:
    1. Instalação do Python e dependências (requirements.txt)
    2. Execução da suíte de testes com Pytest     
    3. Geração de relatório de cobertura
    4. (Opcional) Upload para Codecov ou similar

---

## Instalação e Execução
### Requisitos
- Python 3.11+
- pip e venv

### Passos
basch
cd python
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
pytest -v
`
<img width="834" height="886" alt="image" src="https://github.com/user-attachments/assets/d9617c71-a0d3-432b-812e-d594d9244eda" />



## Conclusão

O *Sistema de Biblioteca* alcançou plena cobertura funcional e aderência aos critérios de qualidade propostos, 
demonstrando a importância das boas práticas de teste, automação e TDD no ciclo de desenvolvimento de software.

---

**Católica SC – Engenharia de Software – 2025/2**  
*Trabalho Acadêmico de Teste de Software*




