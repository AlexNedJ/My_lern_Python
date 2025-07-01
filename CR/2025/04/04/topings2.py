available_topings=["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
reqyasted_topings=["mushrooms", "extra cheese", "free"]
for t in reqyasted_topings:
    if t in available_topings:
        print(f"Adding '{t}' to your pizza.")
    else:
          print(f"Sorry, we don't have '{t}'.")