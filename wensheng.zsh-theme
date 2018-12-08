ZSH_THEME_GIT_PROMPT_PREFIX="%{$reset_color%}%{$fg[cyan]%}["
ZSH_THEME_GIT_PROMPT_SUFFIX="]%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg_bold[red]%}✗%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN=""

RPS1='$(git_prompt_info) $EPS1 %{$fg[magenta]%}%D{[%I:%M:%S]}%{$reset_color%} $EPS1'

local NEWLINE=$'\n'
local ret_status="%(?:%{$fg_bold[green]%}♡ :%{$fg_bold[red]%}♥ )"
PROMPT='%{$fg_bold[green]%}%~% ${NEWLINE}${ret_status} %{$fg_bold[cyan]%}%h %{$fg_bold[yellow]%} %n@%m %{$fg[green]%}%B$%b '
