#!/bin/bash
for i in {1..10}
do
   curl -d "{\"msg\":\"message#${i}\"}" -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/
done
