# 🔍 Visão Geral do Projeto

Este projeto é uma Pokédex interativa desenvolvida em Python, utilizando SQLAlchemy, Cerberus para validação e Rich para interface no terminal.

Ele segue o padrão de arquitetura **MVC (Model-View-Controller)**.

## 📁 Módulos

- `common/`: Estruturas auxiliares (tipos, exceções, etc.)
- `models/`: Comunicação com o banco de dados
- `controllers/`: Regras de negócio
- `views/`: Interface do terminal
- `main/`: Conexão dos módulos MVC, gerencia o fluxo da aplicação
