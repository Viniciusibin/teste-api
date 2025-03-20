# Teste Automatizado da API

Este repositório contém um teste automatizado para a API de cadastro de profissionais.

## Caso de Teste

### Objetivo
Verificar se a API de cadastro de profissionais retorna o status 201 e o profissional cadastrado.

### Pré-condição
- A API deve estar em execução.
- O endpoint `/profissionais` deve estar disponível.

### Procedimento de Teste
1. Enviar uma requisição POST para o endpoint `/profissionais` com os dados de um novo profissional.
2. Verificar o status da resposta.
3. Verificar se o corpo da resposta contém os dados do profissional cadastrado.

### Resultado Esperado

- Status da resposta: `201 Created`.
- Corpo da resposta: `{ "id": 1, "nome": "João Silva", "empresa": "Empresa A" }`.

### Resultado Obtido
- Status da resposta: `201`.
- Corpo da resposta: `{ "id": 1, "nome": "João Silva", "empresa": "Empresa A" }`.

### Pós-condição
O profissional cadastrado deve estar disponível no banco de dados.

## Como Executar o Teste

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/teste-automatizado-api.git
2. Acesse o diretório do projeto
   ```bash
      cd teste-automatizado-api

3. Instale as dependências necessárias:

   ```bash
      pip install requests

4. Execute o teste:

   ```bash
      python teste_profissionais.py


# Registro de Resultados
Execução do teste:


      ```bash
      PS C:\Users\Inteli\Documents\teste-api> python teste_profissionais.py
      Teste PASS: Status 201 recebido.
      Teste FAIL: Dados do profissional incorretos.


# Conclusão do Resultado do Teste

&nbsp;&nbsp;&nbsp;&nbsp; O teste automatizado para a API de cadastro de profissionais foi executado com os seguintes resultados:

- Status da Resposta:

   - Resultado Esperado: 201 Created

   - Resultado Obtido: 201

&nbsp;&nbsp;&nbsp;&nbsp; O status da resposta foi o esperado, indicando que o recurso foi criado com sucesso. Portanto, o teste de status PASS.

### Corpo da Resposta:

- Resultado Esperado: { "id": 1, "nome": "João Silva", "empresa": "Empresa A" }

- Resultado Obtido: Dados incorretos (não especificados no output fornecido)


&nbsp;&nbsp;&nbsp;&nbsp;O corpo da resposta não corresponde ao esperado, indicando que os dados do profissional retornados pela API estão incorretos. Portanto, o teste de dados FAIL.

### Análise

&nbsp;&nbsp;&nbsp;&nbsp; Status da Resposta: A API está funcionando corretamente em termos de status de resposta, retornando o código 201 que indica que o profissional foi cadastrado com sucesso.

&nbsp;&nbsp;&nbsp;&nbsp; Corpo da Resposta: Apesar do status correto, o corpo da resposta não contém os dados esperados. Isso pode indicar um problema na lógica de retorno da API, onde os dados enviados no payload não estão sendo retornados corretamente, ou há um erro na estrutura do JSON retornado.

### Conclusão

&nbsp;&nbsp;&nbsp;&nbsp; O teste parcialmente passou, com o status da resposta correto, mas falhou na validação dos dados retornados. É necessário investigar e corrigir a lógica da API para garantir que os dados do profissional cadastrado sejam retornados corretamente. Após as correções, o teste deve ser executado novamente para garantir que todas as condições sejam atendidas.

