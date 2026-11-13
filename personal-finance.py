from database import insert_transaction, get_transactions, update_transaction, delete_transaction

def total_income_and_expenses():
    transactions = get_transactions()
    if transactions is None:
        return None
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction[4] == "income":
            total_income += transaction[2]
        elif transaction[4] == "expense":
            total_expenses += transaction[2]
    return total_income, total_expenses


def get_balance():
    result = total_income_and_expenses()
    if result is None:
        return None
    total_income, total_expenses = result
    balance = total_income - total_expenses
    return balance



def add_transaction():
    description = input("Digite a descrição da transação: ").strip()
    try:
      amount = float(input("Digite o valor da transação: "))
    except ValueError:
        return "Valor inválido!"
    category = input("Digite a categoria da transação: ").strip()
    transaction_type = input("Digite o tipo da transação (income/expense): ").strip()
    if amount <= 0 or transaction_type not in ["income", "expense"] or description == "" or category == "":
        return "Dados inválidos. Verifique os campos."
    else:
       insert = insert_transaction(description, amount, category, transaction_type)   
       if insert:
        return "Transação adicionada com sucesso!"
       else: 
         return "Erro ao adicionar transação!"

def list_transactions():
    transactions = get_transactions()
    if transactions is None:
        print("Erro ao buscar transações")
        return
    if not transactions:
         print("Nenhuma transação cadastrada.")
         return
    for transaction in transactions:
            print(f"Descrição: {transaction[1]}\nValor: R$ {transaction[2]:.2f}\nCategoria: {transaction[3]}\nTipo: {transaction[4]}\n----------------")
    
def edit_transaction():
    try:
      edit_id = int(input("digite o id: "))
    except ValueError:
        return "Valor inválido!"
    if edit_id <= 0:
        return "ID inválido! Informe um número maior que zero."
    edit_description = input("digite a nova descrição: ").strip()
    try:
      edit_amount = float(input("digite novo valor da transação:"))
    except ValueError:
        return "Valor inválido!"
    edit_category = input("Digite a categoria da transação: ").strip()
    edit_transaction_type = input("Digite novo tipo da transação (income/expense): ").strip()
    if edit_amount <= 0 or edit_transaction_type not in ["income", "expense"] or edit_description == "" or edit_category == "":
        return "Dados inválidos. Verifique os campos."
    updated = update_transaction(edit_id, edit_description, edit_amount, edit_category, edit_transaction_type)
    if updated is True:
      return "Transação atualizada com sucesso!"
    elif updated is False:
      return "Nenhuma transação encontrada com esse ID."
    else:
      return "Erro ao atualizar transação no banco de dados."


def remove_transaction():
    try:
     remove_id = int(input("digite o id que vc quer remover:"))
    except ValueError:
       return "Valor inválido!"
    if remove_id <= 0:
            return "ID inválido! Informe um número maior que zero."
    remove =  delete_transaction(remove_id)
    if remove is True:
        return "Transação deletada com sucesso!"
    elif remove is False:
        return "Nenhuma transação encontrada com o ID fornecido."
    else:
        return "Erro ao excluir transação no banco de dados."
 
    
def main():
   while True:
        print("1. Adicionar transação")
        print("2. Atualizar transação")
        print("3. Excluir")
        print("4. Listar transações")
        print("5. Ver saldo")
        print("6. Sair")
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            result = add_transaction()
            print(result)
        elif choice == "2":
            updated = edit_transaction()
            print(updated)
        elif choice == "3":
            remove = remove_transaction()
            print(remove)
        elif choice == "4":
            list_transactions()
        elif choice == "5":
            balance = get_balance()
            if balance is None:
                print("Erro ao calcular saldo")
            else:
               print(f"Saldo atual: R$ {balance:.2f}")
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()
