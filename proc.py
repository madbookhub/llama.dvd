# coding:utf-8
# ----------------------------------------
import argparse
from collections import namedtuple
import torch
from modules.globals import *

# ----------------------------------------
# Common Type
# ----------------------------------------
Embedding = namedtuple("Embedding", ["Model", "Tokenizer"])

# ----------------------------------------
# Try to apply the parameters of this script.
# ----------------------------------------
def GetReady( Case = CASEOFDIG ):

	Result = {}

	ArgParser = argparse.ArgumentParser(description='')
	for _ in ARGS:
		ArgParser.add_argument( ARGS[_][2], ARGS[_][1], type=ARGS[_][0], default=ARGS[_][3])
	Args = ArgParser.parse_args()

	for Name, Value in vars(Args).items():
		if Name == "document" :
			if Case == CASEOFDOC:
				if len(Value) == 0 : return False
				else : Result[Name] = DOCUMENTFOLDER + Value

		elif Name == "query" :
			if Case == CASEOFDIG:
				if len(Value) == 0 : return False
				else : Result[Name] = Value

		elif Name == "token" :
			Result[Name] = DEF_TOKENLENGTH if Value < MIN_TOKENLENGTH else Value

		elif Name == "context" :
			Result[Name] = DEF_QUANTITYOFCONTEXT if Value < DEF_QUANTITYOFCONTEXT else ( MAX_QUANTITYOFCONTEXT if Value > MAX_QUANTITYOFCONTEXT else Value )

		elif Name == "richness" :
			_ = sum(list(map(lambda e:e["predict"] if e["level"]==Value else 0, RICHNESS)))
			if _ > 0 : Result[Name] = _
			else: return False

		elif Name == "freeplay" :
			if MIN_FREEPLAY <= Value <= MAX_FREEPLAY :
				Result[Name] = round( Value/10, 1 )
			else :
				return False

		elif Name == "output" :
			if Value in [OUTPUT_VECTORS, OUTPUT_DIG, OUTPUT_ALL]:
				Result[Name] = Value
			else: return False

		else: pass

	return Result

# ----------------------------------------
def GetEmbedding():
	from transformers import AutoModel, AutoTokenizer

	M, T = None, None

	Device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

	try:
		T = AutoTokenizer.from_pretrained( MODELOFEMBEDDING )
		M = AutoModel.from_pretrained( MODELOFEMBEDDING ).to( Device )
		M.eval()
	except:
		M, T = None, None

	return Embedding(Model=M, Tokenizer=T)

# ----------------------------------------
def ApplyEmbedding( Embedder, Content, TokenLength=DEF_TOKENLENGTH ):
	IsSucc = False

	try:
		Input = Embedder.Tokenizer( [Content], padding=True, truncation=True, max_length=TokenLength, return_tensors="pt" )
		Input = { k: v.to(Embedder.Model.device) for k,v in Input.items() }

		with torch.no_grad():
			Output = Embedder.Model( **Input )
			SentenceEmbedding = Output[0][:, 0]

		SentenceEmbedding = torch.nn.functional.normalize( SentenceEmbedding, p=2, dim=1 )

		IsSucc = True 
	except:
		pass

	return SentenceEmbedding[0].tolist() if IsSucc else [None]
