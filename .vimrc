set nocompatible
syntax on
set autochdir
set autoread
set nu
set showcmd
set noshowmatch
set mouse=a
set noswapfile
set nobackup
set laststatus=0
set backspace=2
set shortmess=atI

set tabstop=4
set softtabstop=4
set shiftwidth=4

set autoindent
set smartindent
set encoding=utf-8

call plug#begin('~/.vim/plugged')
Plug 'itchyny/lightline.vim'
Plug 'flazz/vim-colorschemes'
Plug 'liuchengxu/space-vim-dark'
call plug#end()

color space-vim-dark 
hi Normal     ctermbg=NONE guibg=NONE
hi LineNr     ctermbg=NONE guibg=NONE
hi SignColumn ctermbg=NONE guibg=NONE

" python-mode {
let g:pymode_lint_checkers = ['pyflakes']
let g:pymode_trim_whitespaces = 0
let g:pymode_options = 0
let g:pymode_rope = 0
let g:pymode_indent = 1
let g:pymode_folding = 0
let g:pymode_options_colorcolumn = 1
let g:pymode_breakpoint_bind = '<leader>br'
let g:pymode_lint = 1
" }
