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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u019e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\7\2Y\n\2\f\2")
        buf.write("\16\2\\\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3d\n\3\3\3\3\3")
        buf.write("\3\4\3\4\5\4j\n\4\3\4\3\4\3\4\5\4o\n\4\7\4q\n\4\f\4\16")
        buf.write("\4t\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6~\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b\u0088\n\b\r\b\16\b\u0089")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t")
        buf.write("\3\n\3\n\5\n\u009a\n\n\3\13\3\13\5\13\u009e\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\6\17\u00ae\n\17\r\17\16\17\u00af\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00b7\n\20\7\20\u00b9\n\20\f\20\16\20\u00bc")
        buf.write("\13\20\5\20\u00be\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u00c9\n\21\f\21\16\21\u00cc\13\21\3")
        buf.write("\21\3\21\5\21\u00d0\n\21\3\21\3\21\3\21\3\22\3\22\5\22")
        buf.write("\u00d7\n\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\7\31\u0105\n\31\f\31\16\31\u0108\13\31")
        buf.write("\5\31\u010a\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0113\n\32\f\32\16\32\u0116\13\32\5\32\u0118\n\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\6\34\u0123")
        buf.write("\n\34\r\34\16\34\u0124\3\35\3\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\7\36\u012f\n\36\f\36\16\36\u0132\13\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\7\37\u013a\n\37\f\37\16\37\u013d")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \7 \u0145\n \f \16 \u0148\13 ")
        buf.write("\3!\3!\3!\3!\3!\3!\7!\u0150\n!\f!\16!\u0153\13!\3\"\3")
        buf.write("\"\3\"\5\"\u0158\n\"\3#\3#\3#\5#\u015d\n#\3$\3$\3$\3$")
        buf.write("\3$\7$\u0164\n$\f$\16$\u0167\13$\3%\3%\5%\u016b\n%\3&")
        buf.write("\3&\3&\3&\3&\5&\u0172\n&\3\'\3\'\5\'\u0176\n\'\3(\3(\3")
        buf.write("(\3(\3(\5(\u017d\n(\3)\3)\3)\7)\u0182\n)\f)\16)\u0185")
        buf.write("\13)\3*\3*\3*\7*\u018a\n*\f*\16*\u018d\13*\3+\3+\3+\3")
        buf.write("+\5+\u0193\n+\3+\3+\7+\u0197\n+\f+\16+\u019a\13+\3+\3")
        buf.write("+\3+\2\7:<>@F,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\3\3\2CD\2\u01a5")
        buf.write("\2Z\3\2\2\2\4_\3\2\2\2\6i\3\2\2\2\bu\3\2\2\2\nw\3\2\2")
        buf.write("\2\f\u0084\3\2\2\2\16\u0087\3\2\2\2\20\u0095\3\2\2\2\22")
        buf.write("\u0099\3\2\2\2\24\u009d\3\2\2\2\26\u009f\3\2\2\2\30\u00a3")
        buf.write("\3\2\2\2\32\u00a7\3\2\2\2\34\u00a9\3\2\2\2\36\u00bd\3")
        buf.write("\2\2\2 \u00bf\3\2\2\2\"\u00d6\3\2\2\2$\u00dc\3\2\2\2&")
        buf.write("\u00df\3\2\2\2(\u00ec\3\2\2\2*\u00f3\3\2\2\2,\u00fa\3")
        buf.write("\2\2\2.\u00fd\3\2\2\2\60\u0100\3\2\2\2\62\u010d\3\2\2")
        buf.write("\2\64\u011b\3\2\2\2\66\u0122\3\2\2\28\u0126\3\2\2\2:\u0128")
        buf.write("\3\2\2\2<\u0133\3\2\2\2>\u013e\3\2\2\2@\u0149\3\2\2\2")
        buf.write("B\u0157\3\2\2\2D\u015c\3\2\2\2F\u015e\3\2\2\2H\u016a\3")
        buf.write("\2\2\2J\u0171\3\2\2\2L\u0175\3\2\2\2N\u017c\3\2\2\2P\u017e")
        buf.write("\3\2\2\2R\u0186\3\2\2\2T\u018e\3\2\2\2VY\5\4\3\2WY\5\n")
        buf.write("\6\2XV\3\2\2\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2")
        buf.write("\2[]\3\2\2\2\\Z\3\2\2\2]^\7\2\2\3^\3\3\2\2\2_`\7\3\2\2")
        buf.write("`a\7\'\2\2ac\5\6\4\2bd\7E\2\2cb\3\2\2\2cd\3\2\2\2de\3")
        buf.write("\2\2\2ef\7&\2\2f\5\3\2\2\2gj\5\24\13\2hj\5\22\n\2ig\3")
        buf.write("\2\2\2ih\3\2\2\2jr\3\2\2\2kn\7(\2\2lo\5\24\13\2mo\5\22")
        buf.write("\n\2nl\3\2\2\2nm\3\2\2\2oq\3\2\2\2pk\3\2\2\2qt\3\2\2\2")
        buf.write("rp\3\2\2\2rs\3\2\2\2s\7\3\2\2\2tr\3\2\2\2uv\3\2\2\2v\t")
        buf.write("\3\2\2\2wx\7\4\2\2xy\7\'\2\2y}\7\36\2\2z{\7\r\2\2{|\7")
        buf.write("\'\2\2|~\5\36\20\2}z\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\7\5\2\2\u0080\u0081\7\'\2\2\u0081\u0082\5\f\7\2")
        buf.write("\u0082\u0083\7\20\2\2\u0083\13\3\2\2\2\u0084\u0085\5\16")
        buf.write("\b\2\u0085\r\3\2\2\2\u0086\u0088\5\20\t\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\17\3\2\2\2\u008b\u0096\5\4\3\2\u008c")
        buf.write("\u0096\5\"\22\2\u008d\u0096\5 \21\2\u008e\u0096\5&\24")
        buf.write("\2\u008f\u0096\5(\25\2\u0090\u0096\5*\26\2\u0091\u0096")
        buf.write("\5,\27\2\u0092\u0096\5.\30\2\u0093\u0096\5\64\33\2\u0094")
        buf.write("\u0096\5\60\31\2\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2")
        buf.write("\2\u0095\u008d\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f")
        buf.write("\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095")
        buf.write("\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0096\21\3\2\2\2\u0097\u009a\5\32\16\2\u0098\u009a\5")
        buf.write("\34\17\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\23\3\2\2\2\u009b\u009e\5\26\f\2\u009c\u009e\5\30\r\2")
        buf.write("\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e\25\3\2")
        buf.write("\2\2\u009f\u00a0\5\32\16\2\u00a0\u00a1\7E\2\2\u00a1\u00a2")
        buf.write("\5N(\2\u00a2\27\3\2\2\2\u00a3\u00a4\5\34\17\2\u00a4\u00a5")
        buf.write("\7E\2\2\u00a5\u00a6\5N(\2\u00a6\31\3\2\2\2\u00a7\u00a8")
        buf.write("\7\36\2\2\u00a8\33\3\2\2\2\u00a9\u00ad\7\36\2\2\u00aa")
        buf.write("\u00ab\7\"\2\2\u00ab\u00ac\7+\2\2\u00ac\u00ae\7#\2\2\u00ad")
        buf.write("\u00aa\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\35\3\2\2\2\u00b1\u00be\5\32")
        buf.write("\16\2\u00b2\u00ba\5\34\17\2\u00b3\u00b6\7(\2\2\u00b4\u00b7")
        buf.write("\5\32\16\2\u00b5\u00b7\5\34\17\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b3\3\2\2\2")
        buf.write("\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00b1")
        buf.write("\3\2\2\2\u00bd\u00b2\3\2\2\2\u00be\37\3\2\2\2\u00bf\u00c0")
        buf.write("\7\b\2\2\u00c0\u00c1\58\35\2\u00c1\u00c2\7\26\2\2\u00c2")
        buf.write("\u00ca\5\16\b\2\u00c3\u00c4\7\13\2\2\u00c4\u00c5\58\35")
        buf.write("\2\u00c5\u00c6\7\26\2\2\u00c6\u00c7\5\16\b\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cf\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7\6\2\2\u00ce\u00d0\5")
        buf.write("\16\b\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d2\7\25\2\2\u00d2\u00d3\7)\2\2")
        buf.write("\u00d3!\3\2\2\2\u00d4\u00d7\5\32\16\2\u00d5\u00d7\5$\23")
        buf.write("\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00d9\7E\2\2\u00d9\u00da\58\35\2\u00da")
        buf.write("\u00db\7&\2\2\u00db#\3\2\2\2\u00dc\u00dd\7\36\2\2\u00dd")
        buf.write("\u00de\5\66\34\2\u00de%\3\2\2\2\u00df\u00e0\7\21\2\2\u00e0")
        buf.write("\u00e1\7$\2\2\u00e1\u00e2\5\26\f\2\u00e2\u00e3\7(\2\2")
        buf.write("\u00e3\u00e4\58\35\2\u00e4\u00e5\7(\2\2\u00e5\u00e6\5")
        buf.write("8\35\2\u00e6\u00e7\7%\2\2\u00e7\u00e8\7\24\2\2\u00e8\u00e9")
        buf.write("\5\16\b\2\u00e9\u00ea\7\7\2\2\u00ea\u00eb\7)\2\2\u00eb")
        buf.write("\'\3\2\2\2\u00ec\u00ed\7\16\2\2\u00ed\u00ee\58\35\2\u00ee")
        buf.write("\u00ef\7\24\2\2\u00ef\u00f0\5\16\b\2\u00f0\u00f1\7\f\2")
        buf.write("\2\u00f1\u00f2\7)\2\2\u00f2)\3\2\2\2\u00f3\u00f4\7\24")
        buf.write("\2\2\u00f4\u00f5\5\16\b\2\u00f5\u00f6\7\16\2\2\u00f6\u00f7")
        buf.write("\58\35\2\u00f7\u00f8\7\t\2\2\u00f8\u00f9\7)\2\2\u00f9")
        buf.write("+\3\2\2\2\u00fa\u00fb\7\n\2\2\u00fb\u00fc\7&\2\2\u00fc")
        buf.write("-\3\2\2\2\u00fd\u00fe\7\31\2\2\u00fe\u00ff\7&\2\2\u00ff")
        buf.write("/\3\2\2\2\u0100\u0109\7\22\2\2\u0101\u0106\58\35\2\u0102")
        buf.write("\u0103\7(\2\2\u0103\u0105\58\35\2\u0104\u0102\3\2\2\2")
        buf.write("\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u0101")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\7&\2\2\u010c\61\3\2\2\2\u010d\u010e\7\36\2\2\u010e")
        buf.write("\u0117\7$\2\2\u010f\u0114\58\35\2\u0110\u0111\7(\2\2\u0111")
        buf.write("\u0113\58\35\2\u0112\u0110\3\2\2\2\u0113\u0116\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0118\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0117\u010f\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\7%\2\2\u011a")
        buf.write("\63\3\2\2\2\u011b\u011c\5\62\32\2\u011c\u011d\7&\2\2\u011d")
        buf.write("\65\3\2\2\2\u011e\u011f\7\"\2\2\u011f\u0120\58\35\2\u0120")
        buf.write("\u0121\7#\2\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125\67\3\2\2\2\u0126\u0127\5:\36\2\u01279\3\2")
        buf.write("\2\2\u0128\u0129\b\36\1\2\u0129\u012a\5<\37\2\u012a\u0130")
        buf.write("\3\2\2\2\u012b\u012c\f\4\2\2\u012c\u012d\7\32\2\2\u012d")
        buf.write("\u012f\5:\36\5\u012e\u012b\3\2\2\2\u012f\u0132\3\2\2\2")
        buf.write("\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131;\3\2\2")
        buf.write("\2\u0132\u0130\3\2\2\2\u0133\u0134\b\37\1\2\u0134\u0135")
        buf.write("\5> \2\u0135\u013b\3\2\2\2\u0136\u0137\f\4\2\2\u0137\u0138")
        buf.write("\t\2\2\2\u0138\u013a\5> \2\u0139\u0136\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("=\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\b \1\2\u013f")
        buf.write("\u0140\5@!\2\u0140\u0146\3\2\2\2\u0141\u0142\f\4\2\2\u0142")
        buf.write("\u0143\7\33\2\2\u0143\u0145\5@!\2\u0144\u0141\3\2\2\2")
        buf.write("\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147?\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a")
        buf.write("\b!\1\2\u014a\u014b\5B\"\2\u014b\u0151\3\2\2\2\u014c\u014d")
        buf.write("\f\4\2\2\u014d\u014e\7\34\2\2\u014e\u0150\5B\"\2\u014f")
        buf.write("\u014c\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0152\3\2\2\2\u0152A\3\2\2\2\u0153\u0151\3\2\2")
        buf.write("\2\u0154\u0155\7B\2\2\u0155\u0158\5B\"\2\u0156\u0158\5")
        buf.write("D#\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158C\3")
        buf.write("\2\2\2\u0159\u015a\7K\2\2\u015a\u015d\5D#\2\u015b\u015d")
        buf.write("\5F$\2\u015c\u0159\3\2\2\2\u015c\u015b\3\2\2\2\u015dE")
        buf.write("\3\2\2\2\u015e\u015f\b$\1\2\u015f\u0160\5H%\2\u0160\u0165")
        buf.write("\3\2\2\2\u0161\u0162\f\4\2\2\u0162\u0164\5\66\34\2\u0163")
        buf.write("\u0161\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166G\3\2\2\2\u0167\u0165\3\2\2")
        buf.write("\2\u0168\u016b\5\62\32\2\u0169\u016b\5J&\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016bI\3\2\2\2\u016c\u016d")
        buf.write("\7$\2\2\u016d\u016e\58\35\2\u016e\u016f\7%\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u0172\5L\'\2\u0171\u016c\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172K\3\2\2\2\u0173\u0176\7\36\2\2\u0174")
        buf.write("\u0176\5N(\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("M\3\2\2\2\u0177\u017d\5T+\2\u0178\u017d\7+\2\2\u0179\u017d")
        buf.write("\7,\2\2\u017a\u017d\7-\2\2\u017b\u017d\7J\2\2\u017c\u0177")
        buf.write("\3\2\2\2\u017c\u0178\3\2\2\2\u017c\u0179\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017dO\3\2\2\2\u017e")
        buf.write("\u0183\7+\2\2\u017f\u0180\7(\2\2\u0180\u0182\7+\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184Q\3\2\2\2\u0185\u0183\3\2\2")
        buf.write("\2\u0186\u018b\7,\2\2\u0187\u0188\7(\2\2\u0188\u018a\7")
        buf.write(",\2\2\u0189\u0187\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018cS\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018e\u0192\7 \2\2\u018f\u0193\5T+\2\u0190\u0193")
        buf.write("\5P)\2\u0191\u0193\5R*\2\u0192\u018f\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0198\3\2\2\2\u0194")
        buf.write("\u0195\7(\2\2\u0195\u0197\5T+\2\u0196\u0194\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7")
        buf.write("!\2\2\u019cU\3\2\2\2(XZcinr}\u0089\u0095\u0099\u009d\u00af")
        buf.write("\u00b6\u00ba\u00bd\u00ca\u00cf\u00d6\u0106\u0109\u0114")
        buf.write("\u0117\u0124\u0130\u013b\u0146\u0151\u0157\u015c\u0165")
        buf.write("\u016a\u0171\u0175\u017c\u0183\u018b\u0192\u0198")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Var'", "'Function'", "'Body'", "'Else'", 
                     "'EndFor'", "'If'", "'EndDo'", "'Break'", "'ElseIf'", 
                     "'EndWhile'", "'Parameter'", "'While'", "'Continue'", 
                     "'EndBody.'", "'For'", "'Return'", "'True'", "'Do'", 
                     "'EndIf'", "'Then'", "'False'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'", "';'", "':'", "','", "'.'", "'\"'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+.'", "'+'", "'-.'", "'-'", 
                     "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", "'=/='", 
                     "'<=.'", "'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'!'", "'&&'", "'||'", "'='" ]

    symbolicNames = [ "<INVALID>", "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", 
                      "IF", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
                      "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                      "DO", "ENDIF", "THEN", "FALSE", "WS", "COMMENT", "RELATION_OP", 
                      "ADDSUB", "MULDIV", "NEGSIGN", "IDENTIFIER", "ARRAY", 
                      "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", 
                      "CM", "DOT", "DOUQUO", "INTEGER", "FLOAT", "BOLEAN", 
                      "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", 
                      "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", 
                      "FNEQUAL", "FLESSOE", "FGROE", "FLESS", "FGR", "INEQUAL", 
                      "ILESSOE", "IGROE", "ILESS", "IGR", "BNEG", "BAND", 
                      "BOR", "AS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT", "LSTRING", "NSIGN" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_var_list = 2
    RULE_main_func = 3
    RULE_func_declare = 4
    RULE_func_body = 5
    RULE_stm_list = 6
    RULE_stm = 7
    RULE_non_initted_var = 8
    RULE_initted_var = 9
    RULE_scalar_init = 10
    RULE_composite_init = 11
    RULE_scalar_var = 12
    RULE_composite_var = 13
    RULE_para_list = 14
    RULE_if_stmt = 15
    RULE_assign_stmt = 16
    RULE_composite_ass = 17
    RULE_for_stmt = 18
    RULE_while_stmt = 19
    RULE_do_while_stmt = 20
    RULE_break_stmt = 21
    RULE_continue_stmt = 22
    RULE_return_stmt = 23
    RULE_func_call = 24
    RULE_call_stmt = 25
    RULE_index_op = 26
    RULE_expression = 27
    RULE_exp0 = 28
    RULE_exp1 = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_exp7 = 35
    RULE_exp8 = 36
    RULE_operand = 37
    RULE_literals = 38
    RULE_int_array = 39
    RULE_float_array = 40
    RULE_array_list = 41

    ruleNames =  [ "program", "var_declare", "var_list", "main_func", "func_declare", 
                   "func_body", "stm_list", "stm", "non_initted_var", "initted_var", 
                   "scalar_init", "composite_init", "scalar_var", "composite_var", 
                   "para_list", "if_stmt", "assign_stmt", "composite_ass", 
                   "for_stmt", "while_stmt", "do_while_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call", "call_stmt", 
                   "index_op", "expression", "exp0", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "operand", "literals", 
                   "int_array", "float_array", "array_list" ]

    EOF = Token.EOF
    VAR=1
    FUNCTION=2
    BODY=3
    ELSE=4
    ENDFOR=5
    IF=6
    ENDDO=7
    BREAK=8
    ELSEIF=9
    ENDWHILE=10
    PARAMETER=11
    WHILE=12
    CONTINUE=13
    ENDBODY=14
    FOR=15
    RETURN=16
    TRUE=17
    DO=18
    ENDIF=19
    THEN=20
    FALSE=21
    WS=22
    COMMENT=23
    RELATION_OP=24
    ADDSUB=25
    MULDIV=26
    NEGSIGN=27
    IDENTIFIER=28
    ARRAY=29
    LB=30
    RB=31
    LK=32
    RK=33
    LP=34
    RP=35
    SEMI=36
    COLON=37
    CM=38
    DOT=39
    DOUQUO=40
    INTEGER=41
    FLOAT=42
    BOLEAN=43
    FADDOP=44
    IADDOP=45
    FSUBOP=46
    ISUBOP=47
    FMULOP=48
    IMULOP=49
    FDIVOP=50
    IDIVOP=51
    IREMAIN=52
    EQUAL=53
    FNEQUAL=54
    FLESSOE=55
    FGROE=56
    FLESS=57
    FGR=58
    INEQUAL=59
    ILESSOE=60
    IGROE=61
    ILESS=62
    IGR=63
    BNEG=64
    BAND=65
    BOR=66
    AS=67
    ERROR_CHAR=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70
    UNTERMINATED_COMMENT=71
    LSTRING=72
    NSIGN=73

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


        def func_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR or _la==BKITParser.FUNCTION:
                self.state = 86
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 84
                    self.var_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 85
                    self.func_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
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

        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(BKITParser.VAR)
            self.state = 94
            self.match(BKITParser.COLON)
            self.state = 95
            self.var_list()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.AS:
                self.state = 96
                self.match(BKITParser.AS)


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

        def initted_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Initted_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Initted_varContext,i)


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
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 101
                self.initted_var()
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
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.initted_var()
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
            self.state = 130
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 132
                    self.stm()

                else:
                    raise NoViableAltException(self)
                self.state = 135 
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

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
                self.do_while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 144
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 145
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 146
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

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_non_initted_var




    def non_initted_var(self):

        localctx = BKITParser.Non_initted_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_non_initted_var)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.composite_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initted_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_init(self):
            return self.getTypedRuleContext(BKITParser.Scalar_initContext,0)


        def composite_init(self):
            return self.getTypedRuleContext(BKITParser.Composite_initContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_initted_var




    def initted_var(self):

        localctx = BKITParser.Initted_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initted_var)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.scalar_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.composite_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_init




    def scalar_init(self):

        localctx = BKITParser.Scalar_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scalar_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.scalar_var()
            self.state = 158
            self.match(BKITParser.AS)
            self.state = 159
            self.literals()
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


        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_init




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.composite_var()
            self.state = 162
            self.match(BKITParser.AS)
            self.state = 163
            self.literals()
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

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BKITParser.IDENTIFIER)
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
            return BKITParser.RULE_composite_var




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKITParser.IDENTIFIER)
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.match(BKITParser.LK)
                self.state = 169
                self.match(BKITParser.INTEGER)
                self.state = 170
                self.match(BKITParser.RK)
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LK):
                    break

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

        def scalar_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_varContext,i)


        def composite_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Composite_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Composite_varContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_para_list




    def para_list(self):

        localctx = BKITParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.composite_var()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 177
                    self.match(BKITParser.CM)
                    self.state = 180
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 178
                        self.scalar_var()
                        pass

                    elif la_ == 2:
                        self.state = 179
                        self.composite_var()
                        pass


                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BKITParser.IF)
            self.state = 190
            self.expression()
            self.state = 191
            self.match(BKITParser.THEN)
            self.state = 192
            self.stm_list()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 193
                self.match(BKITParser.ELSEIF)
                self.state = 194
                self.expression()
                self.state = 195
                self.match(BKITParser.THEN)
                self.state = 196
                self.stm_list()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 203
                self.match(BKITParser.ELSE)
                self.state = 204
                self.stm_list()


            self.state = 207
            self.match(BKITParser.ENDIF)
            self.state = 208
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

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def composite_ass(self):
            return self.getTypedRuleContext(BKITParser.Composite_assContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 210
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 211
                self.composite_ass()
                pass


            self.state = 214
            self.match(BKITParser.AS)
            self.state = 215
            self.expression()
            self.state = 216
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

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_ass




    def composite_ass(self):

        localctx = BKITParser.Composite_assContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_composite_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BKITParser.IDENTIFIER)
            self.state = 219
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

        def scalar_init(self):
            return self.getTypedRuleContext(BKITParser.Scalar_initContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


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
        self.enterRule(localctx, 36, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(BKITParser.FOR)
            self.state = 222
            self.match(BKITParser.LP)
            self.state = 223
            self.scalar_init()
            self.state = 224
            self.match(BKITParser.CM)
            self.state = 225
            self.expression()
            self.state = 226
            self.match(BKITParser.CM)
            self.state = 227
            self.expression()
            self.state = 228
            self.match(BKITParser.RP)
            self.state = 229
            self.match(BKITParser.DO)
            self.state = 230
            self.stm_list()
            self.state = 231
            self.match(BKITParser.ENDFOR)
            self.state = 232
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
        self.enterRule(localctx, 38, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.WHILE)
            self.state = 235
            self.expression()
            self.state = 236
            self.match(BKITParser.DO)
            self.state = 237
            self.stm_list()
            self.state = 238
            self.match(BKITParser.ENDWHILE)
            self.state = 239
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
        self.enterRule(localctx, 40, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKITParser.DO)
            self.state = 242
            self.stm_list()
            self.state = 243
            self.match(BKITParser.WHILE)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(BKITParser.ENDDO)
            self.state = 246
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
        self.enterRule(localctx, 42, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(BKITParser.BREAK)
            self.state = 249
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

        def COMMENT(self):
            return self.getToken(BKITParser.COMMENT, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.COMMENT)
            self.state = 252
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
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKITParser.RETURN)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 28)) & ~0x3f) == 0 and ((1 << (_la - 28)) & ((1 << (BKITParser.IDENTIFIER - 28)) | (1 << (BKITParser.LB - 28)) | (1 << (BKITParser.LP - 28)) | (1 << (BKITParser.INTEGER - 28)) | (1 << (BKITParser.FLOAT - 28)) | (1 << (BKITParser.BOLEAN - 28)) | (1 << (BKITParser.BNEG - 28)) | (1 << (BKITParser.LSTRING - 28)) | (1 << (BKITParser.NSIGN - 28)))) != 0):
                self.state = 255
                self.expression()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 256
                    self.match(BKITParser.CM)
                    self.state = 257
                    self.expression()
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 265
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
        self.enterRule(localctx, 48, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.IDENTIFIER)
            self.state = 268
            self.match(BKITParser.LP)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 28)) & ~0x3f) == 0 and ((1 << (_la - 28)) & ((1 << (BKITParser.IDENTIFIER - 28)) | (1 << (BKITParser.LB - 28)) | (1 << (BKITParser.LP - 28)) | (1 << (BKITParser.INTEGER - 28)) | (1 << (BKITParser.FLOAT - 28)) | (1 << (BKITParser.BOLEAN - 28)) | (1 << (BKITParser.BNEG - 28)) | (1 << (BKITParser.LSTRING - 28)) | (1 << (BKITParser.NSIGN - 28)))) != 0):
                self.state = 269
                self.expression()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 270
                    self.match(BKITParser.CM)
                    self.state = 271
                    self.expression()
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 279
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
        self.enterRule(localctx, 50, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.func_call()
            self.state = 282
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
        self.enterRule(localctx, 52, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 284
                    self.match(BKITParser.LK)
                    self.state = 285
                    self.expression()
                    self.state = 286
                    self.match(BKITParser.RK)

                else:
                    raise NoViableAltException(self)
                self.state = 290 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.exp0(0)
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

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp0Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp0Context,i)


        def RELATION_OP(self):
            return self.getToken(BKITParser.RELATION_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp0



    def exp0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp0)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self.match(BKITParser.RELATION_OP)
                    self.state = 299
                    self.exp0(3) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.BAND or _la==BKITParser.BOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.exp2(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 320
                    self.match(BKITParser.ADDSUB)
                    self.state = 321
                    self.exp3(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 331
                    self.match(BKITParser.MULDIV)
                    self.state = 332
                    self.exp4() 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_exp4)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BNEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(BKITParser.BNEG)
                self.state = 339
                self.exp4()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING, BKITParser.NSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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

        def NSIGN(self):
            return self.getToken(BKITParser.NSIGN, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(BKITParser.NSIGN)
                self.state = 344
                self.exp5()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 351
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 352
                    self.index_op() 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        self.enterRule(localctx, 72, self.RULE_exp8)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(BKITParser.LP)

                self.state = 363
                self.expression()
                self.state = 364
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
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
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(BKITParser.IDENTIFIER)
                pass
            elif token in [BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
                self.match(BKITParser.BOLEAN)
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 377
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
        self.enterRule(localctx, 78, self.RULE_int_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(BKITParser.INTEGER)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 381
                    self.match(BKITParser.CM)
                    self.state = 382
                    self.match(BKITParser.INTEGER) 
                self.state = 387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_float_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(BKITParser.FLOAT)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 389
                    self.match(BKITParser.CM)
                    self.state = 390
                    self.match(BKITParser.FLOAT) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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


        def int_array(self):
            return self.getTypedRuleContext(BKITParser.Int_arrayContext,0)


        def float_array(self):
            return self.getTypedRuleContext(BKITParser.Float_arrayContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_list




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(BKITParser.LB)
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.state = 397
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER]:
                self.state = 398
                self.int_array()
                pass
            elif token in [BKITParser.FLOAT]:
                self.state = 399
                self.float_array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 402
                self.match(BKITParser.CM)
                self.state = 403
                self.array_list()
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
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
        self._predicates[28] = self.exp0_sempred
        self._predicates[29] = self.exp1_sempred
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[34] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp0_sempred(self, localctx:Exp0Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




