# Weighted Set Cover Problem

## Projeto e Análise de Algoritmos

Este repositório contém o código-fonte e informações relacionadas ao trabalho prático da disciplina "Projeto e Análise de Algoritmos". O foco do trabalho é o estudo do problema "Weighted Set Cover".

### Estrutura do Projeto

```bash
|-- src
| |-- init.py
| |-- algorithms
| |-- brute_force.py
| |-- cost_scaling.py
| |-- greedy.py
| |-- test_set.py
```

- O arquivo `__init__.py` é o ponto de entrada do programa principal em Python.
- A pasta `algorithms` contém implementações de diferentes algoritmos relacionados ao problema "Weighted Set Cover":
  - `brute_force.py`: Implementação do algoritmo de força bruta para resolver o problema do set cover.
  - `cost_scaling.py`: Implementação do algoritmo de cost scaling para resolver o problema do set cover.
  - `greedy.py`: Implementação do algoritmo guloso para resolver o problema do set cover.
  - `test_set.py`: Conjunto de testes para os algoritmos mencionados acima.

 Executando o Programa

Para executar o programa, você pode utilizar o arquivo `__init__.py` como ponto de entrada. Certifique-se de ter um ambiente Python configurado corretamente.

```bash
python src/__init__.py
```

### Algoritmos Disponíveis
Brute Force: O algoritmo de força bruta percorre todas as combinações possíveis para encontrar a solução ótima.
Cost Scaling: O algoritmo de cost scaling é uma abordagem específica para o problema do set cover que utiliza uma técnica de escala de custos.
Greedy: O algoritmo guloso constrói a solução passo a passo, fazendo escolhas locais que parecem ser as melhores no momento.

### Testes
O arquivo test_set.py contém um conjunto abrangente de testes para avaliar o desempenho e a precisão dos algoritmos implementados.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, correções ou adicionar novos recursos ao projeto.

Autores
- Geovana Vidal Moreira
- Lincoln Correa Figueiredo Cruz
