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