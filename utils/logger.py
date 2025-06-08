import logging
import os

def setup_basic_logger(log_file: str = '../../logs/review_scraper.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_logger(name: str, log_file: str = "logs/app.log", level=logging.INFO) -> logging.Logger:
    """Returns a reusable logger instance."""
    # Get absolute path to project root (assuming this file is in utils/)
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    full_log_path = os.path.join(root_dir, log_file)

    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(full_log_path), exist_ok=True)

    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding multiple handlers if already configured
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(full_log_path)
        file_handler.setLevel(level)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Formatter
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger