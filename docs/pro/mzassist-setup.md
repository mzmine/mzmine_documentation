# Set up mzassist

:material-menu-open: **mzassist → Set up mzassist**

mzassist lets an AI assistant work with mzmine on the same computer. Install mzmine first, then use
its setup screen to add mzassist to your assistant.

## Before you begin

- Download the installer or portable package for your operating system from
  [mzmine GitHub Releases](https://github.com/mzmine/mzmine/releases/latest).
  Follow the [mzmine installation guide](../getting_started.md#install-update).
- Sign in to mzmine with an Academic, Pro, or Pro trial account. See
  [Users management](../services/users.md) if the mzassist menu is missing.
- Install the desktop assistant you intend to use. Its account, subscription, organization policy,
  and support for local plugins are separate from your mzmine account.
- Keep mzmine and the assistant running on the same computer. A browser-only chat does not gain
  access to mzmine merely by signing in to the same account.

The setup files included with mzmine are specific to the operating system and processor.
Use the files offered by your installation. If setup reports that they are unavailable, follow
[Missing setup files](mzassist-troubleshooting.md#missing-setup-files); installing a package for a
different platform will not resolve that problem.

## Claude Desktop

1. In mzmine, open **mzassist → Set up mzassist** and select **Claude Desktop**.
2. Open the included connector installer and complete the installation in Claude Desktop.
   This installs the connection to mzmine.
3. Use the setup screen to locate `mzassist-plugin.zip`. In Claude's plugin management, choose the
   option to upload a plugin and select that ZIP without extracting it. The plugin adds the mzassist
   workflow instructions used by the assistant.
4. Confirm that both the connection and plugin are enabled. Restart Claude Desktop and start a new chat.

Claude's menu labels can change between versions. Use the help link in the mzmine setup screen or
[Claude's plugin instructions](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
if the upload option has moved.

## ChatGPT desktop or Codex

1. Open **mzassist → Set up mzassist** and choose the ChatGPT / Codex setup option.
2. Use the button to prepare the mzassist plugin. This makes the included package available to the
   assistant's personal local marketplace; it does not complete installation inside the assistant.
3. Restart the assistant. Open **Plugins → your personal local marketplace**, then install or update
   **mzassist**.
4. Start a new chat with the plugin enabled.

This package includes the connection and workflow instructions together. If your assistant does
not offer local plugin installation, check its version and your organization's settings before
continuing. Follow the setup instructions for the application you are actually using.

## Check the connection

In mzmine, open **mzassist → Agent activity** and enable the local connection if it is off.
In a new assistant chat, ask:

> Connect to mzmine and tell me which instance you connected to. Do not start an analysis yet.

If more than one mzmine window is running, choose the intended instance. A successful connection
lets the assistant read the available tasks. You do not need to share sample metadata or results
just to check the connection.

Continue with [your first analysis](mzassist-first-analysis.md), or
[explore an existing feature table](mzassist-results.md).

## Update mzassist

Install the newer mzmine release from GitHub Releases, then reopen **Set up mzassist** and update
the assistant using its included packages. Keep the connector and plugin from the same release.
For Claude, update both the connector and the plugin. Restart the assistant and start a new chat
so it loads the updated tools and instructions.

If your project is already open, save it before updating. Check the connection again after the
update; an earlier sharing decision or workflow review may no longer apply.

{{ git_page_authors }}
