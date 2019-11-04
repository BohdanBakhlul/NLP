import re
scanner=re.Scanner([
  (r"([0-9]+[\-][0-9]+)", lambda scanner,token:("Endash num", token)),
  (r"([0-9])+",           lambda scanner,token:("Int", token)),
  (r"[A-Za-z]+",          lambda scanner,token:("Word", token)),
  (r"[!?;:,'-]+",         lambda scanner,token:("Punct", token)),
  (r"[\(]",               lambda scanner,token:("LParen", token)),
  (r"[\)]",               lambda scanner,token:("RParen", token)),
  (r"[.]",                lambda scanner,token:("Dot", token)),
  (r"\s\-\s",             lambda scanner,token:("Em dash", token)),
  (r"[\w\.-]+@[\w\.-]+",  lambda scanner,token:("E-mail", token)),
  (r"\s+", None), # None == skip token.
])

results, remainder=scanner.scan("The (San) 9-2 Francisco-bas'ed mr. - 123")
print results
