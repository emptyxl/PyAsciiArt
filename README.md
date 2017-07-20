# PyAsciiArt  
Convert image to character painting  

## Installation  
You can use `pip` to install this module:  

```python
pip install PyAsciiArt
```

Or download the source code and manual installation:

```python
python setup.py install
```

## Usage  
There are two ways to use this module.  

##### 1.Use this module as scrapt  

```shell
python -m PyAsciiArt example.png

```
The parameters are described below:  

```shell
PyAsciiArt
    Convert image to character painting.

Usage:
    PyAsciiArt.py <file>... [--contrast C_NUMBER]
                            [--resize WIDTH]
                            [-o OUTPUT_FILE]
                            [-r]
    PyAsciiArt.py (-h | --help)
    PyAsciiArt.py --version

Example:
    PyAsciiArt.py example.png
    PyAsciiArt.py example.png --resize 100 -o result.txt
    PyAsciiArt.py example.png --resize 100 --contrast 0.5 -r

Options:
    --contrast C_NUMBER     Change the image contrast.
    --resize WIDTH          Modify image size, keep proportion by default. The unit is pixel.
    -o OUTPUT_FILE          Output filename.
    -r                      Reverse the result, dark background image may get better result
    -h --help               Show help.
    --version               Show version.
```

##### 2.Be imported by other module
```python
from PyAsciiArt import PyAsciiArt

PyAsciiArt.convert('example.png', resize=128, contrast=1.5)
```

The specific usage can see function Annotations.

