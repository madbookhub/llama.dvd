# coding:utf-8
# ----------------------------------------
from modules.proc import *
from modules.procofdig import *
from modules.llm import *
# ----------------------------------------
_ = GetReady()
if not _ : exit(1)
OutputMode, QuantityofContext, FreeplayLevel, Richness, Query = \
  _["output"], _["context"], _["freeplay"], _["richness"], _["query"]


Embedder = GetEmbedding()
if Embedder.Model is None : exit(2)

VectorofQuery = ApplyEmbedding( Embedder, Query )
if VectorofQuery == [None] : exit(3)


_ = LoadVectorization()
if _ is None : exit(4)
Vectors, Document = ( _ )

Context = GetContext( QuantityofContext, VectorofQuery, Vectors, Document )
if not isinstance( Context, list ) : exit(5)


if OutputMode == OUTPUT_DIG :
	QuerytoLLM( FreeplayLevel, Richness, Query, Context )
else:
	for _ in Context : print( _ )
	
	if OutputMode == OUTPUT_ALL:
		QuerytoLLM( FreeplayLevel, Richness, Query, Context )


exit(0)
