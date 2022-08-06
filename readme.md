# Text File Analyzer (Daisi Hackathon)

Python function as a web service to analyze text file data according to different measures and return detailed information about it.

It will calculate and the following information:
Total number of words, total number of letters, total number of lines, average words per line, average characters per line, average characters per word, most common words, most common letters, unique words, least common letters, longest word, file size in KB.

How to call it from Python:

Step 1 : Load the Daisi

<pre>
import pydaisi as pyd
text_file_analyzer = pyd.Daisi("oghli/Text File Analyzer")
</pre>
Step 2 : call the `text_file_analyzer` end point, passing input file download link to process and analyze text data

<pre>
text_analytics = text_file_analyzer.analyze_text('test.txt').value
text_analytics
</pre>

returns a dictionary containing detailed information about text file.

**Note**: Input text file link should be valid download link of the file.

Step 3 : print text file analysis summary 
<pre>
text_analytics['s']
</pre>

Output look like:
<pre>
____________Summary______________
   File Name: test.txt
   Total words: 365
   Total letters: 1946
   Total lines: 11
   Average words per line: 33.18
   Average characters per line: 214.91
   Average characters per word: 6.48
   Most common words: blockchain, transaction, transactions
   Most common letters: e, t, a
   Longest word: representatives
   Estimate file size: 2.31 KB
</pre>

Finally, **Daisi** is a Cloud Computing platform running Python serverless functions.

For more info check the documentation link: https://doc.daisi.io/
