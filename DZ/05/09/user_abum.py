def make_Albums(name, n_albums, paths=''):
    m_albums={
    "name": name,
    "albums": n_albums
    }
    if paths:
        m_albums["path"]=paths

    return m_albums


while True:
    name=input("Введите имя автора")
    if name=="exit":
        break
    n_albums=input("Введите название альбома")
    if name=="exit":
        break
    paths=input("Введите количество дорожек в альбоме")
    if name=="exit":
        break
    res=make_Albums(name, n_albums, paths=paths)
    print(res, "\nДля того чтобы завершить програму ввеДите exit")