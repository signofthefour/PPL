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
        buf.write("\u0245\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\7\2x\n\2\f\2\16\2{\13\2\3\2\7\2~\n\2\f\2\16\2\u0081")
        buf.write("\13\2\3\2\3\2\7\2\u0085\n\2\f\2\16\2\u0088\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0096\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00a4\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\5\t\u00b7\n\t\3\t\3\t\3\t\5\t")
        buf.write("\u00bc\n\t\7\t\u00be\n\t\f\t\16\t\u00c1\13\t\3\t\3\t\3")
        buf.write("\n\3\n\5\n\u00c7\n\n\3\n\3\n\3\n\5\n\u00cc\n\n\7\n\u00ce")
        buf.write("\n\n\f\n\16\n\u00d1\13\n\3\13\3\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00d9\n\f\3\f\6\f\u00dc\n\f\r\f\16\f\u00dd\3\r\3\r\5")
        buf.write("\r\u00e2\n\r\3\16\3\16\5\16\u00e6\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u00f3\n")
        buf.write("\21\f\21\16\21\u00f6\13\21\3\22\7\22\u00f9\n\22\f\22\16")
        buf.write("\22\u00fc\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0114\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u011f\n\24\f\24\16\24\u0122")
        buf.write("\13\24\3\24\3\24\5\24\u0126\n\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\5\34\u0153\n\34\3\35\3")
        buf.write("\35\5\35\u0157\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3")
        buf.write(" \3!\3!\3!\5!\u0164\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0171\n\"\3\"\3\"\3\"\5\"\u0176\n\"\3")
        buf.write("#\3#\3#\3#\3#\3#\7#\u017e\n#\f#\16#\u0181\13#\3$\3$\3")
        buf.write("$\3$\3$\3$\7$\u0189\n$\f$\16$\u018c\13$\3%\3%\3%\5%\u0191")
        buf.write("\n%\3&\3&\3&\3&\5&\u0197\n&\3\'\3\'\5\'\u019b\n\'\3(\3")
        buf.write("(\3(\3(\3(\5(\u01a2\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u01af\n)\3*\3*\3*\3*\3*\3*\7*\u01b7\n*\f*\16*\u01ba")
        buf.write("\13*\3+\3+\3+\3+\3+\3+\7+\u01c2\n+\f+\16+\u01c5\13+\3")
        buf.write(",\3,\3,\5,\u01ca\n,\3-\3-\3-\3-\5-\u01d0\n-\3.\3.\5.\u01d4")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u01db\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01e8\n\60\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\5\63\u01f3\n\63")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01f9\n\64\3\65\3\65\5\65\u01fd")
        buf.write("\n\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0205\n\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\7\67\u020c\n\67\f\67\16\67\u020f")
        buf.write("\13\67\7\67\u0211\n\67\f\67\16\67\u0214\13\67\3\67\3\67")
        buf.write("\38\38\38\38\38\78\u021d\n8\f8\168\u0220\138\78\u0222")
        buf.write("\n8\f8\168\u0225\138\38\38\39\39\39\39\39\79\u022e\n9")
        buf.write("\f9\169\u0231\139\79\u0233\n9\f9\169\u0236\139\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0243\n:\3:\2\6DFRT;\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\n\3\2\13\16\3\2\60")
        buf.write("\65\4\2$$&&\5\2((**,,\4\2%%\'\'\4\2))++\3\2\13\f\3\2.")
        buf.write("/\2\u0251\2y\3\2\2\2\4\u008b\3\2\2\2\6\u008f\3\2\2\2\b")
        buf.write("\u009d\3\2\2\2\n\u00ab\3\2\2\2\f\u00af\3\2\2\2\16\u00b1")
        buf.write("\3\2\2\2\20\u00b3\3\2\2\2\22\u00c6\3\2\2\2\24\u00d2\3")
        buf.write("\2\2\2\26\u00d4\3\2\2\2\30\u00e1\3\2\2\2\32\u00e5\3\2")
        buf.write("\2\2\34\u00e7\3\2\2\2\36\u00eb\3\2\2\2 \u00ef\3\2\2\2")
        buf.write("\"\u00fa\3\2\2\2$\u0113\3\2\2\2&\u0115\3\2\2\2(\u012a")
        buf.write("\3\2\2\2*\u012c\3\2\2\2,\u0139\3\2\2\2.\u0140\3\2\2\2")
        buf.write("\60\u0147\3\2\2\2\62\u014b\3\2\2\2\64\u014d\3\2\2\2\66")
        buf.write("\u0152\3\2\2\28\u0154\3\2\2\2:\u0158\3\2\2\2<\u015c\3")
        buf.write("\2\2\2>\u015e\3\2\2\2@\u0163\3\2\2\2B\u0175\3\2\2\2D\u0177")
        buf.write("\3\2\2\2F\u0182\3\2\2\2H\u0190\3\2\2\2J\u0196\3\2\2\2")
        buf.write("L\u019a\3\2\2\2N\u01a1\3\2\2\2P\u01ae\3\2\2\2R\u01b0\3")
        buf.write("\2\2\2T\u01bb\3\2\2\2V\u01c9\3\2\2\2X\u01cf\3\2\2\2Z\u01d3")
        buf.write("\3\2\2\2\\\u01da\3\2\2\2^\u01e7\3\2\2\2`\u01e9\3\2\2\2")
        buf.write("b\u01eb\3\2\2\2d\u01f2\3\2\2\2f\u01f8\3\2\2\2h\u01fc\3")
        buf.write("\2\2\2j\u0204\3\2\2\2l\u0206\3\2\2\2n\u0217\3\2\2\2p\u0228")
        buf.write("\3\2\2\2r\u0242\3\2\2\2tu\5\4\3\2uv\7C\2\2vx\3\2\2\2w")
        buf.write("t\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\177\3\2\2\2{")
        buf.write("y\3\2\2\2|~\5\b\5\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2")
        buf.write("\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0082\u0086\5\6\4\2\u0083\u0085\5\b\5\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0089\u008a\7\2\2\3\u008a\3\3\2\2\2\u008b\u008c\7\37")
        buf.write("\2\2\u008c\u008d\7A\2\2\u008d\u008e\5\22\n\2\u008e\5\3")
        buf.write("\2\2\2\u008f\u0090\7\32\2\2\u0090\u0091\7A\2\2\u0091\u0095")
        buf.write("\7\3\2\2\u0092\u0093\7\34\2\2\u0093\u0094\7A\2\2\u0094")
        buf.write("\u0096\5 \21\2\u0095\u0092\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\7\17\2\2\u0098\u0099")
        buf.write("\7A\2\2\u0099\u009a\5\"\22\2\u009a\u009b\7\26\2\2\u009b")
        buf.write("\u009c\7B\2\2\u009c\7\3\2\2\2\u009d\u009e\7\32\2\2\u009e")
        buf.write("\u009f\7A\2\2\u009f\u00a3\7\4\2\2\u00a0\u00a1\7\34\2\2")
        buf.write("\u00a1\u00a2\7A\2\2\u00a2\u00a4\5 \21\2\u00a3\u00a0\3")
        buf.write("\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\7\17\2\2\u00a6\u00a7\7A\2\2\u00a7\u00a8\5\"\22\2\u00a8")
        buf.write("\u00a9\7\26\2\2\u00a9\u00aa\7B\2\2\u00aa\t\3\2\2\2\u00ab")
        buf.write("\u00ac\7\4\2\2\u00ac\u00ad\7E\2\2\u00ad\u00ae\5\20\t\2")
        buf.write("\u00ae\13\3\2\2\2\u00af\u00b0\t\2\2\2\u00b0\r\3\2\2\2")
        buf.write("\u00b1\u00b2\5\20\t\2\u00b2\17\3\2\2\2\u00b3\u00b6\7?")
        buf.write("\2\2\u00b4\u00b7\5\f\7\2\u00b5\u00b7\5\16\b\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00bf\3\2\2\2\u00b8")
        buf.write("\u00bb\7D\2\2\u00b9\u00bc\5\f\7\2\u00ba\u00bc\5\16\b\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00be\3")
        buf.write("\2\2\2\u00bd\u00b8\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c2\u00c3\7@\2\2\u00c3\21\3\2\2\2\u00c4")
        buf.write("\u00c7\5\30\r\2\u00c5\u00c7\5\32\16\2\u00c6\u00c4\3\2")
        buf.write("\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00cf\3\2\2\2\u00c8\u00cb")
        buf.write("\7D\2\2\u00c9\u00cc\5\30\r\2\u00ca\u00cc\5\32\16\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00ce\3\2\2\2")
        buf.write("\u00cd\u00c8\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3")
        buf.write("\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\23\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d2\u00d3\7\4\2\2\u00d3\25\3\2\2\2\u00d4\u00db")
        buf.write("\7\4\2\2\u00d5\u00d8\7=\2\2\u00d6\u00d9\5\26\f\2\u00d7")
        buf.write("\u00d9\7\13\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2")
        buf.write("\2\u00d9\u00da\3\2\2\2\u00da\u00dc\7>\2\2\u00db\u00d5")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\27\3\2\2\2\u00df\u00e2\5\24\13\2")
        buf.write("\u00e0\u00e2\5\26\f\2\u00e1\u00df\3\2\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2\31\3\2\2\2\u00e3\u00e6\5\34\17\2\u00e4")
        buf.write("\u00e6\5\36\20\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2")
        buf.write("\2\u00e6\33\3\2\2\2\u00e7\u00e8\5\26\f\2\u00e8\u00e9\7")
        buf.write("E\2\2\u00e9\u00ea\5\20\t\2\u00ea\35\3\2\2\2\u00eb\u00ec")
        buf.write("\5\24\13\2\u00ec\u00ed\7E\2\2\u00ed\u00ee\5\f\7\2\u00ee")
        buf.write("\37\3\2\2\2\u00ef\u00f4\5\30\r\2\u00f0\u00f1\7D\2\2\u00f1")
        buf.write("\u00f3\5\30\r\2\u00f2\u00f0\3\2\2\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5!\3\2")
        buf.write("\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\5$\23\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb#\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd")
        buf.write("\u0114\5&\24\2\u00fe\u0114\5*\26\2\u00ff\u0100\5(\25\2")
        buf.write("\u0100\u0101\7C\2\2\u0101\u0114\3\2\2\2\u0102\u0114\5")
        buf.write(",\27\2\u0103\u0114\5.\30\2\u0104\u0105\5\60\31\2\u0105")
        buf.write("\u0106\7C\2\2\u0106\u0114\3\2\2\2\u0107\u0108\5\62\32")
        buf.write("\2\u0108\u0109\7C\2\2\u0109\u0114\3\2\2\2\u010a\u010b")
        buf.write("\5\64\33\2\u010b\u010c\7C\2\2\u010c\u0114\3\2\2\2\u010d")
        buf.write("\u010e\5\66\34\2\u010e\u010f\7C\2\2\u010f\u0114\3\2\2")
        buf.write("\2\u0110\u0111\58\35\2\u0111\u0112\7C\2\2\u0112\u0114")
        buf.write("\3\2\2\2\u0113\u00fd\3\2\2\2\u0113\u00fe\3\2\2\2\u0113")
        buf.write("\u00ff\3\2\2\2\u0113\u0102\3\2\2\2\u0113\u0103\3\2\2\2")
        buf.write("\u0113\u0104\3\2\2\2\u0113\u0107\3\2\2\2\u0113\u010a\3")
        buf.write("\2\2\2\u0113\u010d\3\2\2\2\u0113\u0110\3\2\2\2\u0114%")
        buf.write("\3\2\2\2\u0115\u0116\7\33\2\2\u0116\u0117\5B\"\2\u0117")
        buf.write("\u0118\7\36\2\2\u0118\u0120\5\"\22\2\u0119\u011a\7\24")
        buf.write("\2\2\u011a\u011b\5B\"\2\u011b\u011c\7\36\2\2\u011c\u011d")
        buf.write("\5\"\22\2\u011d\u011f\3\2\2\2\u011e\u0119\3\2\2\2\u011f")
        buf.write("\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0125\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7")
        buf.write("\23\2\2\u0124\u0126\5\"\22\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\7\25\2")
        buf.write("\2\u0128\u0129\7B\2\2\u0129\'\3\2\2\2\u012a\u012b\5\4")
        buf.write("\3\2\u012b)\3\2\2\2\u012c\u012d\7\31\2\2\u012d\u012e\7")
        buf.write(";\2\2\u012e\u012f\5:\36\2\u012f\u0130\7D\2\2\u0130\u0131")
        buf.write("\5<\37\2\u0131\u0132\7D\2\2\u0132\u0133\5> \2\u0133\u0134")
        buf.write("\7<\2\2\u0134\u0135\7\22\2\2\u0135\u0136\5\"\22\2\u0136")
        buf.write("\u0137\7\27\2\2\u0137\u0138\7B\2\2\u0138+\3\2\2\2\u0139")
        buf.write("\u013a\7 \2\2\u013a\u013b\5b\62\2\u013b\u013c\7\22\2\2")
        buf.write("\u013c\u013d\5\"\22\2\u013d\u013e\7\30\2\2\u013e\u013f")
        buf.write("\7B\2\2\u013f-\3\2\2\2\u0140\u0141\7\22\2\2\u0141\u0142")
        buf.write("\5\"\22\2\u0142\u0143\7 \2\2\u0143\u0144\5b\62\2\u0144")
        buf.write("\u0145\7#\2\2\u0145\u0146\7B\2\2\u0146/\3\2\2\2\u0147")
        buf.write("\u0148\5\30\r\2\u0148\u0149\7E\2\2\u0149\u014a\5@!\2\u014a")
        buf.write("\61\3\2\2\2\u014b\u014c\7\20\2\2\u014c\63\3\2\2\2\u014d")
        buf.write("\u014e\7\21\2\2\u014e\65\3\2\2\2\u014f\u0153\5l\67\2\u0150")
        buf.write("\u0153\5n8\2\u0151\u0153\5p9\2\u0152\u014f\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\67\3\2\2\2\u0154")
        buf.write("\u0156\7\35\2\2\u0155\u0157\5@!\2\u0156\u0155\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u01579\3\2\2\2\u0158\u0159\5\24\13")
        buf.write("\2\u0159\u015a\7E\2\2\u015a\u015b\5D#\2\u015b;\3\2\2\2")
        buf.write("\u015c\u015d\5B\"\2\u015d=\3\2\2\2\u015e\u015f\5\60\31")
        buf.write("\2\u015f?\3\2\2\2\u0160\u0164\5D#\2\u0161\u0164\5R*\2")
        buf.write("\u0162\u0164\5d\63\2\u0163\u0160\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0163\u0162\3\2\2\2\u0164A\3\2\2\2\u0165\u0166")
        buf.write("\5D#\2\u0166\u0167\t\3\2\2\u0167\u0168\5D#\2\u0168\u0176")
        buf.write("\3\2\2\2\u0169\u0170\5R*\2\u016a\u0171\3\2\2\2\u016b\u0171")
        buf.write("\7\66\2\2\u016c\u0171\7\67\2\2\u016d\u0171\78\2\2\u016e")
        buf.write("\u0171\79\2\2\u016f\u0171\7:\2\2\u0170\u016a\3\2\2\2\u0170")
        buf.write("\u016b\3\2\2\2\u0170\u016c\3\2\2\2\u0170\u016d\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0173\5R*\2\u0173\u0176\3\2\2\2\u0174\u0176")
        buf.write("\5b\62\2\u0175\u0165\3\2\2\2\u0175\u0169\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176C\3\2\2\2\u0177\u0178\b#\1\2\u0178")
        buf.write("\u0179\5F$\2\u0179\u017f\3\2\2\2\u017a\u017b\f\4\2\2\u017b")
        buf.write("\u017c\t\4\2\2\u017c\u017e\5F$\2\u017d\u017a\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180E\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\b$\1\2")
        buf.write("\u0183\u0184\5H%\2\u0184\u018a\3\2\2\2\u0185\u0186\f\4")
        buf.write("\2\2\u0186\u0187\t\5\2\2\u0187\u0189\5H%\2\u0188\u0185")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bG\3\2\2\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u018e\7&\2\2\u018e\u0191\5H%\2\u018f\u0191\5J&\2\u0190")
        buf.write("\u018d\3\2\2\2\u0190\u018f\3\2\2\2\u0191I\3\2\2\2\u0192")
        buf.write("\u0193\5L\'\2\u0193\u0194\5r:\2\u0194\u0197\3\2\2\2\u0195")
        buf.write("\u0197\5L\'\2\u0196\u0192\3\2\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197K\3\2\2\2\u0198\u019b\5l\67\2\u0199\u019b\5N(\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019bM\3\2\2")
        buf.write("\2\u019c\u01a2\5P)\2\u019d\u019e\7;\2\2\u019e\u019f\5")
        buf.write("D#\2\u019f\u01a0\7<\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019c")
        buf.write("\3\2\2\2\u01a1\u019d\3\2\2\2\u01a2O\3\2\2\2\u01a3\u01af")
        buf.write("\7\13\2\2\u01a4\u01af\5\24\13\2\u01a5\u01a6\7F\2\2\u01a6")
        buf.write("\u01a7\7;\2\2\u01a7\u01a8\5R*\2\u01a8\u01a9\7<\2\2\u01a9")
        buf.write("\u01af\3\2\2\2\u01aa\u01ab\7G\2\2\u01ab\u01ac\7;\2\2\u01ac")
        buf.write("\u01ad\7\16\2\2\u01ad\u01af\7<\2\2\u01ae\u01a3\3\2\2\2")
        buf.write("\u01ae\u01a4\3\2\2\2\u01ae\u01a5\3\2\2\2\u01ae\u01aa\3")
        buf.write("\2\2\2\u01afQ\3\2\2\2\u01b0\u01b1\b*\1\2\u01b1\u01b2\5")
        buf.write("T+\2\u01b2\u01b8\3\2\2\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5")
        buf.write("\t\6\2\2\u01b5\u01b7\5T+\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("S\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\b+\1\2\u01bc")
        buf.write("\u01bd\5V,\2\u01bd\u01c3\3\2\2\2\u01be\u01bf\f\4\2\2\u01bf")
        buf.write("\u01c0\t\7\2\2\u01c0\u01c2\5V,\2\u01c1\u01be\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4U\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7\'\2")
        buf.write("\2\u01c7\u01ca\5V,\2\u01c8\u01ca\5X-\2\u01c9\u01c6\3\2")
        buf.write("\2\2\u01c9\u01c8\3\2\2\2\u01caW\3\2\2\2\u01cb\u01cc\5")
        buf.write("Z.\2\u01cc\u01cd\5r:\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0")
        buf.write("\5Z.\2\u01cf\u01cb\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0Y")
        buf.write("\3\2\2\2\u01d1\u01d4\5n8\2\u01d2\u01d4\5\\/\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4[\3\2\2\2\u01d5\u01db")
        buf.write("\5^\60\2\u01d6\u01d7\7;\2\2\u01d7\u01d8\5R*\2\u01d8\u01d9")
        buf.write("\7<\2\2\u01d9\u01db\3\2\2\2\u01da\u01d5\3\2\2\2\u01da")
        buf.write("\u01d6\3\2\2\2\u01db]\3\2\2\2\u01dc\u01e8\7\f\2\2\u01dd")
        buf.write("\u01e8\5\24\13\2\u01de\u01df\7H\2\2\u01df\u01e0\7;\2\2")
        buf.write("\u01e0\u01e1\5D#\2\u01e1\u01e2\7<\2\2\u01e2\u01e8\3\2")
        buf.write("\2\2\u01e3\u01e4\7I\2\2\u01e4\u01e5\7;\2\2\u01e5\u01e6")
        buf.write("\7\16\2\2\u01e6\u01e8\7<\2\2\u01e7\u01dc\3\2\2\2\u01e7")
        buf.write("\u01dd\3\2\2\2\u01e7\u01de\3\2\2\2\u01e7\u01e3\3\2\2\2")
        buf.write("\u01e8_\3\2\2\2\u01e9\u01ea\t\b\2\2\u01eaa\3\2\2\2\u01eb")
        buf.write("\u01ec\5d\63\2\u01ec\u01ed\t\t\2\2\u01ed\u01ee\5d\63\2")
        buf.write("\u01eec\3\2\2\2\u01ef\u01f0\7-\2\2\u01f0\u01f3\5f\64\2")
        buf.write("\u01f1\u01f3\5f\64\2\u01f2\u01ef\3\2\2\2\u01f2\u01f1\3")
        buf.write("\2\2\2\u01f3e\3\2\2\2\u01f4\u01f5\5h\65\2\u01f5\u01f6")
        buf.write("\5r:\2\u01f6\u01f9\3\2\2\2\u01f7\u01f9\5h\65\2\u01f8\u01f4")
        buf.write("\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9g\3\2\2\2\u01fa\u01fd")
        buf.write("\5p9\2\u01fb\u01fd\5j\66\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fdi\3\2\2\2\u01fe\u0205\7\r\2\2\u01ff\u0205")
        buf.write("\5\30\r\2\u0200\u0201\7J\2\2\u0201\u0202\7;\2\2\u0202")
        buf.write("\u0203\7\16\2\2\u0203\u0205\7<\2\2\u0204\u01fe\3\2\2\2")
        buf.write("\u0204\u01ff\3\2\2\2\u0204\u0200\3\2\2\2\u0205k\3\2\2")
        buf.write("\2\u0206\u0207\7\4\2\2\u0207\u0212\7;\2\2\u0208\u020d")
        buf.write("\5@!\2\u0209\u020a\7D\2\2\u020a\u020c\5@!\2\u020b\u0209")
        buf.write("\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u0210\u0208\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3")
        buf.write("\2\2\2\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0215\u0216\7<\2\2\u0216m\3\2\2\2\u0217\u0218")
        buf.write("\7\4\2\2\u0218\u0223\7;\2\2\u0219\u021e\5@!\2\u021a\u021b")
        buf.write("\7D\2\2\u021b\u021d\5@!\2\u021c\u021a\3\2\2\2\u021d\u0220")
        buf.write("\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0219\3\2\2\2")
        buf.write("\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3")
        buf.write("\2\2\2\u0224\u0226\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0227")
        buf.write("\7<\2\2\u0227o\3\2\2\2\u0228\u0229\7\4\2\2\u0229\u0234")
        buf.write("\7;\2\2\u022a\u022f\5@!\2\u022b\u022c\7D\2\2\u022c\u022e")
        buf.write("\5@!\2\u022d\u022b\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0233\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0232\u022a\3\2\2\2\u0233\u0236\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237\3")
        buf.write("\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\7<\2\2\u0238q\3")
        buf.write("\2\2\2\u0239\u023a\7=\2\2\u023a\u023b\5D#\2\u023b\u023c")
        buf.write("\7>\2\2\u023c\u0243\3\2\2\2\u023d\u023e\7=\2\2\u023e\u023f")
        buf.write("\5D#\2\u023f\u0240\7>\2\2\u0240\u0241\5r:\2\u0241\u0243")
        buf.write("\3\2\2\2\u0242\u0239\3\2\2\2\u0242\u023d\3\2\2\2\u0243")
        buf.write("s\3\2\2\2\64y\177\u0086\u0095\u00a3\u00b6\u00bb\u00bf")
        buf.write("\u00c6\u00cb\u00cf\u00d8\u00dd\u00e1\u00e5\u00f4\u00fa")
        buf.write("\u0113\u0120\u0125\u0152\u0156\u0163\u0170\u0175\u017f")
        buf.write("\u018a\u0190\u0196\u019a\u01a1\u01ae\u01b8\u01c3\u01c9")
        buf.write("\u01cf\u01d3\u01da\u01e7\u01f2\u01f8\u01fc\u0204\u020d")
        buf.write("\u0212\u021e\u0223\u022f\u0234\u0242")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
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
                     "'{'", "'}'", "':'", "'.'", "';'", "','", "'='", "'int_of_float'", 
                     "'int_of_string'", "'float_to_int'", "'float_of_string'", 
                     "'bool_of_string'", "'string_of_bool'", "'string_of_int'", 
                     "'string_of_float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR", "WS", "Integer_literal", "Float_literal", 
                      "Boolean_literal", "String_literal", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                      "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", 
                      "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
                      "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", 
                      "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", 
                      "BOOL_OF_STRING", "STRING_OF_BOOL", "STRING_OF_INT", 
                      "STRING_OF_FLOAT" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_main_function_declare = 2
    RULE_function_declare = 3
    RULE_array = 4
    RULE_primitive_data = 5
    RULE_composite_data = 6
    RULE_array_lit = 7
    RULE_var_list = 8
    RULE_scalar_var = 9
    RULE_composite_var = 10
    RULE_var_non_init = 11
    RULE_var_init = 12
    RULE_composite_init = 13
    RULE_primitive_init = 14
    RULE_params_list = 15
    RULE_stmt_list = 16
    RULE_stmt = 17
    RULE_if_stmt = 18
    RULE_var_declare_stmt = 19
    RULE_for_stmt = 20
    RULE_while_stmt = 21
    RULE_dowhile_stmt = 22
    RULE_assign_stmt = 23
    RULE_break_stmt = 24
    RULE_continue_stmt = 25
    RULE_call_stmt = 26
    RULE_return_stmt = 27
    RULE_init_for = 28
    RULE_con_for = 29
    RULE_update_for = 30
    RULE_expr = 31
    RULE_boolean_type_expr = 32
    RULE_int_expr1 = 33
    RULE_int_expr2 = 34
    RULE_int_expr3 = 35
    RULE_int_expr4 = 36
    RULE_int_expr5 = 37
    RULE_int_expr6 = 38
    RULE_int_operand = 39
    RULE_float_expr1 = 40
    RULE_float_expr2 = 41
    RULE_float_expr3 = 42
    RULE_float_expr4 = 43
    RULE_float_expr5 = 44
    RULE_float_expr6 = 45
    RULE_float_operand = 46
    RULE_constant = 47
    RULE_boolean_expr = 48
    RULE_boolean_expr1 = 49
    RULE_boolean_expr2 = 50
    RULE_boolean_expr3 = 51
    RULE_boolean_expr4 = 52
    RULE_int_func_call = 53
    RULE_float_func_call = 54
    RULE_boolean_func_call = 55
    RULE_index_op = 56

    ruleNames =  [ "program", "var_declare", "main_function_declare", "function_declare", 
                   "array", "primitive_data", "composite_data", "array_lit", 
                   "var_list", "scalar_var", "composite_var", "var_non_init", 
                   "var_init", "composite_init", "primitive_init", "params_list", 
                   "stmt_list", "stmt", "if_stmt", "var_declare_stmt", "for_stmt", 
                   "while_stmt", "dowhile_stmt", "assign_stmt", "break_stmt", 
                   "continue_stmt", "call_stmt", "return_stmt", "init_for", 
                   "con_for", "update_for", "expr", "boolean_type_expr", 
                   "int_expr1", "int_expr2", "int_expr3", "int_expr4", "int_expr5", 
                   "int_expr6", "int_operand", "float_expr1", "float_expr2", 
                   "float_expr3", "float_expr4", "float_expr5", "float_expr6", 
                   "float_operand", "constant", "boolean_expr", "boolean_expr1", 
                   "boolean_expr2", "boolean_expr3", "boolean_expr4", "int_func_call", 
                   "float_func_call", "boolean_func_call", "index_op" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    ILLEGAL_ESCAPE=3
    UNCLOSE_STRING=4
    COMMENT=5
    UNTERMINATED_COMMENT=6
    ERROR_CHAR=7
    WS=8
    Integer_literal=9
    Float_literal=10
    Boolean_literal=11
    String_literal=12
    BODY=13
    BREAK=14
    CONTINUE=15
    DO=16
    ELSE=17
    ELSEIF=18
    ENDIF=19
    ENDBODY=20
    ENDFOR=21
    ENDWHILE=22
    FOR=23
    FUNCTION=24
    IF=25
    PARAMETER=26
    RETURN=27
    THEN=28
    VAR=29
    WHILE=30
    TRUE=31
    FALSE=32
    ENDDO=33
    PLUS_INT=34
    PLUS_FLOAT=35
    MINUS_INT=36
    MINUS_FLOAT=37
    STAR_INT=38
    STAR_FLOAT=39
    DIV_INT=40
    DIV_FLOAT=41
    MOD=42
    NOT=43
    AND=44
    OR=45
    EQUAL=46
    NOT_EQUAL_INT=47
    LESS_INT=48
    GREATER_INT=49
    LESS_OR_EQUAL_INT=50
    GREATER_OR_EQUAL_INT=51
    NOT_EQUAL_FLOAT=52
    LESS_FLOAT=53
    GREATER_FLOAT=54
    LESS_OR_EQUAL_FLOAT=55
    GREATER_OR_EQUAL_FLOAT=56
    LEFT_PAREN=57
    RIGHT_PAREN=58
    LEFT_BRACKET=59
    RIGHT_BRACKET=60
    LEFT_BRACE=61
    RIGHT_BRACE=62
    COLON=63
    DOT=64
    SEMI=65
    COMMA=66
    ASSIGN=67
    INT_OF_FLOAT=68
    INT_OF_STRING=69
    FLOAT_TO_INT=70
    FLOAT_OF_STRING=71
    BOOL_OF_STRING=72
    STRING_OF_BOOL=73
    STRING_OF_INT=74
    STRING_OF_FLOAT=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_function_declare(self):
            return self.getTypedRuleContext(BKITParser.Main_function_declareContext,0)


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
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 114
                self.var_declare()
                self.state = 115
                self.match(BKITParser.SEMI)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.function_declare() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 128
            self.main_function_declare()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 129
                self.function_declare()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
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
            self.state = 137
            self.match(BKITParser.VAR)
            self.state = 138
            self.match(BKITParser.COLON)
            self.state = 139
            self.var_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_function_declareContext(ParserRuleContext):

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

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def params_list(self):
            return self.getTypedRuleContext(BKITParser.Params_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_main_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function_declare" ):
                return visitor.visitMain_function_declare(self)
            else:
                return visitor.visitChildren(self)




    def main_function_declare(self):

        localctx = BKITParser.Main_function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BKITParser.FUNCTION)
            self.state = 142
            self.match(BKITParser.COLON)
            self.state = 143
            self.match(BKITParser.T__0)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 144
                self.match(BKITParser.PARAMETER)
                self.state = 145
                self.match(BKITParser.COLON)
                self.state = 146
                self.params_list()


            self.state = 149
            self.match(BKITParser.BODY)
            self.state = 150
            self.match(BKITParser.COLON)
            self.state = 151
            self.stmt_list()
            self.state = 152
            self.match(BKITParser.ENDBODY)
            self.state = 153
            self.match(BKITParser.DOT)
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

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def params_list(self):
            return self.getTypedRuleContext(BKITParser.Params_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BKITParser.FUNCTION)
            self.state = 156
            self.match(BKITParser.COLON)
            self.state = 157
            self.match(BKITParser.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 158
                self.match(BKITParser.PARAMETER)
                self.state = 159
                self.match(BKITParser.COLON)
                self.state = 160
                self.params_list()


            self.state = 163
            self.match(BKITParser.BODY)
            self.state = 164
            self.match(BKITParser.COLON)
            self.state = 165
            self.stmt_list()
            self.state = 166
            self.match(BKITParser.ENDBODY)
            self.state = 167
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
        self.enterRule(localctx, 8, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(BKITParser.ID)
            self.state = 170
            self.match(BKITParser.ASSIGN)
            self.state = 171
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

        def Integer_literal(self):
            return self.getToken(BKITParser.Integer_literal, 0)

        def Float_literal(self):
            return self.getToken(BKITParser.Float_literal, 0)

        def String_literal(self):
            return self.getToken(BKITParser.String_literal, 0)

        def Boolean_literal(self):
            return self.getToken(BKITParser.Boolean_literal, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_data" ):
                return visitor.visitPrimitive_data(self)
            else:
                return visitor.visitChildren(self)




    def primitive_data(self):

        localctx = BKITParser.Primitive_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.String_literal))) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_composite_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
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
        self.enterRule(localctx, 14, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(BKITParser.LEFT_BRACE)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Integer_literal, BKITParser.Float_literal, BKITParser.Boolean_literal, BKITParser.String_literal]:
                self.state = 178
                self.primitive_data()
                pass
            elif token in [BKITParser.LEFT_BRACE]:
                self.state = 179
                self.composite_data()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 182
                self.match(BKITParser.COMMA)
                self.state = 185
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.Integer_literal, BKITParser.Float_literal, BKITParser.Boolean_literal, BKITParser.String_literal]:
                    self.state = 183
                    self.primitive_data()
                    pass
                elif token in [BKITParser.LEFT_BRACE]:
                    self.state = 184
                    self.composite_data()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
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
        self.enterRule(localctx, 16, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 194
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 195
                self.var_init()
                pass


            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 198
                self.match(BKITParser.COMMA)
                self.state = 201
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 200
                    self.var_init()
                    pass


                self.state = 207
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
        self.enterRule(localctx, 18, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(BKITParser.ID)
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


        def Integer_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer_literal)
            else:
                return self.getToken(BKITParser.Integer_literal, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(BKITParser.ID)
            self.state = 217 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 211
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 214
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.ID]:
                        self.state = 212
                        self.composite_var()
                        pass
                    elif token in [BKITParser.Integer_literal]:
                        self.state = 213
                        self.match(BKITParser.Integer_literal)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 216
                    self.match(BKITParser.RIGHT_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 219 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_non_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_non_init" ):
                return visitor.visitVar_non_init(self)
            else:
                return visitor.visitChildren(self)




    def var_non_init(self):

        localctx = BKITParser.Var_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_non_init)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.composite_var()
                pass


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

        def composite_init(self):
            return self.getTypedRuleContext(BKITParser.Composite_initContext,0)


        def primitive_init(self):
            return self.getTypedRuleContext(BKITParser.Primitive_initContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_init)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.composite_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.primitive_init()
                pass


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
        self.enterRule(localctx, 26, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.composite_var()
            self.state = 230
            self.match(BKITParser.ASSIGN)
            self.state = 231
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
        self.enterRule(localctx, 28, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.scalar_var()
            self.state = 234
            self.match(BKITParser.ASSIGN)
            self.state = 235
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
        self.enterRule(localctx, 30, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.var_non_init()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 238
                self.match(BKITParser.COMMA)
                self.state = 239
                self.var_non_init()
                self.state = 244
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
        self.enterRule(localctx, 32, self.RULE_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 245
                    self.stmt() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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


        def var_declare_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.Dowhile_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


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
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.var_declare_stmt()
                self.state = 254
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.dowhile_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.assign_stmt()
                self.state = 259
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.break_stmt()
                self.state = 262
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 264
                self.continue_stmt()
                self.state = 265
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 267
                self.call_stmt()
                self.state = 268
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 270
                self.return_stmt()
                self.state = 271
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

        def boolean_type_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Boolean_type_exprContext)
            else:
                return self.getTypedRuleContext(BKITParser.Boolean_type_exprContext,i)


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
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKITParser.IF)
            self.state = 276
            self.boolean_type_expr()
            self.state = 277
            self.match(BKITParser.THEN)
            self.state = 278
            self.stmt_list()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 279
                self.match(BKITParser.ELSEIF)
                self.state = 280
                self.boolean_type_expr()
                self.state = 281
                self.match(BKITParser.THEN)
                self.state = 282
                self.stmt_list()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 289
                self.match(BKITParser.ELSE)
                self.state = 290
                self.stmt_list()


            self.state = 293
            self.match(BKITParser.ENDIF)
            self.state = 294
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
        self.enterRule(localctx, 38, self.RULE_var_declare_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
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
        self.enterRule(localctx, 40, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BKITParser.FOR)
            self.state = 299
            self.match(BKITParser.LEFT_PAREN)
            self.state = 300
            self.init_for()
            self.state = 301
            self.match(BKITParser.COMMA)
            self.state = 302
            self.con_for()
            self.state = 303
            self.match(BKITParser.COMMA)
            self.state = 304
            self.update_for()
            self.state = 305
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 306
            self.match(BKITParser.DO)
            self.state = 307
            self.stmt_list()
            self.state = 308
            self.match(BKITParser.ENDFOR)
            self.state = 309
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

        def boolean_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_exprContext,0)


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
        self.enterRule(localctx, 42, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(BKITParser.WHILE)
            self.state = 312
            self.boolean_expr()
            self.state = 313
            self.match(BKITParser.DO)
            self.state = 314
            self.stmt_list()
            self.state = 315
            self.match(BKITParser.ENDWHILE)
            self.state = 316
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

        def boolean_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_exprContext,0)


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
        self.enterRule(localctx, 44, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(BKITParser.DO)
            self.state = 319
            self.stmt_list()
            self.state = 320
            self.match(BKITParser.WHILE)
            self.state = 321
            self.boolean_expr()
            self.state = 322
            self.match(BKITParser.ENDDO)
            self.state = 323
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

        def var_non_init(self):
            return self.getTypedRuleContext(BKITParser.Var_non_initContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

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
        self.enterRule(localctx, 46, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.var_non_init()
            self.state = 326
            self.match(BKITParser.ASSIGN)
            self.state = 327
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
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
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
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
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

        def int_func_call(self):
            return self.getTypedRuleContext(BKITParser.Int_func_callContext,0)


        def float_func_call(self):
            return self.getTypedRuleContext(BKITParser.Float_func_callContext,0)


        def boolean_func_call(self):
            return self.getTypedRuleContext(BKITParser.Boolean_func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_stmt)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.float_func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.boolean_func_call()
                pass


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
        self.enterRule(localctx, 54, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(BKITParser.RETURN)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (BKITParser.INT_OF_FLOAT - 68)) | (1 << (BKITParser.INT_OF_STRING - 68)) | (1 << (BKITParser.FLOAT_TO_INT - 68)) | (1 << (BKITParser.FLOAT_OF_STRING - 68)) | (1 << (BKITParser.BOOL_OF_STRING - 68)))) != 0):
                self.state = 339
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

        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = BKITParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.scalar_var()
            self.state = 343
            self.match(BKITParser.ASSIGN)
            self.state = 344
            self.int_expr1(0)
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

        def boolean_type_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_type_exprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_con_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCon_for" ):
                return visitor.visitCon_for(self)
            else:
                return visitor.visitChildren(self)




    def con_for(self):

        localctx = BKITParser.Con_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_con_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.boolean_type_expr()
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

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_update_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_for" ):
                return visitor.visitUpdate_for(self)
            else:
                return visitor.visitChildren(self)




    def update_for(self):

        localctx = BKITParser.Update_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_update_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.assign_stmt()
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

        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


        def float_expr1(self):
            return self.getTypedRuleContext(BKITParser.Float_expr1Context,0)


        def boolean_expr1(self):
            return self.getTypedRuleContext(BKITParser.Boolean_expr1Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.boolean_expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_type_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Int_expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Int_expr1Context,i)


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

        def float_expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Float_expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Float_expr1Context,i)


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

        def boolean_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_exprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_boolean_type_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_type_expr" ):
                return visitor.visitBoolean_type_expr(self)
            else:
                return visitor.visitChildren(self)




    def boolean_type_expr(self):

        localctx = BKITParser.Boolean_type_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_boolean_type_expr)
        self._la = 0 # Token type
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.int_expr1(0)
                self.state = 356
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL_INT) | (1 << BKITParser.LESS_INT) | (1 << BKITParser.GREATER_INT) | (1 << BKITParser.LESS_OR_EQUAL_INT) | (1 << BKITParser.GREATER_OR_EQUAL_INT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 357
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.float_expr1(0)
                self.state = 366
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.MINUS_FLOAT, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                    pass
                elif token in [BKITParser.NOT_EQUAL_FLOAT]:
                    self.state = 361
                    self.match(BKITParser.NOT_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.LESS_FLOAT]:
                    self.state = 362
                    self.match(BKITParser.LESS_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_FLOAT]:
                    self.state = 363
                    self.match(BKITParser.GREATER_FLOAT)
                    pass
                elif token in [BKITParser.LESS_OR_EQUAL_FLOAT]:
                    self.state = 364
                    self.match(BKITParser.LESS_OR_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_OR_EQUAL_FLOAT]:
                    self.state = 365
                    self.match(BKITParser.GREATER_OR_EQUAL_FLOAT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 368
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.boolean_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_expr2(self):
            return self.getTypedRuleContext(BKITParser.Int_expr2Context,0)


        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


        def PLUS_INT(self):
            return self.getToken(BKITParser.PLUS_INT, 0)

        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr1" ):
                return visitor.visitInt_expr1(self)
            else:
                return visitor.visitChildren(self)



    def int_expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Int_expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_int_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.int_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr1)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_INT or _la==BKITParser.MINUS_INT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 378
                    self.int_expr2(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Int_expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_expr3(self):
            return self.getTypedRuleContext(BKITParser.Int_expr3Context,0)


        def int_expr2(self):
            return self.getTypedRuleContext(BKITParser.Int_expr2Context,0)


        def STAR_INT(self):
            return self.getToken(BKITParser.STAR_INT, 0)

        def DIV_INT(self):
            return self.getToken(BKITParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr2" ):
                return visitor.visitInt_expr2(self)
            else:
                return visitor.visitChildren(self)



    def int_expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Int_expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_int_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.int_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr2)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.STAR_INT) | (1 << BKITParser.DIV_INT) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 389
                    self.int_expr3() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Int_expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_expr3(self):
            return self.getTypedRuleContext(BKITParser.Int_expr3Context,0)


        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def int_expr4(self):
            return self.getTypedRuleContext(BKITParser.Int_expr4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_int_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr3" ):
                return visitor.visitInt_expr3(self)
            else:
                return visitor.visitChildren(self)




    def int_expr3(self):

        localctx = BKITParser.Int_expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_int_expr3)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(BKITParser.MINUS_INT)
                self.state = 396
                self.int_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.Integer_literal, BKITParser.LEFT_PAREN, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.int_expr4()
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


    class Int_expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_expr5(self):
            return self.getTypedRuleContext(BKITParser.Int_expr5Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_int_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr4" ):
                return visitor.visitInt_expr4(self)
            else:
                return visitor.visitChildren(self)




    def int_expr4(self):

        localctx = BKITParser.Int_expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_int_expr4)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.int_expr5()
                self.state = 401
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.int_expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_func_call(self):
            return self.getTypedRuleContext(BKITParser.Int_func_callContext,0)


        def int_expr6(self):
            return self.getTypedRuleContext(BKITParser.Int_expr6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_int_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr5" ):
                return visitor.visitInt_expr5(self)
            else:
                return visitor.visitChildren(self)




    def int_expr5(self):

        localctx = BKITParser.Int_expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_int_expr5)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.int_expr6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_operand(self):
            return self.getTypedRuleContext(BKITParser.Int_operandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expr6" ):
                return visitor.visitInt_expr6(self)
            else:
                return visitor.visitChildren(self)




    def int_expr6(self):

        localctx = BKITParser.Int_expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_int_expr6)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.Integer_literal, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.int_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(BKITParser.LEFT_PAREN)
                self.state = 412
                self.int_expr1(0)
                self.state = 413
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


    class Int_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer_literal(self):
            return self.getToken(BKITParser.Integer_literal, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def INT_OF_FLOAT(self):
            return self.getToken(BKITParser.INT_OF_FLOAT, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def float_expr1(self):
            return self.getTypedRuleContext(BKITParser.Float_expr1Context,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def INT_OF_STRING(self):
            return self.getToken(BKITParser.INT_OF_STRING, 0)

        def String_literal(self):
            return self.getToken(BKITParser.String_literal, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_operand" ):
                return visitor.visitInt_operand(self)
            else:
                return visitor.visitChildren(self)




    def int_operand(self):

        localctx = BKITParser.Int_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_int_operand)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Integer_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(BKITParser.Integer_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.scalar_var()
                pass
            elif token in [BKITParser.INT_OF_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(BKITParser.INT_OF_FLOAT)
                self.state = 420
                self.match(BKITParser.LEFT_PAREN)
                self.state = 421
                self.float_expr1(0)
                self.state = 422
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.match(BKITParser.INT_OF_STRING)
                self.state = 425
                self.match(BKITParser.LEFT_PAREN)
                self.state = 426
                self.match(BKITParser.String_literal)
                self.state = 427
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


    class Float_expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_expr2(self):
            return self.getTypedRuleContext(BKITParser.Float_expr2Context,0)


        def float_expr1(self):
            return self.getTypedRuleContext(BKITParser.Float_expr1Context,0)


        def PLUS_FLOAT(self):
            return self.getToken(BKITParser.PLUS_FLOAT, 0)

        def MINUS_FLOAT(self):
            return self.getToken(BKITParser.MINUS_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr1" ):
                return visitor.visitFloat_expr1(self)
            else:
                return visitor.visitChildren(self)



    def float_expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Float_expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_float_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.float_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr1)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_FLOAT or _la==BKITParser.MINUS_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 435
                    self.float_expr2(0) 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Float_expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_expr3(self):
            return self.getTypedRuleContext(BKITParser.Float_expr3Context,0)


        def float_expr2(self):
            return self.getTypedRuleContext(BKITParser.Float_expr2Context,0)


        def STAR_FLOAT(self):
            return self.getToken(BKITParser.STAR_FLOAT, 0)

        def DIV_FLOAT(self):
            return self.getToken(BKITParser.DIV_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr2" ):
                return visitor.visitFloat_expr2(self)
            else:
                return visitor.visitChildren(self)



    def float_expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Float_expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_float_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.float_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr2)
                    self.state = 444
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 445
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.STAR_FLOAT or _la==BKITParser.DIV_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 446
                    self.float_expr3() 
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Float_expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_expr3(self):
            return self.getTypedRuleContext(BKITParser.Float_expr3Context,0)


        def MINUS_FLOAT(self):
            return self.getToken(BKITParser.MINUS_FLOAT, 0)

        def float_expr4(self):
            return self.getTypedRuleContext(BKITParser.Float_expr4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_float_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr3" ):
                return visitor.visitFloat_expr3(self)
            else:
                return visitor.visitChildren(self)




    def float_expr3(self):

        localctx = BKITParser.Float_expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_float_expr3)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(BKITParser.MINUS_FLOAT)
                self.state = 453
                self.float_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.float_expr4()
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


    class Float_expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_expr5(self):
            return self.getTypedRuleContext(BKITParser.Float_expr5Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_float_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr4" ):
                return visitor.visitFloat_expr4(self)
            else:
                return visitor.visitChildren(self)




    def float_expr4(self):

        localctx = BKITParser.Float_expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_float_expr4)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.float_expr5()
                self.state = 458
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.float_expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_func_call(self):
            return self.getTypedRuleContext(BKITParser.Float_func_callContext,0)


        def float_expr6(self):
            return self.getTypedRuleContext(BKITParser.Float_expr6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_float_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr5" ):
                return visitor.visitFloat_expr5(self)
            else:
                return visitor.visitChildren(self)




    def float_expr5(self):

        localctx = BKITParser.Float_expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_float_expr5)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.float_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.float_expr6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_operand(self):
            return self.getTypedRuleContext(BKITParser.Float_operandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def float_expr1(self):
            return self.getTypedRuleContext(BKITParser.Float_expr1Context,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_expr6" ):
                return visitor.visitFloat_expr6(self)
            else:
                return visitor.visitChildren(self)




    def float_expr6(self):

        localctx = BKITParser.Float_expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_float_expr6)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.float_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(BKITParser.LEFT_PAREN)
                self.state = 469
                self.float_expr1(0)
                self.state = 470
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


    class Float_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float_literal(self):
            return self.getToken(BKITParser.Float_literal, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def FLOAT_TO_INT(self):
            return self.getToken(BKITParser.FLOAT_TO_INT, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def FLOAT_OF_STRING(self):
            return self.getToken(BKITParser.FLOAT_OF_STRING, 0)

        def String_literal(self):
            return self.getToken(BKITParser.String_literal, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_operand" ):
                return visitor.visitFloat_operand(self)
            else:
                return visitor.visitChildren(self)




    def float_operand(self):

        localctx = BKITParser.Float_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_float_operand)
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Float_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(BKITParser.Float_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.scalar_var()
                pass
            elif token in [BKITParser.FLOAT_TO_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.match(BKITParser.FLOAT_TO_INT)
                self.state = 477
                self.match(BKITParser.LEFT_PAREN)
                self.state = 478
                self.int_expr1(0)
                self.state = 479
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.match(BKITParser.FLOAT_OF_STRING)
                self.state = 482
                self.match(BKITParser.LEFT_PAREN)
                self.state = 483
                self.match(BKITParser.String_literal)
                self.state = 484
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


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer_literal(self):
            return self.getToken(BKITParser.Integer_literal, 0)

        def Float_literal(self):
            return self.getToken(BKITParser.Float_literal, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = BKITParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not(_la==BKITParser.Integer_literal or _la==BKITParser.Float_literal):
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


    class Boolean_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Boolean_expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Boolean_expr1Context,i)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr" ):
                return visitor.visitBoolean_expr(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expr(self):

        localctx = BKITParser.Boolean_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_boolean_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.boolean_expr1()
            self.state = 490
            _la = self._input.LA(1)
            if not(_la==BKITParser.AND or _la==BKITParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 491
            self.boolean_expr1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def boolean_expr2(self):
            return self.getTypedRuleContext(BKITParser.Boolean_expr2Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_boolean_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr1" ):
                return visitor.visitBoolean_expr1(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expr1(self):

        localctx = BKITParser.Boolean_expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_boolean_expr1)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(BKITParser.NOT)
                self.state = 494
                self.boolean_expr2()
                pass
            elif token in [BKITParser.ID, BKITParser.Boolean_literal, BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.boolean_expr2()
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


    class Boolean_expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expr3(self):
            return self.getTypedRuleContext(BKITParser.Boolean_expr3Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_boolean_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr2" ):
                return visitor.visitBoolean_expr2(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expr2(self):

        localctx = BKITParser.Boolean_expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_boolean_expr2)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.boolean_expr3()
                self.state = 499
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.boolean_expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_func_call(self):
            return self.getTypedRuleContext(BKITParser.Boolean_func_callContext,0)


        def boolean_expr4(self):
            return self.getTypedRuleContext(BKITParser.Boolean_expr4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_boolean_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr3" ):
                return visitor.visitBoolean_expr3(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expr3(self):

        localctx = BKITParser.Boolean_expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_boolean_expr3)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.boolean_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.boolean_expr4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Boolean_literal(self):
            return self.getToken(BKITParser.Boolean_literal, 0)

        def var_non_init(self):
            return self.getTypedRuleContext(BKITParser.Var_non_initContext,0)


        def BOOL_OF_STRING(self):
            return self.getToken(BKITParser.BOOL_OF_STRING, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def String_literal(self):
            return self.getToken(BKITParser.String_literal, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr4" ):
                return visitor.visitBoolean_expr4(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expr4(self):

        localctx = BKITParser.Boolean_expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boolean_expr4)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Boolean_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(BKITParser.Boolean_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.var_non_init()
                pass
            elif token in [BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.match(BKITParser.BOOL_OF_STRING)
                self.state = 511
                self.match(BKITParser.LEFT_PAREN)
                self.state = 512
                self.match(BKITParser.String_literal)
                self.state = 513
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


    class Int_func_callContext(ParserRuleContext):

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
            return BKITParser.RULE_int_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_func_call" ):
                return visitor.visitInt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def int_func_call(self):

        localctx = BKITParser.Int_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_int_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(BKITParser.ID)
            self.state = 517
            self.match(BKITParser.LEFT_PAREN)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (BKITParser.INT_OF_FLOAT - 68)) | (1 << (BKITParser.INT_OF_STRING - 68)) | (1 << (BKITParser.FLOAT_TO_INT - 68)) | (1 << (BKITParser.FLOAT_OF_STRING - 68)) | (1 << (BKITParser.BOOL_OF_STRING - 68)))) != 0):
                self.state = 518
                self.expr()
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 519
                    self.match(BKITParser.COMMA)
                    self.state = 520
                    self.expr()
                    self.state = 525
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 531
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_func_callContext(ParserRuleContext):

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
            return BKITParser.RULE_float_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_func_call" ):
                return visitor.visitFloat_func_call(self)
            else:
                return visitor.visitChildren(self)




    def float_func_call(self):

        localctx = BKITParser.Float_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_float_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(BKITParser.ID)
            self.state = 534
            self.match(BKITParser.LEFT_PAREN)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (BKITParser.INT_OF_FLOAT - 68)) | (1 << (BKITParser.INT_OF_STRING - 68)) | (1 << (BKITParser.FLOAT_TO_INT - 68)) | (1 << (BKITParser.FLOAT_OF_STRING - 68)) | (1 << (BKITParser.BOOL_OF_STRING - 68)))) != 0):
                self.state = 535
                self.expr()
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 536
                    self.match(BKITParser.COMMA)
                    self.state = 537
                    self.expr()
                    self.state = 542
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 548
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_func_callContext(ParserRuleContext):

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
            return BKITParser.RULE_boolean_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_func_call" ):
                return visitor.visitBoolean_func_call(self)
            else:
                return visitor.visitChildren(self)




    def boolean_func_call(self):

        localctx = BKITParser.Boolean_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_boolean_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(BKITParser.ID)
            self.state = 551
            self.match(BKITParser.LEFT_PAREN)
            self.state = 562
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (BKITParser.INT_OF_FLOAT - 68)) | (1 << (BKITParser.INT_OF_STRING - 68)) | (1 << (BKITParser.FLOAT_TO_INT - 68)) | (1 << (BKITParser.FLOAT_OF_STRING - 68)) | (1 << (BKITParser.BOOL_OF_STRING - 68)))) != 0):
                self.state = 552
                self.expr()
                self.state = 557
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 553
                    self.match(BKITParser.COMMA)
                    self.state = 554
                    self.expr()
                    self.state = 559
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 565
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

        def int_expr1(self):
            return self.getTypedRuleContext(BKITParser.Int_expr1Context,0)


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
        self.enterRule(localctx, 112, self.RULE_index_op)
        try:
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 568
                self.int_expr1(0)
                self.state = 569
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 571
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 572
                self.int_expr1(0)
                self.state = 573
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 574
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
        self._predicates[33] = self.int_expr1_sempred
        self._predicates[34] = self.int_expr2_sempred
        self._predicates[40] = self.float_expr1_sempred
        self._predicates[41] = self.float_expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def int_expr1_sempred(self, localctx:Int_expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def int_expr2_sempred(self, localctx:Int_expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def float_expr1_sempred(self, localctx:Float_expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def float_expr2_sempred(self, localctx:Float_expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




