from nltk import word_tokenize, pos_tag

text="""
As the long row of helium-filled white balloons lifted off one by one into the night sky over Berlin, Tina Krone managed to gulp down a tear and lit a sparkler. “I haven’t seen that many people on the streets for 25 years,” she said, surveying the crowds at Bernauer Strasse.

On 9 November 1989, when she and thousands of other East Berliners streamed across the border into the west shortly before midnight, only those old enough to remember the building of the wall had cried.
"""

text2="""
I was rather good in school. My friends were great and did an awesome job. We had some amazing time and did cool stuff. My first real friend was Hans who just arrived in town. He was very cool. I met him on first day of school what is not a surprise.
"""

tokend = word_tokenize(text2)
res = pos_tag(tokend)

for r in res:
	print(r[0] + ' ' + r[1])
