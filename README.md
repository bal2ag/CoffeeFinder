# CoffeeFinder
CoffeeFinder is a simple flask application for keeping track of coffee shops. It exposes a single endpoint:
`/api/coffeeshops/`

You can `POST` to this endpoint to add a coffee shop to the database. Make sure you set the `Content-Type` to `application/json` and include all of the following in your `POST` body:

- `name` The name of the coffee shop. Must be unique across all coffee shops. (**String**)
- `address` The street address of the coffee shop (**String**)
- `zipcode` The zipcode of the coffee shop (**Integer**)
- `price` The price range of the coffee shop (**Integer between 1 and 5 inclusive**)
- `max_seats` The maximum number of seats in the coffee shop (**Integer**)
- `power` Whether or not the coffee shop has outlets available (**Boolean**)
- `wifi` Whether or not the coffee shop has wifi available (**Boolean**)

Example request:
`curl -H "Content-Type: application/json" -X POST -d '{"name":"Cartel Coffee Lab", "address": "123 Derp Street #202", "zipcode": 85283, "price": 2, "max_seats": 40, "power": true, "wifi": true}' http://127.0.0.1:5000/api/coffeeshops/`

You can call the endpoint with `GET` to get a list of all coffeeshops:

```json{
  "coffeeshops": [
    {
      "address": "123 Derp Street #202", 
      "id": 1, 
      "max_seats": 40, 
      "name": "Cartel Coffee Lab", 
      "power": true, 
      "price": 2, 
      "wifi": true, 
      "zipcode": 85283
    }, 
    {
      "address": "123 Derp Street #202", 
      "id": 17, 
      "max_seats": 40, 
      "name": "Cartel Coffee Lab2", 
      "power": true, 
      "price": 2, 
      "wifi": true, 
      "zipcode": 85283
    }
  ]
}
```

# Deployment

TODO

