# Generated from /home/nguyendat/Documents/projects/PPL/SyntaxAnalysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u022b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\7\3\u00b1\n\3\f\3\16\3\u00b4")
        buf.write("\13\3\3\4\3\4\7\4\u00b8\n\4\f\4\16\4\u00bb\13\4\3\4\3")
        buf.write("\4\3\5\3\5\7\5\u00c1\n\5\f\5\16\5\u00c4\13\5\3\5\5\5\u00c7")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00cf\n\6\f\6\16\6\u00d2")
        buf.write("\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00dd\n")
        buf.write("\7\f\7\16\7\u00e0\13\7\3\7\3\7\3\b\3\b\3\t\6\t\u00e7\n")
        buf.write("\t\r\t\16\t\u00e8\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\5\r\u00f5\n\r\3\16\3\16\5\16\u00f9\n\16\3\16\6")
        buf.write("\16\u00fc\n\16\r\16\16\16\u00fd\3\17\3\17\7\17\u0102\n")
        buf.write("\17\f\17\16\17\u0105\13\17\3\20\6\20\u0108\n\20\r\20\16")
        buf.write("\20\u0109\3\20\3\20\5\20\u010e\n\20\3\20\5\20\u0111\n")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\5\24\u011f\n\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u0129\n\27\3\27\6\27\u012c\n\27\r\27")
        buf.write("\16\27\u012d\3\30\6\30\u0131\n\30\r\30\16\30\u0132\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0139\n\31\3\31\6\31\u013c\n\31\r")
        buf.write("\31\16\31\u013d\3\32\3\32\3\32\5\32\u0143\n\32\3\33\3")
        buf.write("\33\3\34\3\34\5\34\u0149\n\34\3\35\3\35\7\35\u014d\n\35")
        buf.write("\f\35\16\35\u0150\13\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3")
        buf.write("=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3H\3")
        buf.write("I\3I\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3")
        buf.write("Q\3Q\3R\3R\3S\3S\3T\3T\4\u00d0\u00de\2U\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31\2\33\2\35\2\37")
        buf.write("\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\13\65\f\67\r9\16;")
        buf.write("\17=\20?\21A\22C\23E\24G\25I\26K\27M\30O\31Q\32S\33U\34")
        buf.write("W\35Y\36[\37] _!a\"c#e$g%i&k\'m(o)q*s+u,w-y.{/}\60\177")
        buf.write("\61\u0081\62\u0083\63\u0085\64\u0087\65\u0089\66\u008b")
        buf.write("\67\u008d8\u008f9\u0091:\u0093;\u0095<\u0097=\u0099>\u009b")
        buf.write("?\u009d@\u009fA\u00a1B\u00a3C\u00a5D\u00a7E\3\2\16\4\3")
        buf.write("\n\f\16\17\4\2\60\60AA\5\2\13\f\16\17\"\"\3\2c|\3\2C\\")
        buf.write("\3\2\62;\4\2GGgg\3\2\60\60\t\2))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\5\2\62;CHch\3\2\629\2\u0233\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2")
        buf.write("\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write("\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I")
        buf.write("\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2")
        buf.write("S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2")
        buf.write("\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2")
        buf.write("\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2")
        buf.write("\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3")
        buf.write("\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ad")
        buf.write("\3\2\2\2\7\u00b5\3\2\2\2\t\u00be\3\2\2\2\13\u00ca\3\2")
        buf.write("\2\2\r\u00d8\3\2\2\2\17\u00e3\3\2\2\2\21\u00e6\3\2\2\2")
        buf.write("\23\u00ec\3\2\2\2\25\u00ee\3\2\2\2\27\u00f0\3\2\2\2\31")
        buf.write("\u00f4\3\2\2\2\33\u00f6\3\2\2\2\35\u00ff\3\2\2\2\37\u0107")
        buf.write("\3\2\2\2!\u0112\3\2\2\2#\u0115\3\2\2\2%\u0118\3\2\2\2")
        buf.write("\'\u011e\3\2\2\2)\u0120\3\2\2\2+\u0122\3\2\2\2-\u0128")
        buf.write("\3\2\2\2/\u0130\3\2\2\2\61\u0138\3\2\2\2\63\u0142\3\2")
        buf.write("\2\2\65\u0144\3\2\2\2\67\u0148\3\2\2\29\u014a\3\2\2\2")
        buf.write(";\u0154\3\2\2\2=\u0159\3\2\2\2?\u015f\3\2\2\2A\u0168\3")
        buf.write("\2\2\2C\u016b\3\2\2\2E\u0170\3\2\2\2G\u0177\3\2\2\2I\u017e")
        buf.write("\3\2\2\2K\u0184\3\2\2\2M\u018b\3\2\2\2O\u0194\3\2\2\2")
        buf.write("Q\u0198\3\2\2\2S\u01a1\3\2\2\2U\u01a4\3\2\2\2W\u01ae\3")
        buf.write("\2\2\2Y\u01b5\3\2\2\2[\u01ba\3\2\2\2]\u01be\3\2\2\2_\u01c4")
        buf.write("\3\2\2\2a\u01c9\3\2\2\2c\u01cf\3\2\2\2e\u01d5\3\2\2\2")
        buf.write("g\u01d7\3\2\2\2i\u01da\3\2\2\2k\u01dc\3\2\2\2m\u01df\3")
        buf.write("\2\2\2o\u01e1\3\2\2\2q\u01e4\3\2\2\2s\u01e6\3\2\2\2u\u01e9")
        buf.write("\3\2\2\2w\u01eb\3\2\2\2y\u01ed\3\2\2\2{\u01f0\3\2\2\2")
        buf.write("}\u01f3\3\2\2\2\177\u01f6\3\2\2\2\u0081\u01f9\3\2\2\2")
        buf.write("\u0083\u01fb\3\2\2\2\u0085\u01fd\3\2\2\2\u0087\u0200\3")
        buf.write("\2\2\2\u0089\u0203\3\2\2\2\u008b\u0207\3\2\2\2\u008d\u020a")
        buf.write("\3\2\2\2\u008f\u020d\3\2\2\2\u0091\u0211\3\2\2\2\u0093")
        buf.write("\u0215\3\2\2\2\u0095\u0217\3\2\2\2\u0097\u0219\3\2\2\2")
        buf.write("\u0099\u021b\3\2\2\2\u009b\u021d\3\2\2\2\u009d\u021f\3")
        buf.write("\2\2\2\u009f\u0221\3\2\2\2\u00a1\u0223\3\2\2\2\u00a3\u0225")
        buf.write("\3\2\2\2\u00a5\u0227\3\2\2\2\u00a7\u0229\3\2\2\2\u00a9")
        buf.write("\u00aa\5\u009bN\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\5\u009d")
        buf.write("O\2\u00ac\4\3\2\2\2\u00ad\u00b2\5\23\n\2\u00ae\u00b1\5")
        buf.write("\23\n\2\u00af\u00b1\5\27\f\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\6\3\2\2\2\u00b4\u00b2\3\2\2")
        buf.write("\2\u00b5\u00b9\7$\2\2\u00b6\u00b8\5\'\24\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00bd\5!\21\2\u00bd\b\3\2\2\2\u00be\u00c2\7$\2")
        buf.write("\2\u00bf\u00c1\5\'\24\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c7\t\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\b")
        buf.write("\5\2\2\u00c9\n\3\2\2\2\u00ca\u00cb\7,\2\2\u00cb\u00cc")
        buf.write("\7,\2\2\u00cc\u00d0\3\2\2\2\u00cd\u00cf\13\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d0\u00ce\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d3\u00d4\7,\2\2\u00d4\u00d5\7,\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00d7\b\6\3\2\u00d7\f\3\2\2\2\u00d8\u00d9")
        buf.write("\7,\2\2\u00d9\u00da\7,\2\2\u00da\u00de\3\2\2\2\u00db\u00dd")
        buf.write("\13\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e1\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\2\2\3\u00e2\16\3\2")
        buf.write("\2\2\u00e3\u00e4\t\3\2\2\u00e4\20\3\2\2\2\u00e5\u00e7")
        buf.write("\t\4\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\b\t\3\2\u00eb\22\3\2\2\2\u00ec\u00ed\t\5")
        buf.write("\2\2\u00ed\24\3\2\2\2\u00ee\u00ef\t\6\2\2\u00ef\26\3\2")
        buf.write("\2\2\u00f0\u00f1\t\7\2\2\u00f1\30\3\2\2\2\u00f2\u00f5")
        buf.write("\5\23\n\2\u00f3\u00f5\5\25\13\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\32\3\2\2\2\u00f6\u00f8\t\b\2\2\u00f7")
        buf.write("\u00f9\5i\65\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fb\3\2\2\2\u00fa\u00fc\5\27\f\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\34\3\2\2\2\u00ff\u0103\t\t\2\2\u0100")
        buf.write("\u0102\5\27\f\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2")
        buf.write("\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\36\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\5\27\f\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u0110\3\2\2\2\u010b\u010d\5")
        buf.write("\35\17\2\u010c\u010e\5\33\16\2\u010d\u010c\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u0111\5\33\16")
        buf.write("\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2\2\2\u0111 \3\2")
        buf.write("\2\2\u0112\u0113\7^\2\2\u0113\u0114\n\n\2\2\u0114\"\3")
        buf.write("\2\2\2\u0115\u0116\7^\2\2\u0116\u0117\t\n\2\2\u0117$\3")
        buf.write("\2\2\2\u0118\u0119\7)\2\2\u0119\u011a\7$\2\2\u011a&\3")
        buf.write("\2\2\2\u011b\u011f\n\13\2\2\u011c\u011f\5#\22\2\u011d")
        buf.write("\u011f\5%\23\2\u011e\u011b\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011d\3\2\2\2\u011f(\3\2\2\2\u0120\u0121\t\f\2")
        buf.write("\2\u0121*\3\2\2\2\u0122\u0123\t\r\2\2\u0123,\3\2\2\2\u0124")
        buf.write("\u0125\7\62\2\2\u0125\u0129\7z\2\2\u0126\u0127\7\62\2")
        buf.write("\2\u0127\u0129\7Z\2\2\u0128\u0124\3\2\2\2\u0128\u0126")
        buf.write("\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u012c\5)\25\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e.\3\2\2\2\u012f\u0131\5\27\f")
        buf.write("\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\60\3\2\2\2\u0134\u0135")
        buf.write("\7\62\2\2\u0135\u0139\7q\2\2\u0136\u0137\7\62\2\2\u0137")
        buf.write("\u0139\7Q\2\2\u0138\u0134\3\2\2\2\u0138\u0136\3\2\2\2")
        buf.write("\u0139\u013b\3\2\2\2\u013a\u013c\5+\26\2\u013b\u013a\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\62\3\2\2\2\u013f\u0143\5/\30\2\u0140\u0143")
        buf.write("\5-\27\2\u0141\u0143\5\61\31\2\u0142\u013f\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143\64\3\2\2\2\u0144")
        buf.write("\u0145\5\37\20\2\u0145\66\3\2\2\2\u0146\u0149\5_\60\2")
        buf.write("\u0147\u0149\5a\61\2\u0148\u0146\3\2\2\2\u0148\u0147\3")
        buf.write("\2\2\2\u01498\3\2\2\2\u014a\u014e\7$\2\2\u014b\u014d\5")
        buf.write("\'\24\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u014e\3\2\2\2\u0151\u0152\7$\2\2\u0152\u0153\b")
        buf.write("\35\4\2\u0153:\3\2\2\2\u0154\u0155\7D\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7f\2\2\u0157\u0158\7{\2\2\u0158<\3")
        buf.write("\2\2\2\u0159\u015a\7D\2\2\u015a\u015b\7t\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e\7m\2\2\u015e>\3")
        buf.write("\2\2\2\u015f\u0160\7E\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164\7k\2\2\u0164\u0165")
        buf.write("\7p\2\2\u0165\u0166\7w\2\2\u0166\u0167\7g\2\2\u0167@\3")
        buf.write("\2\2\2\u0168\u0169\7F\2\2\u0169\u016a\7q\2\2\u016aB\3")
        buf.write("\2\2\2\u016b\u016c\7G\2\2\u016c\u016d\7n\2\2\u016d\u016e")
        buf.write("\7u\2\2\u016e\u016f\7g\2\2\u016fD\3\2\2\2\u0170\u0171")
        buf.write("\7G\2\2\u0171\u0172\7n\2\2\u0172\u0173\7U\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\u0175\7n\2\2\u0175\u0176\7h\2\2\u0176F\3")
        buf.write("\2\2\2\u0177\u0178\7G\2\2\u0178\u0179\7n\2\2\u0179\u017a")
        buf.write("\7u\2\2\u017a\u017b\7g\2\2\u017b\u017c\7K\2\2\u017c\u017d")
        buf.write("\7h\2\2\u017dH\3\2\2\2\u017e\u017f\7G\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180\u0181\7f\2\2\u0181\u0182\7K\2\2\u0182\u0183")
        buf.write("\7h\2\2\u0183J\3\2\2\2\u0184\u0185\7G\2\2\u0185\u0186")
        buf.write("\7p\2\2\u0186\u0187\7f\2\2\u0187\u0188\7H\2\2\u0188\u0189")
        buf.write("\7q\2\2\u0189\u018a\7t\2\2\u018aL\3\2\2\2\u018b\u018c")
        buf.write("\7G\2\2\u018c\u018d\7p\2\2\u018d\u018e\7f\2\2\u018e\u018f")
        buf.write("\7Y\2\2\u018f\u0190\7j\2\2\u0190\u0191\7k\2\2\u0191\u0192")
        buf.write("\7n\2\2\u0192\u0193\7g\2\2\u0193N\3\2\2\2\u0194\u0195")
        buf.write("\7H\2\2\u0195\u0196\7q\2\2\u0196\u0197\7t\2\2\u0197P\3")
        buf.write("\2\2\2\u0198\u0199\7H\2\2\u0199\u019a\7w\2\2\u019a\u019b")
        buf.write("\7p\2\2\u019b\u019c\7e\2\2\u019c\u019d\7v\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7q\2\2\u019f\u01a0\7p\2\2\u01a0R\3")
        buf.write("\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3\7h\2\2\u01a3T\3")
        buf.write("\2\2\2\u01a4\u01a5\7R\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7")
        buf.write("\7t\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9\7o\2\2\u01a9\u01aa")
        buf.write("\7g\2\2\u01aa\u01ab\7v\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01adV\3\2\2\2\u01ae\u01af\7T\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7w\2\2\u01b2\u01b3")
        buf.write("\7t\2\2\u01b3\u01b4\7p\2\2\u01b4X\3\2\2\2\u01b5\u01b6")
        buf.write("\7V\2\2\u01b6\u01b7\7j\2\2\u01b7\u01b8\7g\2\2\u01b8\u01b9")
        buf.write("\7p\2\2\u01b9Z\3\2\2\2\u01ba\u01bb\7X\2\2\u01bb\u01bc")
        buf.write("\7c\2\2\u01bc\u01bd\7t\2\2\u01bd\\\3\2\2\2\u01be\u01bf")
        buf.write("\7Y\2\2\u01bf\u01c0\7j\2\2\u01c0\u01c1\7k\2\2\u01c1\u01c2")
        buf.write("\7n\2\2\u01c2\u01c3\7g\2\2\u01c3^\3\2\2\2\u01c4\u01c5")
        buf.write("\7V\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7\7w\2\2\u01c7\u01c8")
        buf.write("\7g\2\2\u01c8`\3\2\2\2\u01c9\u01ca\7H\2\2\u01ca\u01cb")
        buf.write("\7c\2\2\u01cb\u01cc\7n\2\2\u01cc\u01cd\7u\2\2\u01cd\u01ce")
        buf.write("\7g\2\2\u01ceb\3\2\2\2\u01cf\u01d0\7G\2\2\u01d0\u01d1")
        buf.write("\7p\2\2\u01d1\u01d2\7f\2\2\u01d2\u01d3\7F\2\2\u01d3\u01d4")
        buf.write("\7q\2\2\u01d4d\3\2\2\2\u01d5\u01d6\7-\2\2\u01d6f\3\2\2")
        buf.write("\2\u01d7\u01d8\7-\2\2\u01d8\u01d9\7\60\2\2\u01d9h\3\2")
        buf.write("\2\2\u01da\u01db\7/\2\2\u01dbj\3\2\2\2\u01dc\u01dd\7/")
        buf.write("\2\2\u01dd\u01de\7\60\2\2\u01del\3\2\2\2\u01df\u01e0\7")
        buf.write(",\2\2\u01e0n\3\2\2\2\u01e1\u01e2\7,\2\2\u01e2\u01e3\7")
        buf.write("\60\2\2\u01e3p\3\2\2\2\u01e4\u01e5\7^\2\2\u01e5r\3\2\2")
        buf.write("\2\u01e6\u01e7\7^\2\2\u01e7\u01e8\7\60\2\2\u01e8t\3\2")
        buf.write("\2\2\u01e9\u01ea\7\'\2\2\u01eav\3\2\2\2\u01eb\u01ec\7")
        buf.write("#\2\2\u01ecx\3\2\2\2\u01ed\u01ee\7(\2\2\u01ee\u01ef\7")
        buf.write("(\2\2\u01efz\3\2\2\2\u01f0\u01f1\7~\2\2\u01f1\u01f2\7")
        buf.write("~\2\2\u01f2|\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5\7")
        buf.write("?\2\2\u01f5~\3\2\2\2\u01f6\u01f7\7#\2\2\u01f7\u01f8\7")
        buf.write("?\2\2\u01f8\u0080\3\2\2\2\u01f9\u01fa\7>\2\2\u01fa\u0082")
        buf.write("\3\2\2\2\u01fb\u01fc\7@\2\2\u01fc\u0084\3\2\2\2\u01fd")
        buf.write("\u01fe\7>\2\2\u01fe\u01ff\7?\2\2\u01ff\u0086\3\2\2\2\u0200")
        buf.write("\u0201\7@\2\2\u0201\u0202\7?\2\2\u0202\u0088\3\2\2\2\u0203")
        buf.write("\u0204\7?\2\2\u0204\u0205\7^\2\2\u0205\u0206\7?\2\2\u0206")
        buf.write("\u008a\3\2\2\2\u0207\u0208\7>\2\2\u0208\u0209\7\60\2\2")
        buf.write("\u0209\u008c\3\2\2\2\u020a\u020b\7@\2\2\u020b\u020c\7")
        buf.write("\60\2\2\u020c\u008e\3\2\2\2\u020d\u020e\7>\2\2\u020e\u020f")
        buf.write("\7?\2\2\u020f\u0210\7\60\2\2\u0210\u0090\3\2\2\2\u0211")
        buf.write("\u0212\7@\2\2\u0212\u0213\7?\2\2\u0213\u0214\7\60\2\2")
        buf.write("\u0214\u0092\3\2\2\2\u0215\u0216\7*\2\2\u0216\u0094\3")
        buf.write("\2\2\2\u0217\u0218\7+\2\2\u0218\u0096\3\2\2\2\u0219\u021a")
        buf.write("\7]\2\2\u021a\u0098\3\2\2\2\u021b\u021c\7_\2\2\u021c\u009a")
        buf.write("\3\2\2\2\u021d\u021e\7}\2\2\u021e\u009c\3\2\2\2\u021f")
        buf.write("\u0220\7\177\2\2\u0220\u009e\3\2\2\2\u0221\u0222\7<\2")
        buf.write("\2\u0222\u00a0\3\2\2\2\u0223\u0224\7\60\2\2\u0224\u00a2")
        buf.write("\3\2\2\2\u0225\u0226\7=\2\2\u0226\u00a4\3\2\2\2\u0227")
        buf.write("\u0228\7.\2\2\u0228\u00a6\3\2\2\2\u0229\u022a\7?\2\2\u022a")
        buf.write("\u00a8\3\2\2\2\33\2\u00b0\u00b2\u00b9\u00c2\u00c6\u00d0")
        buf.write("\u00de\u00e8\u00f4\u00f8\u00fd\u0103\u0109\u010d\u0110")
        buf.write("\u011e\u0128\u012d\u0132\u0138\u013d\u0142\u0148\u014e")
        buf.write("\5\3\5\2\b\2\2\3\35\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_ARRAY = 1
    ID = 2
    ILLEGAL_ESCAPE = 3
    UNCLOSE_STRING = 4
    COMMENT = 5
    UNTERMINATED_COMMENT = 6
    ERROR_CHAR = 7
    WS = 8
    Integer_literal = 9
    Float_literal = 10
    Boolean_literal = 11
    String_literal = 12
    BODY = 13
    BREAK = 14
    CONTINUE = 15
    DO = 16
    ELSE = 17
    ELSELF = 18
    ELSEIF = 19
    ENDBODY = 20
    ENDFOR = 21
    ENDWHILE = 22
    FOR = 23
    FUNCTION = 24
    IF = 25
    PARAMETER = 26
    RETURN = 27
    THEN = 28
    VAR = 29
    WHILE = 30
    TRUE = 31
    FALSE = 32
    ENDDO = 33
    PLUS_INT = 34
    PLUS_FLOAT = 35
    MINUS_INT = 36
    MINUS_FLOAT = 37
    STAR_INT = 38
    STAR_FLOAT = 39
    DIV_INT = 40
    DIV_FLOAT = 41
    MOD = 42
    NOT = 43
    AND = 44
    OR = 45
    EQUAL = 46
    NOT_EQUAL_INT = 47
    LESS_INT = 48
    GREATER_INT = 49
    LESS_OR_EQUAL_INT = 50
    GREATER_OR_EQUAL_INT = 51
    NOT_EQUAL_FLOAT = 52
    LESS_FLOAT = 53
    GREATER_FLOAT = 54
    LESS_OR_EQUAL_FLOAT = 55
    GREATER_OR_EQUAL_FLOAT = 56
    LEFT_PAREN = 57
    RIGHT_PARENT = 58
    LEFT_BRACKET = 59
    RIGHT_BRACKET = 60
    LEFT_BRACE = 61
    RIGHT_BRACE = 62
    COLON = 63
    DOT = 64
    SEMI = 65
    COMMA = 66
    ASSIGN = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElSelf'", 
            "'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=\\='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "':'", "'.'", "';'", "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT_ARRAY", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", "Integer_literal", 
            "Float_literal", "Boolean_literal", "String_literal", "BODY", 
            "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", "ELSEIF", "ENDBODY", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
            "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
            "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
            "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
            "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
            "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN" ]

    ruleNames = [ "INT_ARRAY", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", 
                  "LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", "LETTER", 
                  "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", "ILL_ESC_SEQUENCE", 
                  "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", "STRING_CHAR", 
                  "HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", "DECIMAL", 
                  "OCTAL", "Integer_literal", "Float_literal", "Boolean_literal", 
                  "String_literal", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSELF", "ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", 
                  "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", 
                  "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
                  "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", 
                  "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", 
                  "LEFT_PAREN", "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", 
                  "ASSIGN" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.UNCLOSE_STRING_action 
            actions[27] = self.String_literal_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text);
                    self.text = y[1:]
                
     

    def String_literal_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     


