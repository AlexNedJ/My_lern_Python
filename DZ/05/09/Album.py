def make_Albums(name, n_albums, paths=''):
    m_albums={
    "name": name,
    "albums": n_albums
    }
    if paths:
        m_albums["path"]=paths

    return m_albums
res=make_Albums("artemc", "Artemys")
print(res)
res=make_Albums("byba", "bybkin_dom", paths='78')
print(res)