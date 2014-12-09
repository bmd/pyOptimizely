import sys
import json

from optimizely import Optimizely

def cb(j):
    """ Pretty-print response """
    print json.dumps(j, indent=2)

def main(token):
    # create an instance of the Optimizely class and pass in your
    #   API key. The strict parameter will raise an error if 
    #   requests.raise_for_status() != None. This is good if you're
    #   passing in a callback function and don't want to handle 
    #   http errors internally. Strict is true by default.

    optly = Optimizely(token, strict=True)

    # list Optimizely projects that can be accessed by the API key
    #   if you pass an optional callback function, then the call 
    #   will return callback(response). If no callback is defined,
    #   then the call will just return the requests resposne object.

    projects = optly.get('projects/', callback=cb)

    # the PUT and UPDATE endpoints also require a data object (duh),
    #   which should just be a dict of parameters to upload and the
    #   values to update them with. Pass it like so (you should 
    #   replace my project ID with one you want to access. Double duh):

    optly.put('projects/8014416/', data = {'ip_filter': None}, callback=cb)

if __name__ == '__main__':
    main(sys.argv[1])
