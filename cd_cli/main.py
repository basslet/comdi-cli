import json
import os
import sys
from datetime import datetime, timedelta

from babel.numbers import format_currency
from pathvalidate import sanitize_filename

from cd_cli.comdirect_api_client import ComdirectApiClient
from cd_cli.utils import get_colored_logger


def main():
    logger = get_colored_logger(__name__, verbosity="info")

    credentials = {}
    credentials_file = "credentials.json"
    if len(sys.argv) > 1:
        credentials_file += f"_{sys.argv[1]}"
    credentials_were_incomplete = False

    output_dir = "output"
    if len(sys.argv) > 2:
        if os.path.exists(sys.argv[2]):
            output_dir = sys.argv[2]

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
        if key not in credentials:
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
    account_balances, _ = client.get_account_balances()
    account_id = account_balances.values[0].account.account_id

    start_date = datetime.now() - timedelta(days=730)
    account_transactions, account_transactions_json = client.get_account_transactions(
        account_id, start_date=start_date, paging_count=500
    )

    os.makedirs(f"{output_dir}/{account_id}", exist_ok=True)
    filename = f"{output_dir}/{account_id}/account_transactions.json"

    try:
        logger.debug('Try saving account transactions (raw) to "%s".', filename)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(account_transactions_json))
    except Exception:
        logger.warning(
            'Could not save account transactions (raw) to "%s".', filename, exc_info=1
        )

    print()
    print("Direct debit bookings:")
    print(f'{"Date":<10} {"Amount":>12} {"Receipient":<80} {"Mandate reference"}')
    for transaction in account_transactions.values:
        transaction_type = transaction.transaction_type.key
        if transaction_type != "DIRECT_DEBIT":
            continue

        booking_date = str(transaction.booking_date)
        amount = format_currency(
            transaction.amount.value, transaction.amount.unit, locale="de_DE"
        )
        recepient = transaction.remitter.holder_name
        mandate = transaction.direct_debit_mandate_id

        print(f"{booking_date:<10} {amount:>12} {recepient:<80.80} {mandate}")

    document_list = []
    first_page = 0
    total_matches = 0
    while True:
        doc_list = client.get_document_list(paging_first=first_page)
        document_list += doc_list.values
        # index = doc_list.paging.index
        matches = doc_list.paging.matches
        matches_in_response = doc_list.aggregated.matches_in_this_response
        total_matches += matches_in_response
        if total_matches == matches:
            break
        first_page += matches_in_response

    doc_dir = f"{output_dir}/{account_id}/documents/"

    for document in document_list:
        if document.mime_type == "application/pdf":
            file_name = sanitize_filename(
                f"{document.date_creation} {document.name}.pdf", platform="universal"
            )
            if "Wertpapierabrechnung" in document.name:
                path = f"{doc_dir}Wertpapierabrechnung/"
            elif "Ertragsgutschrift" in document.name:
                path = f"{doc_dir}Ertragsgutschrift/"
            else:
                path = f"{doc_dir}"

            if not os.path.exists(path + file_name):
                os.makedirs(path, exist_ok=True)
                with open(path + file_name, "wb") as file:
                    file.write(client.get_document(document))
                    logger.info('Saved "%s".', file_name)

    client.logout()


if __name__ == "__main__":
    main()
