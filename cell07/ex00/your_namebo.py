def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = f" {first.capitallize()} {last.capitalize()}"
        full names.append(full_name)
    return full_names 
persons = {
      "phuwin": "waritsara"
      "Tangsakyuen": "Khamchata"
      "Phuwin": "pancake"
      "pancake": "Phuwin"

}
 
  print(array_of_names(persons))