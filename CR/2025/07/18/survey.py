class Anonymous_Survey():
    def __init__(self, question):
        self.question = question
        self.responses=[]
        
    def show_question(self):
        print(self.question)

    def stor_respones(self, new_response):
        self.responses.append(new_response)

    def show_Resutls(self):
        print("survay results")
        for respones in self.responses:
            print(f"- {respones}")