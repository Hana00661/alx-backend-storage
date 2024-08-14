#!/usr/bin/env python3
"""
 Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    log = nginx.count_documents({})
    get = nginx.count_documents({"method": "GET"})
    post = nginx.count_documents({"method": "POST"})
    put = nginx.count_documents({"method": "PUT"})
    patch = nginx.count_documents({"method": "PATCH"})
    delete = nginx.count_documents({"method": "DELETE"})
    status_check = nginx.count_documents(
        {"$and": [{"method": "GET"}, {"path": "/status"}]})

    print('{} logs\nMethods:\n\
    \tmethod GET: {}\n\
    \tmethod POST: {}\n\
    \tmethod PUT: {}\n\
    \tmethod PATCH: {}\n\
    \tmethod DELETE: {}\n{} status check'
          .format(log, get, post, put, patch, delete, status_check)
          )
