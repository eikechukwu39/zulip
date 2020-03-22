search_results = gateway.transaction.search([
    braintree.TransactionSearch.customer_email == "john.smith@example.com"
])

search_results = gateway.transaction.search([
    braintree.TransactionSearch.customer_email != "john.smith@example.com"
])

search_results = gateway.transaction.search([
    braintree.TransactionSearch.customer_email.starts_with("john.smith")
])

search_results = gateway.transaction.search([
    braintree.TransactionSearch.customer_email.ends_with("example.com")
])

search_results = gateway.transaction.search([
    braintree.TransactionSearch.customer_email.contains("smith")
])
