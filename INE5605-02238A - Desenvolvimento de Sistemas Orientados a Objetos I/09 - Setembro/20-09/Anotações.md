# Relações entre objetos (de classes)
Como os objetos podem se relacionar.

## Generalização
É o caso das subclasses.
- **Ex:** Aluno subclasse de Pessoa, ou ainda, Pessoa generaliza Aluno. 
  - Seta aponta de Aluno pra Pessoa

## Composição
É a mais forte relação em que um objeto tem atributo que é objeto de outra classe. Aqui a classe A tem objeto de B e esse objeto é exclusivo, nasce e morre ali. 
- **Ex:** Carro contém Roda, ou ainda, Roda é propriedade *exclusiva* de Carro. Roda nasce e morre no Carro. 
  - Seta aponta de Carro pra Roda

## Agregação
Muito semelhante à composição porém um pouco mais fraca. Aqui os objetos não morrem junto, eles são compartilháveis.
- **Ex:** classe Disciplina com atributo que é array de objetos Alunos. Alunos não morrem junto com a Disciplina. 
  - Seta aponta de Disciplina pra Aluno

## Associação
Também é do tipo "um atributo numa classe" mas conceitualmente se diferencia das outras pois é pra ser a relação mais fraca deste tipo.

## Dependência
Relação mais fraca entre objetos, por vezes até nem representada em diagramas de clase UML. Aqui temos uma relacionamento de utilização, isto é, classe A usa algum método de classe B.