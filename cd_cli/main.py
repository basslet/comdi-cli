import json
from datetime import datetime, timedelta

from babel.numbers import format_currency

from cd_cli.comdirect_api_client import ComdirectApiClient
from cd_cli.utils import get_colored_logger


def main():
    logger = get_colored_logger(__name__, verbosity="debug")

    credentials = {}
    credentials_file = "credentials.json"
    credentials_were_incomplete = False

    try:
        logger.debug('Try reading credentials from "%s" file.', credentials_file)
        with open(credentials_file, "r", encoding="utf-8") as file:
            contents = file.read()
            credentials = json.loads(contents)
    except FileNotFoundError:
        credentials_were_incomplete = True
        logger.info("Credentials file not found. Please provide credentials.")

    required_keys = ["client_id", "client_secret", "username", "password"]

    for key in required_keys:
        if  key not in credentials:
            credentials_were_incomplete = True
            credentials[key] = input(f'Please enter "{key}": ')

    if credentials_were_incomplete is True:
        logger.debug("Ask if credentials shall be saved as file.")

        save_credentials = input(f'Save credentials in "{credentials_file}"? (y/N): ')
        if save_credentials.upper() == "Y":
            try:
                logger.debug('Try saving credentials to "%s".', credentials_file)
                with open(credentials_file, "w", encoding="utf-8") as file:
                    file.write(json.dumps(credentials))
            except Exception:
                logger.warning(
                    'Could not save credentials to "%s".', credentials_file, exc_info=1
                )

    client = ComdirectApiClient(
        credentials["client_id"],
        credentials["client_secret"],
        credentials["username"],
        credentials["password"],
    )
    client.login()
    client.get_account_balances()
    account_id = client.banking.account_balances.values[0].account.account_id

    start_date = datetime.utcnow() - timedelta(days=730)
    client.get_account_transactions(account_id, start_date=start_date)

    account_transactions_raw = client.banking.raw_responses["account_transactions"]

    filename = "account_transactions_raw.json"

    try:
        logger.debug('Try saving account transactions (raw) to "%s".', filename)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(account_transactions_raw))
    except Exception:
        logger.warning(
            'Could not save account transactions (raw) to "%s".', filename, exc_info=1
        )

    account_transactions = client.banking.account_transactions
    
    print()
    print("Direct debit bookings:")
    print(f"{"Date":<10} {"Amount":>12} {"Receipient":<80} {"Mandate reference"}")
    for transaction in account_transactions.values:
        transaction_type = transaction.transaction_type.key
        if transaction_type != "DIRECT_DEBIT":
            continue
    
        booking_date = str(transaction.booking_date)
        amount = format_currency(transaction.amount.value,transaction.amount.unit, locale="de_DE")
        recepient = transaction.remitter.holder_name
        mandate = transaction.direct_debit_mandate_id

        print(f"{booking_date:<10} {amount:>12} {recepient:<80.80} {mandate}")

    client.logout()

if __name__ == "__main__":
    main()
