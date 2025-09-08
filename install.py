#!/usr/bin/env python3

# make sure terminfo for putty exists
# ls /usr/share/terminfo/p
# if not:
#     sudo apt-get install ncurses-term

import os
import shutil

cur_dir = os.path.abspath(os.path.dirname(__file__))

# oh-my-zsh
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
shutil.copy("%s/wensheng.zsh-theme" % cur_dir, "%s/.oh-my-zsh/themes/" % os.environ['HOME'])

home = os.getenv('HOME', '/home/wensheng')

bundle_list = open("dot-vim/bundle/README.md")
for line in bundle_list:
    item = line.strip().split()
    if os.path.isdir("dot-vim/bundle/%s" % item[1]):
        os.system("git -C dot-vim/bundle/%s pull" % item[1])
    else:
        os.system("git clone %s dot-vim/bundle/%s" % (item[0], item[1]))

dotfiles=[
    'bashrc',
    'zshrc',
    'zprofile',
    'aliases_common',
    'sh_mac',
    'sh_linux',
    'vimrc',
    'gitconfig',
    'hgrc',
    'dircolors',
    'tmux.conf',
    'vim']

for dotfile in dotfiles:
    dst_file = "%s/.%s" % (home, dotfile)
    if os.path.exists(dst_file):
        if not os.path.islink(dst_file):
            os.rename(dst_file, "%s.bk" % dst_file)
        else:
            continue
    os.symlink("%s/dot-%s" % (cur_dir, dotfile), dst_file)

# os.symlink(f'{cur_dir}/dot-config/lvim/config.lua', f'{os.getenv("HOME")}/.config/lvim/config.lua')

os.system("mkdir -p ~/.config")
dotconfigs = [
  'kitty',
  'nvim',
]

for dotconfig in dotconfigs:
    dst_dir = f'{home}/.config/{dotconfig}'
    if os.path.exists(dst_dir):
        if os.path.islink(dst_dir):
            continue
        os.rename(dst_dir, f"{dst_dir}.bk")
    os.symlink(f'{cur_dir}/dot-config/{dotconfig}', dst_dir)

os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")

