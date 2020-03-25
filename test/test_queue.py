from queue import Queue

def test_get_result():
    list_str = list();
    list_str.append("Кто последний? Я - Кузнецов.")
    list_str.append("Кто последний? Я - Поливанов.")
    list_str.append("Следующий!")
    list_str.append("Я только спросить! Я - Иванова.")
    list_str.append("Следующий!")
    list_str.append("Следующий!")
    list_str.append("Следующий!")
    s1 = Queue(list_str)
    assert s1.get_result() == "Заходит Кузнецов!\nЗаходит Петрова!\nЗаходит Иванова!\nЗаходит Поливанов!\nСледующий!"