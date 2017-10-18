import connexion
import logging


logging.basicConfig()
logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)

logger.info("Starting API...")

app = connexion.App(__name__)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
