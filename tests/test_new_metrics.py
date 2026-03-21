import unittest
from langchain_core.documents import Document
from src.metrics.context_precision import ContextPrecisionMetric
from src.metrics.answer_relevancy import AnswerRelevancyMetric

class TestNewMetrics(unittest.TestCase):
    def setUp(self):
        # Usamos llama3.1 que es el juez configurado
        self.prec_metric = ContextPrecisionMetric(provider="ollama", model_id="llama3.1")
        self.ans_metric = AnswerRelevancyMetric(provider="ollama", model_id="llama3.1")

    def test_context_precision(self):
        print("\n--- Test Context Precision ---")
        question = "¿Cuál es el pH óptimo para el cultivo de arándanos?"
        
        # Simulamos 3 documentos recuperados
        docs = [
            Document(page_content="El cultivo de arándano requiere suelos ácidos con un pH entre 4.5 y 5.5.", metadata={"source_id": "doc1"}),
            Document(page_content="La producción mundial de arándanos ha crecido un 10% anual.", metadata={"source_id": "doc2"}),
            Document(page_content="Para corregir el pH, se puede usar azufre elemental.", metadata={"source_id": "doc3"})
        ]
        
        result = self.prec_metric.evaluate(question, docs)
        print(f"Resultado Precision: {result}")
        
        self.assertIn("score", result)
        self.assertTrue(0.0 <= result["score"] <= 1.0)
        self.assertIn("relevance_list", result)

    def test_answer_relevancy(self):
        print("\n--- Test Answer Relevancy ---")
        question = "¿Qué clima requiere el café?"
        response = "El café requiere un clima tropical o subtropical, con temperaturas entre 18°C y 24°C y lluvias frecuentes."
        
        result = self.ans_metric.evaluate(question, response)
        print(f"Resultado Relevancy: {result}")
        
        self.assertIn("score", result)
        self.assertTrue(0.0 <= result["score"] <= 1.0)

if __name__ == "__main__":
    unittest.main()
