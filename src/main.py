from fastapi import FastAPI, APIRouter
from src.helpers.transaction_sum_helper import Graph


app = FastAPI()

payment_db = {}
graph = Graph()

router = APIRouter(prefix="/transactionservice", tags=['transactions'])


@app.get("/")
async def health():
    print(payment_db)
    return {"message": "Payment service"}


@app.put("/transactionservice/transactions/{transaction_id}")
def add_transaction(transaction_id: int, transaction: dict):
    print(payment_db)
    payment_db[transaction_id] = transaction
    if "parent_id" in transaction:
        graph.addEdge(transaction_id, transaction["parent_id"])
    return {"status": "ok"}


@app.get("/transactionservice/transactions/{transaction_id}")
def get_transaction(transaction_id: int):
    try:
        return payment_db[transaction_id]
    except:
        return {"message": "Transaction not found"}


@app.get("/transactionservice/transaction/type/{transaction_type}")
def get_transactions_by_type(transaction_type: str):
    return [transaction for transaction in payment_db if payment_db[transaction]["type"] == transaction_type]


@app.get("/sum/{transaction_id}")
def sum_related_transactions(transaction_id: int):
    print(payment_db)
    return {"sum": graph.BFS(transaction_id, payment_db)}
