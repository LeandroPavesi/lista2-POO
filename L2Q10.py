def reverte_agenda(agenda):

    nova_agenda = {v: k for k, v in agenda.items()}
    

    return nova_agenda

agenda = {'leandro': '27988186961', 'roberto': '2798726283', 'isabel': '27998196000' }

agenda1 = {'Carlos': '27988189723', 'mariana': '2723456283', 'Marcos': '279968526', 'Antonio': '27988766589' }

print(agenda1)

agenda_nova = reverte_agenda(agenda)

print(agenda_nova)


