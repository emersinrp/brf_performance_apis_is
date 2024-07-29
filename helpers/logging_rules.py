import logging

# Configuração do logging
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # Formatter para os logs
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    
    # Handler para logs de sucesso
    success_handler = logging.FileHandler('locust_success_requests.log')
    success_handler.setLevel(logging.INFO)
    success_handler.setFormatter(formatter)
    
    # Handler para logs de erro
    error_handler = logging.FileHandler('locust_error_requests.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    
    # Adicionando handlers ao logger
    logger.addHandler(success_handler)
    logger.addHandler(error_handler)
    
    return logger

logger = setup_logging()
