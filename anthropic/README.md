# Modern Mail for Claude

Write thoughtful personal letters with Claude and save them as Modern Mail drafts. The plugin combines a letter-writing workflow with Modern Mail's authenticated remote MCP connector.

## Setup

Install the plugin, connect Modern Mail from its Connectors tab, and sign in to your Modern Mail account through OAuth. No API key belongs in this package. Ask Claude to write a thank-you note, browse stationery, or revise an existing draft. Choose a card when prompted and review the saved result in Modern Mail.

## Example

“Help me write a thank-you note to our hosts. Show me suitable stationery, then save a draft after I choose.”

## Boundaries

The plugin prepares drafts; it does not purchase postage, submit orders, print, or send mail. Collections containing Cart or Sent letters cannot accept new members. Handwriting composition is distinct from saving text and requires the available glyph workflow and human review.

## Data handling

The plugin sends requested letter copy, recipient details, card choices, and record identifiers to your Modern Mail account through https://mcp.modernmailapp.com. The Markdown/JSON package itself has no independent storage or telemetry. Modern Mail and Claude handle service-side data under their respective policies. Do not include credentials in prompts or package files.

## Release status

Preparation draft, not submitted or published. Licensing, public documentation/support links, live tool testing, and directory validation remain release gates.

## Public links

- [Privacy policy](https://www.modernmailapp.com/policies/privacy-policy)
- [Support](https://www.modernmailapp.com/pages/contact)
- [Terms of service](https://www.modernmailapp.com/policies/terms-of-service)
