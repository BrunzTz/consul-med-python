class Pessoa:

    def __init__(self, nome, endereco, telefone, cpf, sexo, data_nasc, email):

        self.nome = nome,
        self.endereco = endereco,
        self.telefone = telefone,
        self.cpf = cpf,
        self.sexo = sexo,
        self.data_nasc = data_nasc,
        self.email = email
    
    def getNome(self):

        str = ''
        for item in self.nome:
            str = str + item
            return str

    def getEndereco(self):

        str = ''
        for item in self.endereco:
            str = str + item
            return str

    def getTelefone(self):

        str = ''
        for item in self.telefone:
            str = str + item
            return str

    def getCPF(self):

        str = ''
        for item in self.cpf:
            str = str + item
            return str

    def getSexo(self):

        str = ''
        for item in self.sexo:
            str = str + item
            return str

    def getData_nasc(self):

        str = ''
        for item in self.data_nasc:
            str = str + item
            return str

    def getEmail(self):

        return self.email
