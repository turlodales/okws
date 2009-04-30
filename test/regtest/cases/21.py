
desc = "JSON dumps in arrays"

tot = 10

v = [ { "val" : "val-%d" % i } for i in range (0, tot) ]


filedata="""
{$ set { v : %s } $}
{$ for (r, v) {
      print r, "\\n"
   }
$}
""" % v

row="""{"val" : "val-%d", "odd" : %s, "first" : %s, "count" : %d, "even" : %s, "last" : %s, "iter" : %d}"""

def bool2str (b):
    r = "false"
    if b:
        r = "true"
    return r


def mkrow (i, tot):
    return row % (i,
                  bool2str (i % 2 == 1), 
                  bool2str (i == 0),
                  tot,
                  bool2str (i % 2 == 0),
                  bool2str (i == tot - 1),
                  i)
outcome = '\n'.join ( [ mkrow (i, tot) for i in range (0, tot) ] )

   
