# coding:utf-8
# ----------------------------------------
# Global Constants
# ----------------------------------------
CASEOFDOC = 1
CASEOFDIG = 0

MIN_TOKENLENGTH = 128
DEF_TOKENLENGTH = 512

MIN_FREEPLAY = 1
MAX_FREEPLAY = 9
DEF_FREEPLAY = 5

MAX_QUANTITYOFCONTEXT = 5
DEF_QUANTITYOFCONTEXT = 1

OUTPUT_VECTORS = 1
OUTPUT_DIG = 2
OUTPUT_ALL = 3
DEF_OUTPUT = OUTPUT_DIG

RICHNESS = [{"level":1,"predict":30},{"level":2,"predict":70},{"level":3,"predict":128}]
DEF_RICHNESS = 2 # level 2

TOKEN_ENCODING = "cl100k_base"
TOKEN_OVERLAPSIZE = 12

DOCUMENTFOLDER = "documents/"
VECTORSFOLDER = "vectors/"
COMPILEDFILE = "document.json"
VECTORSFILE = "vectors.json"

ARGS = {
		"context" : [int, "--context", "-c", DEF_QUANTITYOFCONTEXT],
		"document" : [str, "--document", "-d", ""],
		"freeplay" : [int, "--freeplay", "-f", DEF_FREEPLAY],
		"output" : [int, "--output", "-o", DEF_OUTPUT],
		"query" : [str, "--query", "-q", ""],
		"richness" : [int, "--richness", "-r", DEF_RICHNESS],
		"token" : [int, "--token", "-t", DEF_TOKENLENGTH],
		}

MODELOFEMBEDDING = "models/embedding"
# ----------------------------------------
