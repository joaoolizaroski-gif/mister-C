# Projeto Final - API REST Biblioteca

API REST desenvolvida em Flask e SQLite p/ disciplina de prog no desen. de sistemas.

## Tema e Tabelas
- **Tema:** Biblioteca
- **Tabela Pai (`autores`):** id, nome, nacionalidade
- **Tabela Filho (`livros`):** id, titulo, ano_publicacao, autor_id (FK)

## Como Rodar o Projeto
1. Instale as dependências: `py -m pip install Flask Flask-SQLAlchemy`
2. Execute o projeto: `py projeto.py`

## Rotas da API

### Autores (Tabela Pai)
- `POST /autores` - Criar autor (Status: 201)
- `GET /autores` - Listar todos os autores (Status: 200)
- `GET /autores/<id>` - Obter autor por ID (Status: 200 / 404)
- `PUT /autores/<id>` - Atualizar autor (Status: 200 / 404)
- `DELETE /autores/<id>` - Remover autor (Status: 200 / 404)

### Livros (Tabela Filho)
- `POST /livros` - Criar livro (Status: 201 / 400 / 404)
- `GET /livros` - Listar todos os livros (Status: 200)
- `GET /livros/<id>` - Obter livro por ID (Status: 200 / 404)
- `PUT /livros/<id>` - Atualizar livro (Status: 200 / 404)
- `DELETE /livros/<id>` - Remover livro (Status: 200 / 404)

### Rotas Especiais e Filtros
- `GET /livros/detalhes` - JOIN entre Livros e Autores trazendo nome do autor (LEFT JOIN)
- `GET /autores/<id>/livros` - Filtro por caminho (Livros de um Autor)
- `GET /livros/busca?titulo=...&ano=...` - Busca por Query String com filtros

### Tmj diegão, abs
- <B