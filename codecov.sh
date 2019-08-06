# If this gets accidentally committed, it isn't a big deal. People can push their code coverage to my codecov page if they really want to.
pytest --cov=./
bash <(curl -s https://codecov.io/bash) -t 94a5cf34-6994-4792-b7eb-d43acace529a
