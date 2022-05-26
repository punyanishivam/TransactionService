To run the project:
    uvicorn src.main:app --reload

Create transaction records:
    PUT: Param: 27 Request Body - {'type': 'yes', 'amount': 127}
    PUT: Param: 35 Request Body - {'type': 'yes', 'amount': 127, 'parent_id': 27}

GET transaction:
    Param: ID

GET transaction_by_type:
    Param: type

GET sum_of_related_transactions:
    Param: ID