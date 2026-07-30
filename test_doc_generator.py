import doc_generator
import os

def test_flowchart():
    classes, imports = doc_generator.parse_ast("src/regression_model_template/controller/kafka_app.py")
    flowchart = doc_generator.generate_flowchart("kafka_app", imports)

    assert "```mermaid\nflowchart TD" in flowchart
    assert "kafka_app --> collections" in flowchart

test_flowchart()
print("doc_generator logic tests pass")
