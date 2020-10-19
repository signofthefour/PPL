# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3M")
        buf.write("\u01b5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\7\2Z\n\2")
        buf.write("\f\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4x\n\4\f\4\16\4{\13\4\3\4\7\4~\n\4\f")
        buf.write("\4\16\4\u0081\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u0092\n\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0098\n\b\7\b\u009a\n\b\f\b\16\b\u009d\13\b\5\b\u009f")
        buf.write("\n\b\3\b\3\b\3\t\3\t\5\t\u00a5\n\t\3\t\3\t\3\t\5\t\u00aa")
        buf.write("\n\t\7\t\u00ac\n\t\f\t\16\t\u00af\13\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\6\13\u00b7\n\13\r\13\16\13\u00b8\3\13\5")
        buf.write("\13\u00bc\n\13\3\f\3\f\3\f\3\f\5\f\u00c2\n\f\3\f\3\f\6")
        buf.write("\f\u00c6\n\f\r\f\16\f\u00c7\3\r\3\r\5\r\u00cc\n\r\3\r")
        buf.write("\3\r\3\r\5\r\u00d1\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\7\20\u00de\n\20\f\20\16\20\u00e1")
        buf.write("\13\20\3\21\3\21\3\21\7\21\u00e6\n\21\f\21\16\21\u00e9")
        buf.write("\13\21\3\21\7\21\u00ec\n\21\f\21\16\21\u00ef\13\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0104\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u010f")
        buf.write("\n\23\f\23\16\23\u0112\13\23\3\23\3\23\5\23\u0116\n\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\5\30\u013a\n\30\3\30\3\30\3\30\3\31\3\31\3\32\3")
        buf.write("\32\3\33\3\33\3\34\3\34\5\34\u0147\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u0156\n \3")
        buf.write("!\3!\3!\3!\3!\3!\7!\u015e\n!\f!\16!\u0161\13!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\7\"\u0169\n\"\f\"\16\"\u016c\13\"\3#")
        buf.write("\3#\3#\3#\3#\3#\7#\u0174\n#\f#\16#\u0177\13#\3$\3$\3$")
        buf.write("\5$\u017c\n$\3%\3%\3%\5%\u0181\n%\3&\3&\3&\3&\5&\u0187")
        buf.write("\n&\3\'\3\'\5\'\u018b\n\'\3(\3(\3(\3(\3(\5(\u0192\n(\3")
        buf.write(")\3)\3)\5)\u0197\n)\3*\3*\3*\3*\3*\7*\u019e\n*\f*\16*")
        buf.write("\u01a1\13*\7*\u01a3\n*\f*\16*\u01a6\13*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\5+\u01b3\n+\3+\2\5@BD,\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRT\2\b\3\2\4\7\3\2)\63\3\2\'(\3\2\35 \3\2!%\3")
        buf.write("\2\37 \2\u01bb\2[\3\2\2\2\4f\3\2\2\2\6j\3\2\2\2\b\u0085")
        buf.write("\3\2\2\2\n\u0089\3\2\2\2\f\u008b\3\2\2\2\16\u008d\3\2")
        buf.write("\2\2\20\u00a4\3\2\2\2\22\u00b0\3\2\2\2\24\u00bb\3\2\2")
        buf.write("\2\26\u00bd\3\2\2\2\30\u00cb\3\2\2\2\32\u00d2\3\2\2\2")
        buf.write("\34\u00d6\3\2\2\2\36\u00da\3\2\2\2 \u00e7\3\2\2\2\"\u0103")
        buf.write("\3\2\2\2$\u0105\3\2\2\2&\u011a\3\2\2\2(\u011c\3\2\2\2")
        buf.write("*\u0129\3\2\2\2,\u0130\3\2\2\2.\u0139\3\2\2\2\60\u013e")
        buf.write("\3\2\2\2\62\u0140\3\2\2\2\64\u0142\3\2\2\2\66\u0144\3")
        buf.write("\2\2\28\u0148\3\2\2\2:\u014c\3\2\2\2<\u014e\3\2\2\2>\u0155")
        buf.write("\3\2\2\2@\u0157\3\2\2\2B\u0162\3\2\2\2D\u016d\3\2\2\2")
        buf.write("F\u017b\3\2\2\2H\u0180\3\2\2\2J\u0186\3\2\2\2L\u018a\3")
        buf.write("\2\2\2N\u0191\3\2\2\2P\u0196\3\2\2\2R\u0198\3\2\2\2T\u01b2")
        buf.write("\3\2\2\2VW\5\4\3\2WX\7<\2\2XZ\3\2\2\2YV\3\2\2\2Z]\3\2")
        buf.write("\2\2[Y\3\2\2\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\6\4")
        buf.write("\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2c")
        buf.write("a\3\2\2\2de\7\2\2\3e\3\3\2\2\2fg\7\30\2\2gh\7:\2\2hi\5")
        buf.write("\20\t\2i\5\3\2\2\2jk\7\23\2\2kl\7:\2\2lp\7\3\2\2mn\7\25")
        buf.write("\2\2no\7:\2\2oq\5\36\20\2pm\3\2\2\2pq\3\2\2\2qr\3\2\2")
        buf.write("\2rs\7\b\2\2sy\7:\2\2tu\5&\24\2uv\7<\2\2vx\3\2\2\2wt\3")
        buf.write("\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\177\3\2\2\2{y\3")
        buf.write("\2\2\2|~\5\"\22\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2")
        buf.write("\2\2\u0082\u0083\7\17\2\2\u0083\u0084\7;\2\2\u0084\7\3")
        buf.write("\2\2\2\u0085\u0086\7\3\2\2\u0086\u0087\7>\2\2\u0087\u0088")
        buf.write("\5\16\b\2\u0088\t\3\2\2\2\u0089\u008a\t\2\2\2\u008a\13")
        buf.write("\3\2\2\2\u008b\u008c\5\16\b\2\u008c\r\3\2\2\2\u008d\u009e")
        buf.write("\78\2\2\u008e\u0092\5\n\6\2\u008f\u0092\5\f\7\2\u0090")
        buf.write("\u0092\5> \2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u009b\3\2\2\2\u0093\u0097\7=\2\2")
        buf.write("\u0094\u0098\5\n\6\2\u0095\u0098\5\f\7\2\u0096\u0098\5")
        buf.write("> \2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0093\3\2\2\2\u009a")
        buf.write("\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u0091\3")
        buf.write("\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1")
        buf.write("\79\2\2\u00a1\17\3\2\2\2\u00a2\u00a5\5\24\13\2\u00a3\u00a5")
        buf.write("\5\30\r\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00ad\3\2\2\2\u00a6\u00a9\7=\2\2\u00a7\u00aa\5\24\13")
        buf.write("\2\u00a8\u00aa\5\30\r\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\21\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7\3")
        buf.write("\2\2\u00b1\23\3\2\2\2\u00b2\u00b6\7\3\2\2\u00b3\u00b4")
        buf.write("\7\66\2\2\u00b4\u00b5\7\4\2\2\u00b5\u00b7\7\67\2\2\u00b6")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\7")
        buf.write("\3\2\2\u00bb\u00b2\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\25")
        buf.write("\3\2\2\2\u00bd\u00c5\7\3\2\2\u00be\u00c1\7\66\2\2\u00bf")
        buf.write("\u00c2\5\26\f\2\u00c0\u00c2\5> \2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7")
        buf.write("\67\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00be\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\27\3\2\2\2\u00c9\u00cc\5\26\f\2\u00ca\u00cc\5\22")
        buf.write("\n\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00d0\7>\2\2\u00ce\u00d1\5\f\7\2\u00cf")
        buf.write("\u00d1\5\n\6\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1\31\3\2\2\2\u00d2\u00d3\5\26\f\2\u00d3\u00d4\7>")
        buf.write("\2\2\u00d4\u00d5\5\16\b\2\u00d5\33\3\2\2\2\u00d6\u00d7")
        buf.write("\5\22\n\2\u00d7\u00d8\7>\2\2\u00d8\u00d9\5\n\6\2\u00d9")
        buf.write("\35\3\2\2\2\u00da\u00df\5\24\13\2\u00db\u00dc\7=\2\2\u00dc")
        buf.write("\u00de\5\24\13\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\37\3")
        buf.write("\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\5&\24\2\u00e3\u00e4")
        buf.write("\7<\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00ed\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00ec\5")
        buf.write("\"\22\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee!\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\u0104\5$\23\2\u00f1\u0104\5(\25\2")
        buf.write("\u00f2\u0104\5*\26\2\u00f3\u0104\5,\27\2\u00f4\u00f5\5")
        buf.write(".\30\2\u00f5\u00f6\7<\2\2\u00f6\u0104\3\2\2\2\u00f7\u00f8")
        buf.write("\5\60\31\2\u00f8\u00f9\7<\2\2\u00f9\u0104\3\2\2\2\u00fa")
        buf.write("\u00fb\5\62\32\2\u00fb\u00fc\7<\2\2\u00fc\u0104\3\2\2")
        buf.write("\2\u00fd\u00fe\5\64\33\2\u00fe\u00ff\7<\2\2\u00ff\u0104")
        buf.write("\3\2\2\2\u0100\u0101\5\66\34\2\u0101\u0102\7<\2\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u00f0\3\2\2\2\u0103\u00f1\3\2\2\2")
        buf.write("\u0103\u00f2\3\2\2\2\u0103\u00f3\3\2\2\2\u0103\u00f4\3")
        buf.write("\2\2\2\u0103\u00f7\3\2\2\2\u0103\u00fa\3\2\2\2\u0103\u00fd")
        buf.write("\3\2\2\2\u0103\u0100\3\2\2\2\u0104#\3\2\2\2\u0105\u0106")
        buf.write("\7\24\2\2\u0106\u0107\5> \2\u0107\u0108\7\27\2\2\u0108")
        buf.write("\u0110\5 \21\2\u0109\u010a\7\r\2\2\u010a\u010b\5> \2\u010b")
        buf.write("\u010c\7\27\2\2\u010c\u010d\5 \21\2\u010d\u010f\3\2\2")
        buf.write("\2\u010e\u0109\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0115\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0113\u0114\7\f\2\2\u0114\u0116\5 \21\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0118\7\16\2\2\u0118\u0119\7;\2\2\u0119%")
        buf.write("\3\2\2\2\u011a\u011b\5\4\3\2\u011b\'\3\2\2\2\u011c\u011d")
        buf.write("\7\22\2\2\u011d\u011e\7\64\2\2\u011e\u011f\58\35\2\u011f")
        buf.write("\u0120\7=\2\2\u0120\u0121\5:\36\2\u0121\u0122\7=\2\2\u0122")
        buf.write("\u0123\5<\37\2\u0123\u0124\7\65\2\2\u0124\u0125\7\13\2")
        buf.write("\2\u0125\u0126\5 \21\2\u0126\u0127\7\20\2\2\u0127\u0128")
        buf.write("\7;\2\2\u0128)\3\2\2\2\u0129\u012a\7\31\2\2\u012a\u012b")
        buf.write("\5> \2\u012b\u012c\7\13\2\2\u012c\u012d\5 \21\2\u012d")
        buf.write("\u012e\7\21\2\2\u012e\u012f\7;\2\2\u012f+\3\2\2\2\u0130")
        buf.write("\u0131\7\13\2\2\u0131\u0132\5 \21\2\u0132\u0133\7\31\2")
        buf.write("\2\u0133\u0134\5> \2\u0134\u0135\7\34\2\2\u0135\u0136")
        buf.write("\7;\2\2\u0136-\3\2\2\2\u0137\u013a\5\26\f\2\u0138\u013a")
        buf.write("\5\22\n\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d\5> \2\u013d")
        buf.write("/\3\2\2\2\u013e\u013f\7\t\2\2\u013f\61\3\2\2\2\u0140\u0141")
        buf.write("\7\n\2\2\u0141\63\3\2\2\2\u0142\u0143\5R*\2\u0143\65\3")
        buf.write("\2\2\2\u0144\u0146\7\26\2\2\u0145\u0147\5> \2\u0146\u0145")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\67\3\2\2\2\u0148\u0149")
        buf.write("\5\22\n\2\u0149\u014a\7>\2\2\u014a\u014b\5> \2\u014b9")
        buf.write("\3\2\2\2\u014c\u014d\5> \2\u014d;\3\2\2\2\u014e\u014f")
        buf.write("\5> \2\u014f=\3\2\2\2\u0150\u0151\5@!\2\u0151\u0152\t")
        buf.write("\3\2\2\u0152\u0153\5@!\2\u0153\u0156\3\2\2\2\u0154\u0156")
        buf.write("\5@!\2\u0155\u0150\3\2\2\2\u0155\u0154\3\2\2\2\u0156?")
        buf.write("\3\2\2\2\u0157\u0158\b!\1\2\u0158\u0159\5B\"\2\u0159\u015f")
        buf.write("\3\2\2\2\u015a\u015b\f\4\2\2\u015b\u015c\t\4\2\2\u015c")
        buf.write("\u015e\5B\"\2\u015d\u015a\3\2\2\2\u015e\u0161\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160A\3\2\2")
        buf.write("\2\u0161\u015f\3\2\2\2\u0162\u0163\b\"\1\2\u0163\u0164")
        buf.write("\5D#\2\u0164\u016a\3\2\2\2\u0165\u0166\f\4\2\2\u0166\u0167")
        buf.write("\t\5\2\2\u0167\u0169\5D#\2\u0168\u0165\3\2\2\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("C\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\b#\1\2\u016e")
        buf.write("\u016f\5F$\2\u016f\u0175\3\2\2\2\u0170\u0171\f\4\2\2\u0171")
        buf.write("\u0172\t\6\2\2\u0172\u0174\5F$\2\u0173\u0170\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176E\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\7&\2\2")
        buf.write("\u0179\u017c\5F$\2\u017a\u017c\5H%\2\u017b\u0178\3\2\2")
        buf.write("\2\u017b\u017a\3\2\2\2\u017cG\3\2\2\2\u017d\u017e\t\7")
        buf.write("\2\2\u017e\u0181\5H%\2\u017f\u0181\5J&\2\u0180\u017d\3")
        buf.write("\2\2\2\u0180\u017f\3\2\2\2\u0181I\3\2\2\2\u0182\u0183")
        buf.write("\5L\'\2\u0183\u0184\5T+\2\u0184\u0187\3\2\2\2\u0185\u0187")
        buf.write("\5L\'\2\u0186\u0182\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("K\3\2\2\2\u0188\u018b\5R*\2\u0189\u018b\5N(\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018bM\3\2\2\2\u018c\u0192")
        buf.write("\5P)\2\u018d\u018e\7\64\2\2\u018e\u018f\5> \2\u018f\u0190")
        buf.write("\7\65\2\2\u0190\u0192\3\2\2\2\u0191\u018c\3\2\2\2\u0191")
        buf.write("\u018d\3\2\2\2\u0192O\3\2\2\2\u0193\u0197\5\24\13\2\u0194")
        buf.write("\u0197\5\n\6\2\u0195\u0197\5\f\7\2\u0196\u0193\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197Q\3\2\2")
        buf.write("\2\u0198\u0199\7\3\2\2\u0199\u01a4\7\64\2\2\u019a\u019f")
        buf.write("\5> \2\u019b\u019c\7=\2\2\u019c\u019e\5> \2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a2\u019a\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a8\7\65\2\2\u01a8S\3\2\2\2\u01a9\u01aa")
        buf.write("\7\66\2\2\u01aa\u01ab\5> \2\u01ab\u01ac\7\67\2\2\u01ac")
        buf.write("\u01b3\3\2\2\2\u01ad\u01ae\7\66\2\2\u01ae\u01af\5> \2")
        buf.write("\u01af\u01b0\7\67\2\2\u01b0\u01b1\5T+\2\u01b1\u01b3\3")
        buf.write("\2\2\2\u01b2\u01a9\3\2\2\2\u01b2\u01ad\3\2\2\2\u01b3U")
        buf.write("\3\2\2\2)[apy\177\u0091\u0097\u009b\u009e\u00a4\u00a9")
        buf.write("\u00ad\u00b8\u00bb\u00c1\u00c7\u00cb\u00d0\u00df\u00e7")
        buf.write("\u00ed\u0103\u0110\u0115\u0139\u0146\u0155\u015f\u016a")
        buf.write("\u0175\u017b\u0180\u0186\u018a\u0191\u0196\u019f\u01a4")
        buf.write("\u01b2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndIf'", "'EndBody'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'\\%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", 
                     "';'", "','", "'='", "'\"'", "'int_of_float'", "'int_of_string'", 
                     "'float_to_int'", "'float_of_string'", "'bool_of_string'", 
                     "'string_of_bool'", "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>", "ID", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
                      "STRING_LIT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", 
                      "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
                      "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", 
                      "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
                      "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
                      "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", 
                      "DOUBLE_QUOTE", "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_TO_INT", 
                      "FLOAT_OF_STRING", "BOOL_OF_STRING", "STRING_OF_BOOL", 
                      "STRING_OF_INT", "STRING_OF_FLOAT", "COMMENT", "WS", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_function_declare = 2
    RULE_array = 3
    RULE_primitive_data = 4
    RULE_composite_data = 5
    RULE_array_lit = 6
    RULE_var_list = 7
    RULE_scalar_var = 8
    RULE_var_non_init = 9
    RULE_composite_var = 10
    RULE_var_init = 11
    RULE_composite_init = 12
    RULE_primitive_init = 13
    RULE_params_list = 14
    RULE_stmt_list = 15
    RULE_stmt = 16
    RULE_if_stmt = 17
    RULE_var_declare_stmt = 18
    RULE_for_stmt = 19
    RULE_while_stmt = 20
    RULE_dowhile_stmt = 21
    RULE_assign_stmt = 22
    RULE_break_stmt = 23
    RULE_continue_stmt = 24
    RULE_call_stmt = 25
    RULE_return_stmt = 26
    RULE_init_for = 27
    RULE_con_for = 28
    RULE_update_for = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_expr7 = 37
    RULE_expr8 = 38
    RULE_operand = 39
    RULE_function_call = 40
    RULE_index_op = 41

    ruleNames =  [ "program", "var_declare", "function_declare", "array", 
                   "primitive_data", "composite_data", "array_lit", "var_list", 
                   "scalar_var", "var_non_init", "composite_var", "var_init", 
                   "composite_init", "primitive_init", "params_list", "stmt_list", 
                   "stmt", "if_stmt", "var_declare_stmt", "for_stmt", "while_stmt", 
                   "dowhile_stmt", "assign_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "init_for", "con_for", "update_for", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "operand", "function_call", 
                   "index_op" ]

    EOF = Token.EOF
    ID=1
    INT_LIT=2
    FLOAT_LIT=3
    BOOL_LIT=4
    STRING_LIT=5
    BODY=6
    BREAK=7
    CONTINUE=8
    DO=9
    ELSE=10
    ELSEIF=11
    ENDIF=12
    ENDBODY=13
    ENDFOR=14
    ENDWHILE=15
    FOR=16
    FUNCTION=17
    IF=18
    PARAMETER=19
    RETURN=20
    THEN=21
    VAR=22
    WHILE=23
    TRUE=24
    FALSE=25
    ENDDO=26
    PLUS_INT=27
    PLUS_FLOAT=28
    MINUS_INT=29
    MINUS_FLOAT=30
    STAR_INT=31
    STAR_FLOAT=32
    DIV_INT=33
    DIV_FLOAT=34
    MOD=35
    NOT=36
    AND=37
    OR=38
    EQUAL=39
    NOT_EQUAL_INT=40
    LESS_INT=41
    GREATER_INT=42
    LESS_OR_EQUAL_INT=43
    GREATER_OR_EQUAL_INT=44
    NOT_EQUAL_FLOAT=45
    LESS_FLOAT=46
    GREATER_FLOAT=47
    LESS_OR_EQUAL_FLOAT=48
    GREATER_OR_EQUAL_FLOAT=49
    LEFT_PAREN=50
    RIGHT_PAREN=51
    LEFT_BRACKET=52
    RIGHT_BRACKET=53
    LEFT_BRACE=54
    RIGHT_BRACE=55
    COLON=56
    DOT=57
    SEMI=58
    COMMA=59
    ASSIGN=60
    DOUBLE_QUOTE=61
    INT_OF_FLOAT=62
    INT_OF_STRING=63
    FLOAT_TO_INT=64
    FLOAT_OF_STRING=65
    BOOL_OF_STRING=66
    STRING_OF_BOOL=67
    STRING_OF_INT=68
    STRING_OF_FLOAT=69
    COMMENT=70
    WS=71
    ILLEGAL_ESCAPE=72
    UNCLOSE_STRING=73
    UNTERMINATED_COMMENT=74
    ERROR_CHAR=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def function_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 84
                self.var_declare()
                self.state = 85
                self.match(BKITParser.SEMI)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 92
                self.function_declare()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.VAR)
            self.state = 101
            self.match(BKITParser.COLON)
            self.state = 102
            self.var_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def params_list(self):
            return self.getTypedRuleContext(BKITParser.Params_listContext,0)


        def var_declare_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declare_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BKITParser.FUNCTION)
            self.state = 105
            self.match(BKITParser.COLON)
            self.state = 106
            self.match(BKITParser.ID)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 107
                self.match(BKITParser.PARAMETER)
                self.state = 108
                self.match(BKITParser.COLON)
                self.state = 109
                self.params_list()


            self.state = 112
            self.match(BKITParser.BODY)
            self.state = 113
            self.match(BKITParser.COLON)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 114
                self.var_declare_stmt()
                self.state = 115
                self.match(BKITParser.SEMI)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 122
                self.stmt()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(BKITParser.ENDBODY)
            self.state = 129
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BKITParser.ID)
            self.state = 132
            self.match(BKITParser.ASSIGN)
            self.state = 133
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_data" ):
                return visitor.visitPrimitive_data(self)
            else:
                return visitor.visitChildren(self)




    def primitive_data(self):

        localctx = BKITParser.Primitive_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_data" ):
                return visitor.visitComposite_data(self)
            else:
                return visitor.visitChildren(self)




    def composite_data(self):

        localctx = BKITParser.Composite_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_composite_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(BKITParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(BKITParser.RIGHT_BRACE, 0)

        def primitive_data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Primitive_dataContext)
            else:
                return self.getTypedRuleContext(BKITParser.Primitive_dataContext,i)


        def composite_data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Composite_dataContext)
            else:
                return self.getTypedRuleContext(BKITParser.Composite_dataContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(BKITParser.LEFT_BRACE)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 140
                    self.primitive_data()
                    pass

                elif la_ == 2:
                    self.state = 141
                    self.composite_data()
                    pass

                elif la_ == 3:
                    self.state = 142
                    self.expr()
                    pass


                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 145
                    self.match(BKITParser.COMMA)
                    self.state = 149
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 146
                        self.primitive_data()
                        pass

                    elif la_ == 2:
                        self.state = 147
                        self.composite_data()
                        pass

                    elif la_ == 3:
                        self.state = 148
                        self.expr()
                        pass


                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 158
            self.match(BKITParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_non_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_non_initContext,i)


        def var_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 160
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 161
                self.var_init()
                pass


            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 164
                self.match(BKITParser.COMMA)
                self.state = 167
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 165
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 166
                    self.var_init()
                    pass


                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_non_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_non_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_non_init" ):
                return visitor.visitVar_non_init(self)
            else:
                return visitor.visitChildren(self)




    def var_non_init(self):

        localctx = BKITParser.Var_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_non_init)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(BKITParser.ID)
                self.state = 180 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 177
                        self.match(BKITParser.LEFT_BRACKET)
                        self.state = 178
                        self.match(BKITParser.INT_LIT)
                        self.state = 179
                        self.match(BKITParser.RIGHT_BRACKET)

                    else:
                        raise NoViableAltException(self)
                    self.state = 182 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def composite_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Composite_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Composite_varContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_var" ):
                return visitor.visitComposite_var(self)
            else:
                return visitor.visitChildren(self)




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKITParser.ID)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.composite_var()
                    pass

                elif la_ == 2:
                    self.state = 190
                    self.expr()
                    pass


                self.state = 193
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LEFT_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def composite_data(self):
            return self.getTypedRuleContext(BKITParser.Composite_dataContext,0)


        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 199
                self.composite_var()
                pass

            elif la_ == 2:
                self.state = 200
                self.scalar_var()
                pass


            self.state = 203
            self.match(BKITParser.ASSIGN)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.state = 204
                self.composite_data()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.state = 205
                self.primitive_data()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_init" ):
                return visitor.visitComposite_init(self)
            else:
                return visitor.visitChildren(self)




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.composite_var()
            self.state = 209
            self.match(BKITParser.ASSIGN)
            self.state = 210
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primitive_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_init" ):
                return visitor.visitPrimitive_init(self)
            else:
                return visitor.visitChildren(self)




    def primitive_init(self):

        localctx = BKITParser.Primitive_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.scalar_var()
            self.state = 213
            self.match(BKITParser.ASSIGN)
            self.state = 214
            self.primitive_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_non_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_non_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = BKITParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.var_non_init()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 217
                self.match(BKITParser.COMMA)
                self.state = 218
                self.var_non_init()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declare_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 224
                self.var_declare_stmt()
                self.state = 225
                self.match(BKITParser.SEMI)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.stmt() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.Dowhile_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.dowhile_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.assign_stmt()
                self.state = 243
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.break_stmt()
                self.state = 246
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 248
                self.continue_stmt()
                self.state = 249
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.call_stmt()
                self.state = 252
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 254
                self.return_stmt()
                self.state = 255
                self.match(BKITParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(BKITParser.IF)
            self.state = 260
            self.expr()
            self.state = 261
            self.match(BKITParser.THEN)
            self.state = 262
            self.stmt_list()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 263
                self.match(BKITParser.ELSEIF)
                self.state = 264
                self.expr()
                self.state = 265
                self.match(BKITParser.THEN)
                self.state = 266
                self.stmt_list()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 273
                self.match(BKITParser.ELSE)
                self.state = 274
                self.stmt_list()


            self.state = 277
            self.match(BKITParser.ENDIF)
            self.state = 278
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_stmt" ):
                return visitor.visitVar_declare_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_stmt(self):

        localctx = BKITParser.Var_declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_declare_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.var_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def init_for(self):
            return self.getTypedRuleContext(BKITParser.Init_forContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def con_for(self):
            return self.getTypedRuleContext(BKITParser.Con_forContext,0)


        def update_for(self):
            return self.getTypedRuleContext(BKITParser.Update_forContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(BKITParser.FOR)
            self.state = 283
            self.match(BKITParser.LEFT_PAREN)
            self.state = 284
            self.init_for()
            self.state = 285
            self.match(BKITParser.COMMA)
            self.state = 286
            self.con_for()
            self.state = 287
            self.match(BKITParser.COMMA)
            self.state = 288
            self.update_for()
            self.state = 289
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 290
            self.match(BKITParser.DO)
            self.state = 291
            self.stmt_list()
            self.state = 292
            self.match(BKITParser.ENDFOR)
            self.state = 293
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKITParser.WHILE)
            self.state = 296
            self.expr()
            self.state = 297
            self.match(BKITParser.DO)
            self.state = 298
            self.stmt_list()
            self.state = 299
            self.match(BKITParser.ENDWHILE)
            self.state = 300
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stmt" ):
                return visitor.visitDowhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.DO)
            self.state = 303
            self.stmt_list()
            self.state = 304
            self.match(BKITParser.WHILE)
            self.state = 305
            self.expr()
            self.state = 306
            self.match(BKITParser.ENDDO)
            self.state = 307
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 309
                self.composite_var()
                pass

            elif la_ == 2:
                self.state = 310
                self.scalar_var()
                pass


            self.state = 313
            self.match(BKITParser.ASSIGN)

            self.state = 314
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(BKITParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(BKITParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BKITParser.RETURN)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 323
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_forContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = BKITParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.scalar_var()
            self.state = 327
            self.match(BKITParser.ASSIGN)
            self.state = 328
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Con_forContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_con_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCon_for" ):
                return visitor.visitCon_for(self)
            else:
                return visitor.visitChildren(self)




    def con_for(self):

        localctx = BKITParser.Con_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_con_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_forContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_update_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_for" ):
                return visitor.visitUpdate_for(self)
            else:
                return visitor.visitChildren(self)




    def update_for(self):

        localctx = BKITParser.Update_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_update_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expr1Context,i)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL_INT(self):
            return self.getToken(BKITParser.NOT_EQUAL_INT, 0)

        def LESS_INT(self):
            return self.getToken(BKITParser.LESS_INT, 0)

        def GREATER_INT(self):
            return self.getToken(BKITParser.GREATER_INT, 0)

        def LESS_OR_EQUAL_INT(self):
            return self.getToken(BKITParser.LESS_OR_EQUAL_INT, 0)

        def GREATER_OR_EQUAL_INT(self):
            return self.getToken(BKITParser.GREATER_OR_EQUAL_INT, 0)

        def NOT_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.NOT_EQUAL_FLOAT, 0)

        def LESS_FLOAT(self):
            return self.getToken(BKITParser.LESS_FLOAT, 0)

        def GREATER_FLOAT(self):
            return self.getToken(BKITParser.GREATER_FLOAT, 0)

        def LESS_OR_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.LESS_OR_EQUAL_FLOAT, 0)

        def GREATER_OR_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.GREATER_OR_EQUAL_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.expr1(0)
                self.state = 335
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL_INT) | (1 << BKITParser.LESS_INT) | (1 << BKITParser.GREATER_INT) | (1 << BKITParser.LESS_OR_EQUAL_INT) | (1 << BKITParser.GREATER_OR_EQUAL_INT) | (1 << BKITParser.NOT_EQUAL_FLOAT) | (1 << BKITParser.LESS_FLOAT) | (1 << BKITParser.GREATER_FLOAT) | (1 << BKITParser.LESS_OR_EQUAL_FLOAT) | (1 << BKITParser.GREATER_OR_EQUAL_FLOAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 336
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKITParser.Expr1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 344
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 345
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 346
                    self.expr2(0) 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def PLUS_FLOAT(self):
            return self.getToken(BKITParser.PLUS_FLOAT, 0)

        def PLUS_INT(self):
            return self.getToken(BKITParser.PLUS_INT, 0)

        def MINUS_FLOAT(self):
            return self.getToken(BKITParser.MINUS_FLOAT, 0)

        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 355
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 356
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.PLUS_INT) | (1 << BKITParser.PLUS_FLOAT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 357
                    self.expr3(0) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context,0)


        def STAR_INT(self):
            return self.getToken(BKITParser.STAR_INT, 0)

        def STAR_FLOAT(self):
            return self.getToken(BKITParser.STAR_FLOAT, 0)

        def DIV_FLOAT(self):
            return self.getToken(BKITParser.DIV_FLOAT, 0)

        def DIV_INT(self):
            return self.getToken(BKITParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 367
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.STAR_INT) | (1 << BKITParser.STAR_FLOAT) | (1 << BKITParser.DIV_INT) | (1 << BKITParser.DIV_FLOAT) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 368
                    self.expr4() 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = BKITParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr4)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(BKITParser.NOT)
                self.state = 375
                self.expr4()
                pass
            elif token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.MINUS_INT, BKITParser.MINUS_FLOAT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.expr5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def MINUS_FLOAT(self):
            return self.getToken(BKITParser.MINUS_FLOAT, 0)

        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKITParser.Expr6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = BKITParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_INT, BKITParser.MINUS_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                _la = self._input.LA(1)
                if not(_la==BKITParser.MINUS_INT or _la==BKITParser.MINUS_FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 380
                self.expr5()
                pass
            elif token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKITParser.Expr7Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKITParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr6)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.expr7()
                self.state = 385
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def expr8(self):
            return self.getTypedRuleContext(BKITParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKITParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr7)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKITParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr8)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(BKITParser.LEFT_PAREN)
                self.state = 396
                self.expr()
                self.state = 397
                self.match(BKITParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self):
            return self.getTypedRuleContext(BKITParser.Var_non_initContext,0)


        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def composite_data(self):
            return self.getTypedRuleContext(BKITParser.Composite_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_operand)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.var_non_init()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.primitive_data()
                pass
            elif token in [BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.composite_data()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(BKITParser.ID)
            self.state = 407
            self.match(BKITParser.LEFT_PAREN)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 408
                self.expr()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 409
                    self.match(BKITParser.COMMA)
                    self.state = 410
                    self.expr()
                    self.state = 415
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_index_op)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 424
                self.expr()
                self.state = 425
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 428
                self.expr()
                self.state = 429
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 430
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr1_sempred
        self._predicates[32] = self.expr2_sempred
        self._predicates[33] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




