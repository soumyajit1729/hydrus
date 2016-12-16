"""
Handlers for the Flask server.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from flask import jsonify, request

def entrypoint():
    """
    Return a set of URI
    """
    return jsonify({
        "root": '/api/',
        "allowed": '/api/available'
    })


def list_resources():
    """
    Provide the list of resources
    """

    # load vocabulary in data/ to create an array of allowed names
    from server.parser import collect_astronomy_resources
    ALLOWED_RESOURCES = collect_astronomy_resources(request.url_rule.endpoint)

    return jsonify(ALLOWED_RESOURCES)

def read_resources(resource):
    """
    Provide a collection of `owl:Class`
    """

    return jsonify({
        "resource": resource
    })

def crud_resource(resource, crud):
    """
    Provide a CRUD operation on a particular resource
    """
    if crud not in ['create', 'read', 'update', 'delete']: return jsonify({"error": 1})

    return jsonify({
        "resource": resource,
        "operation": crud
    })
