import logging

error_logger = logging.getLogger()

def sendmail(data):
    try:
		data = response.data
		sendmail(data)
	except Exception as e: 
	    error_logger.error(str(e) + "|" + str(data))
		



# Outro detalhe, em produção o arquivo **info.log quando voce criar ele no linux precisa ter permissões.**

# sudo chmod -R 777 path/info.log