# Neuro App - Sistema de Avaliação Neuropsicológica

## Visão Geral

O Neuro App é um sistema profissional de avaliação neuropsicológica projetado para que psicólogos realizem avaliações clínicas padronizadas. A aplicação fornece questionários digitais para avaliações comportamentais e do espectro autista, formulários abrangentes de avaliação neuropsicológica e recursos de geração automática de laudos. Todos os dados são armazenados localmente no navegador, garantindo a privacidade dos pacientes e o funcionamento offline.

## Preferências do Usuário

**Estilo de comunicação preferido:** linguagem simples e cotidiana.

# Arquitetura do Sistema

## Arquitetura Frontend

### Framework e Sistema de Build

* React 18 com TypeScript para desenvolvimento de componentes com segurança de tipos.
* Vite como ferramenta de build e servidor de desenvolvimento.
* Roteamento no lado do cliente gerenciado dentro de uma arquitetura de aplicação de página única (SPA).

### Sistema de Componentes da Interface

* Biblioteca de componentes shadcn/ui com componentes básicos do Radix UI para componentes acessíveis e personalizáveis.
* Tailwind CSS para estilização baseada em utilitários com tokens de design personalizados.
* Sistema de design baseado nos princípios do Material Design adaptados para aplicações clínicas.
* Família tipográfica Inter via Google Fonts para uma tipografia profissional.
* Paleta de cores personalizada focada em tons de azul médico (base HSL 210), transmitindo credibilidade profissional.

### Gerenciamento de Estado

* TanStack Query (React Query) para gerenciamento e cache de estado do servidor.
* Estado local do React (useState/useEffect) para gerenciamento em nível de componente.
* Nenhuma biblioteca global de gerenciamento de estado; o estado é elevado quando necessário.

### Manipulação de Formulários

* React Hook Form com resolvedores Zod para validação.
* Integração Drizzle-Zod para validação de formulários baseada em esquemas.

## Arquitetura Backend

### Framework do Servidor

* Servidor Express.js com TypeScript.
* Sistema personalizado de registro de rotas em `server/routes.ts`.
* Middleware para análise de JSON, codificação de URL e registro de requisições.
* Middleware de tratamento de erros com normalização de códigos de status.

### Desenvolvimento vs Produção

* Integração do middleware do Vite em modo de desenvolvimento para HMR (Hot Module Replacement).
* Servir arquivos estáticos em produção a partir de `dist/public`.
* Configuração baseada em ambiente (`NODE_ENV`).

### Gerenciamento de Sessão

* `connect-pg-simple` para sessões armazenadas em PostgreSQL (configurado, mas não utilizado ativamente na implementação atual).

# Soluções de Armazenamento de Dados

## Armazenamento Principal: LocalStorage do Navegador

Persistência no lado do cliente para todos os dados da aplicação.

### Três chaves de armazenamento:

* `neuro_app_professional`: credenciais do profissional.
* `neuro_app_patients`: registros de pacientes.
* `neuro_app_assessments`: respostas e resultados das avaliações.

Não há persistência no lado do servidor na implementação atual.

## Esquema do Banco de Dados (Preparado, mas Inativo)

PostgreSQL com Drizzle ORM.

Esquema definido em `shared/schema.ts`:

* `users`: autenticação (nome de usuário, senha).
* `professionals`: credenciais profissionais (nome, CRP).
* `patients`: registros de pacientes vinculados aos profissionais.
* `assessments`: dados das avaliações com respostas em JSONB.

Banco de dados PostgreSQL serverless da Neon pronto para integração.

Sistema de migração configurado via Drizzle Kit.

## Decisão de Arquitetura dos Dados

A implementação atual utiliza armazenamento em memória (classe `MemStorage`) e LocalStorage do navegador.

O esquema de banco de dados existe, mas não é utilizado ativamente — a aplicação foi projetada para migrar de armazenamento exclusivamente local para armazenamento baseado em banco de dados.

Isso permite operação com foco em uso offline e futura capacidade de sincronização em nuvem.

# Autenticação e Autorização

## Implementação Atual: Login Simples de Profissional

* Sem autenticação por senha — apenas nome e número do CRP.
* Dados do profissional armazenados no LocalStorage.
* Sem gerenciamento de sessão ou tokens JWT.
* Sem funções ou permissões de usuário.