## Example  
##### original image  
![image](https://github.com/emptyxl/PyAsciiArt/raw/master/PyAsciiArt/example.jpeg)

#### example1
```shell
python -m PyAsciiArt example.png --resize 128 
```

```
=========================================;=;;;;;;;;;;;;;;;=;;;#
=.............................   ..                            ;
=........................ ....    .                            =
=............. ........... .... .. ..                          =
=.......................... ....  ..          #                =
=..........................=. .     .. .     .;                =
=.........................@...  ..  ....     @                 =
=........................$......... . ...   $$                 =
=.......................$$$ ....  . .     -$$;                 =
=...................... $$....... .       $$$                  =
=......................$$$.....          $$$$  %.              =
=.....................#$@ ..... .       $@$$.  -@              =
=.....................$@$ .....         $%@@    @;             =
=....................$@%%......        @@@@$    ##             =
=....................;=#%. ...         #%@@;    ##=            =
=...................=;;=  . ..        ;;;%$     #=##           =
= .......... .......;;== ..           ;;;=@     #==#=          =
= ....... ... ..... ;;=#...          .;;;=-     .;=;##.        =
=.........  .......;;;=              ;;;;=.      ;;;#=         =
=..................;;=#              ;;;==       ;;;;=#        =
=.......   .......;;;=              .;;;#        ;;;=;%        =
=....... .........#;;#  .           =;;=#         ;;;==        =
=.........    .. .=;;@ ..-;#; .     ;;;#          -;;;;        =
=  .. ... ....... ;;#=----;-----;.  ;;=-        - -;;;;        =
=  .. ....  .    .==-----;-;;;;-;-;@;=@.        ; ;-;;;        =
=  .. ....   ..  .;;;;;;-;;;;;;;;;;;;@ .        ;  -;;;        =
=     ...       ;=;;;;;-;;;=####;;;;;=          ;; --;;        =
= .   . ..     @##=;;;;;;=@%---=$==;;;          -- --;=        ;
=     .       @--#%=;;;;#@;-..---$#=;;=         --.--;=        =
=            --...=%=;;=@-.......=%=;;;       ;.;---;;-        =
=            ;....-@=;;%$-.......-$#=;;       ;.;---;;.        ;
=           ;..  ..$%;;#@........-$%=;;@      -;-----;         =
=           @. . ..$%;;@@...$....-@%=;;#      ;------;         =
=           %.   ..$%;;@$........-$%=;;%    . ;------;         =
=           %.....;@=;;%$-.......-$#=;;-    = .-----==         =
=           %-...-$=;;;=@%......-$@#;;=     ;  ------#         =
=           %---#$%;;-;=%%$----;$%=;-;;    .=- -- ;-           =
=            $$$%#=;-;;;=%#@$@@%%=;--;      ;- --  =           =
=            #%##=;;---;;;=#@%%#==;;-;      --.--  #           ;
=            .=#==;-=;;-;;;==#==#=;;;       -----              =
=             =#==;;;;---;;;=======%       =-----              =
=              ;;;;;--=-;;;;======;.       #; --;              =
=               =;-----;;;;;;===@        @ ## .-;              =
=                 ==;;;;=;=%%#;;;@    % =. $=  =               =
=.                       .=#;;==;;.   -   @@   -               =
=. .                     %==;;;;;%%  ; @  @-                   =
=.                     .#-;;;;=;;;@  .-  ;$.                   =
=                      --;;;%-;;;;# $    $                     =
=                     $ --;;--;-;==%                           ;
= .                   . ;---;--;;=@. .               .         ;
=   .                   %;;--;;;;=                .            ;
=                       .%=;;;;;;                              ;
=                         %  .. =;; ..       .                 ;
=                  .......#.....%=.-;..........                ;
;               ......----@-----###;-.........                 ;
=             ........----------;----..........                ;
=              ..........-...-...--............                ;
=                ....=..--...=..;-%..-.-....                   ;
=                    ;. .-.=.-.; .#. @.@..                     ;
=                    ;%  .     =  %  % @                       ;
=                    ;  ..-    = .%. @ @                       ;
= .                  ;    . .. =  %. % @  .                    ;
=                    ;-  =     ;  %# % @                       ;
=                    ;   %  .  ;  %  %.#                       ;
=                    ;         -  %  % .                       ;
;                    ;    = . ..  #  %                         ;
=                    ;    - - =   #  %                         ;
=                    ;   . .% %   =                            ;
=                              . .   ..                        ;
=                            .#  =                             ;
;                           .##                                ;
=                         .. ;                                 ;
=                                                              ;
=                                                              ;
=                                                              ;
=                                                              ;
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

#### example2  

```python
PyAsciiArt.convert('example.jpeg', resize=128, contrast=1.5,
                   reverse=True, output='r_example_ascii.txt')
```

```
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;  $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$   $$$$;   $$$$$$$$$$$$;%;   $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$    $$$$$@#%@#$$$$$$$ %$$@   $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$  $= $$;%; % % $$$$ @$$$$%   $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$  @@ $@$%-@.%;$%   =$$$$$#   $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$ #@@ $%$$$.%  @$$$$@.@$@@=  ;$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$ =%@ $#@%$ =  ;@$$$$@@@%%;  $$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$ . @%$@#@  @# #@$$$$$@@@%#= $$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$  #$$%$%%#% =.@$$$$$$@@@@%# $$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$  %$$$ $@@@@= @$$$$$$$$@%@@%;$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$ -@$$$$# ##= @$$$$$$$$$$$@@%# $$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$-@$$$$$$$$$$@$$$$$$$$$$$$$@@#-@$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$%@@@@@@$$$$$$$$@@@@$$$$$$$$@%; $$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$-%    @@$$$$$@%=   -%@$$$$$$$@#-#$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$#  $$; @@$$$$@= $$$  %$$$$%$$$%# @$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$   %$$$ %@$$$$%  $@$; #@$$-$$@@@% .- $$$$$$$$$$.
.$$$$$$$$$$$$$$$=  =$$= @@$$$$@  $$$  =@$@#.  =@@- ;= $$$$$$$$$.
.$$$$$$$$$$$$$$@#   .- -@$$$$$$- .#-  %@$   $$@@%# %%# $$$$$$$$.
.$$$$$$$$$$$$$- %=    ;@@$$$$$$@.    %@$$ #$$$$$@#.#%##$$$$$$$$.
.$$$$$$$$$$$$==##@%##@$$$$$$$$$$@###%@$$$ $$$$$$@@#. %  $$$$$$$.
.$$$$$$$$$$$=%##%@$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$@@# %   $$$$$$$.
.$$$$$$$$$$@%# =%$$$$$$$$$$$$$$$$$$$$$$=%$$$$$$$@@%    .$$$$$$$.
.$$$$$$$$$$$$% =@$$$$$$$$$$$$$$$$$$$$$$%$$$$$$$@$@%     $$$$$$$.
.$$$$$$$## .%% #%@$$$$$$$$$$$$$$$$$$-$-@$$$$$$$@@%= -   $$$$$$$.
.$$$$$$$$$#%@#.%%@$$$$$$$$$$$$$$$$$. .$ $$$$$$@@@#; =   $$$$$$$.
.$$$$$$$$ @%%% %%@$$$$$$$$$$$$$$$$$.-  @$$$$@$@%#=  =   $$$$$$$.
.$$$$$$$$$=### %%@$$$$$$$$  $$$$$$$ =@;%@@@@@@@==-.   .=$$$$$$$.
.$$$$$$$$$$    #%@$$$$$$$$$$$$$$$$$$##$%%@@@@%##       $$$$$$$$.
.$$$$$$$$$$$$  ;@@@$$$$$$$$$$$$$$$$$$ .;%@%%;##-       $$$$$$$$.
.$$$$$$$$$$$$$$ ##@@$$$$$$$$$$$$$$$$$$@  -.--.    .   $$$$$$$$$.
.$$$$$$$$$$$$$$@-%%$@@$$$$$$$$$$$$$$$$@@@%;          $$$$$$$$$$.
.$$$$$$$$$$$$$$$ =%@@@@$$$$$$$$$$$$$$$$$$%##;;      $$$$$$$$$$$.
.$$$$$$$$$$$$$$$$ ;@@@@@$$$$$$$$$$$$$$$$$@@##      $$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$ #%%$@@@$$$$@$$$$$$@@@@@%=     %$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$- ;%%@@@@@@@%%%%@@@#%#=      $$$$$$$$$$$$$$$-
.$$$$$$$$$$$$$$$$$@@%@ =# ;-###%#==-=#;..-   %%@$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$@@@%%%## -  =;             =#=%@%@@$$$$$$$$$$$$$.
.$$$$$$$$$$$$$@@@@%##=;-  ;;--;;;;; .  -;;==.  #@@@$$$$$$$$$$$$.
.$$$$$$$$$$$$$@@@%%##==;;;;;;;;;;;;  ;;;===#=-.%%@@$$$$$$$$$$$$.
.$$$$$$$$$$$$$@@@%%#%%##=======;=======######%%@%@$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$@@@@@%%%%%%%#####%%%%%%%%%@@@@@@$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@$@@@$@$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$ #$$$$$$$$$$$ $$$ $$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$. %$$$$$$%$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$.- $$$$$$#$$$  $$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$.$ $@$$$$. $$; $ $$$$$$$$$$$$$$$$$$$$$$$-
.$$$$$$$$$$$$$$$$$$$$$$ $ $;$$$$ ;$$#$$@$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$ $.$-$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$ $;$ $$$$ $$$$.$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$  ;$ $$$$ $$$$@$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$; ;$;$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$  $%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$.$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$-$.$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
```