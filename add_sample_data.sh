#/bin/bash

curl -X 'POST'   'http://localhost/api/write/add_nodes'   -H 'accept: application/json'   -H 'admin: samplekey' -H'Content-Type: application/json'   -d '[
  {
    "name": "war in Ukraine",
    "node_type": 1
  }
]'