## Infraestrutura Preparada

* Existe um esquema de usuário com campos de nome de usuário e senha.
* Armazenamento de sessões configurado para PostgreSQL.
* Pronto para implementação de um fluxo completo de autenticação.

# Tipos de Avaliação e Escalas Clínicas

## Escala de Comportamento Disruptivo

* 20 perguntas para avaliação de problemas comportamentais.
* Escala Likert de 4 pontos (Nunca/Raramente até Muito frequentemente).
* Dados do questionário em `client/src/data/disruptiveScale.ts`.

## Escala ATA (Avaliação de Traços Autistas)

* 20 perguntas para avaliação do espectro autista.
* Escala de 4 pontos (Não se aplica até Aplica-se muito).
* Dados do questionário em `client/src/data/ataScale.ts`.

## Avaliação Neuropsicológica

Formulário abrangente cobrindo:

* Dados demográficos do paciente.
* Histórico clínico e familiar.
* Domínios cognitivos (atenção, memória, linguagem, funções executivas, habilidades visuoespaciais e habilidades motoras).
* Avaliação emocional e comportamental.
* Conclusões e recomendações.

## Geração de Laudos

* Modelo estruturado de laudo psicológico.
* Integração automática dos dados das avaliações.
* Layouts otimizados para impressão.

# Visualização de Dados

## Biblioteca de Gráficos: Recharts

* Gráficos de barras para análise da distribuição das respostas.
* Gráficos de pizza para visualização da pontuação total.
* Gráficos radar para perfis dos domínios neuropsicológicos.
* Contêineres responsivos para exibição em dispositivos móveis e desktop.

# Fluxo da Aplicação

1. **Login:** o profissional informa nome e CRP.
2. **Painel Principal:** seleção do tipo de avaliação ou busca de paciente.
3. **Avaliação:** preenchimento do questionário ou formulário de avaliação.
4. **Salvar:** os dados são persistidos no LocalStorage com UUID gerado automaticamente.
5. **Pesquisa:** filtragem e visualização das avaliações salvas pelo nome do paciente.
6. **Visualização Detalhada:** gráficos e resultados formatados com possibilidade de impressão.

# Dependências Externas

## Bibliotecas de Interface e Componentes

* `@radix-ui/*` — componentes básicos acessíveis (accordion, dialog, dropdown, popover, select etc.).
* `shadcn/ui` — sistema de componentes pré-construído sobre o Radix.
* `class-variance-authority` — estilização baseada em variantes de componentes.
* `tailwindcss` — framework CSS baseado em utilitários.
* `lucide-react` — biblioteca de ícones.

## Visualização de Dados

* `recharts` — biblioteca de gráficos para React.
* `embla-carousel-react` — componentes de carrossel/slider.

## Formulários e Validação

* `react-hook-form` — gerenciamento de estado de formulários.
* `@hookform/resolvers` — integração de validação de formulários.
* `zod` — validação baseada em esquemas.
* `drizzle-zod` — conversão de esquemas Drizzle para Zod.

## Banco de Dados e ORM

* `drizzle-orm` — ORM para TypeScript.
* `drizzle-kit` — migrações e gerenciamento de esquema do banco de dados.
* `@neondatabase/serverless` — driver serverless para PostgreSQL da Neon.
* `connect-pg-simple` — armazenamento de sessões em PostgreSQL.

## Ferramentas de Build e Desenvolvimento

* `vite` — ferramenta de build e servidor de desenvolvimento.
* `@vitejs/plugin-react` — integração React para Vite.
* `typescript` — tipagem estática.
* `tsx` — execução de TypeScript para Node.js.
* `esbuild` — empacotador JavaScript para build do servidor em produção.

## Utilitários

* `date-fns` — manipulação de datas.
* `clsx` e `tailwind-merge` — combinação condicional de classes CSS.
* `cmdk` — componente de menu de comandos.
* `nanoid` — geração de identificadores.

## Gerenciamento de Estado

* `@tanstack/react-query` — gerenciamento e cache de estado do servidor.

## Plugins Específicos da Replit

* `@replit/vite-plugin-runtime-error-modal` — janela de erros em desenvolvimento.
* `@replit/vite-plugin-cartographer` — mapeamento de código.
* `@replit/vite-plugin-dev-banner` — banner de desenvolvimento.
