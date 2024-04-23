from transformers import pipeline

question = "How many programming languages does BLOOM support?"
context = """
A requalificação da Ponte de Arame, que une os concelhos de Celorico de Basto e Amarante (distrito do Porto), nas freguesias de Arnoia e Rebordelo, respetivamente, está a decorrer a “bom ritmo” e deverá estar concluída em início de junho.

Em comunicado, a Associação de Municípios do Douro e Tâmega (AMDT), promotora da obra, adianta que ambas as margens já estão “com trabalhos avançados para a união fortificada e com segurança necessária para o seu futuro funcionamento”.

Segundo a presidente do Conselho Diretivo da AMDT, Cristina Vieira, responsável pelo projeto, “os trabalhos da empreitada estão a decorrer de acordo com o previsto no projeto e programa-se a sua conclusão para o início do mês de junho”.

E acrescenta: “Algo que desejamos que aconteça a curto prazo e que vai contribuir para a dinâmica do turismo de natureza deste território”."""

perguntas = ["Onde?", "O quê?", "Como?", "Quando?", "Quem?"]



question_answerer = pipeline("question-answering", model="lfcc/bert-portuguese-squad")

print(context)
print("--------------------------")
for p in perguntas:
    result = question_answerer(question=p, context=context)
    print(p)
    print(f"Score: {result['score']} | {result['answer']}")