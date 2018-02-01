# coding=utf-8
from __future__ import absolute_import
from itertools import count
from token import *

from parso._compatibility import py_version

"""
这个文件就是在分配 Token 的序号，N_TOKENS 是系统实现的 Token 的类型数目，
都在这个之后分配就行了
"""

_counter = count(N_TOKENS)
# Never want to see this thing again.
del N_TOKENS

COMMENT = next(_counter)
tok_name[COMMENT] = 'COMMENT'

NL = next(_counter)
tok_name[NL] = 'NL'

# Sets the attributes that don't exist in these tok_name versions.
if py_version >= 30:
    BACKQUOTE = next(_counter)
    tok_name[BACKQUOTE] = 'BACKQUOTE'
else:
    RARROW = next(_counter)
    tok_name[RARROW] = 'RARROW'
    ELLIPSIS = next(_counter)
    tok_name[ELLIPSIS] = 'ELLIPSIS'

if py_version < 35:
    ATEQUAL = next(_counter)
    tok_name[ATEQUAL] = 'ATEQUAL'

ERROR_DEDENT = next(_counter)
tok_name[ERROR_DEDENT] = 'ERROR_DEDENT'


# Map from operator to number (since tokenize doesn't do this)
"""
生成一一对应的 MAP，王垠的 Project 也有类似的用法，都这么懒得么。。。
"""

opmap_raw = """\
( LPAR
) RPAR
[ LSQB
] RSQB
: COLON
, COMMA
; SEMI
+ PLUS
- MINUS
* STAR
/ SLASH
| VBAR
& AMPER
< LESS
> GREATER
= EQUAL
. DOT
% PERCENT
` BACKQUOTE
{ LBRACE
} RBRACE
@ AT
== EQEQUAL
!= NOTEQUAL
<> NOTEQUAL
<= LESSEQUAL
>= GREATEREQUAL
~ TILDE
^ CIRCUMFLEX
<< LEFTSHIFT
>> RIGHTSHIFT
** DOUBLESTAR
+= PLUSEQUAL
-= MINEQUAL
*= STAREQUAL
/= SLASHEQUAL
%= PERCENTEQUAL
&= AMPEREQUAL
|= VBAREQUAL
@= ATEQUAL
^= CIRCUMFLEXEQUAL
<<= LEFTSHIFTEQUAL
>>= RIGHTSHIFTEQUAL
**= DOUBLESTAREQUAL
// DOUBLESLASH
//= DOUBLESLASHEQUAL
-> RARROW
... ELLIPSIS
"""

opmap = {}
for line in opmap_raw.splitlines():
    op, name = line.split()
    opmap[op] = globals()[name]


def generate_token_id(string):
    """
    Uses a token in the grammar (e.g. `'+'` or `'and'`returns the corresponding
    ID for it. The strings are part of the grammar file.
    """
    try:
        return opmap[string]
    except KeyError:
        pass
    return globals()[string]
