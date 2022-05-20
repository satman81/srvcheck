def confGetOrDefault (conf, key, default=None):
    def iteOver(c, k):
        if len(k) == 1:
            out = c[k[0]] if k[0] in c else default
            return int(out) if type(key) == str and out.isdigit() else out
        else:
            ke = k[0]
            k = k[1:]
            return iteOver (c[ke], k) if ke in conf else default
            
    if type(key) == str:
        key = key.split('.')

    return iteOver(conf, key)