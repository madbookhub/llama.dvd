# coding:utf-8
# ----------------------------------------
from modules.proc import *
from modules.procofvectorize import *
# ----------------------------------------
_ = GetReady( CASEOFDOC )
if not _ : exit(1)
TokenLength, NameofDocument = _['token'], _['document']

Chunks = GetContentofDocument( TokenLength, NameofDocument )
if Chunks is None: exit(2)


Embedder = GetEmbedding()
if Embedder.Model is None : exit(3)

Vectors = []
for _ in Chunks:
	_ = ApplyEmbedding( Embedder, _, TokenLength )
	if _ == [None] : exit(4)
	Vectors.append( _ )

SaveVectorization( Vectors, Chunks )

exit(0)
