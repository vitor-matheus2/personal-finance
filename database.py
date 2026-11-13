import os
from dotenv import load_dotenv
import psycopg
load_dotenv()
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


def get_connection():
    return psycopg.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )

def insert_transaction(description, amount, category, transaction_type):
   try:
     conn = get_connection()
     with conn:
       with conn.cursor() as cur:
        cur.execute(
        """INSERT INTO transactions (description, amount, category, transaction_type)
        VALUES (%s, %s, %s, %s);""",
        (description, amount, category, transaction_type)
        )
        return True
   except psycopg.Error as error:
      print("Erro ao inserir transação", error)
      return False



def get_transactions():
    try:
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM transactions;")
                transactions = cur.fetchall()
                return transactions
    except psycopg.Error as error:
        print("Erro ao buscar transações", error)
        return None


def update_transaction(transaction_id, description, amount, category, transaction_type):
    try:
        conn = get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE transactions
                    SET description = %s, amount = %s, category = %s, transaction_type = %s
                    WHERE id = %s;""",
                    (description, amount, category, transaction_type, transaction_id)
                )
                if cur.rowcount == 0:
                    print("Nenhuma transação encontrada com o ID fornecido.")
                    return False
                return True
    except psycopg.Error as error:
        print("Erro ao atualizar transação", error)
        return False

def delete_transaction(transaction_id):
  try:
    conn = get_connection()
    with conn:
      with conn.cursor() as cur:
          cur.execute(
             "DELETE FROM transactions WHERE id = %s;",
            (transaction_id,)
            )
          if cur.rowcount == 0:
           return False
          return True
  except psycopg.Error as error:
        print("Erro ao deletar transação", error)
        return False

