# Generated from /home/nguyendat/Documents/projects/PPL/Assignments/assignment2/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u01b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\7\2\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4m\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4t\n\4\f\4\16\4w\13\4\3\4\7\4z\n\4\f\4\16\4}\13\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u008b")
        buf.write("\n\7\3\7\3\7\3\7\5\7\u0090\n\7\7\7\u0092\n\7\f\7\16\7")
        buf.write("\u0095\13\7\5\7\u0097\n\7\3\7\3\7\3\b\3\b\5\b\u009d\n")
        buf.write("\b\3\b\3\b\3\b\5\b\u00a2\n\b\7\b\u00a4\n\b\f\b\16\b\u00a7")
        buf.write("\13\b\3\t\3\t\3\t\3\t\6\t\u00ad\n\t\r\t\16\t\u00ae\3\t")
        buf.write("\5\t\u00b2\n\t\3\n\3\n\3\n\3\n\5\n\u00b8\n\n\3\n\3\n\6")
        buf.write("\n\u00bc\n\n\r\n\16\n\u00bd\3\13\3\13\3\13\3\13\6\13\u00c4")
        buf.write("\n\13\r\13\16\13\u00c5\3\13\5\13\u00c9\n\13\3\13\3\13")
        buf.write("\3\13\5\13\u00ce\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\7\16\u00db\n\16\f\16\16\16\u00de\13\16")
        buf.write("\3\17\3\17\3\17\7\17\u00e3\n\17\f\17\16\17\u00e6\13\17")
        buf.write("\3\17\7\17\u00e9\n\17\f\17\16\17\u00ec\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0101\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u010c\n\21")
        buf.write("\f\21\16\21\u010f\13\21\3\21\3\21\5\21\u0113\n\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\5\26\u0137\n\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3")
        buf.write("\31\3\31\3\32\3\32\5\32\u0144\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u0153")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u015b\n\37\f")
        buf.write("\37\16\37\u015e\13\37\3 \3 \3 \3 \3 \3 \7 \u0166\n \f")
        buf.write(" \16 \u0169\13 \3!\3!\3!\3!\3!\3!\7!\u0171\n!\f!\16!\u0174")
        buf.write("\13!\3\"\3\"\3\"\5\"\u0179\n\"\3#\3#\3#\5#\u017e\n#\3")
        buf.write("$\3$\3$\3$\5$\u0184\n$\3%\3%\5%\u0188\n%\3&\3&\3&\3&\3")
        buf.write("&\5&\u018f\n&\3\'\3\'\3\'\5\'\u0194\n\'\3(\3(\3(\3(\3")
        buf.write("(\7(\u019b\n(\f(\16(\u019e\13(\7(\u01a0\n(\f(\16(\u01a3")
        buf.write("\13(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01b0\n)\3)\2")
        buf.write("\5<>@*\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNP\2\3\3\2\n\r\2\u01b9\2W\3\2")
        buf.write("\2\2\4b\3\2\2\2\6f\3\2\2\2\b\u0081\3\2\2\2\n\u0085\3\2")
        buf.write("\2\2\f\u0087\3\2\2\2\16\u009c\3\2\2\2\20\u00b1\3\2\2\2")
        buf.write("\22\u00b3\3\2\2\2\24\u00c8\3\2\2\2\26\u00cf\3\2\2\2\30")
        buf.write("\u00d3\3\2\2\2\32\u00d7\3\2\2\2\34\u00e4\3\2\2\2\36\u0100")
        buf.write("\3\2\2\2 \u0102\3\2\2\2\"\u0117\3\2\2\2$\u0119\3\2\2\2")
        buf.write("&\u0126\3\2\2\2(\u012d\3\2\2\2*\u0136\3\2\2\2,\u013b\3")
        buf.write("\2\2\2.\u013d\3\2\2\2\60\u013f\3\2\2\2\62\u0141\3\2\2")
        buf.write("\2\64\u0145\3\2\2\2\66\u0149\3\2\2\28\u014b\3\2\2\2:\u0152")
        buf.write("\3\2\2\2<\u0154\3\2\2\2>\u015f\3\2\2\2@\u016a\3\2\2\2")
        buf.write("B\u0178\3\2\2\2D\u017d\3\2\2\2F\u0183\3\2\2\2H\u0187\3")
        buf.write("\2\2\2J\u018e\3\2\2\2L\u0193\3\2\2\2N\u0195\3\2\2\2P\u01af")
        buf.write("\3\2\2\2RS\5\4\3\2ST\7B\2\2TV\3\2\2\2UR\3\2\2\2VY\3\2")
        buf.write("\2\2WU\3\2\2\2WX\3\2\2\2X]\3\2\2\2YW\3\2\2\2Z\\\5\6\4")
        buf.write("\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2")
        buf.write("_]\3\2\2\2`a\7\2\2\3a\3\3\2\2\2bc\7\36\2\2cd\7@\2\2de")
        buf.write("\5\16\b\2e\5\3\2\2\2fg\7\31\2\2gh\7@\2\2hl\7\3\2\2ij\7")
        buf.write("\33\2\2jk\7@\2\2km\5\32\16\2li\3\2\2\2lm\3\2\2\2mn\3\2")
        buf.write("\2\2no\7\16\2\2ou\7@\2\2pq\5\"\22\2qr\7B\2\2rt\3\2\2\2")
        buf.write("sp\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2v{\3\2\2\2wu\3")
        buf.write("\2\2\2xz\5\36\20\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2")
        buf.write("\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\25\2\2\177\u0080\7A\2")
        buf.write("\2\u0080\7\3\2\2\2\u0081\u0082\7\3\2\2\u0082\u0083\7D")
        buf.write("\2\2\u0083\u0084\5\f\7\2\u0084\t\3\2\2\2\u0085\u0086\t")
        buf.write("\2\2\2\u0086\13\3\2\2\2\u0087\u0096\7>\2\2\u0088\u008b")
        buf.write("\5\n\6\2\u0089\u008b\5\f\7\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u0093\3\2\2\2\u008c\u008f\7C\2\2")
        buf.write("\u008d\u0090\5\n\6\2\u008e\u0090\5\f\7\2\u008f\u008d\3")
        buf.write("\2\2\2\u008f\u008e\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008c")
        buf.write("\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0096\u008a\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u0099\7?\2\2\u0099\r\3\2\2\2\u009a\u009d")
        buf.write("\5\20\t\2\u009b\u009d\5\24\13\2\u009c\u009a\3\2\2\2\u009c")
        buf.write("\u009b\3\2\2\2\u009d\u00a5\3\2\2\2\u009e\u00a1\7C\2\2")
        buf.write("\u009f\u00a2\5\20\t\2\u00a0\u00a2\5\24\13\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3")
        buf.write("\u009e\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00a5\3\2")
        buf.write("\2\2\u00a8\u00ac\7\3\2\2\u00a9\u00aa\7<\2\2\u00aa\u00ab")
        buf.write("\7\n\2\2\u00ab\u00ad\7=\2\2\u00ac\u00a9\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b2\3\2\2\2\u00b0\u00b2\7\3\2\2\u00b1\u00a8\3")
        buf.write("\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\21\3\2\2\2\u00b3\u00bb")
        buf.write("\7\3\2\2\u00b4\u00b7\7<\2\2\u00b5\u00b8\5\22\n\2\u00b6")
        buf.write("\u00b8\5:\36\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7=\2\2\u00ba\u00bc\3")
        buf.write("\2\2\2\u00bb\u00b4\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\23\3\2\2\2\u00bf\u00c3")
        buf.write("\7\3\2\2\u00c0\u00c1\7<\2\2\u00c1\u00c2\7\n\2\2\u00c2")
        buf.write("\u00c4\7=\2\2\u00c3\u00c0\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c9\3")
        buf.write("\2\2\2\u00c7\u00c9\7\3\2\2\u00c8\u00bf\3\2\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cd\7D\2\2\u00cb")
        buf.write("\u00ce\5\f\7\2\u00cc\u00ce\5\n\6\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00cc\3\2\2\2\u00ce\25\3\2\2\2\u00cf\u00d0\5\22")
        buf.write("\n\2\u00d0\u00d1\7D\2\2\u00d1\u00d2\5\f\7\2\u00d2\27\3")
        buf.write("\2\2\2\u00d3\u00d4\7\3\2\2\u00d4\u00d5\7D\2\2\u00d5\u00d6")
        buf.write("\5\n\6\2\u00d6\31\3\2\2\2\u00d7\u00dc\5\20\t\2\u00d8\u00d9")
        buf.write("\7C\2\2\u00d9\u00db\5\20\t\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\33\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\5\"")
        buf.write("\22\2\u00e0\u00e1\7B\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00df")
        buf.write("\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00ea\3\2\2\2\u00e6\u00e4\3\2\2\2")
        buf.write("\u00e7\u00e9\5\36\20\2\u00e8\u00e7\3\2\2\2\u00e9\u00ec")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\35\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u0101\5 \21\2\u00ee")
        buf.write("\u0101\5$\23\2\u00ef\u0101\5&\24\2\u00f0\u0101\5(\25\2")
        buf.write("\u00f1\u00f2\5*\26\2\u00f2\u00f3\7B\2\2\u00f3\u0101\3")
        buf.write("\2\2\2\u00f4\u00f5\5,\27\2\u00f5\u00f6\7B\2\2\u00f6\u0101")
        buf.write("\3\2\2\2\u00f7\u00f8\5.\30\2\u00f8\u00f9\7B\2\2\u00f9")
        buf.write("\u0101\3\2\2\2\u00fa\u00fb\5\60\31\2\u00fb\u00fc\7B\2")
        buf.write("\2\u00fc\u0101\3\2\2\2\u00fd\u00fe\5\62\32\2\u00fe\u00ff")
        buf.write("\7B\2\2\u00ff\u0101\3\2\2\2\u0100\u00ed\3\2\2\2\u0100")
        buf.write("\u00ee\3\2\2\2\u0100\u00ef\3\2\2\2\u0100\u00f0\3\2\2\2")
        buf.write("\u0100\u00f1\3\2\2\2\u0100\u00f4\3\2\2\2\u0100\u00f7\3")
        buf.write("\2\2\2\u0100\u00fa\3\2\2\2\u0100\u00fd\3\2\2\2\u0101\37")
        buf.write("\3\2\2\2\u0102\u0103\7\32\2\2\u0103\u0104\5:\36\2\u0104")
        buf.write("\u0105\7\35\2\2\u0105\u010d\5\34\17\2\u0106\u0107\7\23")
        buf.write("\2\2\u0107\u0108\5:\36\2\u0108\u0109\7\35\2\2\u0109\u010a")
        buf.write("\5\34\17\2\u010a\u010c\3\2\2\2\u010b\u0106\3\2\2\2\u010c")
        buf.write("\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010e\u0112\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\7")
        buf.write("\22\2\2\u0111\u0113\5\34\17\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7\24\2")
        buf.write("\2\u0115\u0116\7A\2\2\u0116!\3\2\2\2\u0117\u0118\5\4\3")
        buf.write("\2\u0118#\3\2\2\2\u0119\u011a\7\30\2\2\u011a\u011b\7:")
        buf.write("\2\2\u011b\u011c\5\64\33\2\u011c\u011d\7C\2\2\u011d\u011e")
        buf.write("\5\66\34\2\u011e\u011f\7C\2\2\u011f\u0120\58\35\2\u0120")
        buf.write("\u0121\7;\2\2\u0121\u0122\7\21\2\2\u0122\u0123\5\34\17")
        buf.write("\2\u0123\u0124\7\26\2\2\u0124\u0125\7A\2\2\u0125%\3\2")
        buf.write("\2\2\u0126\u0127\7\37\2\2\u0127\u0128\5:\36\2\u0128\u0129")
        buf.write("\7\21\2\2\u0129\u012a\5\34\17\2\u012a\u012b\7\27\2\2\u012b")
        buf.write("\u012c\7A\2\2\u012c\'\3\2\2\2\u012d\u012e\7\21\2\2\u012e")
        buf.write("\u012f\5\34\17\2\u012f\u0130\7\37\2\2\u0130\u0131\5:\36")
        buf.write("\2\u0131\u0132\7\"\2\2\u0132\u0133\7A\2\2\u0133)\3\2\2")
        buf.write("\2\u0134\u0137\5\22\n\2\u0135\u0137\7\3\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\7D\2\2\u0139\u013a\5:\36\2\u013a+\3\2\2\2\u013b")
        buf.write("\u013c\7\17\2\2\u013c-\3\2\2\2\u013d\u013e\7\20\2\2\u013e")
        buf.write("/\3\2\2\2\u013f\u0140\5N(\2\u0140\61\3\2\2\2\u0141\u0143")
        buf.write("\7\34\2\2\u0142\u0144\5:\36\2\u0143\u0142\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\63\3\2\2\2\u0145\u0146\7\3\2\2\u0146")
        buf.write("\u0147\7D\2\2\u0147\u0148\5:\36\2\u0148\65\3\2\2\2\u0149")
        buf.write("\u014a\5:\36\2\u014a\67\3\2\2\2\u014b\u014c\5:\36\2\u014c")
        buf.write("9\3\2\2\2\u014d\u014e\5<\37\2\u014e\u014f\7\4\2\2\u014f")
        buf.write("\u0150\5<\37\2\u0150\u0153\3\2\2\2\u0151\u0153\5<\37\2")
        buf.write("\u0152\u014d\3\2\2\2\u0152\u0151\3\2\2\2\u0153;\3\2\2")
        buf.write("\2\u0154\u0155\b\37\1\2\u0155\u0156\5> \2\u0156\u015c")
        buf.write("\3\2\2\2\u0157\u0158\f\4\2\2\u0158\u0159\7\5\2\2\u0159")
        buf.write("\u015b\5> \2\u015a\u0157\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d=\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015f\u0160\b \1\2\u0160\u0161\5@!\2\u0161")
        buf.write("\u0167\3\2\2\2\u0162\u0163\f\4\2\2\u0163\u0164\7\6\2\2")
        buf.write("\u0164\u0166\5@!\2\u0165\u0162\3\2\2\2\u0166\u0169\3\2")
        buf.write("\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168?\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\b!\1\2\u016b\u016c")
        buf.write("\5B\"\2\u016c\u0172\3\2\2\2\u016d\u016e\f\4\2\2\u016e")
        buf.write("\u016f\7\7\2\2\u016f\u0171\5B\"\2\u0170\u016d\3\2\2\2")
        buf.write("\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3")
        buf.write("\2\2\2\u0173A\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176")
        buf.write("\7\b\2\2\u0176\u0179\5B\"\2\u0177\u0179\5D#\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179C\3\2\2\2\u017a\u017b")
        buf.write("\7\t\2\2\u017b\u017e\5D#\2\u017c\u017e\5F$\2\u017d\u017a")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017eE\3\2\2\2\u017f\u0180")
        buf.write("\5H%\2\u0180\u0181\5P)\2\u0181\u0184\3\2\2\2\u0182\u0184")
        buf.write("\5H%\2\u0183\u017f\3\2\2\2\u0183\u0182\3\2\2\2\u0184G")
        buf.write("\3\2\2\2\u0185\u0188\5N(\2\u0186\u0188\5J&\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0186\3\2\2\2\u0188I\3\2\2\2\u0189\u018f")
        buf.write("\5L\'\2\u018a\u018b\7:\2\2\u018b\u018c\5:\36\2\u018c\u018d")
        buf.write("\7;\2\2\u018d\u018f\3\2\2\2\u018e\u0189\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018fK\3\2\2\2\u0190\u0194\5\20\t\2\u0191")
        buf.write("\u0194\5\n\6\2\u0192\u0194\5\f\7\2\u0193\u0190\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194M\3\2\2")
        buf.write("\2\u0195\u0196\7\3\2\2\u0196\u01a1\7:\2\2\u0197\u019c")
        buf.write("\5:\36\2\u0198\u0199\7C\2\2\u0199\u019b\5:\36\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3")
        buf.write("\2\2\2\u019f\u0197\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\7;\2\2\u01a5O\3\2\2\2\u01a6")
        buf.write("\u01a7\7<\2\2\u01a7\u01a8\5:\36\2\u01a8\u01a9\7=\2\2\u01a9")
        buf.write("\u01b0\3\2\2\2\u01aa\u01ab\7<\2\2\u01ab\u01ac\5:\36\2")
        buf.write("\u01ac\u01ad\7=\2\2\u01ad\u01ae\5P)\2\u01ae\u01b0\3\2")
        buf.write("\2\2\u01af\u01a6\3\2\2\2\u01af\u01aa\3\2\2\2\u01b0Q\3")
        buf.write("\2\2\2*W]lu{\u008a\u008f\u0093\u0096\u009c\u00a1\u00a5")
        buf.write("\u00ae\u00b1\u00b7\u00bd\u00c5\u00c8\u00cd\u00dc\u00e4")
        buf.write("\u00ea\u0100\u010d\u0112\u0136\u0143\u0152\u015c\u0167")
        buf.write("\u0172\u0178\u017d\u0183\u0187\u018e\u0193\u019c\u01a1")
        buf.write("\u01af")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndIf'", "'EndBody'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "':'", "'.'", "';'", "','", "'='", "'\"'", 
                     "'int_of_float'", "'int_of_string'", "'float_to_int'", 
                     "'float_of_string'", "'bool_of_string'", "'string_of_bool'", 
                     "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>", "ID", "REL_OP", "BIN_LOGICAL_OP", "ADD_OP", 
                      "MUL_OP", "UN_LOGICAL_OP", "UN_OP", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STRING_LIT", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                      "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", 
                      "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
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
    RULE_array_lit = 5
    RULE_var_list = 6
    RULE_var_non_init = 7
    RULE_composite_var = 8
    RULE_var_init = 9
    RULE_composite_init = 10
    RULE_primitive_init = 11
    RULE_params_list = 12
    RULE_stmt_list = 13
    RULE_stmt = 14
    RULE_if_stmt = 15
    RULE_var_declare_stmt = 16
    RULE_for_stmt = 17
    RULE_while_stmt = 18
    RULE_dowhile_stmt = 19
    RULE_assign_stmt = 20
    RULE_break_stmt = 21
    RULE_continue_stmt = 22
    RULE_call_stmt = 23
    RULE_return_stmt = 24
    RULE_init_for = 25
    RULE_con_for = 26
    RULE_update_for = 27
    RULE_expr = 28
    RULE_expr1 = 29
    RULE_expr2 = 30
    RULE_expr3 = 31
    RULE_expr4 = 32
    RULE_expr5 = 33
    RULE_expr6 = 34
    RULE_expr7 = 35
    RULE_expr8 = 36
    RULE_operand = 37
    RULE_function_call = 38
    RULE_index_op = 39

    ruleNames =  [ "program", "var_declare", "function_declare", "array", 
                   "primitive_data", "array_lit", "var_list", "var_non_init", 
                   "composite_var", "var_init", "composite_init", "primitive_init", 
                   "params_list", "stmt_list", "stmt", "if_stmt", "var_declare_stmt", 
                   "for_stmt", "while_stmt", "dowhile_stmt", "assign_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "return_stmt", 
                   "init_for", "con_for", "update_for", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "operand", "function_call", "index_op" ]

    EOF = Token.EOF
    ID=1
    REL_OP=2
    BIN_LOGICAL_OP=3
    ADD_OP=4
    MUL_OP=5
    UN_LOGICAL_OP=6
    UN_OP=7
    INT_LIT=8
    FLOAT_LIT=9
    BOOL_LIT=10
    STRING_LIT=11
    BODY=12
    BREAK=13
    CONTINUE=14
    DO=15
    ELSE=16
    ELSEIF=17
    ENDIF=18
    ENDBODY=19
    ENDFOR=20
    ENDWHILE=21
    FOR=22
    FUNCTION=23
    IF=24
    PARAMETER=25
    RETURN=26
    THEN=27
    VAR=28
    WHILE=29
    TRUE=30
    FALSE=31
    ENDDO=32
    PLUS_INT=33
    PLUS_FLOAT=34
    MINUS_INT=35
    MINUS_FLOAT=36
    STAR_INT=37
    STAR_FLOAT=38
    DIV_INT=39
    DIV_FLOAT=40
    MOD=41
    NOT=42
    AND=43
    OR=44
    EQUAL=45
    NOT_EQUAL_INT=46
    LESS_INT=47
    GREATER_INT=48
    LESS_OR_EQUAL_INT=49
    GREATER_OR_EQUAL_INT=50
    NOT_EQUAL_FLOAT=51
    LESS_FLOAT=52
    GREATER_FLOAT=53
    LESS_OR_EQUAL_FLOAT=54
    GREATER_OR_EQUAL_FLOAT=55
    LEFT_PAREN=56
    RIGHT_PAREN=57
    LEFT_BRACKET=58
    RIGHT_BRACKET=59
    LEFT_BRACE=60
    RIGHT_BRACE=61
    COLON=62
    DOT=63
    SEMI=64
    COMMA=65
    ASSIGN=66
    DOUBLE_QUOTE=67
    INT_OF_FLOAT=68
    INT_OF_STRING=69
    FLOAT_TO_INT=70
    FLOAT_OF_STRING=71
    BOOL_OF_STRING=72
    STRING_OF_BOOL=73
    STRING_OF_INT=74
    STRING_OF_FLOAT=75
    COMMENT=76
    WS=77
    ILLEGAL_ESCAPE=78
    UNCLOSE_STRING=79
    UNTERMINATED_COMMENT=80
    ERROR_CHAR=81

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




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 80
                self.var_declare()
                self.state = 81
                self.match(BKITParser.SEMI)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 88
                self.function_declare()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.VAR)
            self.state = 97
            self.match(BKITParser.COLON)
            self.state = 98
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




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.FUNCTION)
            self.state = 101
            self.match(BKITParser.COLON)
            self.state = 102
            self.match(BKITParser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 103
                self.match(BKITParser.PARAMETER)
                self.state = 104
                self.match(BKITParser.COLON)
                self.state = 105
                self.params_list()


            self.state = 108
            self.match(BKITParser.BODY)
            self.state = 109
            self.match(BKITParser.COLON)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 110
                self.var_declare_stmt()
                self.state = 111
                self.match(BKITParser.SEMI)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 118
                self.stmt()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(BKITParser.ENDBODY)
            self.state = 125
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




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BKITParser.ID)
            self.state = 128
            self.match(BKITParser.ASSIGN)
            self.state = 129
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




    def primitive_data(self):

        localctx = BKITParser.Primitive_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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


        def array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_litContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_litContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BKITParser.LEFT_BRACE)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 136
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                    self.state = 134
                    self.primitive_data()
                    pass
                elif token in [BKITParser.LEFT_BRACE]:
                    self.state = 135
                    self.array_lit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 138
                    self.match(BKITParser.COMMA)
                    self.state = 141
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                        self.state = 139
                        self.primitive_data()
                        pass
                    elif token in [BKITParser.LEFT_BRACE]:
                        self.state = 140
                        self.array_lit()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 150
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




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 152
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 153
                self.var_init()
                pass


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 156
                self.match(BKITParser.COMMA)
                self.state = 159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 157
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 158
                    self.var_init()
                    pass


                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def var_non_init(self):

        localctx = BKITParser.Var_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_non_init)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(BKITParser.ID)
                self.state = 170 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 167
                        self.match(BKITParser.LEFT_BRACKET)
                        self.state = 168
                        self.match(BKITParser.INT_LIT)
                        self.state = 169
                        self.match(BKITParser.RIGHT_BRACKET)

                    else:
                        raise NoViableAltException(self)
                    self.state = 172 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(BKITParser.ID)
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 181
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.composite_var()
                    pass

                elif la_ == 2:
                    self.state = 180
                    self.expr()
                    pass


                self.state = 183
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 187 
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


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
            return BKITParser.RULE_var_init




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 189
                self.match(BKITParser.ID)
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 190
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 191
                    self.match(BKITParser.INT_LIT)
                    self.state = 192
                    self.match(BKITParser.RIGHT_BRACKET)
                    self.state = 195 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.LEFT_BRACKET):
                        break

                pass

            elif la_ == 2:
                self.state = 197
                self.match(BKITParser.ID)
                pass


            self.state = 200
            self.match(BKITParser.ASSIGN)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.state = 201
                self.array_lit()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.state = 202
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




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.composite_var()
            self.state = 206
            self.match(BKITParser.ASSIGN)
            self.state = 207
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primitive_init




    def primitive_init(self):

        localctx = BKITParser.Primitive_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKITParser.ID)
            self.state = 210
            self.match(BKITParser.ASSIGN)
            self.state = 211
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




    def params_list(self):

        localctx = BKITParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.var_non_init()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 214
                self.match(BKITParser.COMMA)
                self.state = 215
                self.var_non_init()
                self.state = 220
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




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 221
                self.var_declare_stmt()
                self.state = 222
                self.match(BKITParser.SEMI)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    self.stmt() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.dowhile_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.assign_stmt()
                self.state = 240
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 242
                self.break_stmt()
                self.state = 243
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 245
                self.continue_stmt()
                self.state = 246
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 248
                self.call_stmt()
                self.state = 249
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 251
                self.return_stmt()
                self.state = 252
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




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(BKITParser.IF)
            self.state = 257
            self.expr()
            self.state = 258
            self.match(BKITParser.THEN)
            self.state = 259
            self.stmt_list()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 260
                self.match(BKITParser.ELSEIF)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(BKITParser.THEN)
                self.state = 263
                self.stmt_list()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 270
                self.match(BKITParser.ELSE)
                self.state = 271
                self.stmt_list()


            self.state = 274
            self.match(BKITParser.ENDIF)
            self.state = 275
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




    def var_declare_stmt(self):

        localctx = BKITParser.Var_declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_declare_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
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




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(BKITParser.FOR)
            self.state = 280
            self.match(BKITParser.LEFT_PAREN)
            self.state = 281
            self.init_for()
            self.state = 282
            self.match(BKITParser.COMMA)
            self.state = 283
            self.con_for()
            self.state = 284
            self.match(BKITParser.COMMA)
            self.state = 285
            self.update_for()
            self.state = 286
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 287
            self.match(BKITParser.DO)
            self.state = 288
            self.stmt_list()
            self.state = 289
            self.match(BKITParser.ENDFOR)
            self.state = 290
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




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKITParser.WHILE)
            self.state = 293
            self.expr()
            self.state = 294
            self.match(BKITParser.DO)
            self.state = 295
            self.stmt_list()
            self.state = 296
            self.match(BKITParser.ENDWHILE)
            self.state = 297
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




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.DO)
            self.state = 300
            self.stmt_list()
            self.state = 301
            self.match(BKITParser.WHILE)
            self.state = 302
            self.expr()
            self.state = 303
            self.match(BKITParser.ENDDO)
            self.state = 304
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


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 306
                self.composite_var()
                pass

            elif la_ == 2:
                self.state = 307
                self.match(BKITParser.ID)
                pass


            self.state = 310
            self.match(BKITParser.ASSIGN)

            self.state = 311
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




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
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




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
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




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKITParser.RETURN)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.UN_LOGICAL_OP) | (1 << BKITParser.UN_OP) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 320
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_for




    def init_for(self):

        localctx = BKITParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(BKITParser.ID)
            self.state = 324
            self.match(BKITParser.ASSIGN)
            self.state = 325
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




    def con_for(self):

        localctx = BKITParser.Con_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_con_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
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




    def update_for(self):

        localctx = BKITParser.Update_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_update_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
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


        def REL_OP(self):
            return self.getToken(BKITParser.REL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.expr1(0)
                self.state = 332
                self.match(BKITParser.REL_OP)
                self.state = 333
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
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


        def BIN_LOGICAL_OP(self):
            return self.getToken(BKITParser.BIN_LOGICAL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 341
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 342
                    self.match(BKITParser.BIN_LOGICAL_OP)
                    self.state = 343
                    self.expr2(0) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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


        def ADD_OP(self):
            return self.getToken(BKITParser.ADD_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    self.match(BKITParser.ADD_OP)
                    self.state = 354
                    self.expr3(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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


        def MUL_OP(self):
            return self.getToken(BKITParser.MUL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    self.match(BKITParser.MUL_OP)
                    self.state = 365
                    self.expr4() 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def UN_LOGICAL_OP(self):
            return self.getToken(BKITParser.UN_LOGICAL_OP, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr4




    def expr4(self):

        localctx = BKITParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr4)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.UN_LOGICAL_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(BKITParser.UN_LOGICAL_OP)
                self.state = 372
                self.expr4()
                pass
            elif token in [BKITParser.ID, BKITParser.UN_OP, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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

        def UN_OP(self):
            return self.getToken(BKITParser.UN_OP, 0)

        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(BKITParser.Expr6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr5




    def expr5(self):

        localctx = BKITParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr5)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.UN_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(BKITParser.UN_OP)
                self.state = 377
                self.expr5()
                pass
            elif token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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




    def expr6(self):

        localctx = BKITParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr6)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expr7()
                self.state = 382
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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




    def expr7(self):

        localctx = BKITParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr7)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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




    def expr8(self):

        localctx = BKITParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr8)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(BKITParser.LEFT_PAREN)
                self.state = 393
                self.expr()
                self.state = 394
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


        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.var_non_init()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.primitive_data()
                pass
            elif token in [BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.array_lit()
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




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(BKITParser.ID)
            self.state = 404
            self.match(BKITParser.LEFT_PAREN)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.UN_LOGICAL_OP) | (1 << BKITParser.UN_OP) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 405
                self.expr()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 406
                    self.match(BKITParser.COMMA)
                    self.state = 407
                    self.expr()
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
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




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_op)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 421
                self.expr()
                self.state = 422
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 425
                self.expr()
                self.state = 426
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 427
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
        self._predicates[29] = self.expr1_sempred
        self._predicates[30] = self.expr2_sempred
        self._predicates[31] = self.expr3_sempred
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
         




