from global_defuns import *
import io, hyperscan, argparse

word_set = {'password','1987','admin', 'beautiful', 'love'}
literal_set = {'^(19|20)\d{2}$','^\d{10}$', '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$'}

## Flags
hs_caseless = hyperscan.HS_FLAG_CASELESS
hs_dotall = hyperscan.HS_FLAG_DOTALL
hs_multiline = hyperscan.HS_FLAG_MULTILINE
hs_singlematch = hyperscan.HS_FLAG_SINGLEMATCH
hs_allowempty = hyperscan.HS_FLAG_ALLOWEMPTY
hs_utf8 = hyperscan.HS_FLAG_UTF8
hs_ucp = hyperscan.HS_FLAG_UCP
hs_prefilter = hyperscan.HS_FLAG_PREFILTER
hs_som_leftmost = hyperscan.HS_FLAG_SOM_LEFTMOST
hs_combination = hyperscan.HS_FLAG_COMBINATION
hs_quiet = hyperscan.HS_FLAG_QUIET


def compile_database(pattern_set):
    db = hyperscan.Database()
    ### Compile patterns
    expressions, ids, flags = zip(*patterns)
    db.compile(expressions=expressions, ids=ids, elements=len(patterns), flags=flags)
    print(db.info().decode())

def compile_test():
    db = hyperscan.Database()
    patterns = (
        # expression,  id, flags
        (br'fo+',      0,  0),
        (br'^foobar$', 1,  hyperscan.HS_FLAG_CASELESS),
        (br'BAR',      2,  hyperscan.HS_FLAG_CASELESS | hyperscan.HS_FLAG_SOM_LEFTMOST),
    )
    expressions, ids, flags = zip(*patterns)
    db.compile(expressions=expressions, ids=ids, elements=len(patterns), flags=flags)
    print(db.info().decode())

