
📚🤝 EduConecta
Projeto EduConecta: conecta doadores a ONGs e escolas públicas que precisam de materiais e apoio educacional.
É composto por:

Backend em Python usando Flask

Frontend mobile em React Native usando Expo (rodado em emulador Android no Android Studio)

⚙️ Pré-requisitos
Python 3.x

Node.js (>= 16)

npm ou yarn

Android Studio (para rodar o emulador)

Expo CLI

🐍 Backend (Python + Flask)
⚠️ Tudo que envolve Python deve ser feito dentro de uma virtual environment (venv).

1️⃣ Criar e ativar a venv
No terminal, na pasta root do projeto:

bash
Copiar
Editar
python -m venv venv
Ative a venv:

Linux/macOS:

bash
Copiar
Editar
source venv/bin/activate
Windows:

powershell
Copiar
Editar
.\venv\Scripts\activate
2️⃣ Instalar dependências
Ainda com a venv ativada:

bash
Copiar
Editar
pip install -r backend/requirements.txt
3️⃣ Rodar o backend
No terminal (ainda com a venv):

bash
Copiar
Editar
cd backend
flask run
A API vai rodar localmente:

cpp
Copiar
Editar
http://127.0.0.1:5000
📱 Frontend (React Native + Expo)
O frontend foi desenvolvido em React Native e testado usando:

Expo Go

Emulador Android do Android Studio

A baseURL já está configurada no frontend como:

cpp
Copiar
Editar
http://10.0.2.2:5000
Isso permite que o emulador acesse a API local rodando no seu computador.

1️⃣ Instalar dependências do frontend
Na pasta root ou onde está o package.json:

bash
Copiar
Editar
npm install
ou

bash
Copiar
Editar
yarn install
2️⃣ Instalar o Expo CLI globalmente (se ainda não tiver)
bash
Copiar
Editar
npm install -g expo-cli
3️⃣ Rodar o app
bash
Copiar
Editar
expo start
Isso vai abrir o Expo Dev Tools no navegador.
Você pode:

Rodar no emulador Android (Android Studio)

Ou escanear o QR Code com o Expo Go no celular físico

⚠️ Observações importantes
No emulador Android padrão (AVD), use sempre http://10.0.2.2:5000 para acessar o backend local.

Se for rodar em celular físico, troque para o IP local da sua máquina, ex.:

cpp
Copiar
Editar
http://192.168.x.x:5000
✨ Contribuições
