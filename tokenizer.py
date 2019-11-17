import re
scanner=re.Scanner([
  (r"([0-9]+[\-][0-9]+)", lambda scanner,token:("Endash num", token)),
  (r"[\w\.-]+@[\w\.-]+",  lambda scanner,token:("E-mail", token)),
  (r"([0-9])+",           lambda scanner,token:("Int", token)),
  (r"[A-Za-z]+",          lambda scanner,token:("Word", token)),
  (r"[!?;:,'-]+",         lambda scanner,token:("Punct", token)),
  (r"[\(]",               lambda scanner,token:("LParen", token)),
  (r"[\)]",               lambda scanner,token:("RParen", token)),
  (r"[.]",                lambda scanner,token:("Dot", token)),
  (r"\s\-\s",             lambda scanner,token:("Em dash", token)),
  (r"(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])", lambda scanner,token:("Emoji", token)), #emoji regex, found in internet
  (r"\s+", None), # None == skip token.
])

results, remainder=scanner.scan("dsa@dsa.cd The (San) 9-2 Francisco-based mr. - 123. All variations tested")
print results
