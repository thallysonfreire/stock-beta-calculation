# **Análise de Beta de Ações**

Este repositório contém um script em Python para calcular o beta de diferentes ações em relação ao índice Ibovespa (IBOV) usando regressão linear. O código utiliza as bibliotecas `yfinance` e `statsmodels` para coletar dados financeiros e realizar análises estatísticas.

## **Índice**
- [Contexto](#contexto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## **Contexto**
Este projeto visa calcular o beta de várias ações em relação ao índice Ibovespa (IBOV) para avaliar a sensibilidade do retorno das ações em relação ao mercado. O beta é uma medida importante em finanças, usada para entender o risco associado a uma ação comparada ao mercado.

## **Funcionalidades**
- **Coleta de dados:** Baixa dados históricos de preços ajustados de ações e do índice Ibovespa usando a biblioteca `yfinance`.
- **Cálculo do beta:** Calcula o beta de cada ação em relação ao IBOV usando a biblioteca `statsmodels` para regressão linear.
- **Visualização:** Gera gráficos de dispersão e linhas de regressão para visualizar a relação entre os retornos das ações e o IBOV.

## **Estrutura do Projeto**
```
stock-beta-calculation/
│
│── stock-beta.py             # Script principal que realiza o cálculo do beta e a visualização
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do projeto
└── LICENSE                   # Licença do projeto
```

## **Instalação**
### Pré-requisitos
- Python 3.8+
As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute o seguinte comando:
```
pip install -r requirements.txt
```
### **Bibliotecas utilizadas**
- **yfinance:** Para coleta de dados financeiros.
- **statsmodels:** Para análise de regressão linear e cálculo do beta.
- **matplotlib:** Para criação de gráficos.
- **numpy:** Para operações matemáticas e manipulação de arrays.

## **Uso**
### Baixar o repositório
Clone o repositório para sua máquina local:
```
git clone https://github.com/seu-usuario/stock-beta-calculation.git 
cd stock-beta-calculation
```
### **Executar o script**
Após instalar as dependências, execute o script principal:
```
python src/stock-beta.py
```
### **Dados Processados**
O script baixa e processa dados históricos de preços ajustados, calcula o beta para cada ação e gera gráficos de regressão.

### **Exemplo de Análise**
O script inclui exemplos de análise que calculam o beta de ações como WEGE3.SA, PETR4.SA e VALE3.SA em relação ao índice IBOV e plota gráficos de regressão linear para cada ação.

## **Contribuição**
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um *pull request*.

Para contribuir:

1. Faça um *fork* do projeto.
2. Crie uma nova *branch* para sua funcionalidade:
```
git checkout -b feature/nova-funcionalidade
```
3. Faça suas alterações e faça um *commit*:
```
git commit -m 'Adiciona nova funcionalidade'
```
4. Envie as alterações para o repositório principal:
```
git push origin feature/nova-funcionalidade
```
5. Abra um *pull* request para revisão.

## **Licença**
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
