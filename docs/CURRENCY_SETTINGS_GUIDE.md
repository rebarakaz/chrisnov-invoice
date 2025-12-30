# Currency Settings Guide

This guide explains how to manage currency settings in the Chrisnov Invoice application.

## Accessing Currency Settings

1. Navigate to **Settings** from the main sidebar.
2. Click on the **Currencies** card.

## Default Currency

The **Default Currency** is the currency that will be automatically selected when you create a new invoice. This should be the currency you use most often for your business.

To change the default currency:

1. Select a currency from the dropdown menu.
2. Click **Update Default Currency**.

This setting only affects new invoices; the currency of existing invoices will not be changed.

## Supported Currencies

Chrisnov Invoice allows you to create invoices in multiple currencies. The application comes with built-in support for:

- **IDR** (Indonesian Rupiah)
- **USD** (United States Dollar)
- **EUR** (Euro)

When creating or editing an invoice, you can select any of these supported currencies.

## Adding More Currencies

While the web interface allows you to set the default currency, adding new currencies to the list of supported options requires a small code modification.

1. Open the `config.py` file in the project's root directory.
2. Locate the `SUPPORTED_CURRENCIES` dictionary.
3. Add a new entry for the currency you want to support, following the existing format:

    ```python
    'CODE': {'symbol': 'SYMBOL', 'name': 'Full Name', 'position': 'before' or 'after'}
    ```

    For example, to add the British Pound, you would add:

    ```python
    'GBP': {'symbol': '£', 'name': 'British Pound', 'position': 'before'}
    ```

4. Save the `config.py` file and restart the application for the changes to take effect.
