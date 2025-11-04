# Exemplos do Curso Fundamentos de Python 2

Este repositório contém exemplos práticos utilizados nas aulas do curso **Fundamentos de Python 2**. Os arquivos estão organizados por módulos e aulas, facilitando o acompanhamento dos conteúdos e experimentos.

## Estrutura

```
mod/
  aula1/
    arquivo1.2.4.py
    arquivo1.2.py
    ex_randrange.py
    ex_rand_examples.py
  aula2/
    ...
```

- Cada pasta representa uma aula do curso.
- Os arquivos Python trazem exemplos de conceitos fundamentais, como tipos, operadores, controle de fluxo, funções, módulos e geração de números aleatórios.

## Como executar os exemplos

1. Recomenda-se usar um ambiente virtual Python (venv):
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # se existir
   ```
2. Para rodar um exemplo:
   ```zsh
   python mod/aula1/ex_rand_examples.py
   ```
   Ou, se estiver usando o ambiente virtual:
   ```zsh
   .venv/bin/python mod/aula1/ex_rand_examples.py
   ```

## Exemplos de tópicos abordados

- Uso do módulo `random` para geração de números aleatórios
- Diferença entre `randrange`, `randint`, `random`, `choice`, `sample`, `shuffle`, `seed`
- Reprodutibilidade de resultados com `seed`
- Boas práticas para testes e experimentos

## Recomendações

- Sempre utilize `seed()` para garantir reprodutibilidade em testes.
- Para aplicações que exigem segurança, utilize o módulo `secrets` em vez de `random`.
- Consulte os comentários nos arquivos para explicações detalhadas.

---
