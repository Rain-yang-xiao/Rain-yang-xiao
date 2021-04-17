import logging

class Logger:
    def print_log(self):
        logger = logging.getLogger('logger')
        # 设置日志级别
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            sh = logging.StreamHandler()
            # 设置打印日志的格式
            fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            sh.setFormatter(fmt)
            sh.setLevel(logging.DEBUG)
            logger.addHandler(sh)
        return logger