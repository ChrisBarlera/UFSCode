# Tratamento de Exceções
**Exceção** (`Exception`) é um evento de erro que ocorre durante a execução do programa e que quebra o fluxo normal do programa

## Estrutura
Sobre como traduzir o conceito para Python

### `try`
O que vem no bloco de `try` é uma tentativa

### `except`
Podemos "capturar" o erro e tratar aqui neste bloco `except`.
Podemos ter mais de um bloco `except` no mesmo `try`, cada um para um tipo (classe) diferente de `Exception`

### `else`
Caso não tenha exceção na execução de `try`, esse bloco `else` é executado.

### `finally`
Bloco sempre executado, independente se teve erro ou não, ou ainda se já foi tratado.

Estando no bloco `try` podemos ainda chegar direto e intencionalmente no bloco `except` com o uso da cláusula `raise`

### `raise`
Usamos para "levantar" uma exceção que sabemos que acontecerá no fluxo.