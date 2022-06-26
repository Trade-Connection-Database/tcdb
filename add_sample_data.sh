#/bin/bash

curl -X 'POST'   'http://localhost/api/write/add_nodes'   -H 'accept: application/json'   -H 'admin: samplekey' -H'Content-Type: application/json'   -d '[
  {
    "name": "evil corp",
    "node_type": 1,
    "country": 1,
    "in_country_id": "whatever5"
  },
  {
    "name": "adolf hitler",
    "node_type": 1,
    "country": 1,
    "in_country_id": "whatever6"
  },
  {
    "name": "saul the evil",
    "node_type": 1,
    "country": 1,
    "in_country_id": "whatever3"
  },
  {
    "name": "saul goodman",
    "node_type": 1,
    "country": 1,
    "in_country_id": "whatever"
  }
]'
