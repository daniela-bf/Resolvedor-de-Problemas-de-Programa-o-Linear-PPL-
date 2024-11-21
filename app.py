import streamlit as st
import pulp
def resolver_ppl():
   st.title("Resolvedor de Problemas de Programação Linear (PPL)")
   # Escolha de maximizar ou minimizar
   objetivo_tipo = st.selectbox("Escolha o tipo de otimização:", ["Maximizar", "Minimizar"])
   # Entrada de dados da função objetivo
   st.header("Função Objetivo")
   num_variaveis = int(st.number_input("Número de variáveis:", min_value=2, max_value=4, value=2))
   coeficientes_obj = []
   for i in range(num_variaveis):
       coeficientes_obj.append(st.number_input(f"Coeficiente de x{i+1}:", key=f"obj_{i}"))
   # Entrada de dados das restrições
   st.header("Restrições")
   num_restricoes = int(st.number_input("Número de restrições:", min_value=1, value=1))
   coeficientes_restricoes = []
   limites_restricoes = []
   for i in range(num_restricoes):
       st.subheader(f"Restrição {i+1}")
       coefs = []
       for j in range(num_variaveis):
           coefs.append(st.number_input(f"Coeficiente de x{j+1}:", key=f"rest_{i}_{j}"))
       coeficientes_restricoes.append(coefs)
       limites_restricoes.append(st.number_input(f"Limite da restrição:", key=f"lim_{i}"))
   # Resolução do PPL com PuLP
   if objetivo_tipo == "Maximizar":
       problema = pulp.LpProblem("PPL", pulp.LpMaximize)
   else:
       problema = pulp.LpProblem("PPL", pulp.LpMinimize)
   variaveis = pulp.LpVariable.dicts("x", [str(i) for i in range(num_variaveis)], lowBound=0)
   # Função objetivo
   problema += pulp.lpSum([coef * variaveis[str(i)] for i, coef in enumerate(coeficientes_obj)])
   # Restrições
   for i in range(num_restricoes):
       coefs = [float(coef) for coef in coeficientes_restricoes[i]]
       problema += (pulp.lpSum([coef * variaveis[str(j)] for j, coef in enumerate(coefs)]) <= float(limites_restricoes[i]))
   # Resolver o problema
   problema.solve()
   # Saída de resultados
   st.header("Resultados")
   if pulp.LpStatus[problema.status] == "Optimal":
       st.subheader("Solução ótima encontrada:")
       for v in problema.variables():
           st.write(f"{v.name} = {v.varValue}")
       st.write(f"Valor ótimo da função objetivo: {pulp.value(problema.objective)}")
       # Análise de sensibilidade (preços sombra)
       st.subheader("Análise de Sensibilidade")
       for name, c in problema.constraints.items():
           st.write(f"Preço sombra de {name}: {c.pi}")
   else:
       st.write("Não foi possível encontrar uma solução ótima.")
if __name__ == "__main__":
   resolver_ppl()
