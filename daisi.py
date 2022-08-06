import pydaisi as pyd
text_file_analyzer = pyd.Daisi("oghli/Text File Analyzer")
text_analytics = text_file_analyzer.analyze_text('test.txt').value
print(text_analytics['s'])

