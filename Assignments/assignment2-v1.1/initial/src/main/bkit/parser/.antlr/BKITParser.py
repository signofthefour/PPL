# Generated from /home/khanh/Documents/schoolLife/201/PPL/Assignments/assignment2-v1.1/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\7\2\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\5\4j\n\4\3\4\3\4\3\4\5\4o\n\4\7\4q\n\4")
        buf.write("\f\4\16\4t\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6~\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\7\b\u0089\n\b\f")
        buf.write("\b\16\b\u008c\13\b\3\b\7\b\u008f\n\b\f\b\16\b\u0092\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u009d\n\t\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00a3\n\n\f\n\16\n\u00a6\13\n\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u00ac\n\13\f\13\16\13\u00af\13\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b7\n\f\f\f\16\f\u00ba")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c5\n")
        buf.write("\r\f\r\16\r\u00c8\13\r\3\r\3\r\5\r\u00cc\n\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\5\16\u00d3\n\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u0103\n")
        buf.write("\25\f\25\16\25\u0106\13\25\5\25\u0108\n\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u0111\n\26\f\26\16\26\u0114")
        buf.write("\13\26\5\26\u0116\n\26\3\26\3\26\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\6\30\u0121\n\30\r\30\16\30\u0122\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u0134\n\33\f\33\16\33\u0137")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u013f\n\34\f")
        buf.write("\34\16\34\u0142\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7")
        buf.write("\35\u014a\n\35\f\35\16\35\u014d\13\35\3\36\3\36\3\36\5")
        buf.write("\36\u0152\n\36\3\37\3\37\3\37\5\37\u0157\n\37\3 \3 \3")
        buf.write(" \3 \3 \7 \u015e\n \f \16 \u0161\13 \3!\3!\5!\u0165\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\5\"\u016c\n\"\3#\3#\5#\u0170\n#")
        buf.write("\3$\3$\3$\3$\3$\5$\u0177\n$\3%\3%\3%\7%\u017c\n%\f%\16")
        buf.write("%\u017f\13%\3&\3&\3&\7&\u0184\n&\f&\16&\u0187\13&\3\'")
        buf.write("\3\'\3\'\7\'\u018c\n\'\f\'\16\'\u018f\13\'\3(\3(\3(\7")
        buf.write("(\u0194\n(\f(\16(\u0197\13(\3)\3)\3)\3)\5)\u019d\n)\3")
        buf.write("*\3*\3*\5*\u01a2\n*\3*\3*\3*\5*\u01a7\n*\7*\u01a9\n*\f")
        buf.write("*\16*\u01ac\13*\5*\u01ae\n*\3*\3*\3*\2\6\64\668>+\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPR\2\3\3\2,-\2\u01bc\2W\3\2\2\2\4b\3\2")
        buf.write("\2\2\6i\3\2\2\2\bu\3\2\2\2\nw\3\2\2\2\f\u0085\3\2\2\2")
        buf.write("\16\u008a\3\2\2\2\20\u009c\3\2\2\2\22\u009e\3\2\2\2\24")
        buf.write("\u00a7\3\2\2\2\26\u00b3\3\2\2\2\30\u00bb\3\2\2\2\32\u00d2")
        buf.write("\3\2\2\2\34\u00d8\3\2\2\2\36\u00db\3\2\2\2 \u00ea\3\2")
        buf.write("\2\2\"\u00f1\3\2\2\2$\u00f8\3\2\2\2&\u00fb\3\2\2\2(\u00fe")
        buf.write("\3\2\2\2*\u010b\3\2\2\2,\u0119\3\2\2\2.\u0120\3\2\2\2")
        buf.write("\60\u0124\3\2\2\2\62\u012b\3\2\2\2\64\u012d\3\2\2\2\66")
        buf.write("\u0138\3\2\2\28\u0143\3\2\2\2:\u0151\3\2\2\2<\u0156\3")
        buf.write("\2\2\2>\u0158\3\2\2\2@\u0164\3\2\2\2B\u016b\3\2\2\2D\u016f")
        buf.write("\3\2\2\2F\u0176\3\2\2\2H\u0178\3\2\2\2J\u0180\3\2\2\2")
        buf.write("L\u0188\3\2\2\2N\u0190\3\2\2\2P\u019c\3\2\2\2R\u019e\3")
        buf.write("\2\2\2TV\5\4\3\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2")
        buf.write("\2X]\3\2\2\2YW\3\2\2\2Z\\\5\n\6\2[Z\3\2\2\2\\_\3\2\2\2")
        buf.write("][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\2\2\3a\3")
        buf.write("\3\2\2\2bc\7/\2\2cd\7\21\2\2de\5\6\4\2ef\7\20\2\2f\5\3")
        buf.write("\2\2\2gj\5\24\13\2hj\5\22\n\2ig\3\2\2\2ih\3\2\2\2jr\3")
        buf.write("\2\2\2kn\7\22\2\2lo\5\24\13\2mo\5\22\n\2nl\3\2\2\2nm\3")
        buf.write("\2\2\2oq\3\2\2\2pk\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2")
        buf.write("\2s\7\3\2\2\2tr\3\2\2\2uv\3\2\2\2v\t\3\2\2\2wx\7\60\2")
        buf.write("\2xy\7\21\2\2y}\7\t\2\2z{\79\2\2{|\7\21\2\2|~\5\26\f\2")
        buf.write("}z\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080\7\61\2\2\u0080")
        buf.write("\u0081\7\21\2\2\u0081\u0082\5\f\7\2\u0082\u0083\7<\2\2")
        buf.write("\u0083\u0084\7\23\2\2\u0084\13\3\2\2\2\u0085\u0086\5\16")
        buf.write("\b\2\u0086\r\3\2\2\2\u0087\u0089\5\4\3\2\u0088\u0087\3")
        buf.write("\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u0090\3\2\2\2\u008c\u008a\3\2\2\2\u008d")
        buf.write("\u008f\5\20\t\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2")
        buf.write("\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\17\3")
        buf.write("\2\2\2\u0092\u0090\3\2\2\2\u0093\u009d\5\32\16\2\u0094")
        buf.write("\u009d\5\30\r\2\u0095\u009d\5\36\20\2\u0096\u009d\5 \21")
        buf.write("\2\u0097\u009d\5\"\22\2\u0098\u009d\5$\23\2\u0099\u009d")
        buf.write("\5&\24\2\u009a\u009d\5,\27\2\u009b\u009d\5(\25\2\u009c")
        buf.write("\u0093\3\2\2\2\u009c\u0094\3\2\2\2\u009c\u0095\3\2\2\2")
        buf.write("\u009c\u0096\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0098\3")
        buf.write("\2\2\2\u009c\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\21\3\2\2\2\u009e\u00a4\7\t\2\2\u009f\u00a0")
        buf.write("\7\f\2\2\u00a0\u00a1\7\24\2\2\u00a1\u00a3\7\r\2\2\u00a2")
        buf.write("\u009f\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\23\3\2\2\2\u00a6\u00a4\3\2")
        buf.write("\2\2\u00a7\u00ad\7\t\2\2\u00a8\u00a9\7\f\2\2\u00a9\u00aa")
        buf.write("\7\24\2\2\u00aa\u00ac\7\r\2\2\u00ab\u00a8\3\2\2\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7")
        buf.write(".\2\2\u00b1\u00b2\5F$\2\u00b2\25\3\2\2\2\u00b3\u00b8\5")
        buf.write("\22\n\2\u00b4\u00b5\7\22\2\2\u00b5\u00b7\5\22\n\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\27\3\2\2\2\u00ba\u00b8\3\2")
        buf.write("\2\2\u00bb\u00bc\7\64\2\2\u00bc\u00bd\5\60\31\2\u00bd")
        buf.write("\u00be\7B\2\2\u00be\u00c6\5\16\b\2\u00bf\u00c0\7\67\2")
        buf.write("\2\u00c0\u00c1\5\60\31\2\u00c1\u00c2\7B\2\2\u00c2\u00c3")
        buf.write("\5\16\b\2\u00c3\u00c5\3\2\2\2\u00c4\u00bf\3\2\2\2\u00c5")
        buf.write("\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00cb\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7")
        buf.write("\62\2\2\u00ca\u00cc\5\16\b\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7A\2\2")
        buf.write("\u00ce\u00cf\7\23\2\2\u00cf\31\3\2\2\2\u00d0\u00d3\7\t")
        buf.write("\2\2\u00d1\u00d3\5\34\17\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7.\2\2\u00d5")
        buf.write("\u00d6\5\60\31\2\u00d6\u00d7\7\20\2\2\u00d7\33\3\2\2\2")
        buf.write("\u00d8\u00d9\5\60\31\2\u00d9\u00da\5.\30\2\u00da\35\3")
        buf.write("\2\2\2\u00db\u00dc\7=\2\2\u00dc\u00dd\7\16\2\2\u00dd\u00de")
        buf.write("\7\t\2\2\u00de\u00df\7.\2\2\u00df\u00e0\5\60\31\2\u00e0")
        buf.write("\u00e1\7\22\2\2\u00e1\u00e2\5\60\31\2\u00e2\u00e3\7\22")
        buf.write("\2\2\u00e3\u00e4\5\64\33\2\u00e4\u00e5\7\17\2\2\u00e5")
        buf.write("\u00e6\7@\2\2\u00e6\u00e7\5\16\b\2\u00e7\u00e8\7\63\2")
        buf.write("\2\u00e8\u00e9\7\23\2\2\u00e9\37\3\2\2\2\u00ea\u00eb\7")
        buf.write(":\2\2\u00eb\u00ec\5\60\31\2\u00ec\u00ed\7@\2\2\u00ed\u00ee")
        buf.write("\5\16\b\2\u00ee\u00ef\78\2\2\u00ef\u00f0\7\23\2\2\u00f0")
        buf.write("!\3\2\2\2\u00f1\u00f2\7@\2\2\u00f2\u00f3\5\16\b\2\u00f3")
        buf.write("\u00f4\7:\2\2\u00f4\u00f5\5\60\31\2\u00f5\u00f6\7\65\2")
        buf.write("\2\u00f6\u00f7\7\23\2\2\u00f7#\3\2\2\2\u00f8\u00f9\7\66")
        buf.write("\2\2\u00f9\u00fa\7\20\2\2\u00fa%\3\2\2\2\u00fb\u00fc\7")
        buf.write(";\2\2\u00fc\u00fd\7\20\2\2\u00fd\'\3\2\2\2\u00fe\u0107")
        buf.write("\7>\2\2\u00ff\u0104\5\60\31\2\u0100\u0101\7\22\2\2\u0101")
        buf.write("\u0103\5\60\31\2\u0102\u0100\3\2\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0108")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u00ff\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\7\20\2")
        buf.write("\2\u010a)\3\2\2\2\u010b\u010c\7\t\2\2\u010c\u0115\7\16")
        buf.write("\2\2\u010d\u0112\5\60\31\2\u010e\u010f\7\22\2\2\u010f")
        buf.write("\u0111\5\60\31\2\u0110\u010e\3\2\2\2\u0111\u0114\3\2\2")
        buf.write("\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u010d\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\17\2")
        buf.write("\2\u0118+\3\2\2\2\u0119\u011a\5*\26\2\u011a\u011b\7\20")
        buf.write("\2\2\u011b-\3\2\2\2\u011c\u011d\7\f\2\2\u011d\u011e\5")
        buf.write("\60\31\2\u011e\u011f\7\r\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u011c\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123/\3\2\2\2\u0124\u0125\5\62\32")
        buf.write("\2\u0125\61\3\2\2\2\u0126\u0127\5\64\33\2\u0127\u0128")
        buf.write("\7\5\2\2\u0128\u0129\5\64\33\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012c\5\64\33\2\u012b\u0126\3\2\2\2\u012b\u012a\3\2\2")
        buf.write("\2\u012c\63\3\2\2\2\u012d\u012e\b\33\1\2\u012e\u012f\5")
        buf.write("\66\34\2\u012f\u0135\3\2\2\2\u0130\u0131\f\4\2\2\u0131")
        buf.write("\u0132\t\2\2\2\u0132\u0134\5\66\34\2\u0133\u0130\3\2\2")
        buf.write("\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\65\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139")
        buf.write("\b\34\1\2\u0139\u013a\58\35\2\u013a\u0140\3\2\2\2\u013b")
        buf.write("\u013c\f\4\2\2\u013c\u013d\7\6\2\2\u013d\u013f\58\35\2")
        buf.write("\u013e\u013b\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3")
        buf.write("\2\2\2\u0140\u0141\3\2\2\2\u0141\67\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0143\u0144\b\35\1\2\u0144\u0145\5:\36\2\u0145")
        buf.write("\u014b\3\2\2\2\u0146\u0147\f\4\2\2\u0147\u0148\7\7\2\2")
        buf.write("\u0148\u014a\5:\36\2\u0149\u0146\3\2\2\2\u014a\u014d\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c9")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7+\2\2\u014f")
        buf.write("\u0152\5:\36\2\u0150\u0152\5<\37\2\u0151\u014e\3\2\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152;\3\2\2\2\u0153\u0154\7\6\2")
        buf.write("\2\u0154\u0157\5<\37\2\u0155\u0157\5> \2\u0156\u0153\3")
        buf.write("\2\2\2\u0156\u0155\3\2\2\2\u0157=\3\2\2\2\u0158\u0159")
        buf.write("\b \1\2\u0159\u015a\5@!\2\u015a\u015f\3\2\2\2\u015b\u015c")
        buf.write("\f\4\2\2\u015c\u015e\5.\30\2\u015d\u015b\3\2\2\2\u015e")
        buf.write("\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160?\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0165\5*\26")
        buf.write("\2\u0163\u0165\5B\"\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165A\3\2\2\2\u0166\u0167\7\16\2\2\u0167\u0168")
        buf.write("\5\60\31\2\u0168\u0169\7\17\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u016c\5D#\2\u016b\u0166\3\2\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write("C\3\2\2\2\u016d\u0170\7\t\2\2\u016e\u0170\5F$\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170E\3\2\2\2\u0171")
        buf.write("\u0177\5R*\2\u0172\u0177\7\24\2\2\u0173\u0177\7\25\2\2")
        buf.write("\u0174\u0177\7\26\2\2\u0175\u0177\7H\2\2\u0176\u0171\3")
        buf.write("\2\2\2\u0176\u0172\3\2\2\2\u0176\u0173\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177G\3\2\2\2\u0178\u017d")
        buf.write("\7\26\2\2\u0179\u017a\7\22\2\2\u017a\u017c\7\26\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017eI\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0185\7\24\2\2\u0181\u0182\7\22\2\2\u0182\u0184")
        buf.write("\7\24\2\2\u0183\u0181\3\2\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186K\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u018d\7\25\2\2\u0189\u018a\7\22\2")
        buf.write("\2\u018a\u018c\7\25\2\2\u018b\u0189\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("M\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0195\7H\2\2\u0191")
        buf.write("\u0192\7\22\2\2\u0192\u0194\7H\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196O\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019d")
        buf.write("\5J&\2\u0199\u019d\5L\'\2\u019a\u019d\5N(\2\u019b\u019d")
        buf.write("\5H%\2\u019c\u0198\3\2\2\2\u019c\u0199\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019dQ\3\2\2\2\u019e\u01ad")
        buf.write("\7\n\2\2\u019f\u01a2\5R*\2\u01a0\u01a2\5P)\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01aa\3\2\2\2\u01a3")
        buf.write("\u01a6\7\22\2\2\u01a4\u01a7\5R*\2\u01a5\u01a7\5P)\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a9\3\2\2\2")
        buf.write("\u01a8\u01a3\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ad\u01a1\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\7\13\2\2\u01b0S\3\2\2\2*W]")
        buf.write("inr}\u008a\u0090\u009c\u00a4\u00ad\u00b8\u00c6\u00cb\u00d2")
        buf.write("\u0104\u0107\u0112\u0115\u0122\u012b\u0135\u0140\u014b")
        buf.write("\u0151\u0156\u015f\u0164\u016b\u016f\u0176\u017d\u0185")
        buf.write("\u018d\u0195\u019c\u01a1\u01a6\u01aa\u01ad")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "':'", 
                     "','", "'.'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+.'", "'+'", "'-.'", "'-'", "'*.'", "'*'", "'\\.'", 
                     "'\\'", "'%'", "'=='", "'=/='", "'<=.'", "'>=.'", "'<.'", 
                     "'>.'", "'!='", "'<='", "'>='", "'<'", "'>'", "'!'", 
                     "'&&'", "'||'", "'='", "'Var'", "'Function'", "'Body'", 
                     "'Else'", "'EndFor'", "'If'", "'EndDo'", "'Break'", 
                     "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
                     "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", 
                     "'Do'", "'EndIf'", "'Then'", "'False'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "RELATION_OP", "ADDSUB", 
                      "MULDIV", "NEGSIGN", "IDENTIFIER", "LB", "RB", "LK", 
                      "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTEGER", 
                      "FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", 
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
    RULE_main_func = 3
    RULE_func_declare = 4
    RULE_func_body = 5
    RULE_stm_list = 6
    RULE_stm = 7
    RULE_non_initted_var = 8
    RULE_var_init = 9
    RULE_para_list = 10
    RULE_if_stmt = 11
    RULE_assign_stmt = 12
    RULE_composite_ass = 13
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

    ruleNames =  [ "program", "var_declare", "var_list", "main_func", "func_declare", 
                   "func_body", "stm_list", "stm", "non_initted_var", "var_init", 
                   "para_list", "if_stmt", "assign_stmt", "composite_ass", 
                   "for_stmt", "while_stmt", "do_while_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call", "call_stmt", 
                   "index_op", "expression", "exp0", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "operand", "literals", 
                   "bool_array", "int_array", "float_array", "string_array", 
                   "array_index", "array_list" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    RELATION_OP=3
    ADDSUB=4
    MULDIV=5
    NEGSIGN=6
    IDENTIFIER=7
    LB=8
    RB=9
    LK=10
    RK=11
    LP=12
    RP=13
    SEMI=14
    COLON=15
    CM=16
    DOT=17
    INTEGER=18
    FLOAT=19
    BOLEAN=20
    FADDOP=21
    IADDOP=22
    FSUBOP=23
    ISUBOP=24
    FMULOP=25
    IMULOP=26
    FDIVOP=27
    IDIVOP=28
    IREMAIN=29
    EQUAL=30
    FNEQUAL=31
    FLESSOE=32
    FGROE=33
    FLESS=34
    FGR=35
    INEQUAL=36
    ILESSOE=37
    IGROE=38
    ILESS=39
    IGR=40
    BNEG=41
    BAND=42
    BOR=43
    AS=44
    VAR=45
    FUNCTION=46
    BODY=47
    ELSE=48
    ENDFOR=49
    IF=50
    ENDDO=51
    BREAK=52
    ELSEIF=53
    ENDWHILE=54
    PARAMETER=55
    WHILE=56
    CONTINUE=57
    ENDBODY=58
    FOR=59
    RETURN=60
    TRUE=61
    DO=62
    ENDIF=63
    THEN=64
    FALSE=65
    ERROR_CHAR=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68
    UNTERMINATED_COMMENT=69
    LSTRING=70

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
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 82
                self.var_declare()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 88
                self.func_declare()
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


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

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
            self.state = 99
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

        def var_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_initContext,i)


        def non_initted_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Non_initted_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Non_initted_varContext,i)


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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 101
                self.var_init()
                pass

            elif la_ == 2:
                self.state = 102
                self.non_initted_var()
                pass


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 105
                self.match(BKITParser.CM)
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.var_init()
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.non_initted_var()
                    pass


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_main_func)
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
        self.enterRule(localctx, 8, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKITParser.FUNCTION)
            self.state = 118
            self.match(BKITParser.COLON)
            self.state = 119
            self.match(BKITParser.IDENTIFIER)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 120
                self.match(BKITParser.PARAMETER)
                self.state = 121
                self.match(BKITParser.COLON)
                self.state = 122
                self.para_list()


            self.state = 125
            self.match(BKITParser.BODY)
            self.state = 126
            self.match(BKITParser.COLON)
            self.state = 127
            self.func_body()
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
        self.enterRule(localctx, 10, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 12, self.RULE_stm_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 133
                self.var_declare()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 139
                    self.stm() 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_stm)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 152
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 153
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
        self.enterRule(localctx, 16, self.RULE_non_initted_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BKITParser.IDENTIFIER)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LK:
                self.state = 157
                self.match(BKITParser.LK)
                self.state = 158
                self.match(BKITParser.INTEGER)
                self.state = 159
                self.match(BKITParser.RK)
                self.state = 164
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
        self.enterRule(localctx, 18, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BKITParser.IDENTIFIER)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LK:
                self.state = 166
                self.match(BKITParser.LK)
                self.state = 167
                self.match(BKITParser.INTEGER)
                self.state = 168
                self.match(BKITParser.RK)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self.match(BKITParser.AS)
            self.state = 175
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

        def non_initted_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Non_initted_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Non_initted_varContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_para_list




    def para_list(self):

        localctx = BKITParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.non_initted_var()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 178
                self.match(BKITParser.CM)
                self.state = 179
                self.non_initted_var()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 22, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(BKITParser.IF)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(BKITParser.THEN)
            self.state = 188
            self.stm_list()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 189
                self.match(BKITParser.ELSEIF)
                self.state = 190
                self.expression()
                self.state = 191
                self.match(BKITParser.THEN)
                self.state = 192
                self.stm_list()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 199
                self.match(BKITParser.ELSE)
                self.state = 200
                self.stm_list()


            self.state = 203
            self.match(BKITParser.ENDIF)
            self.state = 204
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

        def composite_ass(self):
            return self.getTypedRuleContext(BKITParser.Composite_assContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 207
                self.composite_ass()
                pass


            self.state = 210
            self.match(BKITParser.AS)
            self.state = 211
            self.expression()
            self.state = 212
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_assContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_ass




    def composite_ass(self):

        localctx = BKITParser.Composite_assContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_composite_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expression()
            self.state = 215
            self.index_op()
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

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


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
            self.state = 217
            self.match(BKITParser.FOR)
            self.state = 218
            self.match(BKITParser.LP)
            self.state = 219
            self.match(BKITParser.IDENTIFIER)
            self.state = 220
            self.match(BKITParser.AS)
            self.state = 221
            self.expression()
            self.state = 222
            self.match(BKITParser.CM)
            self.state = 223
            self.expression()
            self.state = 224
            self.match(BKITParser.CM)
            self.state = 225
            self.exp1(0)
            self.state = 226
            self.match(BKITParser.RP)
            self.state = 227
            self.match(BKITParser.DO)
            self.state = 228
            self.stm_list()
            self.state = 229
            self.match(BKITParser.ENDFOR)
            self.state = 230
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
            self.state = 232
            self.match(BKITParser.WHILE)
            self.state = 233
            self.expression()
            self.state = 234
            self.match(BKITParser.DO)
            self.state = 235
            self.stm_list()
            self.state = 236
            self.match(BKITParser.ENDWHILE)
            self.state = 237
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
            self.state = 239
            self.match(BKITParser.DO)
            self.state = 240
            self.stm_list()
            self.state = 241
            self.match(BKITParser.WHILE)
            self.state = 242
            self.expression()
            self.state = 243
            self.match(BKITParser.ENDDO)
            self.state = 244
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
            self.state = 246
            self.match(BKITParser.BREAK)
            self.state = 247
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
            self.state = 249
            self.match(BKITParser.CONTINUE)
            self.state = 250
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
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BKITParser.RETURN)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
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
            self.state = 265
            self.match(BKITParser.IDENTIFIER)
            self.state = 266
            self.match(BKITParser.LP)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
                self.state = 267
                self.expression()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 268
                    self.match(BKITParser.CM)
                    self.state = 269
                    self.expression()
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 277
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
            self.state = 279
            self.func_call()
            self.state = 280
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
            self.state = 286 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 282
                    self.match(BKITParser.LK)
                    self.state = 283
                    self.expression()
                    self.state = 284
                    self.match(BKITParser.RK)

                else:
                    raise NoViableAltException(self)
                self.state = 288 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 290
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.exp1(0)
                self.state = 293
                self.match(BKITParser.RELATION_OP)
                self.state = 294
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
            self.state = 300
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.BAND or _la==BKITParser.BOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 304
                    self.exp2(0) 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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


        def ADDSUB(self):
            return self.getToken(BKITParser.ADDSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 314
                    self.match(BKITParser.ADDSUB)
                    self.state = 315
                    self.exp3(0) 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 322
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 325
                    self.match(BKITParser.MULDIV)
                    self.state = 326
                    self.exp4() 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BNEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(BKITParser.BNEG)
                self.state = 333
                self.exp4()
                pass
            elif token in [BKITParser.ADDSUB, BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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

        def ADDSUB(self):
            return self.getToken(BKITParser.ADDSUB, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp5)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ADDSUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BKITParser.ADDSUB)
                self.state = 338
                self.exp5()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.exp6(0)
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

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 345
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    self.index_op() 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(BKITParser.LP)

                self.state = 357
                self.expression()
                self.state = 358
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(BKITParser.IDENTIFIER)
                pass
            elif token in [BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
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

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


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
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.match(BKITParser.BOLEAN)
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 371
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
            self.state = 374
            self.match(BKITParser.BOLEAN)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 375
                    self.match(BKITParser.CM)
                    self.state = 376
                    self.match(BKITParser.BOLEAN) 
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
            self.state = 382
            self.match(BKITParser.INTEGER)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383
                    self.match(BKITParser.CM)
                    self.state = 384
                    self.match(BKITParser.INTEGER) 
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
            self.state = 390
            self.match(BKITParser.FLOAT)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 391
                    self.match(BKITParser.CM)
                    self.state = 392
                    self.match(BKITParser.FLOAT) 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 398
            self.match(BKITParser.LSTRING)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 399
                    self.match(BKITParser.CM)
                    self.state = 400
                    self.match(BKITParser.LSTRING) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.int_array()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.float_array()
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.string_array()
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
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

        def array_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_listContext,i)


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_indexContext,i)


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
            self.state = 412
            self.match(BKITParser.LB)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (BKITParser.LB - 8)) | (1 << (BKITParser.INTEGER - 8)) | (1 << (BKITParser.FLOAT - 8)) | (1 << (BKITParser.BOLEAN - 8)) | (1 << (BKITParser.LSTRING - 8)))) != 0):
                self.state = 415
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LB]:
                    self.state = 413
                    self.array_list()
                    pass
                elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                    self.state = 414
                    self.array_index()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 417
                    self.match(BKITParser.CM)
                    self.state = 420
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.LB]:
                        self.state = 418
                        self.array_list()
                        pass
                    elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                        self.state = 419
                        self.array_index()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 426
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 429
            self.match(BKITParser.RB)
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
        self._predicates[30] = self.exp6_sempred
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
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




