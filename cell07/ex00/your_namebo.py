def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = f" {first.capitallize()} {last.capitalize()}"
        full names.append(full_name)
    return full_names 
persons = {
      "sawittcha": "waritsara"
      "chutinun": "Khamchata"
      "geno": "pancake"
      "pancake": "geno"

}
 
  print(array_of_names(persons))