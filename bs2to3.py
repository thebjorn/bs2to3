# -*- coding: utf-8 -*-
import re

replacements = r"""

container-fluid     ,container
row-fluid           ,row
span(\d+)	    ,col-md-\1 col-sm-\1
offset(\d+)         ,col-md-offset-\1 col-sm-offset-\1
brand		    ,navbar-brand
hero-unit	    ,jumbotron
icon-(?!bar)(\w+)   ,glyphicon glyphicon-\1
btn(?!-)	    ,xbtn btn-default
btn-mini	    ,xbtn-xs
btn-small	    ,xbtn-sm
btn-large	    ,xbtn-lg
visible-phone	    ,visible-sm
visible-tablet	    ,visible-md
visible-desktop     ,visible-lg
hidden-phone	    ,hidden-sm
hidden-tablet	    ,hidden-md
hidden-desktop	    ,hidden-lg
input-prepend	    ,input-group
input-append	    ,input-group
add-on		    ,input-group-addon
btn-navbar	    ,navbar-xbtn
thumbnail	    ,img-thumbnail
xbtn                ,btn
"""

replace = []
for line in [line for line in replacements.split('\n') if line.strip()]:
    lhs, rhs = [val.strip() for val in line.split(',')]
    replace.append((r'\b' + lhs + r'\b', rhs))
                


other = r"""
      navbar nav	nav navbar-nav
"""


def convert(txt):
    for k, v in replace:
        print k,v
        #print '\t', txt.strip()
        txt = re.sub(k, v, txt)
        #print '\t', txt.strip()
    return txt


def convert_file(fname):
    with open(fname) as fp:
        txt = fp.read()

    cnv = convert(txt)
    if cnv:
        with open(fname, 'w') as fp:
            fp.write(cnv)
    


if __name__ == "__main__":
    import sys
    convert_file(sys.argv[1])
