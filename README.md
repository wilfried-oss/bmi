# BMI

Petite API pour calculer son IMC (indice de masse corporelle), construite avec FastAPI.

On envoie son poids et sa taille, elle renvoie le résultat accompagné d'un petit conseil selon la tranche dans laquelle on tombe.

## Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pytest pour les tests
- uv pour la gestion des dépendances et du build

## Installation

Le projet utilise [uv](https://docs.astral.sh/uv/). Une fois installé :

```bash
git clone https://github.com/wilfried-oss/bmi.git
cd bmi
uv sync
```

## Lancer le serveur

```bash
uv run uvicorn api:app --reload
```

L'application est disponible sur `http://localhost:8000`. La page d'accueil sert directement le fichier statique `static/index.html`.

## Endpoints

| Méthode | Route            | Description                                     |
| ------- | ---------------- | ----------------------------------------------- |
| GET     | `/`              | Page d'accueil                                  |
| GET     | `/healthz`       | Vérifie que l'API répond                        |
| POST    | `/calculate_bmi` | Calcule l'IMC à partir du poids et de la taille |

### Exemple de requête

```bash
curl -X POST http://localhost:8000/calculate_bmi \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "height": 1.75}'
```

Réponse :

```json
{
  "bmi": 22.86,
  "advice": "Normal weight, keep up the good work!"
}
```

`weight` est en kilogrammes, `height` en mètres. Une valeur négative ou nulle sur l'un des deux renvoie une erreur 400.

## Tests

```bash
uv run pytest
```

## À venir

- Validation plus poussée des entrées (unités, valeurs limites)
- Historique des calculs par utilisateur
