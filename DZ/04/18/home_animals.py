animas={
  'morgan':{
        'owner':'sasha',
        'breed':'Yorkshire Terrier'
  },
    'alya':{
        'owner':'valera',
        'breed':'fox'
    }
}

for anima, animase in animas.items():
    print(f"\nNickname animal: {anima.title()}")

    owner = f"{animase['owner']}"
    breed = animase['breed']

    print(f"\tOwner: {owner.title()}")
    print(f"\tBreed: {breed.title()}")

  