Embed a GraphiQL View 
=====================

The ``graphiql`` directive allows us to embed a GraphiQL_ view in the documentation, 
we can optionally make this live and editable if a server is available.

Static View
-----------

A static embedded view:

.. graphiql::
  :query:
    {
      country(code: "BR") {
        name
        native
        capital
        emoji
        currency
        languages {
          code
          name
        }
      }
    }
  :response:
    {
      "data": {
        "country": {
          "name": "Brazil",
          "native": "Brasil",
          "capital": "Brasília",
          "emoji": "🇧🇷",
          "currency": "BRL",
          "languages": [
            {
              "code": "pt",
              "name": "Portuguese"
            }
          ]
        }
      }
    }


Source:

.. code-block:: rst

  .. graphiql::
    :query:
      {
        country(code: "BR") {
          name
          native
          capital
          emoji
          currency
          languages {
            code
            name
          }
        }
      }
    :response:
      {
        "data": {
          "country": {
            "name": "Brazil",
            "native": "Brasil",
            "capital": "Brasília",
            "emoji": "🇧🇷",
            "currency": "BRL",
            "languages": [
              {
                "code": "pt",
                "name": "Portuguese"
              }
            ]
          }
        }
      }


Live, Editable View
-------------------

If a server with a GraphQL API is available the sphinx view can be configured to use it. 
In this case it becomes editable:

.. graphiql:: https://countries.trevorblades.com/
    :query:
      {
        country(code: "BR") {
          name
          native
          capital
          emoji
          currency
          languages {
            code
            name
          }
        }
      }
    :response:
      {
        "data": {
          "country": {
            "name": "Brazil",
            "native": "Brasil",
            "capital": "Brasília",
            "emoji": "🇧🇷",
            "currency": "BRL",
            "languages": [
              {
                "code": "pt",
                "name": "Portuguese"
              }
            ]
          }
        }
      }


Source:

.. note::

  If ``https://countries.trevorblades.com/`` is unavailable the view will revert to the 
  static case.

.. code-block:: rst

  .. graphiql:: https://countries.trevorblades.com/
      :query:
        {
          country(code: "BR") {
            name
            native
            capital
            emoji
            currency
            languages {
              code
              name
            }
          }
        }
      :response:
        {
          "data": {
            "country": {
              "name": "Brazil",
              "native": "Brasil",
              "capital": "Brasília",
              "emoji": "🇧🇷",
              "currency": "BRL",
              "languages": [
                {
                  "code": "pt",
                  "name": "Portuguese"
                }
              ]
            }
          }
        }



.. _GraphiQL: https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme
