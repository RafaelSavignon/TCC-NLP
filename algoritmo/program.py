import spacy

class NERExtractor:
    def __init__(self):
        # Carregue o modelo spaCy apropriado (por exemplo, "pt_core_news_sm" para o Português)
        self.nlp = spacy.load("pt_core_news_sm")
        self.text = ""

    def set_text(self, text):
        # Define a string global
        self.text = text

    def extract_entities(self):
        if not self.text:
            print("Erro: Nenhum texto foi fornecido.")
            return []

        # Processa o texto com o modelo spaCy
        doc = self.nlp(self.text)

        # Extrai as entidades nomeadas
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        return entities

    def load_text_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.set_text(file_content)
                print("Conteúdo do arquivo carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {str(e)}")

# Exemplo de uso da classe
if __name__ == "__main__":
    extractor = NERExtractor()
    arquivo = "exemplo.txt"
    extractor.load_text_from_file(arquivo)

    if extractor.text:
        print("Texto carregado do arquivo:")
        print(extractor.text)
        entidades = extractor.extract_entities()

        if entidades:
            print("\nEntidades Nomeadas encontradas:")
            for entidade, tipo in entidades:
                print(f"Entidade: {entidade}, Tipo: {tipo}")
        else:
            print("Nenhuma entidade nomeada encontrada.")
