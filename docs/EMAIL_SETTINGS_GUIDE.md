# Email Settings Guide

This guide explains how to configure the email settings in Chrisnov Invoice to send invoices and other communications to your clients.

## Accessing Email Settings

1. Navigate to **Settings** from the main sidebar.
2. Click on the **Email** card.

## SMTP Configuration

To send emails, the application needs to connect to an SMTP (Simple Mail Transfer Protocol) server. You can use your existing email provider's SMTP server (like Gmail or Outlook) or a dedicated email service.

### Configuration Fields

- **Mail Server**: The address of the SMTP server (e.g., `smtp.gmail.com`).
- **Port**: The port number for the SMTP server. Common ports are `587` (for TLS) and `465` (for SSL).
- **From Email**: The email address that your emails will be sent from.
- **Username**: The username for your SMTP account (often the same as your email address).
- **Password**: The password for your SMTP account. **Note**: For services like Gmail, you may need to generate an "App Password" instead of using your main account password.
- **Use TLS/SSL**: Check these boxes to enable encrypted communication with your SMTP server. TLS is the most common and recommended option.

### Example: Gmail Configuration

- **Mail Server**: `smtp.gmail.com`
- **Port**: `587`
- **From Email**: Your Gmail address (e.g., `you@gmail.com`)
- **Username**: Your Gmail address
- **Password**: Your 16-digit Google App Password
- **Use TLS**: Enabled

> **Important**: To use Gmail, you must first enable 2-Step Verification on your Google account and then generate an App Password. [Learn how to generate an App Password](https://support.google.com/accounts/answer/185833).

## Testing Your Configuration

After saving your SMTP settings, you can easily test them to ensure everything is working correctly.

1. In the **Test Email Configuration** section, enter an email address where you'd like to receive a test message.
2. Click **Send Test Email**.
3. If your settings are correct, you will receive a confirmation email shortly.

If you encounter an error, the application will provide a message to help you diagnose the issue. Common problems include incorrect credentials, server/port details, or firewall restrictions.
