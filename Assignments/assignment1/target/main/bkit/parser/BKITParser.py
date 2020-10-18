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
        buf.write("\u026e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2\7\2")
        buf.write("\u0082\n\2\f\2\16\2\u0085\13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0093\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5")
        buf.write("\b\u00a6\n\b\3\b\3\b\3\b\5\b\u00ab\n\b\7\b\u00ad\n\b\f")
        buf.write("\b\16\b\u00b0\13\b\3\b\3\b\3\t\3\t\5\t\u00b6\n\t\3\t\3")
        buf.write("\t\3\t\5\t\u00bb\n\t\7\t\u00bd\n\t\f\t\16\t\u00c0\13\t")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\6\13\u00c8\n\13\r\13\16\13")
        buf.write("\u00c9\3\13\5\13\u00cd\n\13\3\f\3\f\3\f\3\f\5\f\u00d3")
        buf.write("\n\f\3\f\6\f\u00d6\n\f\r\f\16\f\u00d7\3\r\3\r\5\r\u00dc")
        buf.write("\n\r\3\r\3\r\3\r\5\r\u00e1\n\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\7\20\u00ee\n\20\f\20\16")
        buf.write("\20\u00f1\13\20\3\21\3\21\3\21\7\21\u00f6\n\21\f\21\16")
        buf.write("\21\u00f9\13\21\3\21\7\21\u00fc\n\21\f\21\16\21\u00ff")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0114\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u011f\n\23\f\23\16\23\u0122\13\23\3\23\3\23\5")
        buf.write("\23\u0126\n\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u014c\n\30\3\31\3")
        buf.write("\31\3\32\3\32\3\33\3\33\3\33\5\33\u0155\n\33\3\34\3\34")
        buf.write("\5\34\u0159\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3 \3 \5 \u0167\n \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u0174\n!\3!\3!\3!\5!\u0179\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\7\"\u0181\n\"\f\"\16\"\u0184\13\"\3#\3#\3#")
        buf.write("\3#\3#\3#\7#\u018c\n#\f#\16#\u018f\13#\3$\3$\3$\5$\u0194")
        buf.write("\n$\3%\3%\3%\3%\5%\u019a\n%\3&\3&\5&\u019e\n&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\5\'\u01a5\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\5(\u01b2\n(\3)\3)\3)\3)\3)\3)\7)\u01ba\n)\f)\16")
        buf.write(")\u01bd\13)\3*\3*\3*\3*\3*\3*\7*\u01c5\n*\f*\16*\u01c8")
        buf.write("\13*\3+\3+\3+\5+\u01cd\n+\3,\3,\3,\3,\5,\u01d3\n,\3-\3")
        buf.write("-\5-\u01d7\n-\3.\3.\3.\3.\3.\5.\u01de\n.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\5/\u01ec\n/\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u01f6\n\61\f\61\16\61\u01f9")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u01fe\n\62\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u0204\n\63\3\64\3\64\5\64\u0208\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u020f\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u0218\n\66\3\67\3\67\3\67\5\67\u021d")
        buf.write("\n\67\38\38\38\38\38\78\u0224\n8\f8\168\u0227\138\78\u0229")
        buf.write("\n8\f8\168\u022c\138\38\38\39\39\39\39\39\79\u0235\n9")
        buf.write("\f9\169\u0238\139\79\u023a\n9\f9\169\u023d\139\39\39\3")
        buf.write(":\3:\3:\3:\3:\7:\u0246\n:\f:\16:\u0249\13:\7:\u024b\n")
        buf.write(":\f:\16:\u024e\13:\3:\3:\3;\3;\3;\3;\3;\7;\u0257\n;\f")
        buf.write(";\16;\u025a\13;\7;\u025c\n;\f;\16;\u025f\13;\3;\3;\3<")
        buf.write("\3<\3<\3<\3<\3<\3<\3<\3<\5<\u026c\n<\3<\2\7BDPR`=\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\n\3\2\4\7\3\2)")
        buf.write(".\4\2\35\35\37\37\5\2!!##%%\4\2\36\36  \4\2\"\"$$\3\2")
        buf.write("\4\5\3\2\'(\2\u0280\2}\3\2\2\2\4\u0088\3\2\2\2\6\u008c")
        buf.write("\3\2\2\2\b\u009a\3\2\2\2\n\u009e\3\2\2\2\f\u00a0\3\2\2")
        buf.write("\2\16\u00a2\3\2\2\2\20\u00b5\3\2\2\2\22\u00c1\3\2\2\2")
        buf.write("\24\u00cc\3\2\2\2\26\u00ce\3\2\2\2\30\u00db\3\2\2\2\32")
        buf.write("\u00e2\3\2\2\2\34\u00e6\3\2\2\2\36\u00ea\3\2\2\2 \u00f7")
        buf.write("\3\2\2\2\"\u0113\3\2\2\2$\u0115\3\2\2\2&\u012a\3\2\2\2")
        buf.write("(\u012c\3\2\2\2*\u0139\3\2\2\2,\u0140\3\2\2\2.\u0147\3")
        buf.write("\2\2\2\60\u014d\3\2\2\2\62\u014f\3\2\2\2\64\u0154\3\2")
        buf.write("\2\2\66\u0156\3\2\2\28\u015a\3\2\2\2:\u015e\3\2\2\2<\u0160")
        buf.write("\3\2\2\2>\u0166\3\2\2\2@\u0178\3\2\2\2B\u017a\3\2\2\2")
        buf.write("D\u0185\3\2\2\2F\u0193\3\2\2\2H\u0199\3\2\2\2J\u019d\3")
        buf.write("\2\2\2L\u01a4\3\2\2\2N\u01b1\3\2\2\2P\u01b3\3\2\2\2R\u01be")
        buf.write("\3\2\2\2T\u01cc\3\2\2\2V\u01d2\3\2\2\2X\u01d6\3\2\2\2")
        buf.write("Z\u01dd\3\2\2\2\\\u01eb\3\2\2\2^\u01ed\3\2\2\2`\u01ef")
        buf.write("\3\2\2\2b\u01fd\3\2\2\2d\u0203\3\2\2\2f\u0207\3\2\2\2")
        buf.write("h\u020e\3\2\2\2j\u0217\3\2\2\2l\u021c\3\2\2\2n\u021e\3")
        buf.write("\2\2\2p\u022f\3\2\2\2r\u0240\3\2\2\2t\u0251\3\2\2\2v\u026b")
        buf.write("\3\2\2\2xy\5\4\3\2yz\7<\2\2z|\3\2\2\2{x\3\2\2\2|\177\3")
        buf.write("\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0083\3\2\2\2\177}\3\2\2\2")
        buf.write("\u0080\u0082\5\6\4\2\u0081\u0080\3\2\2\2\u0082\u0085\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\7\2\2\3\u0087")
        buf.write("\3\3\2\2\2\u0088\u0089\7\30\2\2\u0089\u008a\7:\2\2\u008a")
        buf.write("\u008b\5\20\t\2\u008b\5\3\2\2\2\u008c\u008d\7\23\2\2\u008d")
        buf.write("\u008e\7:\2\2\u008e\u0092\7\3\2\2\u008f\u0090\7\25\2\2")
        buf.write("\u0090\u0091\7:\2\2\u0091\u0093\5\36\20\2\u0092\u008f")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\7\b\2\2\u0095\u0096\7:\2\2\u0096\u0097\5 \21\2")
        buf.write("\u0097\u0098\7\17\2\2\u0098\u0099\7;\2\2\u0099\7\3\2\2")
        buf.write("\2\u009a\u009b\7\3\2\2\u009b\u009c\7>\2\2\u009c\u009d")
        buf.write("\5\16\b\2\u009d\t\3\2\2\2\u009e\u009f\t\2\2\2\u009f\13")
        buf.write("\3\2\2\2\u00a0\u00a1\5\16\b\2\u00a1\r\3\2\2\2\u00a2\u00a5")
        buf.write("\78\2\2\u00a3\u00a6\5\n\6\2\u00a4\u00a6\5\f\7\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00ae\3\2\2\2")
        buf.write("\u00a7\u00aa\7=\2\2\u00a8\u00ab\5\n\6\2\u00a9\u00ab\5")
        buf.write("\f\7\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ad")
        buf.write("\3\2\2\2\u00ac\u00a7\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\79\2\2\u00b2\17\3\2\2")
        buf.write("\2\u00b3\u00b6\5\24\13\2\u00b4\u00b6\5\30\r\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00be\3\2\2\2\u00b7")
        buf.write("\u00ba\7=\2\2\u00b8\u00bb\5\24\13\2\u00b9\u00bb\5\30\r")
        buf.write("\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bd")
        buf.write("\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\21\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c2\7\3\2\2\u00c2\23\3\2\2\2\u00c3")
        buf.write("\u00c7\7\3\2\2\u00c4\u00c5\7\66\2\2\u00c5\u00c6\7\4\2")
        buf.write("\2\u00c6\u00c8\7\67\2\2\u00c7\u00c4\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00cd\7\3\2\2\u00cc\u00c3\3\2\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cd\25\3\2\2\2\u00ce\u00d5\7\3")
        buf.write("\2\2\u00cf\u00d2\7\66\2\2\u00d0\u00d3\5\26\f\2\u00d1\u00d3")
        buf.write("\7\4\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d6\7\67\2\2\u00d5\u00cf\3\2\2")
        buf.write("\2\u00d6\u00d7\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\27\3\2\2\2\u00d9\u00dc\5\26\f\2\u00da\u00dc")
        buf.write("\5\22\n\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00e0\7>\2\2\u00de\u00e1\5\f\7\2")
        buf.write("\u00df\u00e1\5\n\6\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3")
        buf.write("\2\2\2\u00e1\31\3\2\2\2\u00e2\u00e3\5\26\f\2\u00e3\u00e4")
        buf.write("\7>\2\2\u00e4\u00e5\5\16\b\2\u00e5\33\3\2\2\2\u00e6\u00e7")
        buf.write("\5\22\n\2\u00e7\u00e8\7>\2\2\u00e8\u00e9\5\n\6\2\u00e9")
        buf.write("\35\3\2\2\2\u00ea\u00ef\5\24\13\2\u00eb\u00ec\7=\2\2\u00ec")
        buf.write("\u00ee\5\24\13\2\u00ed\u00eb\3\2\2\2\u00ee\u00f1\3\2\2")
        buf.write("\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\37\3")
        buf.write("\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\5&\24\2\u00f3\u00f4")
        buf.write("\7<\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f2\3\2\2\2\u00f6")
        buf.write("\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00fd\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fc\5")
        buf.write("\"\22\2\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe!\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\u0114\5$\23\2\u0101\u0114\5(\25\2")
        buf.write("\u0102\u0114\5*\26\2\u0103\u0114\5,\27\2\u0104\u0105\5")
        buf.write(".\30\2\u0105\u0106\7<\2\2\u0106\u0114\3\2\2\2\u0107\u0108")
        buf.write("\5\60\31\2\u0108\u0109\7<\2\2\u0109\u0114\3\2\2\2\u010a")
        buf.write("\u010b\5\62\32\2\u010b\u010c\7<\2\2\u010c\u0114\3\2\2")
        buf.write("\2\u010d\u010e\5\64\33\2\u010e\u010f\7<\2\2\u010f\u0114")
        buf.write("\3\2\2\2\u0110\u0111\5\66\34\2\u0111\u0112\7<\2\2\u0112")
        buf.write("\u0114\3\2\2\2\u0113\u0100\3\2\2\2\u0113\u0101\3\2\2\2")
        buf.write("\u0113\u0102\3\2\2\2\u0113\u0103\3\2\2\2\u0113\u0104\3")
        buf.write("\2\2\2\u0113\u0107\3\2\2\2\u0113\u010a\3\2\2\2\u0113\u010d")
        buf.write("\3\2\2\2\u0113\u0110\3\2\2\2\u0114#\3\2\2\2\u0115\u0116")
        buf.write("\7\24\2\2\u0116\u0117\5@!\2\u0117\u0118\7\27\2\2\u0118")
        buf.write("\u0120\5 \21\2\u0119\u011a\7\r\2\2\u011a\u011b\5@!\2\u011b")
        buf.write("\u011c\7\27\2\2\u011c\u011d\5 \21\2\u011d\u011f\3\2\2")
        buf.write("\2\u011e\u0119\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0125\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0123\u0124\7\f\2\2\u0124\u0126\5 \21\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\7\16\2\2\u0128\u0129\7;\2\2\u0129%")
        buf.write("\3\2\2\2\u012a\u012b\5\4\3\2\u012b\'\3\2\2\2\u012c\u012d")
        buf.write("\7\22\2\2\u012d\u012e\7\64\2\2\u012e\u012f\58\35\2\u012f")
        buf.write("\u0130\7=\2\2\u0130\u0131\5:\36\2\u0131\u0132\7=\2\2\u0132")
        buf.write("\u0133\5<\37\2\u0133\u0134\7\65\2\2\u0134\u0135\7\13\2")
        buf.write("\2\u0135\u0136\5 \21\2\u0136\u0137\7\20\2\2\u0137\u0138")
        buf.write("\7;\2\2\u0138)\3\2\2\2\u0139\u013a\7\31\2\2\u013a\u013b")
        buf.write("\5`\61\2\u013b\u013c\7\13\2\2\u013c\u013d\5 \21\2\u013d")
        buf.write("\u013e\7\21\2\2\u013e\u013f\7;\2\2\u013f+\3\2\2\2\u0140")
        buf.write("\u0141\7\13\2\2\u0141\u0142\5 \21\2\u0142\u0143\7\31\2")
        buf.write("\2\u0143\u0144\5`\61\2\u0144\u0145\7\34\2\2\u0145\u0146")
        buf.write("\7;\2\2\u0146-\3\2\2\2\u0147\u0148\5\24\13\2\u0148\u014b")
        buf.write("\7>\2\2\u0149\u014c\5> \2\u014a\u014c\5@!\2\u014b\u0149")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c/\3\2\2\2\u014d\u014e")
        buf.write("\7\t\2\2\u014e\61\3\2\2\2\u014f\u0150\7\n\2\2\u0150\63")
        buf.write("\3\2\2\2\u0151\u0155\5n8\2\u0152\u0155\5p9\2\u0153\u0155")
        buf.write("\5r:\2\u0154\u0151\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\65\3\2\2\2\u0156\u0158\7\26\2\2\u0157\u0159")
        buf.write("\5> \2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159\67")
        buf.write("\3\2\2\2\u015a\u015b\5\22\n\2\u015b\u015c\7>\2\2\u015c")
        buf.write("\u015d\5B\"\2\u015d9\3\2\2\2\u015e\u015f\5@!\2\u015f;")
        buf.write("\3\2\2\2\u0160\u0161\5.\30\2\u0161=\3\2\2\2\u0162\u0167")
        buf.write("\5B\"\2\u0163\u0167\5P)\2\u0164\u0167\5b\62\2\u0165\u0167")
        buf.write("\5l\67\2\u0166\u0162\3\2\2\2\u0166\u0163\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167?\3\2\2\2\u0168")
        buf.write("\u0169\5B\"\2\u0169\u016a\t\3\2\2\u016a\u016b\5B\"\2\u016b")
        buf.write("\u0179\3\2\2\2\u016c\u0173\5P)\2\u016d\u0174\3\2\2\2\u016e")
        buf.write("\u0174\7/\2\2\u016f\u0174\7\60\2\2\u0170\u0174\7\61\2")
        buf.write("\2\u0171\u0174\7\62\2\2\u0172\u0174\7\63\2\2\u0173\u016d")
        buf.write("\3\2\2\2\u0173\u016e\3\2\2\2\u0173\u016f\3\2\2\2\u0173")
        buf.write("\u0170\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\5P)\2\u0176\u0179\3\2")
        buf.write("\2\2\u0177\u0179\5`\61\2\u0178\u0168\3\2\2\2\u0178\u016c")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179A\3\2\2\2\u017a\u017b")
        buf.write("\b\"\1\2\u017b\u017c\5D#\2\u017c\u0182\3\2\2\2\u017d\u017e")
        buf.write("\f\4\2\2\u017e\u017f\t\4\2\2\u017f\u0181\5D#\2\u0180\u017d")
        buf.write("\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183C\3\2\2\2\u0184\u0182\3\2\2\2\u0185")
        buf.write("\u0186\b#\1\2\u0186\u0187\5F$\2\u0187\u018d\3\2\2\2\u0188")
        buf.write("\u0189\f\4\2\2\u0189\u018a\t\5\2\2\u018a\u018c\5F$\2\u018b")
        buf.write("\u0188\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018eE\3\2\2\2\u018f\u018d\3\2\2")
        buf.write("\2\u0190\u0191\7\37\2\2\u0191\u0194\5F$\2\u0192\u0194")
        buf.write("\5H%\2\u0193\u0190\3\2\2\2\u0193\u0192\3\2\2\2\u0194G")
        buf.write("\3\2\2\2\u0195\u0196\5J&\2\u0196\u0197\5v<\2\u0197\u019a")
        buf.write("\3\2\2\2\u0198\u019a\5J&\2\u0199\u0195\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019aI\3\2\2\2\u019b\u019e\5n8\2\u019c\u019e")
        buf.write("\5L\'\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("K\3\2\2\2\u019f\u01a5\5N(\2\u01a0\u01a1\7\64\2\2\u01a1")
        buf.write("\u01a2\5B\"\2\u01a2\u01a3\7\65\2\2\u01a3\u01a5\3\2\2\2")
        buf.write("\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a5M\3\2\2")
        buf.write("\2\u01a6\u01b2\7\4\2\2\u01a7\u01b2\5\22\n\2\u01a8\u01a9")
        buf.write("\7@\2\2\u01a9\u01aa\7\64\2\2\u01aa\u01ab\5P)\2\u01ab\u01ac")
        buf.write("\7\65\2\2\u01ac\u01b2\3\2\2\2\u01ad\u01ae\7A\2\2\u01ae")
        buf.write("\u01af\7\64\2\2\u01af\u01b0\7\7\2\2\u01b0\u01b2\7\65\2")
        buf.write("\2\u01b1\u01a6\3\2\2\2\u01b1\u01a7\3\2\2\2\u01b1\u01a8")
        buf.write("\3\2\2\2\u01b1\u01ad\3\2\2\2\u01b2O\3\2\2\2\u01b3\u01b4")
        buf.write("\b)\1\2\u01b4\u01b5\5R*\2\u01b5\u01bb\3\2\2\2\u01b6\u01b7")
        buf.write("\f\4\2\2\u01b7\u01b8\t\6\2\2\u01b8\u01ba\5R*\2\u01b9\u01b6")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bcQ\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01bf\b*\1\2\u01bf\u01c0\5T+\2\u01c0\u01c6\3\2\2\2\u01c1")
        buf.write("\u01c2\f\4\2\2\u01c2\u01c3\t\7\2\2\u01c3\u01c5\5T+\2\u01c4")
        buf.write("\u01c1\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7S\3\2\2\2\u01c8\u01c6\3\2\2")
        buf.write("\2\u01c9\u01ca\7 \2\2\u01ca\u01cd\5T+\2\u01cb\u01cd\5")
        buf.write("V,\2\u01cc\u01c9\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdU\3")
        buf.write("\2\2\2\u01ce\u01cf\5X-\2\u01cf\u01d0\5v<\2\u01d0\u01d3")
        buf.write("\3\2\2\2\u01d1\u01d3\5X-\2\u01d2\u01ce\3\2\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3W\3\2\2\2\u01d4\u01d7\5p9\2\u01d5\u01d7")
        buf.write("\5Z.\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7Y")
        buf.write("\3\2\2\2\u01d8\u01de\5\\/\2\u01d9\u01da\7\64\2\2\u01da")
        buf.write("\u01db\5P)\2\u01db\u01dc\7\65\2\2\u01dc\u01de\3\2\2\2")
        buf.write("\u01dd\u01d8\3\2\2\2\u01dd\u01d9\3\2\2\2\u01de[\3\2\2")
        buf.write("\2\u01df\u01ec\7\5\2\2\u01e0\u01ec\5\22\n\2\u01e1\u01e2")
        buf.write("\7B\2\2\u01e2\u01e3\7\64\2\2\u01e3\u01e4\5B\"\2\u01e4")
        buf.write("\u01e5\7\65\2\2\u01e5\u01ec\3\2\2\2\u01e6\u01e7\7C\2\2")
        buf.write("\u01e7\u01e8\7\64\2\2\u01e8\u01e9\5l\67\2\u01e9\u01ea")
        buf.write("\7\65\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01df\3\2\2\2\u01eb")
        buf.write("\u01e0\3\2\2\2\u01eb\u01e1\3\2\2\2\u01eb\u01e6\3\2\2\2")
        buf.write("\u01ec]\3\2\2\2\u01ed\u01ee\t\b\2\2\u01ee_\3\2\2\2\u01ef")
        buf.write("\u01f0\b\61\1\2\u01f0\u01f1\5b\62\2\u01f1\u01f7\3\2\2")
        buf.write("\2\u01f2\u01f3\f\4\2\2\u01f3\u01f4\t\t\2\2\u01f4\u01f6")
        buf.write("\5`\61\5\u01f5\u01f2\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8a\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01fa\u01fb\7&\2\2\u01fb\u01fe\5d\63\2")
        buf.write("\u01fc\u01fe\5d\63\2\u01fd\u01fa\3\2\2\2\u01fd\u01fc\3")
        buf.write("\2\2\2\u01fec\3\2\2\2\u01ff\u0200\5f\64\2\u0200\u0201")
        buf.write("\5v<\2\u0201\u0204\3\2\2\2\u0202\u0204\5f\64\2\u0203\u01ff")
        buf.write("\3\2\2\2\u0203\u0202\3\2\2\2\u0204e\3\2\2\2\u0205\u0208")
        buf.write("\5r:\2\u0206\u0208\5h\65\2\u0207\u0205\3\2\2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208g\3\2\2\2\u0209\u020f\5j\66\2\u020a\u020b")
        buf.write("\7\64\2\2\u020b\u020c\5@!\2\u020c\u020d\7\65\2\2\u020d")
        buf.write("\u020f\3\2\2\2\u020e\u0209\3\2\2\2\u020e\u020a\3\2\2\2")
        buf.write("\u020fi\3\2\2\2\u0210\u0218\7\6\2\2\u0211\u0218\5\24\13")
        buf.write("\2\u0212\u0213\7D\2\2\u0213\u0214\7\64\2\2\u0214\u0215")
        buf.write("\5l\67\2\u0215\u0216\7\65\2\2\u0216\u0218\3\2\2\2\u0217")
        buf.write("\u0210\3\2\2\2\u0217\u0211\3\2\2\2\u0217\u0212\3\2\2\2")
        buf.write("\u0218k\3\2\2\2\u0219\u021d\7\3\2\2\u021a\u021d\7\7\2")
        buf.write("\2\u021b\u021d\5t;\2\u021c\u0219\3\2\2\2\u021c\u021a\3")
        buf.write("\2\2\2\u021c\u021b\3\2\2\2\u021dm\3\2\2\2\u021e\u021f")
        buf.write("\7\3\2\2\u021f\u022a\7\64\2\2\u0220\u0225\5> \2\u0221")
        buf.write("\u0222\7=\2\2\u0222\u0224\5> \2\u0223\u0221\3\2\2\2\u0224")
        buf.write("\u0227\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0228\u0220\3")
        buf.write("\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u022e\7\65\2\2\u022eo\3\2\2\2\u022f\u0230\7\3\2\2\u0230")
        buf.write("\u023b\7\64\2\2\u0231\u0236\5> \2\u0232\u0233\7=\2\2\u0233")
        buf.write("\u0235\5> \2\u0234\u0232\3\2\2\2\u0235\u0238\3\2\2\2\u0236")
        buf.write("\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u023a\3\2\2\2")
        buf.write("\u0238\u0236\3\2\2\2\u0239\u0231\3\2\2\2\u023a\u023d\3")
        buf.write("\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023e")
        buf.write("\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f\7\65\2\2\u023f")
        buf.write("q\3\2\2\2\u0240\u0241\7\3\2\2\u0241\u024c\7\64\2\2\u0242")
        buf.write("\u0247\5> \2\u0243\u0244\7=\2\2\u0244\u0246\5> \2\u0245")
        buf.write("\u0243\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2")
        buf.write("\u0247\u0248\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3")
        buf.write("\2\2\2\u024a\u0242\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a")
        buf.write("\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024f\3\2\2\2\u024e")
        buf.write("\u024c\3\2\2\2\u024f\u0250\7\65\2\2\u0250s\3\2\2\2\u0251")
        buf.write("\u0252\7\3\2\2\u0252\u025d\7\64\2\2\u0253\u0258\5> \2")
        buf.write("\u0254\u0255\7=\2\2\u0255\u0257\5> \2\u0256\u0254\3\2")
        buf.write("\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258\3\2\2\2\u025b")
        buf.write("\u0253\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025d\u025e\3\2\2\2\u025e\u0260\3\2\2\2\u025f\u025d\3")
        buf.write("\2\2\2\u0260\u0261\7\65\2\2\u0261u\3\2\2\2\u0262\u0263")
        buf.write("\7\66\2\2\u0263\u0264\5B\"\2\u0264\u0265\7\67\2\2\u0265")
        buf.write("\u026c\3\2\2\2\u0266\u0267\7\66\2\2\u0267\u0268\5B\"\2")
        buf.write("\u0268\u0269\7\67\2\2\u0269\u026a\5v<\2\u026a\u026c\3")
        buf.write("\2\2\2\u026b\u0262\3\2\2\2\u026b\u0266\3\2\2\2\u026cw")
        buf.write("\3\2\2\2;}\u0083\u0092\u00a5\u00aa\u00ae\u00b5\u00ba\u00be")
        buf.write("\u00c9\u00cc\u00d2\u00d7\u00db\u00e0\u00ef\u00f7\u00fd")
        buf.write("\u0113\u0120\u0125\u014b\u0154\u0158\u0166\u0173\u0178")
        buf.write("\u0182\u018d\u0193\u0199\u019d\u01a4\u01b1\u01bb\u01c6")
        buf.write("\u01cc\u01d2\u01d6\u01dd\u01eb\u01f7\u01fd\u0203\u0207")
        buf.write("\u020e\u0217\u021c\u0225\u022a\u0236\u023b\u0247\u024c")
        buf.write("\u0258\u025d\u026b")
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
    RULE_boolean_type_expr = 31
    RULE_int_expr1 = 32
    RULE_int_expr2 = 33
    RULE_int_expr3 = 34
    RULE_int_expr4 = 35
    RULE_int_expr5 = 36
    RULE_int_expr6 = 37
    RULE_int_operand = 38
    RULE_float_expr1 = 39
    RULE_float_expr2 = 40
    RULE_float_expr3 = 41
    RULE_float_expr4 = 42
    RULE_float_expr5 = 43
    RULE_float_expr6 = 44
    RULE_float_operand = 45
    RULE_constant = 46
    RULE_boolean_expr = 47
    RULE_boolean_expr1 = 48
    RULE_boolean_expr2 = 49
    RULE_boolean_expr3 = 50
    RULE_boolean_expr4 = 51
    RULE_boolean_operand = 52
    RULE_string_expr = 53
    RULE_int_func_call = 54
    RULE_float_func_call = 55
    RULE_boolean_func_call = 56
    RULE_string_func_call = 57
    RULE_index_op = 58

    ruleNames =  [ "program", "var_declare", "function_declare", "array", 
                   "primitive_data", "composite_data", "array_lit", "var_list", 
                   "scalar_var", "var_non_init", "composite_var", "var_init", 
                   "composite_init", "primitive_init", "params_list", "stmt_list", 
                   "stmt", "if_stmt", "var_declare_stmt", "for_stmt", "while_stmt", 
                   "dowhile_stmt", "assign_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "init_for", "con_for", "update_for", 
                   "expr", "boolean_type_expr", "int_expr1", "int_expr2", 
                   "int_expr3", "int_expr4", "int_expr5", "int_expr6", "int_operand", 
                   "float_expr1", "float_expr2", "float_expr3", "float_expr4", 
                   "float_expr5", "float_expr6", "float_operand", "constant", 
                   "boolean_expr", "boolean_expr1", "boolean_expr2", "boolean_expr3", 
                   "boolean_expr4", "boolean_operand", "string_expr", "int_func_call", 
                   "float_func_call", "boolean_func_call", "string_func_call", 
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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 118
                self.var_declare()
                self.state = 119
                self.match(BKITParser.SEMI)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 126
                self.function_declare()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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
            self.state = 134
            self.match(BKITParser.VAR)
            self.state = 135
            self.match(BKITParser.COLON)
            self.state = 136
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
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BKITParser.FUNCTION)
            self.state = 139
            self.match(BKITParser.COLON)
            self.state = 140
            self.match(BKITParser.ID)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 141
                self.match(BKITParser.PARAMETER)
                self.state = 142
                self.match(BKITParser.COLON)
                self.state = 143
                self.params_list()


            self.state = 146
            self.match(BKITParser.BODY)
            self.state = 147
            self.match(BKITParser.COLON)
            self.state = 148
            self.stmt_list()
            self.state = 149
            self.match(BKITParser.ENDBODY)
            self.state = 150
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
            self.state = 152
            self.match(BKITParser.ID)
            self.state = 153
            self.match(BKITParser.ASSIGN)
            self.state = 154
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
            self.state = 156
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
            self.state = 158
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
        self.enterRule(localctx, 12, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BKITParser.LEFT_BRACE)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.state = 161
                self.primitive_data()
                pass
            elif token in [BKITParser.LEFT_BRACE]:
                self.state = 162
                self.composite_data()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 165
                self.match(BKITParser.COMMA)
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                    self.state = 166
                    self.primitive_data()
                    pass
                elif token in [BKITParser.LEFT_BRACE]:
                    self.state = 167
                    self.composite_data()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 177
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 178
                self.var_init()
                pass


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 181
                self.match(BKITParser.COMMA)
                self.state = 184
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 182
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 183
                    self.var_init()
                    pass


                self.state = 190
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
            self.state = 191
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(BKITParser.ID)
                self.state = 197 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 194
                        self.match(BKITParser.LEFT_BRACKET)
                        self.state = 195
                        self.match(BKITParser.INT_LIT)
                        self.state = 196
                        self.match(BKITParser.RIGHT_BRACKET)

                    else:
                        raise NoViableAltException(self)
                    self.state = 199 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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


        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

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
            self.state = 204
            self.match(BKITParser.ID)
            self.state = 211 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 205
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 208
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID]:
                    self.state = 206
                    self.composite_var()
                    pass
                elif token in [BKITParser.INT_LIT]:
                    self.state = 207
                    self.match(BKITParser.INT_LIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 213 
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
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 215
                self.composite_var()
                pass

            elif la_ == 2:
                self.state = 216
                self.scalar_var()
                pass


            self.state = 219
            self.match(BKITParser.ASSIGN)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.state = 220
                self.composite_data()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.state = 221
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
            self.state = 224
            self.composite_var()
            self.state = 225
            self.match(BKITParser.ASSIGN)
            self.state = 226
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
            self.state = 228
            self.scalar_var()
            self.state = 229
            self.match(BKITParser.ASSIGN)
            self.state = 230
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
            self.state = 232
            self.var_non_init()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 233
                self.match(BKITParser.COMMA)
                self.state = 234
                self.var_non_init()
                self.state = 239
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
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 240
                self.var_declare_stmt()
                self.state = 241
                self.match(BKITParser.SEMI)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 248
                    self.stmt() 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.dowhile_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.assign_stmt()
                self.state = 259
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.break_stmt()
                self.state = 262
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 264
                self.continue_stmt()
                self.state = 265
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 267
                self.call_stmt()
                self.state = 268
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
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
        self.enterRule(localctx, 34, self.RULE_if_stmt)
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
        self.enterRule(localctx, 36, self.RULE_var_declare_stmt)
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
        self.enterRule(localctx, 38, self.RULE_for_stmt)
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
        self.enterRule(localctx, 40, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(BKITParser.WHILE)
            self.state = 312
            self.boolean_expr(0)
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
        self.enterRule(localctx, 42, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(BKITParser.DO)
            self.state = 319
            self.stmt_list()
            self.state = 320
            self.match(BKITParser.WHILE)
            self.state = 321
            self.boolean_expr(0)
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


        def boolean_type_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_type_exprContext,0)


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
            self.state = 325
            self.var_non_init()
            self.state = 326
            self.match(BKITParser.ASSIGN)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 327
                self.expr()
                pass

            elif la_ == 2:
                self.state = 328
                self.boolean_type_expr()
                pass


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
            self.state = 331
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
            self.state = 333
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
        self.enterRule(localctx, 50, self.RULE_call_stmt)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.float_func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
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
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(BKITParser.RETURN)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.INT_OF_FLOAT) | (1 << BKITParser.INT_OF_STRING))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT_TO_INT - 64)) | (1 << (BKITParser.FLOAT_OF_STRING - 64)) | (1 << (BKITParser.BOOL_OF_STRING - 64)))) != 0):
                self.state = 341
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
        self.enterRule(localctx, 54, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.scalar_var()
            self.state = 345
            self.match(BKITParser.ASSIGN)
            self.state = 346
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
        self.enterRule(localctx, 56, self.RULE_con_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
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
        self.enterRule(localctx, 58, self.RULE_update_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
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


        def string_expr(self):
            return self.getTypedRuleContext(BKITParser.String_exprContext,0)


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
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.boolean_expr1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.string_expr()
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
        self.enterRule(localctx, 62, self.RULE_boolean_type_expr)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.int_expr1(0)
                self.state = 359
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL_INT) | (1 << BKITParser.LESS_INT) | (1 << BKITParser.GREATER_INT) | (1 << BKITParser.LESS_OR_EQUAL_INT) | (1 << BKITParser.GREATER_OR_EQUAL_INT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 360
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.float_expr1(0)
                self.state = 369
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID, BKITParser.FLOAT_LIT, BKITParser.MINUS_FLOAT, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                    pass
                elif token in [BKITParser.NOT_EQUAL_FLOAT]:
                    self.state = 364
                    self.match(BKITParser.NOT_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.LESS_FLOAT]:
                    self.state = 365
                    self.match(BKITParser.LESS_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_FLOAT]:
                    self.state = 366
                    self.match(BKITParser.GREATER_FLOAT)
                    pass
                elif token in [BKITParser.LESS_OR_EQUAL_FLOAT]:
                    self.state = 367
                    self.match(BKITParser.LESS_OR_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_OR_EQUAL_FLOAT]:
                    self.state = 368
                    self.match(BKITParser.GREATER_OR_EQUAL_FLOAT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 371
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.boolean_expr(0)
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_int_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.int_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr1)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_INT or _la==BKITParser.MINUS_INT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 381
                    self.int_expr2(0) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_int_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.int_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr2)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.STAR_INT) | (1 << BKITParser.DIV_INT) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 392
                    self.int_expr3() 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_int_expr3)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(BKITParser.MINUS_INT)
                self.state = 399
                self.int_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.LEFT_PAREN, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
        self.enterRule(localctx, 70, self.RULE_int_expr4)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.int_expr5()
                self.state = 404
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
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
        self.enterRule(localctx, 72, self.RULE_int_expr5)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
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
        self.enterRule(localctx, 74, self.RULE_int_expr6)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.int_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.match(BKITParser.LEFT_PAREN)
                self.state = 415
                self.int_expr1(0)
                self.state = 416
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

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

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

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_operand" ):
                return visitor.visitInt_operand(self)
            else:
                return visitor.visitChildren(self)




    def int_operand(self):

        localctx = BKITParser.Int_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_int_operand)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(BKITParser.INT_LIT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.scalar_var()
                pass
            elif token in [BKITParser.INT_OF_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.match(BKITParser.INT_OF_FLOAT)
                self.state = 423
                self.match(BKITParser.LEFT_PAREN)
                self.state = 424
                self.float_expr1(0)
                self.state = 425
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(BKITParser.INT_OF_STRING)
                self.state = 428
                self.match(BKITParser.LEFT_PAREN)
                self.state = 429
                self.match(BKITParser.STRING_LIT)
                self.state = 430
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_float_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.float_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr1)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 437
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_FLOAT or _la==BKITParser.MINUS_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 438
                    self.float_expr2(0) 
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_float_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.float_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr2)
                    self.state = 447
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 448
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.STAR_FLOAT or _la==BKITParser.DIV_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 449
                    self.float_expr3() 
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_float_expr3)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(BKITParser.MINUS_FLOAT)
                self.state = 456
                self.float_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.FLOAT_LIT, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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
        self.enterRule(localctx, 84, self.RULE_float_expr4)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.float_expr5()
                self.state = 461
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
        self.enterRule(localctx, 86, self.RULE_float_expr5)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.float_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
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
        self.enterRule(localctx, 88, self.RULE_float_expr6)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.FLOAT_LIT, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.float_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(BKITParser.LEFT_PAREN)
                self.state = 472
                self.float_expr1(0)
                self.state = 473
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

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

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

        def string_expr(self):
            return self.getTypedRuleContext(BKITParser.String_exprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_float_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_operand" ):
                return visitor.visitFloat_operand(self)
            else:
                return visitor.visitChildren(self)




    def float_operand(self):

        localctx = BKITParser.Float_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_float_operand)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(BKITParser.FLOAT_LIT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.scalar_var()
                pass
            elif token in [BKITParser.FLOAT_TO_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(BKITParser.FLOAT_TO_INT)
                self.state = 480
                self.match(BKITParser.LEFT_PAREN)
                self.state = 481
                self.int_expr1(0)
                self.state = 482
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(BKITParser.FLOAT_OF_STRING)
                self.state = 485
                self.match(BKITParser.LEFT_PAREN)
                self.state = 486
                self.string_expr()
                self.state = 487
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

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = BKITParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT_LIT or _la==BKITParser.FLOAT_LIT):
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

        def boolean_expr1(self):
            return self.getTypedRuleContext(BKITParser.Boolean_expr1Context,0)


        def boolean_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Boolean_exprContext)
            else:
                return self.getTypedRuleContext(BKITParser.Boolean_exprContext,i)


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



    def boolean_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Boolean_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_boolean_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.boolean_expr1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 501
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Boolean_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expr)
                    self.state = 496
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 497
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 498
                    self.boolean_expr(3) 
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 96, self.RULE_boolean_expr1)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(BKITParser.NOT)
                self.state = 505
                self.boolean_expr2()
                pass
            elif token in [BKITParser.ID, BKITParser.BOOL_LIT, BKITParser.LEFT_PAREN, BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
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
        self.enterRule(localctx, 98, self.RULE_boolean_expr2)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.boolean_expr3()
                self.state = 510
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
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
        self.enterRule(localctx, 100, self.RULE_boolean_expr3)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.boolean_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
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

        def boolean_operand(self):
            return self.getTypedRuleContext(BKITParser.Boolean_operandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def boolean_type_expr(self):
            return self.getTypedRuleContext(BKITParser.Boolean_type_exprContext,0)


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
        self.enterRule(localctx, 102, self.RULE_boolean_expr4)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.BOOL_LIT, BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.boolean_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(BKITParser.LEFT_PAREN)
                self.state = 521
                self.boolean_type_expr()
                self.state = 522
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


    class Boolean_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def var_non_init(self):
            return self.getTypedRuleContext(BKITParser.Var_non_initContext,0)


        def BOOL_OF_STRING(self):
            return self.getToken(BKITParser.BOOL_OF_STRING, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def string_expr(self):
            return self.getTypedRuleContext(BKITParser.String_exprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_operand" ):
                return visitor.visitBoolean_operand(self)
            else:
                return visitor.visitChildren(self)




    def boolean_operand(self):

        localctx = BKITParser.Boolean_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boolean_operand)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(BKITParser.BOOL_LIT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.var_non_init()
                pass
            elif token in [BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.match(BKITParser.BOOL_OF_STRING)
                self.state = 529
                self.match(BKITParser.LEFT_PAREN)
                self.state = 530
                self.string_expr()
                self.state = 531
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


    class String_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def string_func_call(self):
            return self.getTypedRuleContext(BKITParser.String_func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = BKITParser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_string_expr)
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(BKITParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.string_func_call()
                pass


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
        self.enterRule(localctx, 108, self.RULE_int_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(BKITParser.ID)
            self.state = 541
            self.match(BKITParser.LEFT_PAREN)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.INT_OF_FLOAT) | (1 << BKITParser.INT_OF_STRING))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT_TO_INT - 64)) | (1 << (BKITParser.FLOAT_OF_STRING - 64)) | (1 << (BKITParser.BOOL_OF_STRING - 64)))) != 0):
                self.state = 542
                self.expr()
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 543
                    self.match(BKITParser.COMMA)
                    self.state = 544
                    self.expr()
                    self.state = 549
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 555
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
        self.enterRule(localctx, 110, self.RULE_float_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(BKITParser.ID)
            self.state = 558
            self.match(BKITParser.LEFT_PAREN)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.INT_OF_FLOAT) | (1 << BKITParser.INT_OF_STRING))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT_TO_INT - 64)) | (1 << (BKITParser.FLOAT_OF_STRING - 64)) | (1 << (BKITParser.BOOL_OF_STRING - 64)))) != 0):
                self.state = 559
                self.expr()
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 560
                    self.match(BKITParser.COMMA)
                    self.state = 561
                    self.expr()
                    self.state = 566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 571
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 572
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
        self.enterRule(localctx, 112, self.RULE_boolean_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(BKITParser.ID)
            self.state = 575
            self.match(BKITParser.LEFT_PAREN)
            self.state = 586
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.INT_OF_FLOAT) | (1 << BKITParser.INT_OF_STRING))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT_TO_INT - 64)) | (1 << (BKITParser.FLOAT_OF_STRING - 64)) | (1 << (BKITParser.BOOL_OF_STRING - 64)))) != 0):
                self.state = 576
                self.expr()
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 577
                    self.match(BKITParser.COMMA)
                    self.state = 578
                    self.expr()
                    self.state = 583
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 589
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_func_callContext(ParserRuleContext):

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
            return BKITParser.RULE_string_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_func_call" ):
                return visitor.visitString_func_call(self)
            else:
                return visitor.visitChildren(self)




    def string_func_call(self):

        localctx = BKITParser.String_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_string_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(BKITParser.ID)
            self.state = 592
            self.match(BKITParser.LEFT_PAREN)
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.INT_OF_FLOAT) | (1 << BKITParser.INT_OF_STRING))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT_TO_INT - 64)) | (1 << (BKITParser.FLOAT_OF_STRING - 64)) | (1 << (BKITParser.BOOL_OF_STRING - 64)))) != 0):
                self.state = 593
                self.expr()
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 594
                    self.match(BKITParser.COMMA)
                    self.state = 595
                    self.expr()
                    self.state = 600
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 606
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
        self.enterRule(localctx, 116, self.RULE_index_op)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 609
                self.int_expr1(0)
                self.state = 610
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 612
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 613
                self.int_expr1(0)
                self.state = 614
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 615
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
        self._predicates[32] = self.int_expr1_sempred
        self._predicates[33] = self.int_expr2_sempred
        self._predicates[39] = self.float_expr1_sempred
        self._predicates[40] = self.float_expr2_sempred
        self._predicates[47] = self.boolean_expr_sempred
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
         

    def boolean_expr_sempred(self, localctx:Boolean_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




