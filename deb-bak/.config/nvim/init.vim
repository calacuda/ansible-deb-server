inoremap jj <Esc>
set nu!

let g:airline_theme = "pinknord"

let g:tokyonight_transparent = "true"
let g:tokyonight_transparent_sidebar = "true"
let g:tokyonight_dark_sidebar = "false"
" let g:deoplete#enable_at_startup = 1
let g:neomake_python_enabled_makers = ['flake8']
" Enable alignment
let g:neoformat_basic_format_align = 1
" Enable tab to space conversion
let g:neoformat_basic_format_retab = 1
" Enable trimmming of trailing whitespace
let g:neoformat_basic_format_trim = 1
" set highlight duration time to 1000 ms, i.e., 1 second
let g:highlightedyank_highlight_duration = 1000
let g:jellybeans_use_term_italics = 1
let g:jellybeans_overrides = {
\    'background': { 'ctermbg': 'none', '256ctermbg': 'none' },
\}
if has('termguicolors') && &termguicolors
    let g:jellybeans_overrides['background']['guibg'] = 'none'
endif


call plug#begin('~/.config/nvim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vifm/vifm.vim'
Plug 'ap/vim-css-color'
" Plug 'davidhalter/jedi-vim'  "makes things very ugly
" Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
" Plug 'zchee/deoplete-jedi'
Plug 'jiangmiao/auto-pairs'
Plug 'scrooloose/nerdcommenter'
Plug 'sbdchd/neoformat'
Plug 'scrooloose/nerdtree'
Plug 'neomake/neomake'
Plug 'machakann/vim-highlightedyank'
let g:plug_url_format = 'https://git::@github.com/%s.git'
Plug 'nanotech/jellybeans.vim'
unlet g:plug_url_format
call plug#end()

" colorscheme tokyonight
colorscheme jellybeans
