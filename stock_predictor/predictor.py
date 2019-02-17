import argparse
import base64
import json

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

#Based on google example
def predict_stock(data):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    service = discovery.build('ml', 'v1')
    name = 'projects/gopher-231919/models/stockpredict'

    response = service.projects().predict(
        name=name,
        body={'instances': {"x": data}}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions'][0]['y']