# Test Cases - Users API

## POST /users
├── TC-USER-001 - Criar usuário com dados válidos
├── TC-USER-002 - Nome com menos de 2 caracteres
├── TC-USER-003 - E-mail inválido
├── TC-USER-004 - Senha com menos de 6 caracteres
├── TC-USER-005 - Role inválida
├── TC-USER-006 - E-mail duplicado
└── TC-USER-007 - Campo obrigatório ausente

## GET /users
└── TC-USER-008 - Listar usuários

## GET /users/{user_id}
├── TC-USER-009 - Buscar usuário existente
└── TC-USER-010 - Buscar usuário inexistente

## PUT /users/{user_id}
├── TC-USER-011 - Atualizar usuário com dados válidos
├── TC-USER-012 - Atualizar usuário inexistente
├── TC-USER-013 - Atualizar com e-mail duplicado
├── TC-USER-014 - Atualizar com nome inválido
├── TC-USER-015 - Atualizar com e-mail inválido
└── TC-USER-016 - Atualizar com role inválida

## DELETE /users/{user_id}
├── TC-USER-017 - Excluir usuário existente
└── TC-USER-018 - Excluir usuário inexistente

## POST /products
├── TC-PRODUCT-001 - Criar produto com dados válidos
├── TC-PRODUCT-002 - Nome inválido
├── TC-PRODUCT-003 - Preço igual a zero
├── TC-PRODUCT-004 - Preço negativo
├── TC-PRODUCT-005 - Estoque negativo
└── TC-PRODUCT-006 - Nome duplicado

## GET /products
└── TC-PRODUCT-007 - Listar produtos

## GET /products/{product_id}
├── TC-PRODUCT-008 - Buscar produto existente
└── TC-PRODUCT-009 - Buscar produto inexistente

## PUT /products/{product_id}
├── TC-PRODUCT-010 - Atualizar produto com dados válidos
├── TC-PRODUCT-011 - Atualizar produto inexistente
├── TC-PRODUCT-012 - Atualizar com nome duplicado
├── TC-PRODUCT-013 - Atualizar com nome inválido
├── TC-PRODUCT-014 - Atualizar com preço inválido
└── TC-PRODUCT-015 - Atualizar com estoque inválido

## DELETE /products/{product_id}
├── TC-PRODUCT-016 - Excluir produto existente
└── TC-PRODUCT-017 - Excluir produto inexistente