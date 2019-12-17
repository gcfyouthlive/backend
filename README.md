# API

trasaction POST
```json
{
    "user": "9929c155-7fd2-4673-a400-be712956ab4c",
    "trans_date": "2014-12-01",
    "purpose": "test",
    "attendees": [
        "9929c155-7fd2-4673-a400-be712956ab4c"
    ]
}
```
user is in uuid form

reciept POST
```JSON
{
    "transaction": "c7747cff-d338-4b1f-a0f4-c0645ba08d6b",
    "acc_title": "test",
    "reci_establishment": "test",
    "reci_amt": 1234.0,
    "reci_date": "2015-12-12",
    "reci_or": "12455132412312432234",
    "img": null
}
```
transaction link is in uuid form