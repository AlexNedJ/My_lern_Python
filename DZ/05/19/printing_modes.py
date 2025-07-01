def print_modes(unprindent_desings, compenetd_modes):
    while unprindent_desings:
        current_design =unprindent_desings.pop()
        print(f"Printing mode:{current_design}")
        compenetd_modes.append(current_design)

def show_complited_modes(compenetd_modes):
    print("\nThe foowing modes have been printed")
    for compenetd_mode in compenetd_modes:
        print(compenetd_mode)

def sandwiches(*topings0):
    print(f"{topings0}")