import logging
import os

class Logger:
    @staticmethod
    def get_logger(name):

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        

        logger.propagate = False 
        
    
        if not logger.handlers:
            formatter = Logger._create_formatter()
            
            Logger._create_console_handler(logger, formatter)
            Logger._create_file_handler(logger, formatter)
    
        return logger
        
    @staticmethod
    def _create_console_handler(logger, formatter):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    @staticmethod
    def _create_file_handler(logger, formatter, log_file='framework.log'):
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    @staticmethod
    def _create_formatter():
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
