# Generated from /home/khanh/Documents/schoolLife/201/PPL/Assignments/assignment1/initial/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u01a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4o\n\4\f\4\16\4r\13\4\3")
        buf.write("\5\3\5\5\5v\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0080")
        buf.write("\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\7\t\u008b\n\t")
        buf.write("\f\t\16\t\u008e\13\t\3\t\7\t\u0091\n\t\f\t\16\t\u0094")
        buf.write("\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009f\n")
        buf.write("\n\3\13\3\13\3\13\3\13\7\13\u00a5\n\13\f\13\16\13\u00a8")
        buf.write("\13\13\3\f\3\f\3\f\3\f\7\f\u00ae\n\f\f\f\16\f\u00b1\13")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u00c1\n\16\f\16\16\16\u00c4\13\16\3")
        buf.write("\16\3\16\5\16\u00c8\n\16\3\16\3\16\3\16\3\17\3\17\5\17")
        buf.write("\u00cf\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\5\25\u00fa\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u0103\n\26\f\26\16\26\u0106\13\26\5\26\u0108\n\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u0111\n\30\3")
        buf.write("\30\3\30\3\30\3\30\6\30\u0117\n\30\r\30\16\30\u0118\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0122\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\7\33\u012a\n\33\f\33\16\33\u012d")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0135\n\34\f")
        buf.write("\34\16\34\u0138\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7")
        buf.write("\35\u0140\n\35\f\35\16\35\u0143\13\35\3\36\3\36\3\36\5")
        buf.write("\36\u0148\n\36\3\37\3\37\3\37\5\37\u014d\n\37\3 \3 \5")
        buf.write(" \u0151\n \3!\3!\5!\u0155\n!\3\"\3\"\3\"\3\"\3\"\5\"\u015c")
        buf.write("\n\"\3#\3#\5#\u0160\n#\3$\3$\3$\3$\3$\5$\u0167\n$\3%\3")
        buf.write("%\3%\7%\u016c\n%\f%\16%\u016f\13%\3&\3&\3&\7&\u0174\n")
        buf.write("&\f&\16&\u0177\13&\3\'\3\'\3\'\7\'\u017c\n\'\f\'\16\'")
        buf.write("\u017f\13\'\3(\3(\3(\7(\u0184\n(\f(\16(\u0187\13(\3)\3")
        buf.write(")\3)\3)\5)\u018d\n)\3*\3*\3*\3*\7*\u0193\n*\f*\16*\u0196")
        buf.write("\13*\5*\u0198\n*\3*\3*\3+\3+\5+\u019e\n+\3,\3,\3,\2\5")
        buf.write("\64\668-\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTV\2\5\3\2*+\3\2\25\30\3")
        buf.write("\2\27\30\2\u01a7\2[\3\2\2\2\4f\3\2\2\2\6k\3\2\2\2\bu\3")
        buf.write("\2\2\2\nw\3\2\2\2\fy\3\2\2\2\16\u0087\3\2\2\2\20\u008c")
        buf.write("\3\2\2\2\22\u009e\3\2\2\2\24\u00a0\3\2\2\2\26\u00a9\3")
        buf.write("\2\2\2\30\u00b5\3\2\2\2\32\u00b7\3\2\2\2\34\u00ce\3\2")
        buf.write("\2\2\36\u00d4\3\2\2\2 \u00e3\3\2\2\2\"\u00ea\3\2\2\2$")
        buf.write("\u00f1\3\2\2\2&\u00f4\3\2\2\2(\u00f7\3\2\2\2*\u00fd\3")
        buf.write("\2\2\2,\u010b\3\2\2\2.\u0110\3\2\2\2\60\u011a\3\2\2\2")
        buf.write("\62\u0121\3\2\2\2\64\u0123\3\2\2\2\66\u012e\3\2\2\28\u0139")
        buf.write("\3\2\2\2:\u0147\3\2\2\2<\u014c\3\2\2\2>\u0150\3\2\2\2")
        buf.write("@\u0154\3\2\2\2B\u015b\3\2\2\2D\u015f\3\2\2\2F\u0166\3")
        buf.write("\2\2\2H\u0168\3\2\2\2J\u0170\3\2\2\2L\u0178\3\2\2\2N\u0180")
        buf.write("\3\2\2\2P\u018c\3\2\2\2R\u018e\3\2\2\2T\u019d\3\2\2\2")
        buf.write("V\u019f\3\2\2\2XZ\5\4\3\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\f\7\2_^\3\2\2\2")
        buf.write("`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7")
        buf.write("\2\2\3e\3\3\2\2\2fg\7-\2\2gh\7\17\2\2hi\5\6\4\2ij\7\16")
        buf.write("\2\2j\5\3\2\2\2kp\5\b\5\2lm\7\20\2\2mo\5\b\5\2nl\3\2\2")
        buf.write("\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\7\3\2\2\2rp\3\2\2\2")
        buf.write("sv\5\26\f\2tv\5\24\13\2us\3\2\2\2ut\3\2\2\2v\t\3\2\2\2")
        buf.write("wx\3\2\2\2x\13\3\2\2\2yz\7.\2\2z{\7\17\2\2{\177\7\7\2")
        buf.write("\2|}\7\67\2\2}~\7\17\2\2~\u0080\5\30\r\2\177|\3\2\2\2")
        buf.write("\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7/")
        buf.write("\2\2\u0082\u0083\7\17\2\2\u0083\u0084\5\16\b\2\u0084\u0085")
        buf.write("\7:\2\2\u0085\u0086\7\21\2\2\u0086\r\3\2\2\2\u0087\u0088")
        buf.write("\5\20\t\2\u0088\17\3\2\2\2\u0089\u008b\5\4\3\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u0092\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008f\u0091\5\22\n\2\u0090\u008f\3\2\2\2\u0091\u0094")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\21\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u009f\5\34\17\2")
        buf.write("\u0096\u009f\5\32\16\2\u0097\u009f\5\36\20\2\u0098\u009f")
        buf.write("\5 \21\2\u0099\u009f\5\"\22\2\u009a\u009f\5$\23\2\u009b")
        buf.write("\u009f\5&\24\2\u009c\u009f\5,\27\2\u009d\u009f\5(\25\2")
        buf.write("\u009e\u0095\3\2\2\2\u009e\u0096\3\2\2\2\u009e\u0097\3")
        buf.write("\2\2\2\u009e\u0098\3\2\2\2\u009e\u0099\3\2\2\2\u009e\u009a")
        buf.write("\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\23\3\2\2\2\u00a0\u00a6\7\7\2\2\u00a1")
        buf.write("\u00a2\7\n\2\2\u00a2\u00a3\7\22\2\2\u00a3\u00a5\7\13\2")
        buf.write("\2\u00a4\u00a1\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a9\u00af\7\7\2\2\u00aa\u00ab\7\n\2\2\u00ab")
        buf.write("\u00ac\7\22\2\2\u00ac\u00ae\7\13\2\2\u00ad\u00aa\3\2\2")
        buf.write("\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2")
        buf.write("\u00b3\7,\2\2\u00b3\u00b4\5F$\2\u00b4\27\3\2\2\2\u00b5")
        buf.write("\u00b6\5\6\4\2\u00b6\31\3\2\2\2\u00b7\u00b8\7\62\2\2\u00b8")
        buf.write("\u00b9\5\60\31\2\u00b9\u00ba\7@\2\2\u00ba\u00c2\5\20\t")
        buf.write("\2\u00bb\u00bc\7\65\2\2\u00bc\u00bd\5\60\31\2\u00bd\u00be")
        buf.write("\7@\2\2\u00be\u00bf\5\20\t\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00bb\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c8\5\20\t\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00ca\7?\2\2\u00ca\u00cb\7\21\2\2\u00cb\33\3\2")
        buf.write("\2\2\u00cc\u00cf\7\7\2\2\u00cd\u00cf\5.\30\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d1\7,\2\2\u00d1\u00d2\5\60\31\2\u00d2\u00d3\7\16\2")
        buf.write("\2\u00d3\35\3\2\2\2\u00d4\u00d5\7;\2\2\u00d5\u00d6\7\f")
        buf.write("\2\2\u00d6\u00d7\7\7\2\2\u00d7\u00d8\7,\2\2\u00d8\u00d9")
        buf.write("\5\60\31\2\u00d9\u00da\7\20\2\2\u00da\u00db\5\60\31\2")
        buf.write("\u00db\u00dc\7\20\2\2\u00dc\u00dd\5\60\31\2\u00dd\u00de")
        buf.write("\7\r\2\2\u00de\u00df\7>\2\2\u00df\u00e0\5\20\t\2\u00e0")
        buf.write("\u00e1\7\61\2\2\u00e1\u00e2\7\21\2\2\u00e2\37\3\2\2\2")
        buf.write("\u00e3\u00e4\78\2\2\u00e4\u00e5\5\60\31\2\u00e5\u00e6")
        buf.write("\7>\2\2\u00e6\u00e7\5\20\t\2\u00e7\u00e8\7\66\2\2\u00e8")
        buf.write("\u00e9\7\21\2\2\u00e9!\3\2\2\2\u00ea\u00eb\7>\2\2\u00eb")
        buf.write("\u00ec\5\20\t\2\u00ec\u00ed\78\2\2\u00ed\u00ee\5\60\31")
        buf.write("\2\u00ee\u00ef\7\63\2\2\u00ef\u00f0\7\21\2\2\u00f0#\3")
        buf.write("\2\2\2\u00f1\u00f2\7\64\2\2\u00f2\u00f3\7\16\2\2\u00f3")
        buf.write("%\3\2\2\2\u00f4\u00f5\79\2\2\u00f5\u00f6\7\16\2\2\u00f6")
        buf.write("\'\3\2\2\2\u00f7\u00f9\7<\2\2\u00f8\u00fa\5\60\31\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fc\7\16\2\2\u00fc)\3\2\2\2\u00fd\u00fe\7\7\2")
        buf.write("\2\u00fe\u0107\7\f\2\2\u00ff\u0104\5\60\31\2\u0100\u0101")
        buf.write("\7\20\2\2\u0101\u0103\5\60\31\2\u0102\u0100\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u00ff\3")
        buf.write("\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write("\7\r\2\2\u010a+\3\2\2\2\u010b\u010c\5*\26\2\u010c\u010d")
        buf.write("\7\16\2\2\u010d-\3\2\2\2\u010e\u0111\5*\26\2\u010f\u0111")
        buf.write("\7\7\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("\u0116\3\2\2\2\u0112\u0113\7\n\2\2\u0113\u0114\5\60\31")
        buf.write("\2\u0114\u0115\7\13\2\2\u0115\u0117\3\2\2\2\u0116\u0112")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119/\3\2\2\2\u011a\u011b\5\62\32\2\u011b")
        buf.write("\61\3\2\2\2\u011c\u011d\5\64\33\2\u011d\u011e\7\5\2\2")
        buf.write("\u011e\u011f\5\64\33\2\u011f\u0122\3\2\2\2\u0120\u0122")
        buf.write("\5\64\33\2\u0121\u011c\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\63\3\2\2\2\u0123\u0124\b\33\1\2\u0124\u0125\5\66\34\2")
        buf.write("\u0125\u012b\3\2\2\2\u0126\u0127\f\4\2\2\u0127\u0128\t")
        buf.write("\2\2\2\u0128\u012a\5\66\34\2\u0129\u0126\3\2\2\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\65\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\b\34")
        buf.write("\1\2\u012f\u0130\58\35\2\u0130\u0136\3\2\2\2\u0131\u0132")
        buf.write("\f\4\2\2\u0132\u0133\t\3\2\2\u0133\u0135\58\35\2\u0134")
        buf.write("\u0131\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\67\3\2\2\2\u0138\u0136\3\2")
        buf.write("\2\2\u0139\u013a\b\35\1\2\u013a\u013b\5:\36\2\u013b\u0141")
        buf.write("\3\2\2\2\u013c\u013d\f\4\2\2\u013d\u013e\7\6\2\2\u013e")
        buf.write("\u0140\5:\36\2\u013f\u013c\3\2\2\2\u0140\u0143\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u01429\3\2\2")
        buf.write("\2\u0143\u0141\3\2\2\2\u0144\u0145\7)\2\2\u0145\u0148")
        buf.write("\5:\36\2\u0146\u0148\5<\37\2\u0147\u0144\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148;\3\2\2\2\u0149\u014a\t\4\2\2\u014a")
        buf.write("\u014d\5<\37\2\u014b\u014d\5> \2\u014c\u0149\3\2\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d=\3\2\2\2\u014e\u0151\5.\30\2\u014f")
        buf.write("\u0151\5@!\2\u0150\u014e\3\2\2\2\u0150\u014f\3\2\2\2\u0151")
        buf.write("?\3\2\2\2\u0152\u0155\5*\26\2\u0153\u0155\5B\"\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155A\3\2\2\2\u0156")
        buf.write("\u0157\7\f\2\2\u0157\u0158\5\60\31\2\u0158\u0159\7\r\2")
        buf.write("\2\u0159\u015c\3\2\2\2\u015a\u015c\5D#\2\u015b\u0156\3")
        buf.write("\2\2\2\u015b\u015a\3\2\2\2\u015cC\3\2\2\2\u015d\u0160")
        buf.write("\7\7\2\2\u015e\u0160\5F$\2\u015f\u015d\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160E\3\2\2\2\u0161\u0167\5V,\2\u0162\u0167")
        buf.write("\7\22\2\2\u0163\u0167\7\23\2\2\u0164\u0167\7\24\2\2\u0165")
        buf.write("\u0167\7F\2\2\u0166\u0161\3\2\2\2\u0166\u0162\3\2\2\2")
        buf.write("\u0166\u0163\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0165\3")
        buf.write("\2\2\2\u0167G\3\2\2\2\u0168\u016d\7\24\2\2\u0169\u016a")
        buf.write("\7\20\2\2\u016a\u016c\7\24\2\2\u016b\u0169\3\2\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016eI\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0175\7\22\2")
        buf.write("\2\u0171\u0172\7\20\2\2\u0172\u0174\7\22\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176K\3\2\2\2\u0177\u0175\3\2\2\2\u0178")
        buf.write("\u017d\7\23\2\2\u0179\u017a\7\20\2\2\u017a\u017c\7\23")
        buf.write("\2\2\u017b\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017eM\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0185\7F\2\2\u0181\u0182\7\20\2\2\u0182")
        buf.write("\u0184\7F\2\2\u0183\u0181\3\2\2\2\u0184\u0187\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186O\3\2\2")
        buf.write("\2\u0187\u0185\3\2\2\2\u0188\u018d\5J&\2\u0189\u018d\5")
        buf.write("L\'\2\u018a\u018d\5N(\2\u018b\u018d\5H%\2\u018c\u0188")
        buf.write("\3\2\2\2\u018c\u0189\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018dQ\3\2\2\2\u018e\u0197\7\b\2\2\u018f")
        buf.write("\u0194\5T+\2\u0190\u0191\7\20\2\2\u0191\u0193\5T+\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0197\u018f\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019a\7\t\2\2\u019aS\3\2\2\2\u019b\u019e")
        buf.write("\5R*\2\u019c\u019e\5P)\2\u019d\u019b\3\2\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019eU\3\2\2\2\u019f\u01a0\5R*\2\u01a0W\3\2\2")
        buf.write("\2\'[apu\177\u008c\u0092\u009e\u00a6\u00af\u00c2\u00c7")
        buf.write("\u00ce\u00f9\u0104\u0107\u0110\u0118\u0121\u012b\u0136")
        buf.write("\u0141\u0147\u014c\u0150\u0154\u015b\u015f\u0166\u016d")
        buf.write("\u0175\u017d\u0185\u018c\u0194\u0197\u019d")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'", "';'", "':'", "','", "'.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+.'", "'+'", "'-.'", "'-'", 
                     "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", "'=/='", 
                     "'<=.'", "'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'!'", "'&&'", "'||'", "'='", "'Var'", 
                     "'Function'", "'Body'", "'Else'", "'EndFor'", "'If'", 
                     "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", 
                     "'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", 
                     "'True'", "'Do'", "'EndIf'", "'Then'", "'False'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "RELATION_OP", "MULDIV", 
                      "IDENTIFIER", "LB", "RB", "LK", "RK", "LP", "RP", 
                      "SEMI", "COLON", "CM", "DOT", "INTEGER", "FLOAT", 
                      "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", 
                      "FMULOP", "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", 
                      "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", "FLESS", "FGR", 
                      "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", "BNEG", 
                      "BAND", "BOR", "AS", "VAR", "FUNCTION", "BODY", "ELSE", 
                      "ENDFOR", "IF", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
                      "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
                      "RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT", "LSTRING" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_var_list = 2
    RULE_decl = 3
    RULE_main_func = 4
    RULE_func_declare = 5
    RULE_func_body = 6
    RULE_stm_list = 7
    RULE_stm = 8
    RULE_non_initted_var = 9
    RULE_var_init = 10
    RULE_para_list = 11
    RULE_if_stmt = 12
    RULE_assign_stmt = 13
    RULE_for_stmt = 14
    RULE_while_stmt = 15
    RULE_do_while_stmt = 16
    RULE_break_stmt = 17
    RULE_continue_stmt = 18
    RULE_return_stmt = 19
    RULE_func_call = 20
    RULE_call_stmt = 21
    RULE_index_op = 22
    RULE_expression = 23
    RULE_exp0 = 24
    RULE_exp1 = 25
    RULE_exp2 = 26
    RULE_exp3 = 27
    RULE_exp4 = 28
    RULE_exp5 = 29
    RULE_exp6 = 30
    RULE_exp7 = 31
    RULE_exp8 = 32
    RULE_operand = 33
    RULE_literals = 34
    RULE_bool_array = 35
    RULE_int_array = 36
    RULE_float_array = 37
    RULE_string_array = 38
    RULE_array_index = 39
    RULE_array_list = 40
    RULE_element = 41
    RULE_arraylit = 42

    ruleNames =  [ "program", "var_declare", "var_list", "decl", "main_func", 
                   "func_declare", "func_body", "stm_list", "stm", "non_initted_var", 
                   "var_init", "para_list", "if_stmt", "assign_stmt", "for_stmt", 
                   "while_stmt", "do_while_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "func_call", "call_stmt", "index_op", 
                   "expression", "exp0", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "operand", "literals", 
                   "bool_array", "int_array", "float_array", "string_array", 
                   "array_index", "array_list", "element", "arraylit" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    RELATION_OP=3
    MULDIV=4
    IDENTIFIER=5
    LB=6
    RB=7
    LK=8
    RK=9
    LP=10
    RP=11
    SEMI=12
    COLON=13
    CM=14
    DOT=15
    INTEGER=16
    FLOAT=17
    BOLEAN=18
    FADDOP=19
    IADDOP=20
    FSUBOP=21
    ISUBOP=22
    FMULOP=23
    IMULOP=24
    FDIVOP=25
    IDIVOP=26
    IREMAIN=27
    EQUAL=28
    FNEQUAL=29
    FLESSOE=30
    FGROE=31
    FLESS=32
    FGR=33
    INEQUAL=34
    ILESSOE=35
    IGROE=36
    ILESS=37
    IGR=38
    BNEG=39
    BAND=40
    BOR=41
    AS=42
    VAR=43
    FUNCTION=44
    BODY=45
    ELSE=46
    ENDFOR=47
    IF=48
    ENDDO=49
    BREAK=50
    ELSEIF=51
    ENDWHILE=52
    PARAMETER=53
    WHILE=54
    CONTINUE=55
    ENDBODY=56
    FOR=57
    RETURN=58
    TRUE=59
    DO=60
    ENDIF=61
    THEN=62
    FALSE=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    UNTERMINATED_COMMENT=67
    LSTRING=68

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

        def func_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declareContext,i)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




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
                self.state = 86
                self.var_declare()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 92
                self.func_declare()
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


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




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
            self.state = 103
            self.match(BKITParser.SEMI)
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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.DeclContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.decl()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 106
                self.match(BKITParser.CM)
                self.state = 107
                self.decl()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_init(self):
            return self.getTypedRuleContext(BKITParser.Var_initContext,0)


        def non_initted_var(self):
            return self.getTypedRuleContext(BKITParser.Non_initted_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_decl




    def decl(self):

        localctx = BKITParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.var_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.non_initted_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_main_func




    def main_func(self):

        localctx = BKITParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main_func)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

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

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def para_list(self):
            return self.getTypedRuleContext(BKITParser.Para_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKITParser.FUNCTION)
            self.state = 120
            self.match(BKITParser.COLON)
            self.state = 121
            self.match(BKITParser.IDENTIFIER)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 122
                self.match(BKITParser.PARAMETER)
                self.state = 123
                self.match(BKITParser.COLON)
                self.state = 124
                self.para_list()


            self.state = 127
            self.match(BKITParser.BODY)
            self.state = 128
            self.match(BKITParser.COLON)
            self.state = 129
            self.func_body()
            self.state = 130
            self.match(BKITParser.ENDBODY)
            self.state = 131
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm_list(self):
            return self.getTypedRuleContext(BKITParser.Stm_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.stm_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stm_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stm_list




    def stm_list(self):

        localctx = BKITParser.Stm_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stm_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 135
                self.var_declare()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self.stm() 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stm




    def stm(self):

        localctx = BKITParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stm)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 153
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 154
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 155
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_initted_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LK)
            else:
                return self.getToken(BKITParser.LK, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def RK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RK)
            else:
                return self.getToken(BKITParser.RK, i)

        def getRuleIndex(self):
            return BKITParser.RULE_non_initted_var




    def non_initted_var(self):

        localctx = BKITParser.Non_initted_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_non_initted_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BKITParser.IDENTIFIER)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LK:
                self.state = 159
                self.match(BKITParser.LK)
                self.state = 160
                self.match(BKITParser.INTEGER)
                self.state = 161
                self.match(BKITParser.RK)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def LK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LK)
            else:
                return self.getToken(BKITParser.LK, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def RK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RK)
            else:
                return self.getToken(BKITParser.RK, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_init




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKITParser.IDENTIFIER)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LK:
                self.state = 168
                self.match(BKITParser.LK)
                self.state = 169
                self.match(BKITParser.INTEGER)
                self.state = 170
                self.match(BKITParser.RK)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(BKITParser.AS)
            self.state = 177
            self.literals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para_list




    def para_list(self):

        localctx = BKITParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_para_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.var_list()
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stm_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stm_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stm_listContext,i)


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
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKITParser.IF)
            self.state = 182
            self.expression()
            self.state = 183
            self.match(BKITParser.THEN)
            self.state = 184
            self.stm_list()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 185
                self.match(BKITParser.ELSEIF)
                self.state = 186
                self.expression()
                self.state = 187
                self.match(BKITParser.THEN)
                self.state = 188
                self.stm_list()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 195
                self.match(BKITParser.ELSE)
                self.state = 196
                self.stm_list()


            self.state = 199
            self.match(BKITParser.ENDIF)
            self.state = 200
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

        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 202
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 203
                self.index_op()
                pass


            self.state = 206
            self.match(BKITParser.AS)
            self.state = 207
            self.expression()
            self.state = 208
            self.match(BKITParser.SEMI)
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

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stm_list(self):
            return self.getTypedRuleContext(BKITParser.Stm_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(BKITParser.FOR)
            self.state = 211
            self.match(BKITParser.LP)
            self.state = 212
            self.match(BKITParser.IDENTIFIER)
            self.state = 213
            self.match(BKITParser.AS)
            self.state = 214
            self.expression()
            self.state = 215
            self.match(BKITParser.CM)
            self.state = 216
            self.expression()
            self.state = 217
            self.match(BKITParser.CM)
            self.state = 218
            self.expression()
            self.state = 219
            self.match(BKITParser.RP)
            self.state = 220
            self.match(BKITParser.DO)
            self.state = 221
            self.stm_list()
            self.state = 222
            self.match(BKITParser.ENDFOR)
            self.state = 223
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

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stm_list(self):
            return self.getTypedRuleContext(BKITParser.Stm_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(BKITParser.WHILE)
            self.state = 226
            self.expression()
            self.state = 227
            self.match(BKITParser.DO)
            self.state = 228
            self.stm_list()
            self.state = 229
            self.match(BKITParser.ENDWHILE)
            self.state = 230
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stm_list(self):
            return self.getTypedRuleContext(BKITParser.Stm_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKITParser.DO)
            self.state = 233
            self.stm_list()
            self.state = 234
            self.match(BKITParser.WHILE)
            self.state = 235
            self.expression()
            self.state = 236
            self.match(BKITParser.ENDDO)
            self.state = 237
            self.match(BKITParser.DOT)
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKITParser.BREAK)
            self.state = 240
            self.match(BKITParser.SEMI)
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(BKITParser.CONTINUE)
            self.state = 243
            self.match(BKITParser.SEMI)
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKITParser.RETURN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (BKITParser.IDENTIFIER - 5)) | (1 << (BKITParser.LB - 5)) | (1 << (BKITParser.LP - 5)) | (1 << (BKITParser.INTEGER - 5)) | (1 << (BKITParser.FLOAT - 5)) | (1 << (BKITParser.BOLEAN - 5)) | (1 << (BKITParser.FSUBOP - 5)) | (1 << (BKITParser.ISUBOP - 5)) | (1 << (BKITParser.BNEG - 5)) | (1 << (BKITParser.LSTRING - 5)))) != 0):
                self.state = 246
                self.expression()


            self.state = 249
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.IDENTIFIER)
            self.state = 252
            self.match(BKITParser.LP)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (BKITParser.IDENTIFIER - 5)) | (1 << (BKITParser.LB - 5)) | (1 << (BKITParser.LP - 5)) | (1 << (BKITParser.INTEGER - 5)) | (1 << (BKITParser.FLOAT - 5)) | (1 << (BKITParser.BOLEAN - 5)) | (1 << (BKITParser.FSUBOP - 5)) | (1 << (BKITParser.ISUBOP - 5)) | (1 << (BKITParser.BNEG - 5)) | (1 << (BKITParser.LSTRING - 5)))) != 0):
                self.state = 253
                self.expression()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 254
                    self.match(BKITParser.CM)
                    self.state = 255
                    self.expression()
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 263
            self.match(BKITParser.RP)
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

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.func_call()
            self.state = 266
            self.match(BKITParser.SEMI)
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

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LK)
            else:
                return self.getToken(BKITParser.LK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def RK(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RK)
            else:
                return self.getToken(BKITParser.RK, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_op




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 268
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 269
                self.match(BKITParser.IDENTIFIER)
                pass


            self.state = 276 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 272
                    self.match(BKITParser.LK)
                    self.state = 273
                    self.expression()
                    self.state = 274
                    self.match(BKITParser.RK)

                else:
                    raise NoViableAltException(self)
                self.state = 278 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(BKITParser.Exp0Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.exp0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def RELATION_OP(self):
            return self.getToken(BKITParser.RELATION_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp0




    def exp0(self):

        localctx = BKITParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp0)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.exp1(0)
                self.state = 283
                self.match(BKITParser.RELATION_OP)
                self.state = 284
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def BAND(self):
            return self.getToken(BKITParser.BAND, 0)

        def BOR(self):
            return self.getToken(BKITParser.BOR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 292
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 293
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.BAND or _la==BKITParser.BOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 294
                    self.exp2(0) 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def FADDOP(self):
            return self.getToken(BKITParser.FADDOP, 0)

        def FSUBOP(self):
            return self.getToken(BKITParser.FSUBOP, 0)

        def IADDOP(self):
            return self.getToken(BKITParser.IADDOP, 0)

        def ISUBOP(self):
            return self.getToken(BKITParser.ISUBOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FADDOP) | (1 << BKITParser.IADDOP) | (1 << BKITParser.FSUBOP) | (1 << BKITParser.ISUBOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 305
                    self.exp3(0) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULDIV(self):
            return self.getToken(BKITParser.MULDIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    self.match(BKITParser.MULDIV)
                    self.state = 316
                    self.exp4() 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BNEG(self):
            return self.getToken(BKITParser.BNEG, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp4)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BNEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(BKITParser.BNEG)
                self.state = 323
                self.exp4()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.FSUBOP, BKITParser.ISUBOP, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.exp5()
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


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def FSUBOP(self):
            return self.getToken(BKITParser.FSUBOP, 0)

        def ISUBOP(self):
            return self.getToken(BKITParser.ISUBOP, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FSUBOP, BKITParser.ISUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                _la = self._input.LA(1)
                if not(_la==BKITParser.FSUBOP or _la==BKITParser.ISUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 328
                self.exp5()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.exp6()
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


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp6)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.exp7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def exp8(self):
            return self.getTypedRuleContext(BKITParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp7)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp8




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp8)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(BKITParser.LP)

                self.state = 341
                self.expression()
                self.state = 342
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.operand()
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

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operand)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(BKITParser.IDENTIFIER)
                pass
            elif token in [BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.literals()
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


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraylit(self):
            return self.getTypedRuleContext(BKITParser.ArraylitContext,0)


        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def BOLEAN(self):
            return self.getToken(BKITParser.BOLEAN, 0)

        def LSTRING(self):
            return self.getToken(BKITParser.LSTRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literals




    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literals)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.arraylit()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(BKITParser.BOLEAN)
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.match(BKITParser.LSTRING)
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


    class Bool_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.BOLEAN)
            else:
                return self.getToken(BKITParser.BOLEAN, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_bool_array




    def bool_array(self):

        localctx = BKITParser.Bool_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_bool_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(BKITParser.BOLEAN)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 359
                    self.match(BKITParser.CM)
                    self.state = 360
                    self.match(BKITParser.BOLEAN) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_int_array




    def int_array(self):

        localctx = BKITParser.Int_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_int_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(BKITParser.INTEGER)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 367
                    self.match(BKITParser.CM)
                    self.state = 368
                    self.match(BKITParser.INTEGER) 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.FLOAT)
            else:
                return self.getToken(BKITParser.FLOAT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_float_array




    def float_array(self):

        localctx = BKITParser.Float_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_float_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(BKITParser.FLOAT)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 375
                    self.match(BKITParser.CM)
                    self.state = 376
                    self.match(BKITParser.FLOAT) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSTRING(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSTRING)
            else:
                return self.getToken(BKITParser.LSTRING, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_string_array




    def string_array(self):

        localctx = BKITParser.String_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_string_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(BKITParser.LSTRING)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383
                    self.match(BKITParser.CM)
                    self.state = 384
                    self.match(BKITParser.LSTRING) 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_array(self):
            return self.getTypedRuleContext(BKITParser.Int_arrayContext,0)


        def float_array(self):
            return self.getTypedRuleContext(BKITParser.Float_arrayContext,0)


        def string_array(self):
            return self.getTypedRuleContext(BKITParser.String_arrayContext,0)


        def bool_array(self):
            return self.getTypedRuleContext(BKITParser.Bool_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_index




    def array_index(self):

        localctx = BKITParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_array_index)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.int_array()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.float_array()
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.string_array()
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.bool_array()
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


    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ElementContext)
            else:
                return self.getTypedRuleContext(BKITParser.ElementContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_list




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(BKITParser.LB)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & ((1 << (BKITParser.LB - 6)) | (1 << (BKITParser.INTEGER - 6)) | (1 << (BKITParser.FLOAT - 6)) | (1 << (BKITParser.BOLEAN - 6)) | (1 << (BKITParser.LSTRING - 6)))) != 0):
                self.state = 397
                self.element()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 398
                    self.match(BKITParser.CM)

                    self.state = 399
                    self.element()
                    self.state = 404
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 407
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def array_index(self):
            return self.getTypedRuleContext(BKITParser.Array_indexContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element




    def element(self):

        localctx = BKITParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_element)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.array_index()
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


    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_arraylit




    def arraylit(self):

        localctx = BKITParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.array_list()
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
        self._predicates[25] = self.exp1_sempred
        self._predicates[26] = self.exp2_sempred
        self._predicates[27] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




