import requests
import json

def getCreds() :
    creds = dict()
    creds['access_token'] = 'EAAHTKY1O2KEBO8tppS3ZCNuovKjFZCuJCVbKHaV3WWUunvTjpxSBLk39Xalm2TwKcssa4rUg4sUgtPDITv1Hu6clQdKfyoGgCErRrflgGeZCqH51AcncxgYP6kzuK56hekEpNcJh8lKBi9VP83hWegrQRC56NCcOJuatV7OMFyPgppcRMCMHhXbFPE0LXjNfFB6twZDZD'
    creds['client_id'] = '513650394585249'
    creds['client_secret'] = '33eb0d1fd18cea31abb54fa9591db51e'
    creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
    creds['graph_version'] = 'v6.0' # v ersion of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
    creds['debug'] = 'no' # debug mode for api call
    creds['page_id'] = '106512302375604' # users page id
    # creds['instagram_account_id'] = '17841468008215235' # users instagram account id
    # creds['ig_username'] = 'IG-USERNAME' # ig username

    return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :

	print ("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli