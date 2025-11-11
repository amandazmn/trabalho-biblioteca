class EmailServiceStub:
    def __init__(self):
        self.enviados = []

    def enviar(self, usuario_id: str, assunto: str, corpo: str):
        self.enviados.append({"usuario": usuario_id, "assunto": assunto, "corpo": corpo})
