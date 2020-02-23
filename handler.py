import datetime
import logging
import requests
import zipfile
import StringIO
import json
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("function " + name + " ran at " + str(current_time))
    unzipFiles()
    showFiles()


def listDownloadFiles(event, context):
    run(event, context)
    return {
        "statusCode": 200,
        "body": json.dumps({"files": showFiles()})
    }


def unzipFiles():
    logger.info("Unzipping megasena file")
    response = requests.get(
        "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip", stream=True)
    megasenaZipfile = zipfile.ZipFile(StringIO.StringIO(response.content))
    megasenaZipfile.extractall('/tmp')


def showFiles():
    logger.info("Showing files unziped:")
    arr = os.listdir("/tmp")
    print(arr)
    return arr
