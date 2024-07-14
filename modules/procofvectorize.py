# coding:utf-8
# ----------------------------------------
import json
import tiktoken
from modules.globals import *

# ----------------------------------------
# Split the content of document into multiple pieces(chunk)
# ----------------------------------------
def Chunk( TokenLength, Content ):
	Result = []

	SumofLength = 0
	ThisChunk = ''
	
	Encoder = tiktoken.get_encoding("cl100k_base")
	
	Lines = Content.splitlines()  # suppose each line ends with CRLF 
	for Line in Lines:
		# Line = Line.replace(' ', '')
		LineLength = len( Encoder.encode(Line) )

		if LineLength > TokenLength :
			NubmberofParts = - ( -LineLength // TokenLength )
			for i in range( NubmberofParts ):
				Since = i * NubmberofParts
				Till = Since + TokenLength
				# Don't split a word
				while not Line[Since:Till].rstrip().isspace():
					Since, Till = Since+1, Till+1
					if Since >= LineLength : break
				Result.append( Line[Since:Till] )

		if SumofLength + LineLength <= TokenLength:
			SumofLength += LineLength+1
			ThisChunk += Line+'\n'
		else:
			Result.append(ThisChunk)
			SumofLength, ThisChunk = LineLength, Line		

	if len( ThisChunk ) > 0 : Result.append( ThisChunk )

	return [_ for _ in Result if _.strip()]

# ----------------------------------------
def GetContentofDocument( TokenLength, NameofDocument ):
	try:
		with open(NameofDocument, 'r', encoding='utf-8') as _:
			return Chunk( TokenLength, _.read() )
	except:
		return None
	return

# ----------------------------------------
def SaveVectorization( Vectors, Content ):
	with open( f"{VECTORSFOLDER}{VECTORSFILE}", "w", encoding="utf-8" ) as _:
		json.dump( Vectors, _ )

	with open( f"{VECTORSFOLDER}{COMPILEDFILE}", "w", encoding="utf-8" ) as _:
		json.dump( Content, _, ensure_ascii=False )

	return
