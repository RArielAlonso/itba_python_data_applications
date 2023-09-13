#!/bin/bash

echo "Obtenemos y actualizamos todos los modulos de python"

pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

echo "Todos los modulos de python han sido actualizado"