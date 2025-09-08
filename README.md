# dotfiles

my dotfiles

## Dependencies:

    sudo apt install zsh zsh-autosuggestions

Install NeoVim:

    curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
    chmod u+x nvim.appimage
    ./nvim.appimage --appimage-extract
    sudo cp -rp squashfs-root/usr/* /usr/local

Install LunarVim by following: https://www.lunarvim.org/docs/installation

## putty config

    sudo apt install ncurses-term 

Connection-Data-Terminal details/Terminal-type string: putty-256color

