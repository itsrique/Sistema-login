# 🔐 Sistema de Login Simples

Um sistema de login feito em Python que permite cadastrar usuários e realizar autenticação utilizando um arquivo `.txt` como banco de dados.

---

## 📌 Funcionalidades

- Cadastro de usuários
- Login com verificação de senha
- Impede usuários duplicados
- Armazenamento em arquivo local (`usuarios.txt`)
- Interface simples via terminal

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Manipulação de arquivos (`.txt`)

---

## ▶️ Como executar

1. Abra a pasta do projeto

2. Execute o arquivo:


python main.py

---

## 💡 Como funciona

Os usuários são armazenados no arquivo `usuarios.txt` no formato:


usuario ; senha


O sistema lê esse arquivo para validar login e evitar cadastros duplicados.
