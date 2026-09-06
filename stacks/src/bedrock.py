import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    Handler para a execução da chamada ao Amazon Bedrock via Custom Resource.
    Invoca a API Converse durante o provisionamento da Stack.
    """
    request_type = event.get('RequestType')
    logger.info(f"Custom Resource RequestType: {request_type}")

    # Quando a stack é destruída (cdk destroy), evita fazer novas chamadas
    if request_type == 'Delete':
        return {'Status': 'SUCCESS'}

    client = boto3.client('bedrock-runtime')
    
    try:
        logger.info("Invocando o modelo Qwen 3 no Amazon Bedrock...")
        
        response = client.converse(
            modelId='qwen.qwen3-7b-instruct-v1:0',
            messages=[{
                'role': 'user', 
                'content': [{'text': 'Hello from CDK Automated Custom Resource'}]
            }]
        )
        
        logger.info(f"Resposta do Bedrock recebida com sucesso: {response}")
        
    except Exception as e:
        logger.error(f"Erro ao invocar o Amazon Bedrock: {str(e)}")
        # Propaga a exceção para garantir que falhas no Bedrock interrompam o deploy
        raise e

    return {'Status': 'SUCCESS'}
