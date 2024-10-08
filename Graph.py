import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd



# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3694481",
    database="clientes"
)

# Criar um cursor para executar a query
cursor = conexao.cursor()

# Query para somar vendas por mês no último ano
query = """
    SELECT 
        DATE_FORMAT(data_venda, '%Y-%m') AS mes, 
        SUM(valor_venda) AS total_vendas 
    FROM vendas 
    WHERE data_venda >= CURDATE() - INTERVAL 1 YEAR 
    GROUP BY mes
    ORDER BY mes;
"""

# Executar a query
cursor.execute(query)
resultados = cursor.fetchall()

# Fechar a conexão
conexao.close()

# Transformar os resultados em um DataFrame (opcional, facilita o trabalho com os dados)
df = pd.DataFrame(resultados, columns=['Mes', 'Total Vendas'])

# Criar o gráfico de barras
plt.bar(df['Mes'], df['Total Vendas'], color='skyblue')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Mês (Último Ano)')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar corte dos rótulos

# Exibir o gráfico
plt.show()