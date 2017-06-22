import json


def add_visitors(visitors, file):
    with open(file, "r", -1, "UTF-8") as old_visitors_file:
        old_visitors = json.load(old_visitors_file)
    with open(file, "w", -1, "UTF-8") as new_visitors_file:
        for v in visitors:
            old_visitors["visitors"].append(v)
        json.dump(old_visitors, new_visitors_file)


def send_success_response(visitors):
    positive_response_for_several_persons = "Дорогие %s, мы очень рады, что вы придёте!\n"
    positive_response_for_single_person = "Дорогой(ая) %s, мы очень рады, что Вы придёте!\n"
    negative_response_for_several_persons = "Дорогие %s, нам очень жаль, что вы не придёте!\n"
    negative_response_for_single_persons = "Дорогой(ая) %s, нам очень жаль, что Вы не придёте!\n"

    will_go_persons = []
    wont_go_persons = []
    for v in visitors:
        if v["willGo"]:
            will_go_persons.append(v["name"])
        else:
            wont_go_persons.append(v["name"])

    positive_response = ""
    negative_response = ""
    if len(will_go_persons) > 1:
        positive_response = positive_response + positive_response_for_several_persons % ", ".join(will_go_persons)
    elif len(will_go_persons) == 1:
        positive_response = positive_response + positive_response_for_single_person % ", ".join(will_go_persons)

    if len(wont_go_persons) > 1:
        negative_response = negative_response + negative_response_for_several_persons % ", ".join(wont_go_persons)
    elif len(wont_go_persons) == 1:
        negative_response = negative_response + negative_response_for_single_persons % ", ".join(wont_go_persons)

    result = {"success": "true", "message": "Ваш ответ успешно отправлен!", "positive_desc": positive_response,
              "negative_desc": negative_response}
    print("Content-Type: application/json\n\n")
    print(json.dumps(result))


def send_error_responce(exp):
    result = {"success": "false", "message": "Возникла ошибка при добавлении гостей в список!", "exp": exp}
    print("Content-Type: application/json\n\n")
    print(json.dumps(result))
