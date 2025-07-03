# Guia de Instalação do Projeto Clairfy Backend

Este guia tem como objetivo auxiliar na preparação do ambiente de desenvolvimento para o backend do projeto **Clairfy**. Siga os passos abaixo cuidadosamente para garantir que tudo funcione corretamente.

## 🧰 1. Instale o Homebrew (caso ainda não tenha)

O Homebrew é um gerenciador de pacotes para macOS. Se você já possui o Homebrew instalado, pode pular para o próximo passo.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Para garantir que está instalado corretamente:

```bash
brew --version
```

---

## 🐳 2. Instale o Docker

O Docker é essencial para rodar o projeto em containers. Instale com o comando abaixo:

```bash
brew install --cask docker
```

Após instalar:

1. **Abra o Docker Desktop** (procure por "Docker" no Spotlight).
2. Aguarde até que o Docker esteja rodando (ícone da baleia no topo da tela).

Verifique se está funcionando corretamente:

```bash
docker --version
docker run hello-world
```

---

## 🐍 3. Instale o Python

Este projeto usa Python para gerenciar dependências e scripts locais.

```bash
brew install python
```

Verifique a instalação:

```bash
python3 --version
pip3 --version
```

---

## 🧪 4. Crie e ative um ambiente virtual

Um ambiente virtual isola as dependências do projeto para evitar conflitos.

```bash
python3 -m venv venv         # Cria o ambiente virtual
source venv/bin/activate     # Ativa o ambiente virtual
```

Com o ambiente ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🏗️ 5. Build e execução do projeto com Docker

Com tudo instalado, agora vamos buildar e rodar o container Docker do backend.

### 🔨 Build da imagem Docker

No diretório raiz do projeto (onde está o `Dockerfile`), execute:

```bash
docker build -t clairfy-backend .
```

### 🚀 Execute o container

```bash
docker run -d --name dev -p 8000:80 clairfy-backend
```

Este comando irá:

* Criar um container chamado `dev`.
* Tornar a aplicação acessível localmente na porta `8000`.

---

## 🧼 Dicas úteis

* Para parar o container:

```bash
docker stop dev
```

* Para remover o container:

```bash
docker rm dev
```

* Para visualizar os logs:

```bash
docker logs dev
```

* Para testar:

```bash
docker rm -f dev 2>/dev/null && docker build -t clairfy-backend . && docker run -d --name dev -p 8000:80 clairfy-backend
```

---

Se tiver algum problema ou dúvida, verifique se todos os passos foram seguidos corretamente. Caso precise de ajuda, entre em contato com o time de desenvolvimento.
