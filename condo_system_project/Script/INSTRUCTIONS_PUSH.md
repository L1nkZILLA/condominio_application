Instruções para criar repositório no GitHub e publicar os arquivos:

1. Criar repositório no GitHub (ex: condo-system)
2. Local:
   git init
   git add .
   git commit -m "Initial commit - condo system skeleton"
   git branch -M main
   git remote add origin git@github.com:<your-user>/<repo>.git
   git push -u origin main

3. Criar GitHub Actions ou CI se desejar para build/test
