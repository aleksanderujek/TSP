def factory(classToInstantiate):
  def f(*arg):
    def g():
      return classToInstantiate(*arg)
    return g
  return f