class Todo:
    def __init__(self):
        self.issue = {}
        self.count = 0

    def add_issue(self,issue,clock,complete):
        self.issue[issue] = [clock,complete] 
        self.count +=1   
    
    
    def delete_issue(self,issue):
        self.issue.pop(issue) 
        self.count -=1

    def get_count(self):
        return self.count    
    
    def change_issue(self,issue):
        temp = self.issue.get(issue)
        temp[1] = True
        self.issue.update({issue:temp})

    def show(self):
        nums = 1
        for key,value in self.issue.items():
            print(f'{nums}.{key} time:{value[0]} {"Vypolneno" if value[1] else "Ne vypolneno"}')   
        nums += 1

todo = Todo()
todo.add_issue("zavtrak", "8:30", True)             
todo.add_issue("uborka", "10:30", False)             
todo.add_issue("kopm_kot", "12:30", False)    
todo.show()         