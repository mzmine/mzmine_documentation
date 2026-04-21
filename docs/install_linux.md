# Installation on Linux

Download the latest version, install mzmine, login, and run mzmine. See mzmine [command-line interface](commandline_tool.md) as a reference.
```bash
# with gh (github) installed, download of latest .deb installer is quite easy
# gh auth login
# sudo apt install gh
# gh release download --repo mzmine/mzmine --pattern "mzmine*.deb"

# or find installer at https://github.com/mzmine/mzmine/releases/latest 
wget https://github.com/mzmine/mzmine/releases/download/text-action-release/mzmine_4.3.1_amd64.deb

# create required dir and install mzmine
sudo mkdir -p /usr/share/desktop-directories/
sudo apt install mzmine*.deb

# potential dependencies that may be required 
# sudo apt-get install xdg-utils
# sudo apt-get install libgl1
# sudo apt-get install libgtk-3-0
# sudo apt-get install libxtst6

# run mzmine and print help. also check -login-console -batch
/opt/mzmine/bin/mzmine -help
```