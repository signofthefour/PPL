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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3N")
        buf.write("\u0259\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13\2")
        buf.write("\3\2\7\2\u0084\n\2\f\2\16\2\u0087\13\2\3\2\3\2\7\2\u008b")
        buf.write("\n\2\f\2\16\2\u008e\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4\u009c\n\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a9\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t")
        buf.write("\u00bc\n\t\f\t\16\t\u00bf\13\t\3\t\3\t\3\t\5\t\u00c4\n")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\7\n\u00cb\n\n\f\n\16\n\u00ce\13")
        buf.write("\n\3\13\3\13\3\13\7\13\u00d3\n\13\f\13\16\13\u00d6\13")
        buf.write("\13\3\f\3\f\3\f\7\f\u00db\n\f\f\f\16\f\u00de\13\f\3\r")
        buf.write("\3\r\5\r\u00e2\n\r\3\r\3\r\3\r\5\r\u00e7\n\r\7\r\u00e9")
        buf.write("\n\r\f\r\16\r\u00ec\13\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\6\17\u00f4\n\17\r\17\16\17\u00f5\3\20\3\20\5\20\u00fa")
        buf.write("\n\20\3\21\3\21\5\21\u00fe\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\7\24\u010b\n\24\f\24")
        buf.write("\16\24\u010e\13\24\3\25\7\25\u0111\n\25\f\25\16\25\u0114")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u012c\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0137\n\27\f\27\16\27\u013a\13")
        buf.write("\27\3\27\3\27\5\27\u013e\n\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u0167\n\37\3 \3 \5 \u016b\n \3!\3!\3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\5$\u0178\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u0185\n%\3%\3%\3%\5%\u018a\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\7&\u0192\n&\f&\16&\u0195\13&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\7\'\u019d\n\'\f\'\16\'\u01a0\13\'\3(\3(\3(")
        buf.write("\5(\u01a5\n(\3)\3)\3)\3)\5)\u01ab\n)\3*\3*\5*\u01af\n")
        buf.write("*\3+\3+\3+\3+\3+\5+\u01b6\n+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u01c3\n,\3-\3-\3-\3-\3-\3-\7-\u01cb\n-\f-\16")
        buf.write("-\u01ce\13-\3.\3.\3.\3.\3.\3.\7.\u01d6\n.\f.\16.\u01d9")
        buf.write("\13.\3/\3/\3/\5/\u01de\n/\3\60\3\60\3\60\3\60\5\60\u01e4")
        buf.write("\n\60\3\61\3\61\5\61\u01e8\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u01ef\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u01fc\n\63\3\64\3\64\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\5\66\u0207\n\66\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u020d\n\67\38\38\58\u0211\n8\39\39\39")
        buf.write("\39\39\39\59\u0219\n9\3:\3:\3:\3:\3:\7:\u0220\n:\f:\16")
        buf.write(":\u0223\13:\7:\u0225\n:\f:\16:\u0228\13:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\7;\u0231\n;\f;\16;\u0234\13;\7;\u0236\n;\f;\16")
        buf.write(";\u0239\13;\3;\3;\3<\3<\3<\3<\3<\7<\u0242\n<\f<\16<\u0245")
        buf.write("\13<\7<\u0247\n<\f<\16<\u024a\13<\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\5=\u0257\n=\3=\2\6JLXZ>\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvx\2\r\3\2\f\17\4\2\4\4\f\f\4\2\4")
        buf.write("\4\r\r\4\2\4\4\17\17\3\2\61\66\4\2%%\'\'\5\2))++--\4\2")
        buf.write("&&((\4\2**,,\3\2\f\r\3\2/\60\2\u0265\2\177\3\2\2\2\4\u0091")
        buf.write("\3\2\2\2\6\u0095\3\2\2\2\b\u00a2\3\2\2\2\n\u00af\3\2\2")
        buf.write("\2\f\u00b3\3\2\2\2\16\u00b5\3\2\2\2\20\u00b7\3\2\2\2\22")
        buf.write("\u00c7\3\2\2\2\24\u00cf\3\2\2\2\26\u00d7\3\2\2\2\30\u00e1")
        buf.write("\3\2\2\2\32\u00ed\3\2\2\2\34\u00ef\3\2\2\2\36\u00f9\3")
        buf.write("\2\2\2 \u00fd\3\2\2\2\"\u00ff\3\2\2\2$\u0103\3\2\2\2&")
        buf.write("\u0107\3\2\2\2(\u0112\3\2\2\2*\u012b\3\2\2\2,\u012d\3")
        buf.write("\2\2\2.\u0141\3\2\2\2\60\u0143\3\2\2\2\62\u014f\3\2\2")
        buf.write("\2\64\u0155\3\2\2\2\66\u015b\3\2\2\28\u015f\3\2\2\2:\u0161")
        buf.write("\3\2\2\2<\u0166\3\2\2\2>\u0168\3\2\2\2@\u016c\3\2\2\2")
        buf.write("B\u0170\3\2\2\2D\u0172\3\2\2\2F\u0177\3\2\2\2H\u0189\3")
        buf.write("\2\2\2J\u018b\3\2\2\2L\u0196\3\2\2\2N\u01a4\3\2\2\2P\u01aa")
        buf.write("\3\2\2\2R\u01ae\3\2\2\2T\u01b5\3\2\2\2V\u01c2\3\2\2\2")
        buf.write("X\u01c4\3\2\2\2Z\u01cf\3\2\2\2\\\u01dd\3\2\2\2^\u01e3")
        buf.write("\3\2\2\2`\u01e7\3\2\2\2b\u01ee\3\2\2\2d\u01fb\3\2\2\2")
        buf.write("f\u01fd\3\2\2\2h\u01ff\3\2\2\2j\u0206\3\2\2\2l\u020c\3")
        buf.write("\2\2\2n\u0210\3\2\2\2p\u0218\3\2\2\2r\u021a\3\2\2\2t\u022b")
        buf.write("\3\2\2\2v\u023c\3\2\2\2x\u0256\3\2\2\2z{\5\4\3\2{|\7D")
        buf.write("\2\2|~\3\2\2\2}z\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\u0085\3\2\2\2\u0081\177\3\2\2\2\u0082")
        buf.write("\u0084\5\b\5\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3")
        buf.write("\2\2\2\u0087\u0085\3\2\2\2\u0088\u008c\5\6\4\2\u0089\u008b")
        buf.write("\5\b\5\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008f\u0090\7\2\2\3\u0090\3\3\2\2")
        buf.write("\2\u0091\u0092\7 \2\2\u0092\u0093\7B\2\2\u0093\u0094\5")
        buf.write("\30\r\2\u0094\5\3\2\2\2\u0095\u0096\7\33\2\2\u0096\u0097")
        buf.write("\7B\2\2\u0097\u009b\7\3\2\2\u0098\u0099\7\35\2\2\u0099")
        buf.write("\u009a\7B\2\2\u009a\u009c\5&\24\2\u009b\u0098\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7")
        buf.write("\20\2\2\u009e\u009f\7B\2\2\u009f\u00a0\5(\25\2\u00a0\u00a1")
        buf.write("\7\27\2\2\u00a1\7\3\2\2\2\u00a2\u00a3\7\33\2\2\u00a3\u00a4")
        buf.write("\7B\2\2\u00a4\u00a8\7\4\2\2\u00a5\u00a6\7\35\2\2\u00a6")
        buf.write("\u00a7\7B\2\2\u00a7\u00a9\5&\24\2\u00a8\u00a5\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7")
        buf.write("\20\2\2\u00ab\u00ac\7B\2\2\u00ac\u00ad\5(\25\2\u00ad\u00ae")
        buf.write("\7\27\2\2\u00ae\t\3\2\2\2\u00af\u00b0\7\4\2\2\u00b0\u00b1")
        buf.write("\7F\2\2\u00b1\u00b2\5\20\t\2\u00b2\13\3\2\2\2\u00b3\u00b4")
        buf.write("\t\2\2\2\u00b4\r\3\2\2\2\u00b5\u00b6\5\20\t\2\u00b6\17")
        buf.write("\3\2\2\2\u00b7\u00c3\7@\2\2\u00b8\u00bd\5\20\t\2\u00b9")
        buf.write("\u00ba\7E\2\2\u00ba\u00bc\5\20\t\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00c4\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c4")
        buf.write("\5\22\n\2\u00c1\u00c4\5\24\13\2\u00c2\u00c4\5\26\f\2\u00c3")
        buf.write("\u00b8\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\7")
        buf.write("A\2\2\u00c6\21\3\2\2\2\u00c7\u00cc\t\3\2\2\u00c8\u00c9")
        buf.write("\7E\2\2\u00c9\u00cb\t\3\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\23\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d4\t\4")
        buf.write("\2\2\u00d0\u00d1\7E\2\2\u00d1\u00d3\t\4\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\25\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7")
        buf.write("\u00dc\t\5\2\2\u00d8\u00d9\7E\2\2\u00d9\u00db\t\5\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\27\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e2\5\36\20\2\u00e0\u00e2\5 \21\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00ea\3\2\2\2")
        buf.write("\u00e3\u00e6\7E\2\2\u00e4\u00e7\5\36\20\2\u00e5\u00e7")
        buf.write("\5 \21\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\31\3\2")
        buf.write("\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\7\4\2\2\u00ee\33")
        buf.write("\3\2\2\2\u00ef\u00f3\7\4\2\2\u00f0\u00f1\7>\2\2\u00f1")
        buf.write("\u00f2\7\f\2\2\u00f2\u00f4\7?\2\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\35\3\2\2\2\u00f7\u00fa\5\32\16\2\u00f8\u00fa")
        buf.write("\5\34\17\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa")
        buf.write("\37\3\2\2\2\u00fb\u00fe\5\"\22\2\u00fc\u00fe\5$\23\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe!\3\2\2\2\u00ff")
        buf.write("\u0100\5\34\17\2\u0100\u0101\7F\2\2\u0101\u0102\5\20\t")
        buf.write("\2\u0102#\3\2\2\2\u0103\u0104\5\32\16\2\u0104\u0105\7")
        buf.write("F\2\2\u0105\u0106\5\f\7\2\u0106%\3\2\2\2\u0107\u010c\5")
        buf.write("\36\20\2\u0108\u0109\7E\2\2\u0109\u010b\5\36\20\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d\'\3\2\2\2\u010e\u010c\3\2\2")
        buf.write("\2\u010f\u0111\5*\26\2\u0110\u010f\3\2\2\2\u0111\u0114")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write(")\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u012c\5,\27\2\u0116")
        buf.write("\u012c\5\60\31\2\u0117\u0118\5.\30\2\u0118\u0119\7D\2")
        buf.write("\2\u0119\u012c\3\2\2\2\u011a\u012c\5\62\32\2\u011b\u012c")
        buf.write("\5\64\33\2\u011c\u011d\5\66\34\2\u011d\u011e\7D\2\2\u011e")
        buf.write("\u012c\3\2\2\2\u011f\u0120\58\35\2\u0120\u0121\7D\2\2")
        buf.write("\u0121\u012c\3\2\2\2\u0122\u0123\5:\36\2\u0123\u0124\7")
        buf.write("D\2\2\u0124\u012c\3\2\2\2\u0125\u0126\5<\37\2\u0126\u0127")
        buf.write("\7D\2\2\u0127\u012c\3\2\2\2\u0128\u0129\5> \2\u0129\u012a")
        buf.write("\7D\2\2\u012a\u012c\3\2\2\2\u012b\u0115\3\2\2\2\u012b")
        buf.write("\u0116\3\2\2\2\u012b\u0117\3\2\2\2\u012b\u011a\3\2\2\2")
        buf.write("\u012b\u011b\3\2\2\2\u012b\u011c\3\2\2\2\u012b\u011f\3")
        buf.write("\2\2\2\u012b\u0122\3\2\2\2\u012b\u0125\3\2\2\2\u012b\u0128")
        buf.write("\3\2\2\2\u012c+\3\2\2\2\u012d\u012e\7\34\2\2\u012e\u012f")
        buf.write("\5H%\2\u012f\u0130\7\37\2\2\u0130\u0138\5(\25\2\u0131")
        buf.write("\u0132\7\25\2\2\u0132\u0133\5H%\2\u0133\u0134\7\37\2\2")
        buf.write("\u0134\u0135\5(\25\2\u0135\u0137\3\2\2\2\u0136\u0131\3")
        buf.write("\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013d\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013c\7\24\2\2\u013c\u013e\5(\25\2\u013d\u013b\3\2\2")
        buf.write("\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140")
        buf.write("\7\26\2\2\u0140-\3\2\2\2\u0141\u0142\5\4\3\2\u0142/\3")
        buf.write("\2\2\2\u0143\u0144\7\32\2\2\u0144\u0145\7<\2\2\u0145\u0146")
        buf.write("\5@!\2\u0146\u0147\7E\2\2\u0147\u0148\5B\"\2\u0148\u0149")
        buf.write("\7E\2\2\u0149\u014a\5D#\2\u014a\u014b\7=\2\2\u014b\u014c")
        buf.write("\7\23\2\2\u014c\u014d\5(\25\2\u014d\u014e\7\30\2\2\u014e")
        buf.write("\61\3\2\2\2\u014f\u0150\7!\2\2\u0150\u0151\5h\65\2\u0151")
        buf.write("\u0152\7\23\2\2\u0152\u0153\5(\25\2\u0153\u0154\7\31\2")
        buf.write("\2\u0154\63\3\2\2\2\u0155\u0156\7\23\2\2\u0156\u0157\5")
        buf.write("(\25\2\u0157\u0158\7!\2\2\u0158\u0159\5h\65\2\u0159\u015a")
        buf.write("\7$\2\2\u015a\65\3\2\2\2\u015b\u015c\5\36\20\2\u015c\u015d")
        buf.write("\7F\2\2\u015d\u015e\5F$\2\u015e\67\3\2\2\2\u015f\u0160")
        buf.write("\7\21\2\2\u01609\3\2\2\2\u0161\u0162\7\22\2\2\u0162;\3")
        buf.write("\2\2\2\u0163\u0167\5r:\2\u0164\u0167\5t;\2\u0165\u0167")
        buf.write("\5v<\2\u0166\u0163\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167=\3\2\2\2\u0168\u016a\7\36\2\2\u0169\u016b")
        buf.write("\5F$\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b?")
        buf.write("\3\2\2\2\u016c\u016d\5\32\16\2\u016d\u016e\7F\2\2\u016e")
        buf.write("\u016f\5J&\2\u016fA\3\2\2\2\u0170\u0171\5H%\2\u0171C\3")
        buf.write("\2\2\2\u0172\u0173\5\66\34\2\u0173E\3\2\2\2\u0174\u0178")
        buf.write("\5J&\2\u0175\u0178\5X-\2\u0176\u0178\5j\66\2\u0177\u0174")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("G\3\2\2\2\u0179\u017a\5J&\2\u017a\u017b\t\6\2\2\u017b")
        buf.write("\u017c\5J&\2\u017c\u018a\3\2\2\2\u017d\u0184\5X-\2\u017e")
        buf.write("\u0185\3\2\2\2\u017f\u0185\7\67\2\2\u0180\u0185\78\2\2")
        buf.write("\u0181\u0185\79\2\2\u0182\u0185\7:\2\2\u0183\u0185\7;")
        buf.write("\2\2\u0184\u017e\3\2\2\2\u0184\u017f\3\2\2\2\u0184\u0180")
        buf.write("\3\2\2\2\u0184\u0181\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\5X-\2\u0187")
        buf.write("\u018a\3\2\2\2\u0188\u018a\5h\65\2\u0189\u0179\3\2\2\2")
        buf.write("\u0189\u017d\3\2\2\2\u0189\u0188\3\2\2\2\u018aI\3\2\2")
        buf.write("\2\u018b\u018c\b&\1\2\u018c\u018d\5L\'\2\u018d\u0193\3")
        buf.write("\2\2\2\u018e\u018f\f\4\2\2\u018f\u0190\t\7\2\2\u0190\u0192")
        buf.write("\5L\'\2\u0191\u018e\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194K\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\b\'\1\2\u0197\u0198\5N(\2\u0198")
        buf.write("\u019e\3\2\2\2\u0199\u019a\f\4\2\2\u019a\u019b\t\b\2\2")
        buf.write("\u019b\u019d\5N(\2\u019c\u0199\3\2\2\2\u019d\u01a0\3\2")
        buf.write("\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019fM\3")
        buf.write("\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\7\'\2\2\u01a2\u01a5")
        buf.write("\5N(\2\u01a3\u01a5\5P)\2\u01a4\u01a1\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5O\3\2\2\2\u01a6\u01a7\5R*\2\u01a7\u01a8")
        buf.write("\5x=\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\5R*\2\u01aa\u01a6")
        buf.write("\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abQ\3\2\2\2\u01ac\u01af")
        buf.write("\5r:\2\u01ad\u01af\5T+\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01afS\3\2\2\2\u01b0\u01b6\5V,\2\u01b1\u01b2")
        buf.write("\7<\2\2\u01b2\u01b3\5J&\2\u01b3\u01b4\7=\2\2\u01b4\u01b6")
        buf.write("\3\2\2\2\u01b5\u01b0\3\2\2\2\u01b5\u01b1\3\2\2\2\u01b6")
        buf.write("U\3\2\2\2\u01b7\u01c3\7\f\2\2\u01b8\u01c3\5\32\16\2\u01b9")
        buf.write("\u01ba\7G\2\2\u01ba\u01bb\7<\2\2\u01bb\u01bc\5X-\2\u01bc")
        buf.write("\u01bd\7=\2\2\u01bd\u01c3\3\2\2\2\u01be\u01bf\7H\2\2\u01bf")
        buf.write("\u01c0\7<\2\2\u01c0\u01c1\7\17\2\2\u01c1\u01c3\7=\2\2")
        buf.write("\u01c2\u01b7\3\2\2\2\u01c2\u01b8\3\2\2\2\u01c2\u01b9\3")
        buf.write("\2\2\2\u01c2\u01be\3\2\2\2\u01c3W\3\2\2\2\u01c4\u01c5")
        buf.write("\b-\1\2\u01c5\u01c6\5Z.\2\u01c6\u01cc\3\2\2\2\u01c7\u01c8")
        buf.write("\f\4\2\2\u01c8\u01c9\t\t\2\2\u01c9\u01cb\5Z.\2\u01ca\u01c7")
        buf.write("\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cdY\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf")
        buf.write("\u01d0\b.\1\2\u01d0\u01d1\5\\/\2\u01d1\u01d7\3\2\2\2\u01d2")
        buf.write("\u01d3\f\4\2\2\u01d3\u01d4\t\n\2\2\u01d4\u01d6\5\\/\2")
        buf.write("\u01d5\u01d2\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8[\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01da\u01db\7(\2\2\u01db\u01de\5\\/\2\u01dc\u01de")
        buf.write("\5^\60\2\u01dd\u01da\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("]\3\2\2\2\u01df\u01e0\5`\61\2\u01e0\u01e1\5x=\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e4\5`\61\2\u01e3\u01df\3\2\2\2")
        buf.write("\u01e3\u01e2\3\2\2\2\u01e4_\3\2\2\2\u01e5\u01e8\5t;\2")
        buf.write("\u01e6\u01e8\5b\62\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3")
        buf.write("\2\2\2\u01e8a\3\2\2\2\u01e9\u01ef\5d\63\2\u01ea\u01eb")
        buf.write("\7<\2\2\u01eb\u01ec\5X-\2\u01ec\u01ed\7=\2\2\u01ed\u01ef")
        buf.write("\3\2\2\2\u01ee\u01e9\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ef")
        buf.write("c\3\2\2\2\u01f0\u01fc\7\r\2\2\u01f1\u01fc\5\32\16\2\u01f2")
        buf.write("\u01f3\7I\2\2\u01f3\u01f4\7<\2\2\u01f4\u01f5\5J&\2\u01f5")
        buf.write("\u01f6\7=\2\2\u01f6\u01fc\3\2\2\2\u01f7\u01f8\7J\2\2\u01f8")
        buf.write("\u01f9\7<\2\2\u01f9\u01fa\7\17\2\2\u01fa\u01fc\7=\2\2")
        buf.write("\u01fb\u01f0\3\2\2\2\u01fb\u01f1\3\2\2\2\u01fb\u01f2\3")
        buf.write("\2\2\2\u01fb\u01f7\3\2\2\2\u01fce\3\2\2\2\u01fd\u01fe")
        buf.write("\t\13\2\2\u01feg\3\2\2\2\u01ff\u0200\5j\66\2\u0200\u0201")
        buf.write("\t\f\2\2\u0201\u0202\5j\66\2\u0202i\3\2\2\2\u0203\u0204")
        buf.write("\7.\2\2\u0204\u0207\5l\67\2\u0205\u0207\5l\67\2\u0206")
        buf.write("\u0203\3\2\2\2\u0206\u0205\3\2\2\2\u0207k\3\2\2\2\u0208")
        buf.write("\u0209\5n8\2\u0209\u020a\5x=\2\u020a\u020d\3\2\2\2\u020b")
        buf.write("\u020d\5n8\2\u020c\u0208\3\2\2\2\u020c\u020b\3\2\2\2\u020d")
        buf.write("m\3\2\2\2\u020e\u0211\5v<\2\u020f\u0211\5p9\2\u0210\u020e")
        buf.write("\3\2\2\2\u0210\u020f\3\2\2\2\u0211o\3\2\2\2\u0212\u0219")
        buf.write("\7\16\2\2\u0213\u0219\5\36\20\2\u0214\u0215\7K\2\2\u0215")
        buf.write("\u0216\7<\2\2\u0216\u0217\7\17\2\2\u0217\u0219\7=\2\2")
        buf.write("\u0218\u0212\3\2\2\2\u0218\u0213\3\2\2\2\u0218\u0214\3")
        buf.write("\2\2\2\u0219q\3\2\2\2\u021a\u021b\7\4\2\2\u021b\u0226")
        buf.write("\7<\2\2\u021c\u0221\5F$\2\u021d\u021e\7E\2\2\u021e\u0220")
        buf.write("\5F$\2\u021f\u021d\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f")
        buf.write("\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0224\u021c\3\2\2\2\u0225\u0228\3\2\2\2")
        buf.write("\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\3")
        buf.write("\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a\7=\2\2\u022as\3")
        buf.write("\2\2\2\u022b\u022c\7\4\2\2\u022c\u0237\7<\2\2\u022d\u0232")
        buf.write("\5F$\2\u022e\u022f\7E\2\2\u022f\u0231\5F$\2\u0230\u022e")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2")
        buf.write("\u0235\u022d\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u023b\7=\2\2\u023bu\3\2\2\2\u023c\u023d")
        buf.write("\7\4\2\2\u023d\u0248\7<\2\2\u023e\u0243\5F$\2\u023f\u0240")
        buf.write("\7E\2\2\u0240\u0242\5F$\2\u0241\u023f\3\2\2\2\u0242\u0245")
        buf.write("\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u023e\3\2\2\2")
        buf.write("\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3")
        buf.write("\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c")
        buf.write("\7=\2\2\u024cw\3\2\2\2\u024d\u024e\7>\2\2\u024e\u024f")
        buf.write("\5J&\2\u024f\u0250\7?\2\2\u0250\u0257\3\2\2\2\u0251\u0252")
        buf.write("\7>\2\2\u0252\u0253\5J&\2\u0253\u0254\7?\2\2\u0254\u0255")
        buf.write("\5x=\2\u0255\u0257\3\2\2\2\u0256\u024d\3\2\2\2\u0256\u0251")
        buf.write("\3\2\2\2\u0257y\3\2\2\2\65\177\u0085\u008c\u009b\u00a8")
        buf.write("\u00bd\u00c3\u00cc\u00d4\u00dc\u00e1\u00e6\u00ea\u00f5")
        buf.write("\u00f9\u00fd\u010c\u0112\u012b\u0138\u013d\u0166\u016a")
        buf.write("\u0177\u0184\u0189\u0193\u019e\u01a4\u01aa\u01ae\u01b5")
        buf.write("\u01c2\u01cc\u01d7\u01dd\u01e3\u01e7\u01ee\u01fb\u0206")
        buf.write("\u020c\u0210\u0218\u0221\u0226\u0232\u0237\u0243\u0248")
        buf.write("\u0256")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndIf.'", "'EndBody.'", "'EndFor.'", 
                     "'EndWhile.'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'EndDo.'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", 
                     "','", "'='", "'int_of_float'", "'int_of_string'", 
                     "'float_to_int'", "'float_of_string'", "'bool_of_string'", 
                     "'string_of_bool'", "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR", "WS", "ERROR_DEC", "Integer_literal", 
                      "Float_literal", "Boolean_literal", "String_literal", 
                      "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                      "ENDIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", 
                      "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", 
                      "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", 
                      "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", 
                      "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
                      "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                      "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "INT_OF_FLOAT", 
                      "INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", 
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
    RULE_int_array = 8
    RULE_float_array = 9
    RULE_string_array = 10
    RULE_var_list = 11
    RULE_scalar_var = 12
    RULE_composite_var = 13
    RULE_var_non_init = 14
    RULE_var_init = 15
    RULE_composite_init = 16
    RULE_primitive_init = 17
    RULE_params_list = 18
    RULE_stmt_list = 19
    RULE_stmt = 20
    RULE_if_stmt = 21
    RULE_var_declare_stmt = 22
    RULE_for_stmt = 23
    RULE_while_stmt = 24
    RULE_dowhile_stmt = 25
    RULE_assign_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_call_stmt = 29
    RULE_return_stmt = 30
    RULE_init_for = 31
    RULE_con_for = 32
    RULE_update_for = 33
    RULE_expr = 34
    RULE_boolean_type_expr = 35
    RULE_int_expr1 = 36
    RULE_int_expr2 = 37
    RULE_int_expr3 = 38
    RULE_int_expr4 = 39
    RULE_int_expr5 = 40
    RULE_int_expr6 = 41
    RULE_int_operand = 42
    RULE_float_expr1 = 43
    RULE_float_expr2 = 44
    RULE_float_expr3 = 45
    RULE_float_expr4 = 46
    RULE_float_expr5 = 47
    RULE_float_expr6 = 48
    RULE_float_operand = 49
    RULE_constant = 50
    RULE_boolean_expr = 51
    RULE_boolean_expr1 = 52
    RULE_boolean_expr2 = 53
    RULE_boolean_expr3 = 54
    RULE_boolean_expr4 = 55
    RULE_int_func_call = 56
    RULE_float_func_call = 57
    RULE_boolean_func_call = 58
    RULE_index_op = 59

    ruleNames =  [ "program", "var_declare", "main_function_declare", "function_declare", 
                   "array", "primitive_data", "composite_data", "array_lit", 
                   "int_array", "float_array", "string_array", "var_list", 
                   "scalar_var", "composite_var", "var_non_init", "var_init", 
                   "composite_init", "primitive_init", "params_list", "stmt_list", 
                   "stmt", "if_stmt", "var_declare_stmt", "for_stmt", "while_stmt", 
                   "dowhile_stmt", "assign_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "init_for", "con_for", "update_for", 
                   "expr", "boolean_type_expr", "int_expr1", "int_expr2", 
                   "int_expr3", "int_expr4", "int_expr5", "int_expr6", "int_operand", 
                   "float_expr1", "float_expr2", "float_expr3", "float_expr4", 
                   "float_expr5", "float_expr6", "float_operand", "constant", 
                   "boolean_expr", "boolean_expr1", "boolean_expr2", "boolean_expr3", 
                   "boolean_expr4", "int_func_call", "float_func_call", 
                   "boolean_func_call", "index_op" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    ILLEGAL_ESCAPE=3
    UNCLOSE_STRING=4
    COMMENT=5
    UNTERMINATED_COMMENT=6
    ERROR_CHAR=7
    WS=8
    ERROR_DEC=9
    Integer_literal=10
    Float_literal=11
    Boolean_literal=12
    String_literal=13
    BODY=14
    BREAK=15
    CONTINUE=16
    DO=17
    ELSE=18
    ELSEIF=19
    ENDIF=20
    ENDBODY=21
    ENDFOR=22
    ENDWHILE=23
    FOR=24
    FUNCTION=25
    IF=26
    PARAMETER=27
    RETURN=28
    THEN=29
    VAR=30
    WHILE=31
    TRUE=32
    FALSE=33
    ENDDO=34
    PLUS_INT=35
    PLUS_FLOAT=36
    MINUS_INT=37
    MINUS_FLOAT=38
    STAR_INT=39
    STAR_FLOAT=40
    DIV_INT=41
    DIV_FLOAT=42
    MOD=43
    NOT=44
    AND=45
    OR=46
    EQUAL=47
    NOT_EQUAL_INT=48
    LESS_INT=49
    GREATER_INT=50
    LESS_OR_EQUAL_INT=51
    GREATER_OR_EQUAL_INT=52
    NOT_EQUAL_FLOAT=53
    LESS_FLOAT=54
    GREATER_FLOAT=55
    LESS_OR_EQUAL_FLOAT=56
    GREATER_OR_EQUAL_FLOAT=57
    LEFT_PAREN=58
    RIGHT_PAREN=59
    LEFT_BRACKET=60
    RIGHT_BRACKET=61
    LEFT_BRACE=62
    RIGHT_BRACE=63
    COLON=64
    DOT=65
    SEMI=66
    COMMA=67
    ASSIGN=68
    INT_OF_FLOAT=69
    INT_OF_STRING=70
    FLOAT_TO_INT=71
    FLOAT_OF_STRING=72
    BOOL_OF_STRING=73
    STRING_OF_BOOL=74
    STRING_OF_INT=75
    STRING_OF_FLOAT=76

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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 120
                self.var_declare()
                self.state = 121
                self.match(BKITParser.SEMI)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 128
                    self.function_declare() 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 134
            self.main_function_declare()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 135
                self.function_declare()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
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
            self.state = 143
            self.match(BKITParser.VAR)
            self.state = 144
            self.match(BKITParser.COLON)
            self.state = 145
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
            self.state = 147
            self.match(BKITParser.FUNCTION)
            self.state = 148
            self.match(BKITParser.COLON)
            self.state = 149
            self.match(BKITParser.T__0)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 150
                self.match(BKITParser.PARAMETER)
                self.state = 151
                self.match(BKITParser.COLON)
                self.state = 152
                self.params_list()


            self.state = 155
            self.match(BKITParser.BODY)
            self.state = 156
            self.match(BKITParser.COLON)
            self.state = 157
            self.stmt_list()
            self.state = 158
            self.match(BKITParser.ENDBODY)
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
            self.state = 160
            self.match(BKITParser.FUNCTION)
            self.state = 161
            self.match(BKITParser.COLON)
            self.state = 162
            self.match(BKITParser.ID)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 163
                self.match(BKITParser.PARAMETER)
                self.state = 164
                self.match(BKITParser.COLON)
                self.state = 165
                self.params_list()


            self.state = 168
            self.match(BKITParser.BODY)
            self.state = 169
            self.match(BKITParser.COLON)
            self.state = 170
            self.stmt_list()
            self.state = 171
            self.match(BKITParser.ENDBODY)
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
            self.state = 173
            self.match(BKITParser.ID)
            self.state = 174
            self.match(BKITParser.ASSIGN)
            self.state = 175
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
            self.state = 177
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
            self.state = 179
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

        def array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_litContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_litContext,i)


        def int_array(self):
            return self.getTypedRuleContext(BKITParser.Int_arrayContext,0)


        def float_array(self):
            return self.getTypedRuleContext(BKITParser.Float_arrayContext,0)


        def string_array(self):
            return self.getTypedRuleContext(BKITParser.String_arrayContext,0)


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
            self.state = 181
            self.match(BKITParser.LEFT_BRACE)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 182
                self.array_lit()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 183
                    self.match(BKITParser.COMMA)
                    self.state = 184
                    self.array_lit()
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 190
                self.int_array()
                pass

            elif la_ == 3:
                self.state = 191
                self.float_array()
                pass

            elif la_ == 4:
                self.state = 192
                self.string_array()
                pass


            self.state = 195
            self.match(BKITParser.RIGHT_BRACE)
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

        def Integer_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer_literal)
            else:
                return self.getToken(BKITParser.Integer_literal, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_int_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_array" ):
                return visitor.visitInt_array(self)
            else:
                return visitor.visitChildren(self)




    def int_array(self):

        localctx = BKITParser.Int_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_int_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==BKITParser.ID or _la==BKITParser.Integer_literal):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 198
                self.match(BKITParser.COMMA)
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==BKITParser.ID or _la==BKITParser.Integer_literal):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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


    class Float_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Float_literal)
            else:
                return self.getToken(BKITParser.Float_literal, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_float_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_array" ):
                return visitor.visitFloat_array(self)
            else:
                return visitor.visitChildren(self)




    def float_array(self):

        localctx = BKITParser.Float_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_float_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            _la = self._input.LA(1)
            if not(_la==BKITParser.ID or _la==BKITParser.Float_literal):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 206
                self.match(BKITParser.COMMA)
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==BKITParser.ID or _la==BKITParser.Float_literal):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def String_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.String_literal)
            else:
                return self.getToken(BKITParser.String_literal, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_string_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_array" ):
                return visitor.visitString_array(self)
            else:
                return visitor.visitChildren(self)




    def string_array(self):

        localctx = BKITParser.String_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_string_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==BKITParser.ID or _la==BKITParser.String_literal):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 214
                self.match(BKITParser.COMMA)
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==BKITParser.ID or _la==BKITParser.String_literal):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 22, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 221
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 222
                self.var_init()
                pass


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 225
                self.match(BKITParser.COMMA)
                self.state = 228
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 226
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 227
                    self.var_init()
                    pass


                self.state = 234
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
        self.enterRule(localctx, 24, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
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

        def Integer_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer_literal)
            else:
                return self.getToken(BKITParser.Integer_literal, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(BKITParser.ID)
            self.state = 241 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 238
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 239
                    self.match(BKITParser.Integer_literal)
                    self.state = 240
                    self.match(BKITParser.RIGHT_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 243 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_var_non_init)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
        self.enterRule(localctx, 30, self.RULE_var_init)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.composite_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        self.enterRule(localctx, 32, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.composite_var()
            self.state = 254
            self.match(BKITParser.ASSIGN)
            self.state = 255
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
        self.enterRule(localctx, 34, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.scalar_var()
            self.state = 258
            self.match(BKITParser.ASSIGN)
            self.state = 259
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
        self.enterRule(localctx, 36, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.var_non_init()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 262
                self.match(BKITParser.COMMA)
                self.state = 263
                self.var_non_init()
                self.state = 268
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
        self.enterRule(localctx, 38, self.RULE_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.stmt() 
                self.state = 274
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.var_declare_stmt()
                self.state = 278
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.dowhile_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.assign_stmt()
                self.state = 283
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.break_stmt()
                self.state = 286
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 288
                self.continue_stmt()
                self.state = 289
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 291
                self.call_stmt()
                self.state = 292
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 294
                self.return_stmt()
                self.state = 295
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
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.IF)
            self.state = 300
            self.boolean_type_expr()
            self.state = 301
            self.match(BKITParser.THEN)
            self.state = 302
            self.stmt_list()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 303
                self.match(BKITParser.ELSEIF)
                self.state = 304
                self.boolean_type_expr()
                self.state = 305
                self.match(BKITParser.THEN)
                self.state = 306
                self.stmt_list()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 313
                self.match(BKITParser.ELSE)
                self.state = 314
                self.stmt_list()


            self.state = 317
            self.match(BKITParser.ENDIF)
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
        self.enterRule(localctx, 44, self.RULE_var_declare_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
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

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(BKITParser.FOR)
            self.state = 322
            self.match(BKITParser.LEFT_PAREN)
            self.state = 323
            self.init_for()
            self.state = 324
            self.match(BKITParser.COMMA)
            self.state = 325
            self.con_for()
            self.state = 326
            self.match(BKITParser.COMMA)
            self.state = 327
            self.update_for()
            self.state = 328
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 329
            self.match(BKITParser.DO)
            self.state = 330
            self.stmt_list()
            self.state = 331
            self.match(BKITParser.ENDFOR)
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

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(BKITParser.WHILE)
            self.state = 334
            self.boolean_expr()
            self.state = 335
            self.match(BKITParser.DO)
            self.state = 336
            self.stmt_list()
            self.state = 337
            self.match(BKITParser.ENDWHILE)
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

        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stmt" ):
                return visitor.visitDowhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BKITParser.DO)
            self.state = 340
            self.stmt_list()
            self.state = 341
            self.match(BKITParser.WHILE)
            self.state = 342
            self.boolean_expr()
            self.state = 343
            self.match(BKITParser.ENDDO)
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
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.var_non_init()
            self.state = 346
            self.match(BKITParser.ASSIGN)
            self.state = 347
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
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
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
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
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
        self.enterRule(localctx, 58, self.RULE_call_stmt)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.float_func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
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
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(BKITParser.RETURN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (BKITParser.INT_OF_FLOAT - 69)) | (1 << (BKITParser.INT_OF_STRING - 69)) | (1 << (BKITParser.FLOAT_TO_INT - 69)) | (1 << (BKITParser.FLOAT_OF_STRING - 69)) | (1 << (BKITParser.BOOL_OF_STRING - 69)))) != 0):
                self.state = 359
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
        self.enterRule(localctx, 62, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.scalar_var()
            self.state = 363
            self.match(BKITParser.ASSIGN)
            self.state = 364
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
        self.enterRule(localctx, 64, self.RULE_con_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
        self.enterRule(localctx, 66, self.RULE_update_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 68, self.RULE_expr)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
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
        self.enterRule(localctx, 70, self.RULE_boolean_type_expr)
        self._la = 0 # Token type
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.int_expr1(0)
                self.state = 376
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL_INT) | (1 << BKITParser.LESS_INT) | (1 << BKITParser.GREATER_INT) | (1 << BKITParser.LESS_OR_EQUAL_INT) | (1 << BKITParser.GREATER_OR_EQUAL_INT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 377
                self.int_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.float_expr1(0)
                self.state = 386
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.MINUS_FLOAT, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                    pass
                elif token in [BKITParser.NOT_EQUAL_FLOAT]:
                    self.state = 381
                    self.match(BKITParser.NOT_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.LESS_FLOAT]:
                    self.state = 382
                    self.match(BKITParser.LESS_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_FLOAT]:
                    self.state = 383
                    self.match(BKITParser.GREATER_FLOAT)
                    pass
                elif token in [BKITParser.LESS_OR_EQUAL_FLOAT]:
                    self.state = 384
                    self.match(BKITParser.LESS_OR_EQUAL_FLOAT)
                    pass
                elif token in [BKITParser.GREATER_OR_EQUAL_FLOAT]:
                    self.state = 385
                    self.match(BKITParser.GREATER_OR_EQUAL_FLOAT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 388
                self.float_expr1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_int_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.int_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr1)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_INT or _la==BKITParser.MINUS_INT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.int_expr2(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_int_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.int_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Int_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expr2)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.STAR_INT) | (1 << BKITParser.DIV_INT) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 409
                    self.int_expr3() 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_int_expr3)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(BKITParser.MINUS_INT)
                self.state = 416
                self.int_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.Integer_literal, BKITParser.LEFT_PAREN, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
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
        self.enterRule(localctx, 78, self.RULE_int_expr4)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.int_expr5()
                self.state = 421
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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
        self.enterRule(localctx, 80, self.RULE_int_expr5)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.int_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
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
        self.enterRule(localctx, 82, self.RULE_int_expr6)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.Integer_literal, BKITParser.INT_OF_FLOAT, BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.int_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(BKITParser.LEFT_PAREN)
                self.state = 432
                self.int_expr1(0)
                self.state = 433
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
        self.enterRule(localctx, 84, self.RULE_int_operand)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Integer_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(BKITParser.Integer_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.scalar_var()
                pass
            elif token in [BKITParser.INT_OF_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.match(BKITParser.INT_OF_FLOAT)
                self.state = 440
                self.match(BKITParser.LEFT_PAREN)
                self.state = 441
                self.float_expr1(0)
                self.state = 442
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.INT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.match(BKITParser.INT_OF_STRING)
                self.state = 445
                self.match(BKITParser.LEFT_PAREN)
                self.state = 446
                self.match(BKITParser.String_literal)
                self.state = 447
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_float_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.float_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr1)
                    self.state = 453
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 454
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.PLUS_FLOAT or _la==BKITParser.MINUS_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 455
                    self.float_expr2(0) 
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_float_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.float_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Float_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expr2)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 465
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.STAR_FLOAT or _la==BKITParser.DIV_FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 466
                    self.float_expr3() 
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_float_expr3)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(BKITParser.MINUS_FLOAT)
                self.state = 473
                self.float_expr3()
                pass
            elif token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.LEFT_PAREN, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
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
        self.enterRule(localctx, 92, self.RULE_float_expr4)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.float_expr5()
                self.state = 478
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
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
        self.enterRule(localctx, 94, self.RULE_float_expr5)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.float_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
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
        self.enterRule(localctx, 96, self.RULE_float_expr6)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.Float_literal, BKITParser.FLOAT_TO_INT, BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.float_operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
                self.match(BKITParser.LEFT_PAREN)
                self.state = 489
                self.float_expr1(0)
                self.state = 490
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
        self.enterRule(localctx, 98, self.RULE_float_operand)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Float_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(BKITParser.Float_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.scalar_var()
                pass
            elif token in [BKITParser.FLOAT_TO_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(BKITParser.FLOAT_TO_INT)
                self.state = 497
                self.match(BKITParser.LEFT_PAREN)
                self.state = 498
                self.int_expr1(0)
                self.state = 499
                self.match(BKITParser.RIGHT_PAREN)
                pass
            elif token in [BKITParser.FLOAT_OF_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 501
                self.match(BKITParser.FLOAT_OF_STRING)
                self.state = 502
                self.match(BKITParser.LEFT_PAREN)
                self.state = 503
                self.match(BKITParser.String_literal)
                self.state = 504
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
        self.enterRule(localctx, 100, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
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
        self.enterRule(localctx, 102, self.RULE_boolean_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.boolean_expr1()
            self.state = 510
            _la = self._input.LA(1)
            if not(_la==BKITParser.AND or _la==BKITParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 511
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
        self.enterRule(localctx, 104, self.RULE_boolean_expr1)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(BKITParser.NOT)
                self.state = 514
                self.boolean_expr2()
                pass
            elif token in [BKITParser.ID, BKITParser.Boolean_literal, BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
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
        self.enterRule(localctx, 106, self.RULE_boolean_expr2)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.boolean_expr3()
                self.state = 519
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
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
        self.enterRule(localctx, 108, self.RULE_boolean_expr3)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.boolean_func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
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
        self.enterRule(localctx, 110, self.RULE_boolean_expr4)
        try:
            self.state = 534
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.Boolean_literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(BKITParser.Boolean_literal)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.var_non_init()
                pass
            elif token in [BKITParser.BOOL_OF_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 530
                self.match(BKITParser.BOOL_OF_STRING)
                self.state = 531
                self.match(BKITParser.LEFT_PAREN)
                self.state = 532
                self.match(BKITParser.String_literal)
                self.state = 533
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
        self.enterRule(localctx, 112, self.RULE_int_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(BKITParser.ID)
            self.state = 537
            self.match(BKITParser.LEFT_PAREN)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (BKITParser.INT_OF_FLOAT - 69)) | (1 << (BKITParser.INT_OF_STRING - 69)) | (1 << (BKITParser.FLOAT_TO_INT - 69)) | (1 << (BKITParser.FLOAT_OF_STRING - 69)) | (1 << (BKITParser.BOOL_OF_STRING - 69)))) != 0):
                self.state = 538
                self.expr()
                self.state = 543
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 539
                    self.match(BKITParser.COMMA)
                    self.state = 540
                    self.expr()
                    self.state = 545
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 550
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 551
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
        self.enterRule(localctx, 114, self.RULE_float_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(BKITParser.ID)
            self.state = 554
            self.match(BKITParser.LEFT_PAREN)
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (BKITParser.INT_OF_FLOAT - 69)) | (1 << (BKITParser.INT_OF_STRING - 69)) | (1 << (BKITParser.FLOAT_TO_INT - 69)) | (1 << (BKITParser.FLOAT_OF_STRING - 69)) | (1 << (BKITParser.BOOL_OF_STRING - 69)))) != 0):
                self.state = 555
                self.expr()
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 556
                    self.match(BKITParser.COMMA)
                    self.state = 557
                    self.expr()
                    self.state = 562
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 568
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
        self.enterRule(localctx, 116, self.RULE_boolean_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(BKITParser.ID)
            self.state = 571
            self.match(BKITParser.LEFT_PAREN)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (BKITParser.INT_OF_FLOAT - 69)) | (1 << (BKITParser.INT_OF_STRING - 69)) | (1 << (BKITParser.FLOAT_TO_INT - 69)) | (1 << (BKITParser.FLOAT_OF_STRING - 69)) | (1 << (BKITParser.BOOL_OF_STRING - 69)))) != 0):
                self.state = 572
                self.expr()
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 573
                    self.match(BKITParser.COMMA)
                    self.state = 574
                    self.expr()
                    self.state = 579
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 585
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
        self.enterRule(localctx, 118, self.RULE_index_op)
        try:
            self.state = 596
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 588
                self.int_expr1(0)
                self.state = 589
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 592
                self.int_expr1(0)
                self.state = 593
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 594
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
        self._predicates[36] = self.int_expr1_sempred
        self._predicates[37] = self.int_expr2_sempred
        self._predicates[43] = self.float_expr1_sempred
        self._predicates[44] = self.float_expr2_sempred
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
         




