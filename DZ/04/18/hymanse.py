survey={
 'oeksandr':'c++',
 'tatiana':'go',
 'tatiana2':'go',
 'tatiana3':'go',
 'gena':'python',
 'gena2':'python',
 'bybek':'c'
}


survey2={
  'babek':'java', 
  'bibik':'python',
  'bybek':'c++',
  'bebek':'ruby',
}

survey3={
  'bobek':'c',
  'bybyk':'haskell',
  'bubak':'dellfi',
  'babuk':'ruby'  
}

people=[survey,survey2,survey3]

for name in people:
    for n, n_inf in name.items():
        print(f"имя пользователя:{n.title()}\nИзучает: {n_inf}")
        