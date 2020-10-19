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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01bc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3m\n\3\3\3\3\3\3\4\3\4\5\4s\n\4")
        buf.write("\3\4\3\4\3\4\5\4x\n\4\7\4z\n\4\f\4\16\4}\13\4\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\7\7\u0090\n\7\f\7\16\7\u0093\13\7\3\7\3\7")
        buf.write("\3\b\7\b\u0098\n\b\f\b\16\b\u009b\13\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00a6\n\t\3\n\3\n\5\n\u00aa\n")
        buf.write("\n\3\13\3\13\5\13\u00ae\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\6\17\u00be\n\17\r")
        buf.write("\17\16\17\u00bf\3\20\3\20\5\20\u00c4\n\20\3\20\3\20\3")
        buf.write("\20\5\20\u00c9\n\20\7\20\u00cb\n\20\f\20\16\20\u00ce\13")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u00d9\n\21\f\21\16\21\u00dc\13\21\3\21\3\21\5\21\u00e0")
        buf.write("\n\21\3\21\3\21\3\21\3\22\3\22\5\22\u00e7\n\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u0115\n\31\f\31\16\31\u0118\13\31\5\31\u011a\n\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0123\n\32\f\32\16")
        buf.write("\32\u0126\13\32\5\32\u0128\n\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\6\34\u0133\n\34\r\34\16\34\u0134")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u013e\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\7\37\u0146\n\37\f\37\16\37")
        buf.write("\u0149\13\37\3 \3 \3 \3 \3 \3 \7 \u0151\n \f \16 \u0154")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\7!\u015c\n!\f!\16!\u015f\13!\3")
        buf.write("\"\3\"\3\"\5\"\u0164\n\"\3#\3#\3#\5#\u0169\n#\3$\3$\3")
        buf.write("$\3$\3$\7$\u0170\n$\f$\16$\u0173\13$\3%\3%\5%\u0177\n")
        buf.write("%\3&\3&\3&\3&\3&\5&\u017e\n&\3\'\3\'\3\'\5\'\u0183\n\'")
        buf.write("\3(\3(\3(\3(\3(\5(\u018a\n(\3)\3)\3)\7)\u018f\n)\f)\16")
        buf.write(")\u0192\13)\3*\3*\3*\7*\u0197\n*\f*\16*\u019a\13*\3+\3")
        buf.write("+\3+\7+\u019f\n+\f+\16+\u01a2\13+\3,\3,\3,\5,\u01a7\n")
        buf.write(",\3-\3-\3-\5-\u01ac\n-\3-\3-\3-\5-\u01b1\n-\7-\u01b3\n")
        buf.write("-\f-\16-\u01b6\13-\5-\u01b8\n-\3-\3-\3-\2\6<>@F.\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVX\2\3\3\2,-\2\u01c6\2]\3\2\2\2\4h\3\2")
        buf.write("\2\2\6r\3\2\2\2\b~\3\2\2\2\n\u0080\3\2\2\2\f\u0091\3\2")
        buf.write("\2\2\16\u0099\3\2\2\2\20\u00a5\3\2\2\2\22\u00a9\3\2\2")
        buf.write("\2\24\u00ad\3\2\2\2\26\u00af\3\2\2\2\30\u00b3\3\2\2\2")
        buf.write("\32\u00b7\3\2\2\2\34\u00b9\3\2\2\2\36\u00c3\3\2\2\2 \u00cf")
        buf.write("\3\2\2\2\"\u00e6\3\2\2\2$\u00ec\3\2\2\2&\u00ef\3\2\2\2")
        buf.write("(\u00fc\3\2\2\2*\u0103\3\2\2\2,\u010a\3\2\2\2.\u010d\3")
        buf.write("\2\2\2\60\u0110\3\2\2\2\62\u011d\3\2\2\2\64\u012b\3\2")
        buf.write("\2\2\66\u0132\3\2\2\28\u0136\3\2\2\2:\u013d\3\2\2\2<\u013f")
        buf.write("\3\2\2\2>\u014a\3\2\2\2@\u0155\3\2\2\2B\u0163\3\2\2\2")
        buf.write("D\u0168\3\2\2\2F\u016a\3\2\2\2H\u0176\3\2\2\2J\u017d\3")
        buf.write("\2\2\2L\u0182\3\2\2\2N\u0189\3\2\2\2P\u018b\3\2\2\2R\u0193")
        buf.write("\3\2\2\2T\u019b\3\2\2\2V\u01a6\3\2\2\2X\u01a8\3\2\2\2")
        buf.write("Z\\\5\4\3\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^")
        buf.write("c\3\2\2\2_]\3\2\2\2`b\5\n\6\2a`\3\2\2\2be\3\2\2\2ca\3")
        buf.write("\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\2\2\3g\3\3\2")
        buf.write("\2\2hi\7/\2\2ij\7\21\2\2jl\5\6\4\2km\7.\2\2lk\3\2\2\2")
        buf.write("lm\3\2\2\2mn\3\2\2\2no\7\20\2\2o\5\3\2\2\2ps\5\24\13\2")
        buf.write("qs\5\22\n\2rp\3\2\2\2rq\3\2\2\2s{\3\2\2\2tw\7\22\2\2u")
        buf.write("x\5\24\13\2vx\5\22\n\2wu\3\2\2\2wv\3\2\2\2xz\3\2\2\2y")
        buf.write("t\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\7\3\2\2\2}{\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\t\3\2\2\2\u0080\u0081\7\60\2\2")
        buf.write("\u0081\u0082\7\21\2\2\u0082\u0086\7\t\2\2\u0083\u0084")
        buf.write("\79\2\2\u0084\u0085\7\21\2\2\u0085\u0087\5\36\20\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\7\61\2\2\u0089\u008a\7\21\2\2\u008a\u008b")
        buf.write("\5\f\7\2\u008b\u008c\7<\2\2\u008c\u008d\7\23\2\2\u008d")
        buf.write("\13\3\2\2\2\u008e\u0090\5\4\3\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\5")
        buf.write("\16\b\2\u0095\r\3\2\2\2\u0096\u0098\5\20\t\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\17\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u00a6\5\"\22\2\u009d\u00a6\5 \21\2\u009e\u00a6\5&\24")
        buf.write("\2\u009f\u00a6\5(\25\2\u00a0\u00a6\5*\26\2\u00a1\u00a6")
        buf.write("\5,\27\2\u00a2\u00a6\5.\30\2\u00a3\u00a6\5\64\33\2\u00a4")
        buf.write("\u00a6\5\60\31\2\u00a5\u009c\3\2\2\2\u00a5\u009d\3\2\2")
        buf.write("\2\u00a5\u009e\3\2\2\2\u00a5\u009f\3\2\2\2\u00a5\u00a0")
        buf.write("\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\21\3\2\2\2\u00a7")
        buf.write("\u00aa\5\32\16\2\u00a8\u00aa\5\34\17\2\u00a9\u00a7\3\2")
        buf.write("\2\2\u00a9\u00a8\3\2\2\2\u00aa\23\3\2\2\2\u00ab\u00ae")
        buf.write("\5\26\f\2\u00ac\u00ae\5\30\r\2\u00ad\u00ab\3\2\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\25\3\2\2\2\u00af\u00b0\5\32\16\2")
        buf.write("\u00b0\u00b1\7.\2\2\u00b1\u00b2\5N(\2\u00b2\27\3\2\2\2")
        buf.write("\u00b3\u00b4\5\34\17\2\u00b4\u00b5\7.\2\2\u00b5\u00b6")
        buf.write("\5N(\2\u00b6\31\3\2\2\2\u00b7\u00b8\7\t\2\2\u00b8\33\3")
        buf.write("\2\2\2\u00b9\u00bd\7\t\2\2\u00ba\u00bb\7\f\2\2\u00bb\u00bc")
        buf.write("\7\24\2\2\u00bc\u00be\7\r\2\2\u00bd\u00ba\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\35\3\2\2\2\u00c1\u00c4\5\32\16\2\u00c2\u00c4\5")
        buf.write("\34\17\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\u00cc\3\2\2\2\u00c5\u00c8\7\22\2\2\u00c6\u00c9\5\32\16")
        buf.write("\2\u00c7\u00c9\5\34\17\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\37\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7\64")
        buf.write("\2\2\u00d0\u00d1\58\35\2\u00d1\u00d2\7B\2\2\u00d2\u00da")
        buf.write("\5\16\b\2\u00d3\u00d4\7\67\2\2\u00d4\u00d5\58\35\2\u00d5")
        buf.write("\u00d6\7B\2\2\u00d6\u00d7\5\16\b\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00d3\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\u00df\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\7\62\2\2\u00de\u00e0\5\16\b\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\7A\2\2\u00e2\u00e3\7\23\2\2\u00e3!\3\2\2")
        buf.write("\2\u00e4\u00e7\5\32\16\2\u00e5\u00e7\5$\23\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\7.\2\2\u00e9\u00ea\58\35\2\u00ea\u00eb\7\20\2\2")
        buf.write("\u00eb#\3\2\2\2\u00ec\u00ed\7\t\2\2\u00ed\u00ee\5\66\34")
        buf.write("\2\u00ee%\3\2\2\2\u00ef\u00f0\7=\2\2\u00f0\u00f1\7\16")
        buf.write("\2\2\u00f1\u00f2\5\26\f\2\u00f2\u00f3\7\22\2\2\u00f3\u00f4")
        buf.write("\58\35\2\u00f4\u00f5\7\22\2\2\u00f5\u00f6\58\35\2\u00f6")
        buf.write("\u00f7\7\17\2\2\u00f7\u00f8\7@\2\2\u00f8\u00f9\5\16\b")
        buf.write("\2\u00f9\u00fa\7\63\2\2\u00fa\u00fb\7\23\2\2\u00fb\'\3")
        buf.write("\2\2\2\u00fc\u00fd\7:\2\2\u00fd\u00fe\58\35\2\u00fe\u00ff")
        buf.write("\7@\2\2\u00ff\u0100\5\16\b\2\u0100\u0101\78\2\2\u0101")
        buf.write("\u0102\7\23\2\2\u0102)\3\2\2\2\u0103\u0104\7@\2\2\u0104")
        buf.write("\u0105\5\16\b\2\u0105\u0106\7:\2\2\u0106\u0107\58\35\2")
        buf.write("\u0107\u0108\7\65\2\2\u0108\u0109\7\23\2\2\u0109+\3\2")
        buf.write("\2\2\u010a\u010b\7\66\2\2\u010b\u010c\7\20\2\2\u010c-")
        buf.write("\3\2\2\2\u010d\u010e\7;\2\2\u010e\u010f\7\20\2\2\u010f")
        buf.write("/\3\2\2\2\u0110\u0119\7>\2\2\u0111\u0116\58\35\2\u0112")
        buf.write("\u0113\7\22\2\2\u0113\u0115\58\35\2\u0114\u0112\3\2\2")
        buf.write("\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0119")
        buf.write("\u0111\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011b\u011c\7\20\2\2\u011c\61\3\2\2\2\u011d\u011e\7\t")
        buf.write("\2\2\u011e\u0127\7\16\2\2\u011f\u0124\58\35\2\u0120\u0121")
        buf.write("\7\22\2\2\u0121\u0123\58\35\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u011f\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a")
        buf.write("\7\17\2\2\u012a\63\3\2\2\2\u012b\u012c\5\62\32\2\u012c")
        buf.write("\u012d\7\20\2\2\u012d\65\3\2\2\2\u012e\u012f\7\f\2\2\u012f")
        buf.write("\u0130\58\35\2\u0130\u0131\7\r\2\2\u0131\u0133\3\2\2\2")
        buf.write("\u0132\u012e\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3")
        buf.write("\2\2\2\u0134\u0135\3\2\2\2\u0135\67\3\2\2\2\u0136\u0137")
        buf.write("\5:\36\2\u01379\3\2\2\2\u0138\u0139\5<\37\2\u0139\u013a")
        buf.write("\7\5\2\2\u013a\u013b\5<\37\2\u013b\u013e\3\2\2\2\u013c")
        buf.write("\u013e\5<\37\2\u013d\u0138\3\2\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e;\3\2\2\2\u013f\u0140\b\37\1\2\u0140\u0141\5> \2")
        buf.write("\u0141\u0147\3\2\2\2\u0142\u0143\f\4\2\2\u0143\u0144\t")
        buf.write("\2\2\2\u0144\u0146\5> \2\u0145\u0142\3\2\2\2\u0146\u0149")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("=\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\b \1\2\u014b")
        buf.write("\u014c\5@!\2\u014c\u0152\3\2\2\2\u014d\u014e\f\4\2\2\u014e")
        buf.write("\u014f\7\6\2\2\u014f\u0151\5@!\2\u0150\u014d\3\2\2\2\u0151")
        buf.write("\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153?\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\b!\1\2")
        buf.write("\u0156\u0157\5B\"\2\u0157\u015d\3\2\2\2\u0158\u0159\f")
        buf.write("\4\2\2\u0159\u015a\7\7\2\2\u015a\u015c\5B\"\2\u015b\u0158")
        buf.write("\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015eA\3\2\2\2\u015f\u015d\3\2\2\2\u0160")
        buf.write("\u0161\7+\2\2\u0161\u0164\5B\"\2\u0162\u0164\5D#\2\u0163")
        buf.write("\u0160\3\2\2\2\u0163\u0162\3\2\2\2\u0164C\3\2\2\2\u0165")
        buf.write("\u0166\7\6\2\2\u0166\u0169\5D#\2\u0167\u0169\5F$\2\u0168")
        buf.write("\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169E\3\2\2\2\u016a")
        buf.write("\u016b\b$\1\2\u016b\u016c\5H%\2\u016c\u0171\3\2\2\2\u016d")
        buf.write("\u016e\f\4\2\2\u016e\u0170\5\66\34\2\u016f\u016d\3\2\2")
        buf.write("\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172G\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0177")
        buf.write("\5\62\32\2\u0175\u0177\5J&\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177I\3\2\2\2\u0178\u0179\7\16\2\2\u0179")
        buf.write("\u017a\58\35\2\u017a\u017b\7\17\2\2\u017b\u017e\3\2\2")
        buf.write("\2\u017c\u017e\5L\'\2\u017d\u0178\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017eK\3\2\2\2\u017f\u0183\7\t\2\2\u0180\u0183")
        buf.write("\5N(\2\u0181\u0183\7\26\2\2\u0182\u017f\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183M\3\2\2\2\u0184")
        buf.write("\u018a\5X-\2\u0185\u018a\7\24\2\2\u0186\u018a\7\25\2\2")
        buf.write("\u0187\u018a\7\26\2\2\u0188\u018a\7H\2\2\u0189\u0184\3")
        buf.write("\2\2\2\u0189\u0185\3\2\2\2\u0189\u0186\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u0188\3\2\2\2\u018aO\3\2\2\2\u018b\u0190")
        buf.write("\7\24\2\2\u018c\u018d\7\22\2\2\u018d\u018f\7\24\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191Q\3\2\2\2\u0192\u0190\3\2\2")
        buf.write("\2\u0193\u0198\7\25\2\2\u0194\u0195\7\22\2\2\u0195\u0197")
        buf.write("\7\25\2\2\u0196\u0194\3\2\2\2\u0197\u019a\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199S\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u01a0\7H\2\2\u019c\u019d\7\22\2\2")
        buf.write("\u019d\u019f\7H\2\2\u019e\u019c\3\2\2\2\u019f\u01a2\3")
        buf.write("\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1U")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a7\5P)\2\u01a4\u01a7")
        buf.write("\5R*\2\u01a5\u01a7\5T+\2\u01a6\u01a3\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7W\3\2\2\2\u01a8\u01b7")
        buf.write("\7\n\2\2\u01a9\u01ac\5X-\2\u01aa\u01ac\5V,\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01b4\3\2\2\2\u01ad")
        buf.write("\u01b0\7\22\2\2\u01ae\u01b1\5X-\2\u01af\u01b1\5V,\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b3\3\2\2\2")
        buf.write("\u01b2\u01ad\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b7\u01ab\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\7\13\2\2\u01baY\3\2\2\2-]c")
        buf.write("lrw{\u0086\u0091\u0099\u00a5\u00a9\u00ad\u00bf\u00c3\u00c8")
        buf.write("\u00cc\u00da\u00df\u00e6\u0116\u0119\u0124\u0127\u0134")
        buf.write("\u013d\u0147\u0152\u015d\u0163\u0168\u0171\u0176\u017d")
        buf.write("\u0182\u0189\u0190\u0198\u01a0\u01a6\u01ab\u01b0\u01b4")
        buf.write("\u01b7")
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
    RULE_string_array = 41
    RULE_array_index = 42
    RULE_array_list = 43

    ruleNames =  [ "program", "var_declare", "var_list", "main_func", "func_declare", 
                   "func_body", "stm_list", "stm", "non_initted_var", "initted_var", 
                   "scalar_init", "composite_init", "scalar_var", "composite_var", 
                   "para_list", "if_stmt", "assign_stmt", "composite_ass", 
                   "for_stmt", "while_stmt", "do_while_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call", "call_stmt", 
                   "index_op", "expression", "exp0", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "operand", "literals", 
                   "int_array", "float_array", "string_array", "array_index", 
                   "array_list" ]

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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 88
                self.var_declare()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 94
                self.func_declare()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BKITParser.VAR)
            self.state = 103
            self.match(BKITParser.COLON)
            self.state = 104
            self.var_list()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.AS:
                self.state = 105
                self.match(BKITParser.AS)


            self.state = 108
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 110
                self.initted_var()
                pass

            elif la_ == 2:
                self.state = 111
                self.non_initted_var()
                pass


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 114
                self.match(BKITParser.CM)
                self.state = 117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 115
                    self.initted_var()
                    pass

                elif la_ == 2:
                    self.state = 116
                    self.non_initted_var()
                    pass


                self.state = 123
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BKITParser.FUNCTION)
            self.state = 127
            self.match(BKITParser.COLON)
            self.state = 128
            self.match(BKITParser.IDENTIFIER)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 129
                self.match(BKITParser.PARAMETER)
                self.state = 130
                self.match(BKITParser.COLON)
                self.state = 131
                self.para_list()


            self.state = 134
            self.match(BKITParser.BODY)
            self.state = 135
            self.match(BKITParser.COLON)
            self.state = 136
            self.func_body()
            self.state = 137
            self.match(BKITParser.ENDBODY)
            self.state = 138
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


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 140
                self.var_declare()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm_list" ):
                return visitor.visitStm_list(self)
            else:
                return visitor.visitChildren(self)




    def stm_list(self):

        localctx = BKITParser.Stm_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stm_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self.stm() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = BKITParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stm)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 160
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 161
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 162
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_initted_var" ):
                return visitor.visitNon_initted_var(self)
            else:
                return visitor.visitChildren(self)




    def non_initted_var(self):

        localctx = BKITParser.Non_initted_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_non_initted_var)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitted_var" ):
                return visitor.visitInitted_var(self)
            else:
                return visitor.visitChildren(self)




    def initted_var(self):

        localctx = BKITParser.Initted_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initted_var)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.scalar_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_init" ):
                return visitor.visitScalar_init(self)
            else:
                return visitor.visitChildren(self)




    def scalar_init(self):

        localctx = BKITParser.Scalar_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scalar_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.scalar_var()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_init" ):
                return visitor.visitComposite_init(self)
            else:
                return visitor.visitChildren(self)




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.composite_var()
            self.state = 178
            self.match(BKITParser.AS)
            self.state = 179
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_var" ):
                return visitor.visitComposite_var(self)
            else:
                return visitor.visitChildren(self)




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(BKITParser.IDENTIFIER)
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.match(BKITParser.LK)
                self.state = 185
                self.match(BKITParser.INTEGER)
                self.state = 186
                self.match(BKITParser.RK)
                self.state = 189 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = BKITParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 191
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 192
                self.composite_var()
                pass


            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 195
                self.match(BKITParser.CM)
                self.state = 198
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 197
                    self.composite_var()
                    pass


                self.state = 204
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(BKITParser.IF)
            self.state = 206
            self.expression()
            self.state = 207
            self.match(BKITParser.THEN)
            self.state = 208
            self.stm_list()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 209
                self.match(BKITParser.ELSEIF)
                self.state = 210
                self.expression()
                self.state = 211
                self.match(BKITParser.THEN)
                self.state = 212
                self.stm_list()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 219
                self.match(BKITParser.ELSE)
                self.state = 220
                self.stm_list()


            self.state = 223
            self.match(BKITParser.ENDIF)
            self.state = 224
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 226
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 227
                self.composite_ass()
                pass


            self.state = 230
            self.match(BKITParser.AS)
            self.state = 231
            self.expression()
            self.state = 232
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_ass" ):
                return visitor.visitComposite_ass(self)
            else:
                return visitor.visitChildren(self)




    def composite_ass(self):

        localctx = BKITParser.Composite_assContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_composite_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.IDENTIFIER)
            self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(BKITParser.FOR)
            self.state = 238
            self.match(BKITParser.LP)
            self.state = 239
            self.scalar_init()
            self.state = 240
            self.match(BKITParser.CM)
            self.state = 241
            self.expression()
            self.state = 242
            self.match(BKITParser.CM)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(BKITParser.RP)
            self.state = 245
            self.match(BKITParser.DO)
            self.state = 246
            self.stm_list()
            self.state = 247
            self.match(BKITParser.ENDFOR)
            self.state = 248
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BKITParser.WHILE)
            self.state = 251
            self.expression()
            self.state = 252
            self.match(BKITParser.DO)
            self.state = 253
            self.stm_list()
            self.state = 254
            self.match(BKITParser.ENDWHILE)
            self.state = 255
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(BKITParser.DO)
            self.state = 258
            self.stm_list()
            self.state = 259
            self.match(BKITParser.WHILE)
            self.state = 260
            self.expression()
            self.state = 261
            self.match(BKITParser.ENDDO)
            self.state = 262
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(BKITParser.BREAK)
            self.state = 265
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.CONTINUE)
            self.state = 268
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BKITParser.RETURN)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
                self.state = 271
                self.expression()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 272
                    self.match(BKITParser.CM)
                    self.state = 273
                    self.expression()
                    self.state = 278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 281
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKITParser.IDENTIFIER)
            self.state = 284
            self.match(BKITParser.LP)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
                self.state = 285
                self.expression()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 286
                    self.match(BKITParser.CM)
                    self.state = 287
                    self.expression()
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 295
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
            self.state = 297
            self.func_call()
            self.state = 298
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 300
                    self.match(BKITParser.LK)
                    self.state = 301
                    self.expression()
                    self.state = 302
                    self.match(BKITParser.RK)

                else:
                    raise NoViableAltException(self)
                self.state = 306 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = BKITParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp0)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.exp1(0)
                self.state = 311
                self.match(BKITParser.RELATION_OP)
                self.state = 312
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 318
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.BAND or _la==BKITParser.BOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.exp2(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 332
                    self.match(BKITParser.ADDSUB)
                    self.state = 333
                    self.exp3(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 343
                    self.match(BKITParser.MULDIV)
                    self.state = 344
                    self.exp4() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp4)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BNEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(BKITParser.BNEG)
                self.state = 351
                self.exp4()
                pass
            elif token in [BKITParser.ADDSUB, BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ADDSUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(BKITParser.ADDSUB)
                self.state = 356
                self.exp5()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    self.index_op() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp8)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(BKITParser.LP)

                self.state = 375
                self.expression()
                self.state = 376
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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


        def BOLEAN(self):
            return self.getToken(BKITParser.BOLEAN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.match(BKITParser.BOLEAN)
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 389
                self.match(BKITParser.BOLEAN)
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 390
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_array" ):
                return visitor.visitInt_array(self)
            else:
                return visitor.visitChildren(self)




    def int_array(self):

        localctx = BKITParser.Int_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_int_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(BKITParser.INTEGER)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 394
                    self.match(BKITParser.CM)
                    self.state = 395
                    self.match(BKITParser.INTEGER) 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_array" ):
                return visitor.visitFloat_array(self)
            else:
                return visitor.visitChildren(self)




    def float_array(self):

        localctx = BKITParser.Float_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_float_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(BKITParser.FLOAT)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 402
                    self.match(BKITParser.CM)
                    self.state = 403
                    self.match(BKITParser.FLOAT) 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_array" ):
                return visitor.visitString_array(self)
            else:
                return visitor.visitChildren(self)




    def string_array(self):

        localctx = BKITParser.String_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_string_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(BKITParser.LSTRING)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 410
                    self.match(BKITParser.CM)
                    self.state = 411
                    self.match(BKITParser.LSTRING) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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


        def getRuleIndex(self):
            return BKITParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = BKITParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_index)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.int_array()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.float_array()
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.string_array()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BKITParser.LB)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (BKITParser.LB - 8)) | (1 << (BKITParser.INTEGER - 8)) | (1 << (BKITParser.FLOAT - 8)) | (1 << (BKITParser.LSTRING - 8)))) != 0):
                self.state = 425
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LB]:
                    self.state = 423
                    self.array_list()
                    pass
                elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.LSTRING]:
                    self.state = 424
                    self.array_index()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 427
                    self.match(BKITParser.CM)
                    self.state = 430
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.LB]:
                        self.state = 428
                        self.array_list()
                        pass
                    elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.LSTRING]:
                        self.state = 429
                        self.array_index()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 436
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 439
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
        self._predicates[29] = self.exp1_sempred
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[34] = self.exp6_sempred
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
         




