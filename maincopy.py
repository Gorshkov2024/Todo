class Todo:
    def __init__(self): # Конструктор класса Todo (добавляет словарь дел и счетчики).
        self.issue = {}
        self.count = 0
        self.__count_no_complete = 0
        self.__count_transfer = 0

    def add_issue(self,issue,clock,complete,transfer): # Функция добавляет новое дело
        self.issue[issue] = [clock,complete,transfer] 
        self.init_count()
    
    
    def delete_issue(self,issue): # Функция удаляет дело
        self.issue.pop(issue)
        self.init_count()
        
    def get_count(self): # Функция возвращает общее кол-во дел
        return self.count
     
    @property
    def count_no_complete(self): # Функция возвращает кол-во невыполненных дел
        return self.__count_no_complete 
    
    @property
    def count_transfer(self): # Функция возвращает кол-во перенесенных дел
        return self.__count_transfer
    
    @count_no_complete.setter
    def count_no_complete(self,count_no_complete): # Закладывает значение в кол-во невыполненных дел
        self.__count_no_complete = count_no_complete

    @count_transfer.setter
    def count_transfer(self,count_transfer): #Закладывает в кол-во перенесенных дел
        self.__count_transfer = count_transfer  
        
    
    def change_issue(self,issue): # Функция изменяет состояние дела (выполнено/не выполнено)
        temp = self.issue.get(issue) # (temp) Временная переменная
        if temp[1] == False:
            temp[1] = True
            
        else:    
            temp[1] = False
            
        self.issue.update({issue:temp})
        self.init_count()

    def change_transfer(self,issue): # Функция изменяет состояние дела (перенесено/не перенесено)
        temp = self.issue.get(issue)
        if temp[2] == False:
            temp[2] = True
            
        else:    
            temp[2] = False
            
        self.issue.update({issue:temp})
        self.init_count()

    def init_count(self): # Функция обновляет данные счетчиков на актуальные
        c_complete = 0
        c_transfer = 0
        count = 0
        for value in self.issue.values():
            count +=1
            if value[1] == False:
                c_complete +=1
            if value[2] == True:
                c_transfer +=1
        self.count_no_complete = c_complete
        self.count_transfer = c_transfer
        self.count = count



    def show(self): # Функция выводит инфу о всех делах
        nums = 1
        for key,value in self.issue.items():
            print(f'{nums}.{key} time:{value[0]} {"Vypolneno" if value[1] else "Ne vypolneno"} {"Pereneseno" if value[2] else "Ne pereneseno"}') 
            nums += 1
        print(f'Ne vypolnennye dela: {self.count_no_complete}')
        print(f'Perenesennye dela: {self.count_transfer}') 
        print(f'Obschee kol-vo del: {self.count}')
        

todo = Todo()
todo.add_issue("zavtrak", "8:30", False,False)             
todo.add_issue("uborka", "10:30", False,False)             
todo.add_issue("kopm_kot", "12:30", False,False)    
todo.show()     