set -e
set -o xtrace

curl https://pythonify.util.repl.co/recreate_python3_venv.sh | bash

if [[ -f 'pyproject.toml.backup' ]]; then
  mv pyproject.toml pyproject.toml.working
  mv pyproject.toml.backup pyproject.toml
  ./venv/bin/poetry install

  poetry add -D -E yapf -E rope -E pyflakes replit-python-lsp-server@^1.5.9
fi
