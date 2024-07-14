# coding:utf-8
# ----------------------------------------
import json
import re
from urllib import request, parse

# ----------------------------------------
PROMPT = """
Please provide a detailed answer (include key points, practical applications, and any relevant examples or case studies) for the question of:\"%s\" ,based on following context:...%s...
"""

# ----------------------------------------
LLM_TEMPERATURE = 0.5
LLM_PREFIX = "data: "
LLM_URL = "http://localhost:8080/completion" 

# ----------------------------------------
def QuerytoLLM( SizeofPrediction, Query, Context ):

	# case of llama.cpp Server service

	# The Transfer-Encoding is used for Stream output (Typewriter mode)
	Headers = {"Content-Type":"application/json", "Transfer-Encoding":"chunked"}

	Content = re.sub( "[\r\n]", '', ''.join(Context) ) # To enhandce inference?

	Body = { "stream":True, "n_predict":SizeofPrediction, "temperature":LLM_TEMPERATURE, "prompt":PROMPT % ( Query, Content ) }

	Data = json.dumps( Body ).encode("utf-8")

	Req = request.Request(url=LLM_URL, headers=Headers, data=Data, method="POST")

	try:
		Rep = request.urlopen( Req ) 
		if Rep.status != 200 : raise Exception()

		while True: # The loop operation is used for Stream output.
			_ = Rep.readline().decode() # cover Binarystream to String

			if _.startswith( LLM_PREFIX ) : _ = _[len(LLM_PREFIX) : ]

			try: _ = json.loads( _ ) # cover String to JSON
			except: continue

			if not ("content" or "stop") in _ or _["stop"] : break

			print(_["content"].rstrip("\n"), end='', flush=True)

		print()
	except:
		pass
	finally:
		if 'Rep' in locals() : Rep.close()

	return
