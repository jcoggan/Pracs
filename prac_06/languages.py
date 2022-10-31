from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [["Python", "Dynamic", True, 1991], ["Ruby", "Dynamic", True, 1995],
                         ["Visual Basic", "Static", False, 1991]]
are_dynamic = []

for programming_language in programming_languages:
    language = ProgrammingLanguage(programming_language[0], programming_language[1], programming_language[2],
                                   programming_language[3])
    if ProgrammingLanguage.is_dynamic(language):
        are_dynamic.append(programming_language[0])
print("The dynamically typed languages are:")
for language in are_dynamic:
    print(language)
