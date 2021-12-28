# autoservis API

## Get all orders

*Method:* `GET`

*URL* : `https://autoservis.herokuapp.com/getOrders`

*Success Response:*
  
  200 OK

*returned content:*

```json
[ 
    {
        "car_id": "6",
        "owner_id": "2",
        "date": "2021-11-11",
        "type": "sedan",
        "brand": "opel",
        "model": "zafira",
        "problem": "nestartuje",
        "name": "juraj",
        "surname": "ivan",
        "phone": "09022222222",
        "email": "otooto@gmail.com"
    }
]
```

---

## Create new order

*Method:* `POST`

*URL* : `https://autoservis.herokuapp.com/createOrder`

*Success Response:*
  
  201 created

*Excepted example:*

```json
[ 
    {
        "type": "sedan",
        "brand": "opel",
        "model": "zafira",
        "problem": "nestartuje",
        "name": "juraj",
        "surname": "ivan",
        "phone": "090222222222",
        "email": "otooto@gmail.com"
    }
]
```

---

## Edit an existing order

*Method:* `PUT`

*URL* : `https://autoservis.herokuapp.com/updateOrder/<id>`

*Success Response:*
  
  200 updated

*Excepted example:*

```json
[ 
    {
        "owner_id": "2",
        "type": "sedan",
        "brand": "opel",
        "model": "zafira",
        "problem": "nestartuje",
        "name": "juraj",
        "surname": "ivan",
        "phone": "09022222222",
        "email": "otooto@gmail.com"
    }
]
```

---

## Delete order

*Method:* `DELETE`

*URL* : `https://autoservis.herokuapp.com/deleteOrder/<id>`

*Success Response:*
  
  204 delete

