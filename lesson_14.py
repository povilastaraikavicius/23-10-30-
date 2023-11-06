import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
name = input("Enter Your Name:\n")
age = input("Enter Your age:\n")
logging.info(f"{name},is {age} years old, logged in successfully !! ")

# -----------------data.log file output-------------
# 12/05/2021 21:01:37 - root - INFO - Tom has logged in successfully !!
# 12/05/2021 21:02:47 - root - INFO - Karl has logged in successfully !!
# 12/05/2021 21:03:27 - root - INFO - Rahul has logged in successfully !!

# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.debug('This is Debug Message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# -------------------------CONSOLE OUTPUT------------------
# 12/05/2021 20:46:41 - root - DEBUG - This is Debug Message
# 12/05/2021 20:46:41 - root - INFO - This is an info message

