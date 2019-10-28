###### Complie Search Terms Into Database, Scan for Matches, and Return with Results
import os, sys, io, hyperscan, argparse

### hyperscan search flags
flagchars = {
    'c': hyperscan.HS_FLAG_CASELESS,
    'd': hyperscan.HS_FLAG_DOTALL,
    'm': hyperscan.HS_FLAG_MULTILINE,
    's': hyperscan.HS_FLAG_SINGLEMATCH,
    'E': hyperscan.HS_FLAG_ALLOWEMPTY,
    'W': hyperscan.HS_FLAG_UCP,
    '8': hyperscan.HS_FLAG_UTF8,
    'P': hyperscan.HS_FLAG_PREFILTER,
    'L': hyperscan.HS_FLAG_SOM_LEFTMOST,
}

### Process each expresion before adding to hyperscan.db
def process_expression(expr):
    expr = expr.strip()
    cpos = expr.find(':')
    lppos = expr.find('/')
    if cpos > lppos:
        id_ = None
    else:
        id_ = int(expr[:cpos])
        if id_ < 0:
            raise TypeError('expression ids must be unsigned')
    rppos = expr.rfind('/')
    expression = expr[lppos + 1:rppos].encode('utf8')
    flags = 0
    for fc in expr[rppos + 1:]:
        flags |= flagchars[fc]
    return id_, expression, flags

### Build hyperscan database from text file
def build_database(expr_path, mode=hyperscan.HS_MODE_STREAM):
    ids = []
    expressions = []
    flags = []
    with io.open(expr_path, 'r') as f:
        for line in f:
            id_, expression, flags_ = process_expression(line)
            ids.append(id_)
            expressions.append(expression)
            flags.append(flags_)
    database = hyperscan.Database(mode=mode)
    database.compile(expressions=expressions, ids=ids, flags=flags,)
    return len(expressions), database

def search_db():
    mode = (hyperscan.HS_MODE_BLOCK if args.block_mode
            else hyperscan.HS_MODE_STREAM)

