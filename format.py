from yapf.yapflib.yapf_api import FormatFile

FormatFile("length.py", in_place=True)
FormatFile("time.py", in_place=True)
FormatFile("currency.py", in_place=True)

# args parser for cm to mm converter
parser.add_argument('--cm-to-mm', type=float, dest="cm_to_mm")
#demo