from collections import deque

class Queue:
    def __init__(self,  stringList : list):
        self.list_of_command = stringList
        self.dl = deque()
        self.res_list=[]

    def choice(self):
        for i in self.list_of_command:
            if "Следующий" in i:
                self.next()
            elif "Я только спросить!" in i:
                self.add_to_head(i.split('- ')[1].strip('.'))
            elif "Кто последний" in i:
                self.add_to_end(i.split('- ')[1].strip('.'))
                
    def add_to_end(self, string):
        self.dl.append(string)

    def add_to_head(self, string):
        self.dl.appendleft(string)

    def next(self):
        if (len(self.dl))<1:
            self.res_list.append("В очереди никого нет.")
        else:
            self.res_list.append(str("Заходит "+self.dl.popleft()+"!"))

    def get_result(self):
        self.choice()
        return "\n".join(self.res_list)


if __name__== '__main__':
    n = int(input())
    list_str=[]
    for __ in (range(0, n)):
        list_str.append(str(input()))
    # list_str = list();
    # list_str.append("Кто последний? Я - Кузнецов.")
    # #list_str.append("Кто последний? Я - Поливанов.")
    # # list_str.append("Следующий!")
    # list_str.append("Я только спросить! Я - Иванова.")
    # # list_str.append("Я только спросить! Я - Петрова.")
    # list_str.append("Следующий!")
    # # list_str.append("Следующий!")
    # # list_str.append("Следующий!")
    seq = Queue(list_str)
    print(seq.get_result())
