# AWS Credits Collector - CDK Python

Este projeto provisiona via AWS CDK (Python) a infraestrutura necessária para cumprir os 5 requisitos do painel **Explore AWS / Earn AWS Credits** e destravar até **$100 USD em créditos na AWS**.

## Requisitos Prévios

- Python 3.9+ com ambiente virtual ativo (`.venv`) e dependências instaladas (`pip install -r requirements.txt`)
- AWS CLI instalado e autenticado (`aws configure`)
- AWS CDK CLI instalado (`npm install -g aws-cdk`)
- Acesso ativo a pelo menos um modelo no Amazon Bedrock (*Model Access granted* na região do deploy)

## Quick Start (Deploy)

```bash
# 1. Bootstrap do CDK (Apenas na primeira execução por conta/região)
cdk bootstrap aws://<your-account-id>/<region>

# 2. Sintetizar e validar a infraestrutura
cdk synth

# 3. Executar o deploy de todos os recursos
cdk deploy

# 4. Limpeza do ambiente
cdk destroy
```

> Information: Could take between 12 and 24 hours to get update the status of milestones.

> Note: AWS is not recognizing Bedrock API call to check the milestone related to it, I keep the code for learning purpose only.

## 📋 Milestones coverage

| Task | Provisoned Resource | Award |
| --- | --- | --- |
| **Launch an instance using EC2** | Instância EC2 (`t2.micro`) na VPC default | $20 USD |
| **Set up a cost budget using AWS Budgets** | Orçamento mensal de custo no AWS Budgets | $20 USD |
| **Create an Aurora or RDS database** | Instância RDS PostgreSQL (`t3.micro`) | $20 USD |
| **Create a web app using AWS Lambda** | AWS Lambda + HTTP API Gateway | $20 USD |
| **Use a foundation model in Amazon Bedrock** | Custom Resource (Lambda + `boto3`) invocando modelo Bedrock | $20 USD |

---





# 🚀 AWS Credits Collector - CDK Python

Este projeto em AWS CDK (Python) automatiza a criação dos 5 recursos necessários para cumprir os requisitos do painel **Explore AWS / Earn AWS Credits** e liberar até **$100 USD em créditos na sua conta AWS**.

---

## 📋 Atividades Cobertas

| Atividade | Recurso Provisionado | Recompensa |
| --- | --- | --- |
| **Launch an instance using EC2** | Instância EC2 (`t2.micro`) na VPC default | $20 USD |
| **Set up a cost budget using AWS Budgets** | Orçamento mensal de custo no AWS Budgets | $20 USD |
| **Create an Aurora or RDS database** | Instância RDS PostgreSQL (`t3.micro`) | $20 USD |
| **Create a web app using AWS Lambda** | AWS Lambda + HTTP API Gateway | $20 USD |
| **Use a foundation model in Amazon Bedrock** | Custom Resource (Lambda + `boto3`) invocando modelo Bedrock | $20 USD |

---

## 🛠️ Pré-requisitos

1. **AWS CLI** instalado e configurado com permissões de Administrador (`aws configure`).
2. **Node.js** instalado (necessário para o AWS CDK CLI).
3. **Python 3.9+** e `pip` instalados.
4. **AWS CDK CLI** instalado globalmente:
```bash
npm install -g aws-cdk

```


5. **Acesso aos modelos do Amazon Bedrock**:
* Acesse o console AWS na região de deploy (ex: `us-east-1`).
* Vá para **Amazon Bedrock > Model access**.
* Garanta que o acesso ao modelo **Anthropic Claude** ou **Amazon Titan** esteja ativo (*Access granted*).



---

## 📂 Estrutura do Projeto

```text
.
├── app.py                # Ponto de entrada da aplicação CDK
├── app_stack.py          # Definção da Stack com todos os 5 recursos
├── cdk.json              # Configurações da CLI do CDK
├── requirements.txt      # Dependências Python
└── README.md             # Instruções do projeto

```

---

## ⚙️ Configuração do Ambiente

### 1. Clonar ou criar a pasta do projeto

```bash
mkdir aws-credits-cdk
cd aws-credits-cdk

```

### 2. Criar e ativar o ambiente virtual (venv)

* **Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


* **Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

```



### 3. Instalar as dependências

Certifique-se de que o seu `requirements.txt` contém:

```text
aws-cdk-lib>=2.100.0
constructs>=10.0.0
aws-cdk.aws-apigatewayv2-alpha>=2.100.0a0
aws-cdk.aws-apigatewayv2-integrations-alpha>=2.100.0a0

```

Instale com o pip:

```bash
pip install -r requirements.txt

```

---

## 🚀 Passo a Passo para o Deploy

### 1. Bootstrap da Conta/Região (Apenas na primeira vez)

Se você nunca usou o CDK nesta conta/região, execute o bootstrap para provisionar o bucket S3 de assets do CDK:

```bash
cdk bootstrap aws://SUA_CONTA_AWS/SUA_REGIAO

```

> *Exemplo:* `cdk bootstrap aws://123456789012/us-east-1`

### 2. Sintetizar o Template CloudFormation

Gere e valide o template CloudFormation gerado pelo código Python:

```bash
cdk synth

```

### 3. Executar o Deploy

Execute o deploy de toda a infraestrutura em um único comando:

```bash
cdk deploy

```

Confirme a criação dos recursos de segurança digitando **`y`** quando solicitado.

---

## ⏳ Verificação dos Créditos

* Acesse a aba **Explore AWS** no console da AWS para acompanhar o status.
* ⚠️ **Atenção:** A AWS pode levar entre **12 a 24 horas** para processar e atualizar as 5 atividades como `Completed` no painel.

---

## 🧹 Limpeza (Cleanup)

Após os **$100 USD** em créditos estarem liberados e refletidos na sua conta, é fundamental remover a infraestrutura provisionada para evitar qualquer custo adicional fora do Free Tier.

### 1. Destruir os Recursos via CDK

```bash
cdk destroy

```

Confirme a remoção digitando **`y`**.

### 2. Verificações Manuais de Pós-Limpeza (Opcional)

Para garantir que não restaram resíduos:

* **EC2:** Verifique se a instância foi finalizada (*Terminated*).
* **RDS:** Verifique se a instância de banco de dados foi excluída.
* **CloudWatch Logs:** Opcionalmente, apague os *Log Groups* criados pelas funções Lambda.
