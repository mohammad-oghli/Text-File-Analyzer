# Text File Analyzer (Daisi Hackathon)

Python function as a web service to analyze text file data according to different measures and return detailed information about it.

It will calculate and return the following information:
Total number of words, total number of letters, total number of lines, average words per line, average characters per line, average characters per word, most common words, most common letters, unique words, least common letters, longest word, file size in KB.

How to call it from Python:

Step 1 : Load the Daisi

<pre>
import pydaisi as pyd
text_file_analyzer = pyd.Daisi("oghli/Text File Analyzer")
</pre>
Step 2 : call the `text_file_analyzer` end point, passing input file download link to process and analyze text data

<pre>
file_link = "https://drive.google.com/uc?export=download&id=1r1Urz_92YixjegWvaW_6cVTJQvGCOmGk"
text_analytics = text_file_analyzer.analyze_text(file_link).value
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
   File Link: https://drive.google.com/uc?export=download&id=1r1Urz_92YixjegWvaW_6cVTJQvGCOmGk
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

Print most common words with number of occurrences in text:
<pre>
text_analytics['top_words']
</pre>

Print most common short words (less than 4 letters) with number of occurrences:
<pre>
text_analytics['top_swords']
</pre>

Print most common letters with number of occurrences:
<pre>
text_analytics['top_chars']
</pre>

Print all unique words:
<pre>
text_analytics['u_words']
</pre>

Print the least used letters:
<pre>
text_analytics['lc_chars']
</pre>

You can also test it on any file link, check this text file sample: 

https://drive.google.com/uc?export=download&id=1cQqW8p9tPHexhwS0Iw_Rs-lBgk8R47ri

You can also call the function using `curl` in **git** command line or **terminal** using the following command:
<pre>
curl -X POST "https://app.daisi.io/pebble-api/pebbles/b82adc6f-6869-4b06-abe9-6d0fedb36ed8/compute/analyze_text" -H "Content-Type: application/json" -d '{"file_url": "_value_"}'
</pre>

just replace the `_value_` with the file link.

Finally, **Daisi** is a Cloud Computing platform running Python serverless functions.

For more info check the documentation link: https://doc.daisi.io/

Don't forget to support me by staring the Daisi if you find it useful.