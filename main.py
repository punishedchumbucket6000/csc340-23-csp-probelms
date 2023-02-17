from constraint import Problem


def coloring_map():
  p = Problem()
  p.addVariable('WA', ["Red", "Green", "Blue"])
  p.addVariable('NT', ["Red", "Green", "Blue"])
  p.addVariable('SA', ["Red", "Green", "Blue"])
  p.addVariable('Q', ["Red", "Green", "Blue"])
  p.addVariable('NSW', ["Red", "Green", "Blue"])
  p.addVariable('V', ["Red", "Green", "Blue"])
  p.addVariable('T', ["Red", "Green", "Blue"])

  sol1 = p.getSolution()
  print(sol1)

  p.addConstraint(lambda a, b: a != b, ("WA", "SA"))
  p.addConstraint(lambda a, b: a != b, ("NT", "SA"))
  p.addConstraint(lambda a, b: a != b, ("Q", "SA"))
  p.addConstraint(lambda a, b: a != b, ("NSW", "SA"))
  p.addConstraint(lambda a, b: a != b, ("V", "SA"))
  p.addConstraint(lambda a, b: a != b, ("WA", "NT"))
  p.addConstraint(lambda a, b: a != b, ("NT", "Q"))
  p.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
  p.addConstraint(lambda a, b: a != b, ("NSW", "V"))

  sol2 = p.getSolution()
  print(sol2)


def scheduling_problem():
    # Look at "Part 2" instructions and do that here.
    pass




def main():
  coloring_map()
  scheduling_problem()
  

if __name__ == "__main__":
  main()