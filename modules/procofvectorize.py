# coding:utf-8
# ----------------------------------------
import re
import json
import tiktoken
from modules.globals import *

# ----------------------------------------
# Split the content of document into multiple pieces(chunk)
# ----------------------------------------
def Chunk( SizeofChunk, Content ):

	# Give up if wihtou proper arguments !
	if not isinstance( Content, str ) : return False
	Remain = len( Content )
	if Remain == 0 or SizeofChunk < MIN_TOKENLENGTH : return False

	LengthofOverlap = SizeofChunk // 3 # about 1/3

	Chunks = []

	# Chunk, means splitting the content of document to multi parts, but, how to avoid the mistake of sundering a word while splitting? The first trick is splitting all lines, because each line is a natural separator which splits content without cut any words incorrectly.
	Lines = Content.splitlines()

	for ThisLine in Lines :

		Since, Till, Remain = 0, SizeofChunk-1, len( ThisLine )
		Endding = Remain -1 # index of the lastest character of string
	
		while Remain > 0 :
			if Remain <= SizeofChunk :
				Chunks.append( ThisLine[Since:] )
				Remain = 0
			else:
				Anchor = Till # save it because this pointer will be moved.

				# The second trick is, find out the lastest space, and then take its former content.
				while Till > Since :
					if ThisLine[Till] == chr(32) : break
					else : Till -= 1

				if Till == Since : Till = Anchor # no space? copy all!
				
				Chunk.append( ThisLine[Since:Till+1] ) # don't miss the space.

				Remain -= ( Till - Since +1 )
				# Move the pointer! Be aware that Since and Till may be same.
				Since, Till = Till+1, min( Till+SizeofChunk, Endding )

	return Chunks

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
