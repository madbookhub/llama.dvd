# coding:utf-8
# ----------------------------------------
import numpy
import json
from modules.globals import *

# ----------------------------------------
def LoadVectorization():
	try:
		with open( f"{VECTORSFOLDER}{VECTORSFILE}", "r", encoding="utf-8" ) as _:
			Vectors = json.load( _ )

		with open( f"{VECTORSFOLDER}{COMPILEDFILE}", "r", encoding="utf-8" ) as _:
			Document = json.load( _ )

		return Vectors, Document
	except:
		return None

	return

# ----------------------------------------
def GetSimilarity( V1, V2 ):
	p = numpy.dot( V1, V2 )
	Magitude = numpy.linalg.norm(V1) * numpy.linalg.norm(V2)
	return p/Magitude if Magitude else 0

# ----------------------------------------
def GetContext( Quantity, Query, Vectors, Document ):
	if not isinstance(Vectors, list) or not isinstance(Document, list):
		return None

	Match = numpy.array([GetSimilarity(Query, _) for _ in Vectors])

	k = 1 if len(Match) <= Quantity else Quantity

	return numpy.array( Document )[Match.argsort()[-k:][::-1]].tolist()
