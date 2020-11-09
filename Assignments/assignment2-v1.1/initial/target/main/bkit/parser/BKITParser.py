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
        buf.write("\u01c9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\7\2^\n\2\f\2\16\2a\13\2\3\2\7\2d\n\2\f\2\16\2g\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3o\n\3\3\3\3\3\3\4\3\4\5\4")
        buf.write("u\n\4\3\4\3\4\3\4\5\4z\n\4\7\4|\n\4\f\4\16\4\177\13\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0089\n\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\b\7\b\u0094\n\b\f\b\16\b\u0097")
        buf.write("\13\b\3\b\7\b\u009a\n\b\f\b\16\b\u009d\13\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a8\n\t\3\n\3\n\5\n\u00ac")
        buf.write("\n\n\3\13\3\13\5\13\u00b0\n\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\6\17\u00c0\n\17")
        buf.write("\r\17\16\17\u00c1\3\20\3\20\5\20\u00c6\n\20\3\20\3\20")
        buf.write("\3\20\5\20\u00cb\n\20\7\20\u00cd\n\20\f\20\16\20\u00d0")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00db\n\21\f\21\16\21\u00de\13\21\3\21\3\21\5\21\u00e2")
        buf.write("\n\21\3\21\3\21\3\21\3\22\3\22\5\22\u00e9\n\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0119\n\31\f\31\16\31\u011c\13\31\5\31\u011e")
        buf.write("\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0127\n")
        buf.write("\32\f\32\16\32\u012a\13\32\5\32\u012c\n\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\6\34\u0137\n\34\r\34")
        buf.write("\16\34\u0138\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u0142")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u014a\n\37\f")
        buf.write("\37\16\37\u014d\13\37\3 \3 \3 \3 \3 \3 \7 \u0155\n \f")
        buf.write(" \16 \u0158\13 \3!\3!\3!\3!\3!\3!\7!\u0160\n!\f!\16!\u0163")
        buf.write("\13!\3\"\3\"\3\"\5\"\u0168\n\"\3#\3#\3#\5#\u016d\n#\3")
        buf.write("$\3$\3$\3$\3$\7$\u0174\n$\f$\16$\u0177\13$\3%\3%\5%\u017b")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0182\n&\3\'\3\'\3\'\5\'\u0187\n")
        buf.write("\'\3(\3(\3(\3(\3(\5(\u018e\n(\3)\3)\3)\7)\u0193\n)\f)")
        buf.write("\16)\u0196\13)\3*\3*\3*\7*\u019b\n*\f*\16*\u019e\13*\3")
        buf.write("+\3+\3+\7+\u01a3\n+\f+\16+\u01a6\13+\3,\3,\3,\7,\u01ab")
        buf.write("\n,\f,\16,\u01ae\13,\3-\3-\3-\3-\5-\u01b4\n-\3.\3.\3.")
        buf.write("\5.\u01b9\n.\3.\3.\3.\5.\u01be\n.\7.\u01c0\n.\f.\16.\u01c3")
        buf.write("\13.\5.\u01c5\n.\3.\3.\3.\2\6<>@F/\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\2\3\3\2,-\2\u01d4\2_\3\2\2\2\4j\3\2\2\2\6t\3\2\2")
        buf.write("\2\b\u0080\3\2\2\2\n\u0082\3\2\2\2\f\u0090\3\2\2\2\16")
        buf.write("\u0095\3\2\2\2\20\u00a7\3\2\2\2\22\u00ab\3\2\2\2\24\u00af")
        buf.write("\3\2\2\2\26\u00b1\3\2\2\2\30\u00b5\3\2\2\2\32\u00b9\3")
        buf.write("\2\2\2\34\u00bb\3\2\2\2\36\u00c5\3\2\2\2 \u00d1\3\2\2")
        buf.write("\2\"\u00e8\3\2\2\2$\u00ee\3\2\2\2&\u00f1\3\2\2\2(\u0100")
        buf.write("\3\2\2\2*\u0107\3\2\2\2,\u010e\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u0114\3\2\2\2\62\u0121\3\2\2\2\64\u012f\3\2\2\2\66")
        buf.write("\u0136\3\2\2\28\u013a\3\2\2\2:\u0141\3\2\2\2<\u0143\3")
        buf.write("\2\2\2>\u014e\3\2\2\2@\u0159\3\2\2\2B\u0167\3\2\2\2D\u016c")
        buf.write("\3\2\2\2F\u016e\3\2\2\2H\u017a\3\2\2\2J\u0181\3\2\2\2")
        buf.write("L\u0186\3\2\2\2N\u018d\3\2\2\2P\u018f\3\2\2\2R\u0197\3")
        buf.write("\2\2\2T\u019f\3\2\2\2V\u01a7\3\2\2\2X\u01b3\3\2\2\2Z\u01b5")
        buf.write("\3\2\2\2\\^\5\4\3\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3")
        buf.write("\2\2\2`e\3\2\2\2a_\3\2\2\2bd\5\n\6\2cb\3\2\2\2dg\3\2\2")
        buf.write("\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7\2\2\3i")
        buf.write("\3\3\2\2\2jk\7/\2\2kl\7\21\2\2ln\5\6\4\2mo\7.\2\2nm\3")
        buf.write("\2\2\2no\3\2\2\2op\3\2\2\2pq\7\20\2\2q\5\3\2\2\2ru\5\24")
        buf.write("\13\2su\5\22\n\2tr\3\2\2\2ts\3\2\2\2u}\3\2\2\2vy\7\22")
        buf.write("\2\2wz\5\24\13\2xz\5\22\n\2yw\3\2\2\2yx\3\2\2\2z|\3\2")
        buf.write("\2\2{v\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\7\3\2")
        buf.write("\2\2\177}\3\2\2\2\u0080\u0081\3\2\2\2\u0081\t\3\2\2\2")
        buf.write("\u0082\u0083\7\60\2\2\u0083\u0084\7\21\2\2\u0084\u0088")
        buf.write("\7\t\2\2\u0085\u0086\79\2\2\u0086\u0087\7\21\2\2\u0087")
        buf.write("\u0089\5\36\20\2\u0088\u0085\3\2\2\2\u0088\u0089\3\2\2")
        buf.write("\2\u0089\u008a\3\2\2\2\u008a\u008b\7\61\2\2\u008b\u008c")
        buf.write("\7\21\2\2\u008c\u008d\5\f\7\2\u008d\u008e\7<\2\2\u008e")
        buf.write("\u008f\7\23\2\2\u008f\13\3\2\2\2\u0090\u0091\5\16\b\2")
        buf.write("\u0091\r\3\2\2\2\u0092\u0094\5\4\3\2\u0093\u0092\3\2\2")
        buf.write("\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u009b\3\2\2\2\u0097\u0095\3\2\2\2\u0098")
        buf.write("\u009a\5\20\t\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\17\3")
        buf.write("\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a8\5\"\22\2\u009f")
        buf.write("\u00a8\5 \21\2\u00a0\u00a8\5&\24\2\u00a1\u00a8\5(\25\2")
        buf.write("\u00a2\u00a8\5*\26\2\u00a3\u00a8\5,\27\2\u00a4\u00a8\5")
        buf.write(".\30\2\u00a5\u00a8\5\64\33\2\u00a6\u00a8\5\60\31\2\u00a7")
        buf.write("\u009e\3\2\2\2\u00a7\u009f\3\2\2\2\u00a7\u00a0\3\2\2\2")
        buf.write("\u00a7\u00a1\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3\3")
        buf.write("\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\21\3\2\2\2\u00a9\u00ac\5\32\16\2\u00aa")
        buf.write("\u00ac\5\34\17\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2")
        buf.write("\2\u00ac\23\3\2\2\2\u00ad\u00b0\5\26\f\2\u00ae\u00b0\5")
        buf.write("\30\r\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\25\3\2\2\2\u00b1\u00b2\5\32\16\2\u00b2\u00b3\7.\2\2\u00b3")
        buf.write("\u00b4\5N(\2\u00b4\27\3\2\2\2\u00b5\u00b6\5\34\17\2\u00b6")
        buf.write("\u00b7\7.\2\2\u00b7\u00b8\5N(\2\u00b8\31\3\2\2\2\u00b9")
        buf.write("\u00ba\7\t\2\2\u00ba\33\3\2\2\2\u00bb\u00bf\7\t\2\2\u00bc")
        buf.write("\u00bd\7\f\2\2\u00bd\u00be\7\24\2\2\u00be\u00c0\7\r\2")
        buf.write("\2\u00bf\u00bc\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\35\3\2\2\2\u00c3\u00c6")
        buf.write("\5\32\16\2\u00c4\u00c6\5\34\17\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\u00ce\3\2\2\2\u00c7\u00ca\7\22\2")
        buf.write("\2\u00c8\u00cb\5\32\16\2\u00c9\u00cb\5\34\17\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc")
        buf.write("\u00c7\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\37\3\2\2\2\u00d0\u00ce\3\2")
        buf.write("\2\2\u00d1\u00d2\7\64\2\2\u00d2\u00d3\58\35\2\u00d3\u00d4")
        buf.write("\7B\2\2\u00d4\u00dc\5\16\b\2\u00d5\u00d6\7\67\2\2\u00d6")
        buf.write("\u00d7\58\35\2\u00d7\u00d8\7B\2\2\u00d8\u00d9\5\16\b\2")
        buf.write("\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2\2\u00db\u00de\3")
        buf.write("\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e1")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\62\2\2\u00e0")
        buf.write("\u00e2\5\16\b\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2")
        buf.write("\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7A\2\2\u00e4\u00e5")
        buf.write("\7\23\2\2\u00e5!\3\2\2\2\u00e6\u00e9\5\32\16\2\u00e7\u00e9")
        buf.write("\5$\23\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\7.\2\2\u00eb\u00ec\58\35\2")
        buf.write("\u00ec\u00ed\7\20\2\2\u00ed#\3\2\2\2\u00ee\u00ef\7\t\2")
        buf.write("\2\u00ef\u00f0\5\66\34\2\u00f0%\3\2\2\2\u00f1\u00f2\7")
        buf.write("=\2\2\u00f2\u00f3\7\16\2\2\u00f3\u00f4\5\32\16\2\u00f4")
        buf.write("\u00f5\7.\2\2\u00f5\u00f6\58\35\2\u00f6\u00f7\7\22\2\2")
        buf.write("\u00f7\u00f8\58\35\2\u00f8\u00f9\7\22\2\2\u00f9\u00fa")
        buf.write("\5<\37\2\u00fa\u00fb\7\17\2\2\u00fb\u00fc\7@\2\2\u00fc")
        buf.write("\u00fd\5\16\b\2\u00fd\u00fe\7\63\2\2\u00fe\u00ff\7\23")
        buf.write("\2\2\u00ff\'\3\2\2\2\u0100\u0101\7:\2\2\u0101\u0102\5")
        buf.write("8\35\2\u0102\u0103\7@\2\2\u0103\u0104\5\16\b\2\u0104\u0105")
        buf.write("\78\2\2\u0105\u0106\7\23\2\2\u0106)\3\2\2\2\u0107\u0108")
        buf.write("\7@\2\2\u0108\u0109\5\16\b\2\u0109\u010a\7:\2\2\u010a")
        buf.write("\u010b\58\35\2\u010b\u010c\7\65\2\2\u010c\u010d\7\23\2")
        buf.write("\2\u010d+\3\2\2\2\u010e\u010f\7\66\2\2\u010f\u0110\7\20")
        buf.write("\2\2\u0110-\3\2\2\2\u0111\u0112\7;\2\2\u0112\u0113\7\20")
        buf.write("\2\2\u0113/\3\2\2\2\u0114\u011d\7>\2\2\u0115\u011a\58")
        buf.write("\35\2\u0116\u0117\7\22\2\2\u0117\u0119\58\35\2\u0118\u0116")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011d\u0115\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0120\7\20\2\2\u0120\61\3\2\2\2\u0121\u0122")
        buf.write("\7\t\2\2\u0122\u012b\7\16\2\2\u0123\u0128\58\35\2\u0124")
        buf.write("\u0125\7\22\2\2\u0125\u0127\58\35\2\u0126\u0124\3\2\2")
        buf.write("\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012b")
        buf.write("\u0123\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u012e\7\17\2\2\u012e\63\3\2\2\2\u012f\u0130\5\62")
        buf.write("\32\2\u0130\u0131\7\20\2\2\u0131\65\3\2\2\2\u0132\u0133")
        buf.write("\7\f\2\2\u0133\u0134\58\35\2\u0134\u0135\7\r\2\2\u0135")
        buf.write("\u0137\3\2\2\2\u0136\u0132\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\67\3\2")
        buf.write("\2\2\u013a\u013b\5:\36\2\u013b9\3\2\2\2\u013c\u013d\5")
        buf.write("<\37\2\u013d\u013e\7\5\2\2\u013e\u013f\5<\37\2\u013f\u0142")
        buf.write("\3\2\2\2\u0140\u0142\5<\37\2\u0141\u013c\3\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142;\3\2\2\2\u0143\u0144\b\37\1\2\u0144")
        buf.write("\u0145\5> \2\u0145\u014b\3\2\2\2\u0146\u0147\f\4\2\2\u0147")
        buf.write("\u0148\t\2\2\2\u0148\u014a\5> \2\u0149\u0146\3\2\2\2\u014a")
        buf.write("\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c=\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\b \1\2")
        buf.write("\u014f\u0150\5@!\2\u0150\u0156\3\2\2\2\u0151\u0152\f\4")
        buf.write("\2\2\u0152\u0153\7\6\2\2\u0153\u0155\5@!\2\u0154\u0151")
        buf.write("\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157?\3\2\2\2\u0158\u0156\3\2\2\2\u0159")
        buf.write("\u015a\b!\1\2\u015a\u015b\5B\"\2\u015b\u0161\3\2\2\2\u015c")
        buf.write("\u015d\f\4\2\2\u015d\u015e\7\7\2\2\u015e\u0160\5B\"\2")
        buf.write("\u015f\u015c\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3")
        buf.write("\2\2\2\u0161\u0162\3\2\2\2\u0162A\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0164\u0165\7+\2\2\u0165\u0168\5B\"\2\u0166\u0168")
        buf.write("\5D#\2\u0167\u0164\3\2\2\2\u0167\u0166\3\2\2\2\u0168C")
        buf.write("\3\2\2\2\u0169\u016a\7\6\2\2\u016a\u016d\5D#\2\u016b\u016d")
        buf.write("\5F$\2\u016c\u0169\3\2\2\2\u016c\u016b\3\2\2\2\u016dE")
        buf.write("\3\2\2\2\u016e\u016f\b$\1\2\u016f\u0170\5H%\2\u0170\u0175")
        buf.write("\3\2\2\2\u0171\u0172\f\4\2\2\u0172\u0174\5\66\34\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176G\3\2\2\2\u0177\u0175\3\2\2")
        buf.write("\2\u0178\u017b\5\62\32\2\u0179\u017b\5J&\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u0179\3\2\2\2\u017bI\3\2\2\2\u017c\u017d")
        buf.write("\7\16\2\2\u017d\u017e\58\35\2\u017e\u017f\7\17\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u0182\5L\'\2\u0181\u017c\3\2\2\2")
        buf.write("\u0181\u0180\3\2\2\2\u0182K\3\2\2\2\u0183\u0187\7\t\2")
        buf.write("\2\u0184\u0187\5N(\2\u0185\u0187\7\26\2\2\u0186\u0183")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("M\3\2\2\2\u0188\u018e\5Z.\2\u0189\u018e\7\24\2\2\u018a")
        buf.write("\u018e\7\25\2\2\u018b\u018e\7\26\2\2\u018c\u018e\7H\2")
        buf.write("\2\u018d\u0188\3\2\2\2\u018d\u0189\3\2\2\2\u018d\u018a")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("O\3\2\2\2\u018f\u0194\7\26\2\2\u0190\u0191\7\22\2\2\u0191")
        buf.write("\u0193\7\26\2\2\u0192\u0190\3\2\2\2\u0193\u0196\3\2\2")
        buf.write("\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195Q\3\2")
        buf.write("\2\2\u0196\u0194\3\2\2\2\u0197\u019c\7\24\2\2\u0198\u0199")
        buf.write("\7\22\2\2\u0199\u019b\7\24\2\2\u019a\u0198\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019dS\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a4\7\25\2")
        buf.write("\2\u01a0\u01a1\7\22\2\2\u01a1\u01a3\7\25\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5U\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("\u01ac\7H\2\2\u01a8\u01a9\7\22\2\2\u01a9\u01ab\7H\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01adW\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01b4\5R*\2\u01b0\u01b4\5T+\2\u01b1\u01b4")
        buf.write("\5V,\2\u01b2\u01b4\5P)\2\u01b3\u01af\3\2\2\2\u01b3\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("Y\3\2\2\2\u01b5\u01c4\7\n\2\2\u01b6\u01b9\5Z.\2\u01b7")
        buf.write("\u01b9\5X-\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01c1\3\2\2\2\u01ba\u01bd\7\22\2\2\u01bb\u01be\5Z.\2")
        buf.write("\u01bc\u01be\5X-\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2")
        buf.write("\2\2\u01be\u01c0\3\2\2\2\u01bf\u01ba\3\2\2\2\u01c0\u01c3")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01b8\3\2\2\2")
        buf.write("\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\7")
        buf.write("\13\2\2\u01c7[\3\2\2\2._enty}\u0088\u0095\u009b\u00a7")
        buf.write("\u00ab\u00af\u00c1\u00c5\u00ca\u00ce\u00dc\u00e1\u00e8")
        buf.write("\u011a\u011d\u0128\u012b\u0138\u0141\u014b\u0156\u0161")
        buf.write("\u0167\u016c\u0175\u017a\u0181\u0186\u018d\u0194\u019c")
        buf.write("\u01a4\u01ac\u01b3\u01b8\u01bd\u01c1\u01c4")
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
    RULE_bool_array = 39
    RULE_int_array = 40
    RULE_float_array = 41
    RULE_string_array = 42
    RULE_array_index = 43
    RULE_array_list = 44

    ruleNames =  [ "program", "var_declare", "var_list", "main_func", "func_declare", 
                   "func_body", "stm_list", "stm", "non_initted_var", "initted_var", 
                   "scalar_init", "composite_init", "scalar_var", "composite_var", 
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
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 90
                self.var_declare()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 96
                self.func_declare()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
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
            self.state = 104
            self.match(BKITParser.VAR)
            self.state = 105
            self.match(BKITParser.COLON)
            self.state = 106
            self.var_list()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.AS:
                self.state = 107
                self.match(BKITParser.AS)


            self.state = 110
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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 112
                self.initted_var()
                pass

            elif la_ == 2:
                self.state = 113
                self.non_initted_var()
                pass


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 116
                self.match(BKITParser.CM)
                self.state = 119
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 117
                    self.initted_var()
                    pass

                elif la_ == 2:
                    self.state = 118
                    self.non_initted_var()
                    pass


                self.state = 125
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
            self.state = 128
            self.match(BKITParser.FUNCTION)
            self.state = 129
            self.match(BKITParser.COLON)
            self.state = 130
            self.match(BKITParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 131
                self.match(BKITParser.PARAMETER)
                self.state = 132
                self.match(BKITParser.COLON)
                self.state = 133
                self.para_list()


            self.state = 136
            self.match(BKITParser.BODY)
            self.state = 137
            self.match(BKITParser.COLON)
            self.state = 138
            self.func_body()
            self.state = 139
            self.match(BKITParser.ENDBODY)
            self.state = 140
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm_list" ):
                return visitor.visitStm_list(self)
            else:
                return visitor.visitChildren(self)




    def stm_list(self):

        localctx = BKITParser.Stm_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stm_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 144
                self.var_declare()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    self.stm() 
                self.state = 155
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 161
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 162
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 163
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 164
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
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
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.scalar_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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
            self.state = 175
            self.scalar_var()
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
            self.state = 179
            self.composite_var()
            self.state = 180
            self.match(BKITParser.AS)
            self.state = 181
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
            self.state = 183
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
            self.state = 185
            self.match(BKITParser.IDENTIFIER)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.match(BKITParser.LK)
                self.state = 187
                self.match(BKITParser.INTEGER)
                self.state = 188
                self.match(BKITParser.RK)
                self.state = 191 
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 193
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 194
                self.composite_var()
                pass


            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 197
                self.match(BKITParser.CM)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 198
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 199
                    self.composite_var()
                    pass


                self.state = 206
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
            self.state = 207
            self.match(BKITParser.IF)
            self.state = 208
            self.expression()
            self.state = 209
            self.match(BKITParser.THEN)
            self.state = 210
            self.stm_list()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 211
                self.match(BKITParser.ELSEIF)
                self.state = 212
                self.expression()
                self.state = 213
                self.match(BKITParser.THEN)
                self.state = 214
                self.stm_list()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 221
                self.match(BKITParser.ELSE)
                self.state = 222
                self.stm_list()


            self.state = 225
            self.match(BKITParser.ENDIF)
            self.state = 226
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 228
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 229
                self.composite_ass()
                pass


            self.state = 232
            self.match(BKITParser.AS)
            self.state = 233
            self.expression()
            self.state = 234
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
            self.state = 236
            self.match(BKITParser.IDENTIFIER)
            self.state = 237
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

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


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
            self.state = 239
            self.match(BKITParser.FOR)
            self.state = 240
            self.match(BKITParser.LP)
            self.state = 241
            self.scalar_var()
            self.state = 242
            self.match(BKITParser.AS)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(BKITParser.CM)
            self.state = 245
            self.expression()
            self.state = 246
            self.match(BKITParser.CM)
            self.state = 247
            self.exp1(0)
            self.state = 248
            self.match(BKITParser.RP)
            self.state = 249
            self.match(BKITParser.DO)
            self.state = 250
            self.stm_list()
            self.state = 251
            self.match(BKITParser.ENDFOR)
            self.state = 252
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
            self.state = 254
            self.match(BKITParser.WHILE)
            self.state = 255
            self.expression()
            self.state = 256
            self.match(BKITParser.DO)
            self.state = 257
            self.stm_list()
            self.state = 258
            self.match(BKITParser.ENDWHILE)
            self.state = 259
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
            self.state = 261
            self.match(BKITParser.DO)
            self.state = 262
            self.stm_list()
            self.state = 263
            self.match(BKITParser.WHILE)
            self.state = 264
            self.expression()
            self.state = 265
            self.match(BKITParser.ENDDO)
            self.state = 266
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
            self.state = 268
            self.match(BKITParser.BREAK)
            self.state = 269
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
            self.state = 271
            self.match(BKITParser.CONTINUE)
            self.state = 272
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
            self.state = 274
            self.match(BKITParser.RETURN)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
                self.state = 275
                self.expression()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 276
                    self.match(BKITParser.CM)
                    self.state = 277
                    self.expression()
                    self.state = 282
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 285
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
            self.state = 287
            self.match(BKITParser.IDENTIFIER)
            self.state = 288
            self.match(BKITParser.LP)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDSUB) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOLEAN) | (1 << BKITParser.BNEG))) != 0) or _la==BKITParser.LSTRING:
                self.state = 289
                self.expression()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 290
                    self.match(BKITParser.CM)
                    self.state = 291
                    self.expression()
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 299
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
            self.state = 301
            self.func_call()
            self.state = 302
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
            self.state = 308 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 304
                    self.match(BKITParser.LK)
                    self.state = 305
                    self.expression()
                    self.state = 306
                    self.match(BKITParser.RK)

                else:
                    raise NoViableAltException(self)
                self.state = 310 
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
            self.state = 312
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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.exp1(0)
                self.state = 315
                self.match(BKITParser.RELATION_OP)
                self.state = 316
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
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
            self.state = 322
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.BAND or _la==BKITParser.BOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.exp2(0) 
                self.state = 331
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
            self.state = 333
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 336
                    self.match(BKITParser.ADDSUB)
                    self.state = 337
                    self.exp3(0) 
                self.state = 342
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
            self.state = 344
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 347
                    self.match(BKITParser.MULDIV)
                    self.state = 348
                    self.exp4() 
                self.state = 353
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
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BNEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(BKITParser.BNEG)
                self.state = 355
                self.exp4()
                pass
            elif token in [BKITParser.ADDSUB, BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ADDSUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(BKITParser.ADDSUB)
                self.state = 360
                self.exp5()
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.LP, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
            self.state = 365
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.index_op() 
                self.state = 373
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
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(BKITParser.LP)

                self.state = 379
                self.expression()
                self.state = 380
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.IDENTIFIER, BKITParser.LB, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
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
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
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
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.array_list()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.match(BKITParser.BOLEAN)
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 394
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_array" ):
                return visitor.visitBool_array(self)
            else:
                return visitor.visitChildren(self)




    def bool_array(self):

        localctx = BKITParser.Bool_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_bool_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(BKITParser.BOLEAN)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 398
                    self.match(BKITParser.CM)
                    self.state = 399
                    self.match(BKITParser.BOLEAN) 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_int_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(BKITParser.INTEGER)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 406
                    self.match(BKITParser.CM)
                    self.state = 407
                    self.match(BKITParser.INTEGER) 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_float_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(BKITParser.FLOAT)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 414
                    self.match(BKITParser.CM)
                    self.state = 415
                    self.match(BKITParser.FLOAT) 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_string_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(BKITParser.LSTRING)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 422
                    self.match(BKITParser.CM)
                    self.state = 423
                    self.match(BKITParser.LSTRING) 
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = BKITParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_index)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.int_array()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.float_array()
                pass
            elif token in [BKITParser.LSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.string_array()
                pass
            elif token in [BKITParser.BOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(BKITParser.LB)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (BKITParser.LB - 8)) | (1 << (BKITParser.INTEGER - 8)) | (1 << (BKITParser.FLOAT - 8)) | (1 << (BKITParser.BOLEAN - 8)) | (1 << (BKITParser.LSTRING - 8)))) != 0):
                self.state = 438
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LB]:
                    self.state = 436
                    self.array_list()
                    pass
                elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                    self.state = 437
                    self.array_index()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 440
                    self.match(BKITParser.CM)
                    self.state = 443
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.LB]:
                        self.state = 441
                        self.array_list()
                        pass
                    elif token in [BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOLEAN, BKITParser.LSTRING]:
                        self.state = 442
                        self.array_index()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 449
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 452
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
         




