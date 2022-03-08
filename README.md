# ansible-deb-server

An ansible playbook to setup a fresh install of Debian running as a server. This playbook installs packages and does some set up to get the server to a minimum thresh hold of functionality (can't do much without sudo, curl, git, build-essentials and the like after all). after this initial configuration it then installs some packages, and my configs for them, to personalize the system (zsh, neovim, ipython, etc). These packages and configs are not necessary for basic functionality but they're a part of all the setups I make

## setup:

edit the file < roles/ssh-config/defaults/main.yml > to change the ssh port

