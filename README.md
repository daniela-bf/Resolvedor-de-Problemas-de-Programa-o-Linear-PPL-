Resolvedor de Problemas de Programação Linear (PPL) 

Este aplicativo foi desenvolvido em Python usando Streamlit e PuLP para resolver problemas de programação linear (PPL) utilizando o método Simplex. Resolvendo problemas de Maximizar e Minimizar. O aplicativo permitirá a entrada dos dados da função objetivo e das restrições, resolve o problema e exibe os resultados, como a solução ótima e os preços sombras das restrições. 

  

1. Instalação 

Clone este repositório ou faça o download dos arquivos. 

Instale as bibliotecas necessárias usando pip: 

            pip install streamlit pulp 

  

2. Como Rodar 

Execute o comando abaixo para iniciar o aplicativo Streamlit: 

              streamlit run app.py 

O navegador padrão será aberto automaticamente com a interface do aplicativo. 

  
Passos do Processo 

1. Configuração da Função Objetivo 

   Escolha o número de variáveis (entre 2 e 4). 

   Insira os coeficientes correspondentes para cada variável na função objetivo. 

  

2. Adicionar Restrições 

   Indique o número total de restrições. 

   Para cada restrição, insira: Os coeficientes das variáveis. 

   O limite da restrição. 

  
3. Escolha do Tipo de Otimização 
  
  Selecione se deseja maximizar ou minimizar a função objetivo. 


Exemplo 
Suponha que você tenha a seguinte função objetivo e restrições: 
Problema: Maximizar o lucro da produção de móveis. 
Tipo de otimização: Maximizar 

   Número de variáveis: 4 (Escrivaninha, Mesa, Armário, Prateleira) 
   Função objetivo: 
   Coeficientes: x1 = 80 (Mesa), x2 = 70 (Escrivaninha), x3 = 100 (Armário), x4 = 16 (Prateleira) 
   Número de restrições: 3 
   Restrição 1: x1 + x2 + x3 + 4x4 ≤ 250 (Tábua) 
   Restrição 2: x2 + x3 + 2x4 ≤ 600 (Prancha) 
   Restrição 3: 3x1 + 2x2 + 4x3 ≤ 500 (Painel) 



  Observações:
  1. O Streamlit é uma biblioteca em Python projetada para simplificar a criação de aplicativos de visualização e interação de dados. Ele permite que você transforme scripts de Python em aplicativos web interativos de maneira rápida e intuitiva, sem necessidade de conhecimento avançado de front-end.
  2. O PuLP é uma biblioteca Python usada para resolver problemas de otimização linear e inteira, implementando o método Simplex e outros algoritmos. Ele serve como um front-end para otimizadores como CBC, Gurobi, CPLEX, entre outros.

 
