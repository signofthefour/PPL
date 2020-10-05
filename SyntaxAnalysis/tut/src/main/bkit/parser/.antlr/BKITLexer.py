# Generated from /home/nguyendat/Documents/projects/PPL/SyntaxAnalysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0238\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\3\2\3\2\7\2\u00ae\n\2\f\2\16\2\u00b1\13\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\7\3\u00b8\n\3\f\3\16\3\u00bb\13\3\3\4\3\4")
        buf.write("\7\4\u00bf\n\4\f\4\16\4\u00c2\13\4\3\4\3\4\3\5\3\5\7\5")
        buf.write("\u00c8\n\5\f\5\16\5\u00cb\13\5\3\5\5\5\u00ce\n\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\7\6\u00d6\n\6\f\6\16\6\u00d9\13\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00e4\n\7\f\7\16")
        buf.write("\7\u00e7\13\7\3\7\3\7\3\b\3\b\3\t\6\t\u00ee\n\t\r\t\16")
        buf.write("\t\u00ef\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\5\r")
        buf.write("\u00fc\n\r\3\16\3\16\5\16\u0100\n\16\3\16\6\16\u0103\n")
        buf.write("\16\r\16\16\16\u0104\3\17\3\17\7\17\u0109\n\17\f\17\16")
        buf.write("\17\u010c\13\17\3\20\6\20\u010f\n\20\r\20\16\20\u0110")
        buf.write("\3\20\3\20\5\20\u0115\n\20\3\20\5\20\u0118\n\20\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\5\24\u0126\n\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0130\n\27\3\27\6\27\u0133\n\27\r\27\16\27\u0134")
        buf.write("\3\30\6\30\u0138\n\30\r\30\16\30\u0139\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0140\n\31\3\31\6\31\u0143\n\31\r\31\16\31")
        buf.write("\u0144\3\32\5\32\u0148\n\32\3\32\3\32\3\32\5\32\u014d")
        buf.write("\n\32\3\33\5\33\u0150\n\33\3\33\3\33\3\34\3\34\5\34\u0156")
        buf.write("\n\34\3\35\3\35\7\35\u015a\n\35\f\35\16\35\u015d\13\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\4")
        buf.write("\u00d7\u00e5\2U\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2")
        buf.write("/\2\61\2\63\13\65\f\67\r9\16;\17=\20?\21A\22C\23E\24G")
        buf.write("\25I\26K\27M\30O\31Q\32S\33U\34W\35Y\36[\37] _!a\"c#e")
        buf.write("$g%i&k\'m(o)q*s+u,w-y.{/}\60\177\61\u0081\62\u0083\63")
        buf.write("\u0085\64\u0087\65\u0089\66\u008b\67\u008d8\u008f9\u0091")
        buf.write(":\u0093;\u0095<\u0097=\u0099>\u009b?\u009d@\u009fA\u00a1")
        buf.write("B\u00a3C\u00a5D\u00a7E\3\2\16\4\3\n\f\16\17\4\2\60\60")
        buf.write("AA\5\2\13\f\16\17\"\"\3\2c|\3\2C\\\3\2\62;\4\2GGgg\3\2")
        buf.write("\60\60\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\5\2\62;C")
        buf.write("Hch\3\2\629\2\u0243\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\3\u00a9\3\2\2\2\5\u00b4\3\2\2\2\7\u00bc\3\2\2")
        buf.write("\2\t\u00c5\3\2\2\2\13\u00d1\3\2\2\2\r\u00df\3\2\2\2\17")
        buf.write("\u00ea\3\2\2\2\21\u00ed\3\2\2\2\23\u00f3\3\2\2\2\25\u00f5")
        buf.write("\3\2\2\2\27\u00f7\3\2\2\2\31\u00fb\3\2\2\2\33\u00fd\3")
        buf.write("\2\2\2\35\u0106\3\2\2\2\37\u010e\3\2\2\2!\u0119\3\2\2")
        buf.write("\2#\u011c\3\2\2\2%\u011f\3\2\2\2\'\u0125\3\2\2\2)\u0127")
        buf.write("\3\2\2\2+\u0129\3\2\2\2-\u012f\3\2\2\2/\u0137\3\2\2\2")
        buf.write("\61\u013f\3\2\2\2\63\u014c\3\2\2\2\65\u014f\3\2\2\2\67")
        buf.write("\u0155\3\2\2\29\u0157\3\2\2\2;\u0161\3\2\2\2=\u0166\3")
        buf.write("\2\2\2?\u016c\3\2\2\2A\u0175\3\2\2\2C\u0178\3\2\2\2E\u017d")
        buf.write("\3\2\2\2G\u0184\3\2\2\2I\u018b\3\2\2\2K\u0191\3\2\2\2")
        buf.write("M\u0198\3\2\2\2O\u01a1\3\2\2\2Q\u01a5\3\2\2\2S\u01ae\3")
        buf.write("\2\2\2U\u01b1\3\2\2\2W\u01bb\3\2\2\2Y\u01c2\3\2\2\2[\u01c7")
        buf.write("\3\2\2\2]\u01cb\3\2\2\2_\u01d1\3\2\2\2a\u01d6\3\2\2\2")
        buf.write("c\u01dc\3\2\2\2e\u01e2\3\2\2\2g\u01e4\3\2\2\2i\u01e7\3")
        buf.write("\2\2\2k\u01e9\3\2\2\2m\u01ec\3\2\2\2o\u01ee\3\2\2\2q\u01f1")
        buf.write("\3\2\2\2s\u01f3\3\2\2\2u\u01f6\3\2\2\2w\u01f8\3\2\2\2")
        buf.write("y\u01fa\3\2\2\2{\u01fd\3\2\2\2}\u0200\3\2\2\2\177\u0203")
        buf.write("\3\2\2\2\u0081\u0206\3\2\2\2\u0083\u0208\3\2\2\2\u0085")
        buf.write("\u020a\3\2\2\2\u0087\u020d\3\2\2\2\u0089\u0210\3\2\2\2")
        buf.write("\u008b\u0214\3\2\2\2\u008d\u0217\3\2\2\2\u008f\u021a\3")
        buf.write("\2\2\2\u0091\u021e\3\2\2\2\u0093\u0222\3\2\2\2\u0095\u0224")
        buf.write("\3\2\2\2\u0097\u0226\3\2\2\2\u0099\u0228\3\2\2\2\u009b")
        buf.write("\u022a\3\2\2\2\u009d\u022c\3\2\2\2\u009f\u022e\3\2\2\2")
        buf.write("\u00a1\u0230\3\2\2\2\u00a3\u0232\3\2\2\2\u00a5\u0234\3")
        buf.write("\2\2\2\u00a7\u0236\3\2\2\2\u00a9\u00af\5\u009bN\2\u00aa")
        buf.write("\u00ab\5\63\32\2\u00ab\u00ac\5\u00a5S\2\u00ac\u00ae\3")
        buf.write("\2\2\2\u00ad\u00aa\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b3\5\u009dO\2\u00b3\4\3\2\2\2")
        buf.write("\u00b4\u00b9\5\23\n\2\u00b5\u00b8\5\23\n\2\u00b6\u00b8")
        buf.write("\5\27\f\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\6\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00c0\7$\2")
        buf.write("\2\u00bd\u00bf\5\'\24\2\u00be\u00bd\3\2\2\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\5!\21\2")
        buf.write("\u00c4\b\3\2\2\2\u00c5\u00c9\7$\2\2\u00c6\u00c8\5\'\24")
        buf.write("\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00ce\t\2\2\2\u00cd\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d0\b\5\2\2\u00d0\n\3\2\2")
        buf.write("\2\u00d1\u00d2\7,\2\2\u00d2\u00d3\7,\2\2\u00d3\u00d7\3")
        buf.write("\2\2\2\u00d4\u00d6\13\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d9\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7")
        buf.write(",\2\2\u00db\u00dc\7,\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\b\6\3\2\u00de\f\3\2\2\2\u00df\u00e0\7,\2\2\u00e0\u00e1")
        buf.write("\7,\2\2\u00e1\u00e5\3\2\2\2\u00e2\u00e4\13\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5\3")
        buf.write("\2\2\2\u00e8\u00e9\7\2\2\3\u00e9\16\3\2\2\2\u00ea\u00eb")
        buf.write("\t\3\2\2\u00eb\20\3\2\2\2\u00ec\u00ee\t\4\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\b\t\3\2")
        buf.write("\u00f2\22\3\2\2\2\u00f3\u00f4\t\5\2\2\u00f4\24\3\2\2\2")
        buf.write("\u00f5\u00f6\t\6\2\2\u00f6\26\3\2\2\2\u00f7\u00f8\t\7")
        buf.write("\2\2\u00f8\30\3\2\2\2\u00f9\u00fc\5\23\n\2\u00fa\u00fc")
        buf.write("\5\25\13\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("\32\3\2\2\2\u00fd\u00ff\t\b\2\2\u00fe\u0100\5i\65\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2")
        buf.write("\u0101\u0103\5\27\f\2\u0102\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\34\3\2\2\2\u0106\u010a\t\t\2\2\u0107\u0109\5\27\f\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\36\3\2\2\2\u010c\u010a\3\2")
        buf.write("\2\2\u010d\u010f\5\27\f\2\u010e\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0117\3\2\2\2\u0112\u0114\5\35\17\2\u0113\u0115\5\33")
        buf.write("\16\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0118\5\33\16\2\u0117\u0112\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118 \3\2\2\2\u0119\u011a\7^\2\2\u011a")
        buf.write("\u011b\n\n\2\2\u011b\"\3\2\2\2\u011c\u011d\7^\2\2\u011d")
        buf.write("\u011e\t\n\2\2\u011e$\3\2\2\2\u011f\u0120\7)\2\2\u0120")
        buf.write("\u0121\7$\2\2\u0121&\3\2\2\2\u0122\u0126\n\13\2\2\u0123")
        buf.write("\u0126\5#\22\2\u0124\u0126\5%\23\2\u0125\u0122\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126(\3\2\2")
        buf.write("\2\u0127\u0128\t\f\2\2\u0128*\3\2\2\2\u0129\u012a\t\r")
        buf.write("\2\2\u012a,\3\2\2\2\u012b\u012c\7\62\2\2\u012c\u0130\7")
        buf.write("z\2\2\u012d\u012e\7\62\2\2\u012e\u0130\7Z\2\2\u012f\u012b")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0132\3\2\2\2\u0131")
        buf.write("\u0133\5)\25\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135.\3\2\2")
        buf.write("\2\u0136\u0138\5\27\f\2\u0137\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\60\3\2\2\2\u013b\u013c\7\62\2\2\u013c\u0140\7q\2\2\u013d")
        buf.write("\u013e\7\62\2\2\u013e\u0140\7Q\2\2\u013f\u013b\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u0140\u0142\3\2\2\2\u0141\u0143\5")
        buf.write("+\26\2\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\62\3\2\2\2\u0146\u0148")
        buf.write("\5i\65\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014d\5/\30\2\u014a\u014d\5-\27\2")
        buf.write("\u014b\u014d\5\61\31\2\u014c\u0147\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014d\64\3\2\2\2\u014e\u0150")
        buf.write("\5i\65\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0152\5\37\20\2\u0152\66\3\2\2\2")
        buf.write("\u0153\u0156\5_\60\2\u0154\u0156\5a\61\2\u0155\u0153\3")
        buf.write("\2\2\2\u0155\u0154\3\2\2\2\u01568\3\2\2\2\u0157\u015b")
        buf.write("\7$\2\2\u0158\u015a\5\'\24\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\7")
        buf.write("$\2\2\u015f\u0160\b\35\4\2\u0160:\3\2\2\2\u0161\u0162")
        buf.write("\7D\2\2\u0162\u0163\7q\2\2\u0163\u0164\7f\2\2\u0164\u0165")
        buf.write("\7{\2\2\u0165<\3\2\2\2\u0166\u0167\7D\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\u0169\7g\2\2\u0169\u016a\7c\2\2\u016a\u016b")
        buf.write("\7m\2\2\u016b>\3\2\2\2\u016c\u016d\7E\2\2\u016d\u016e")
        buf.write("\7q\2\2\u016e\u016f\7p\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7p\2\2\u0172\u0173\7w\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174@\3\2\2\2\u0175\u0176\7F\2\2\u0176\u0177")
        buf.write("\7q\2\2\u0177B\3\2\2\2\u0178\u0179\7G\2\2\u0179\u017a")
        buf.write("\7n\2\2\u017a\u017b\7u\2\2\u017b\u017c\7g\2\2\u017cD\3")
        buf.write("\2\2\2\u017d\u017e\7G\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7U\2\2\u0180\u0181\7g\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7h\2\2\u0183F\3\2\2\2\u0184\u0185\7G\2\2\u0185\u0186")
        buf.write("\7n\2\2\u0186\u0187\7u\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7K\2\2\u0189\u018a\7h\2\2\u018aH\3\2\2\2\u018b\u018c")
        buf.write("\7G\2\2\u018c\u018d\7p\2\2\u018d\u018e\7f\2\2\u018e\u018f")
        buf.write("\7K\2\2\u018f\u0190\7h\2\2\u0190J\3\2\2\2\u0191\u0192")
        buf.write("\7G\2\2\u0192\u0193\7p\2\2\u0193\u0194\7f\2\2\u0194\u0195")
        buf.write("\7H\2\2\u0195\u0196\7q\2\2\u0196\u0197\7t\2\2\u0197L\3")
        buf.write("\2\2\2\u0198\u0199\7G\2\2\u0199\u019a\7p\2\2\u019a\u019b")
        buf.write("\7f\2\2\u019b\u019c\7Y\2\2\u019c\u019d\7j\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7n\2\2\u019f\u01a0\7g\2\2\u01a0N\3")
        buf.write("\2\2\2\u01a1\u01a2\7H\2\2\u01a2\u01a3\7q\2\2\u01a3\u01a4")
        buf.write("\7t\2\2\u01a4P\3\2\2\2\u01a5\u01a6\7H\2\2\u01a6\u01a7")
        buf.write("\7w\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7e\2\2\u01a9\u01aa")
        buf.write("\7v\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad")
        buf.write("\7p\2\2\u01adR\3\2\2\2\u01ae\u01af\7K\2\2\u01af\u01b0")
        buf.write("\7h\2\2\u01b0T\3\2\2\2\u01b1\u01b2\7R\2\2\u01b2\u01b3")
        buf.write("\7c\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6")
        buf.write("\7o\2\2\u01b6\u01b7\7g\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9")
        buf.write("\7g\2\2\u01b9\u01ba\7t\2\2\u01baV\3\2\2\2\u01bb\u01bc")
        buf.write("\7T\2\2\u01bc\u01bd\7g\2\2\u01bd\u01be\7v\2\2\u01be\u01bf")
        buf.write("\7w\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c1\7p\2\2\u01c1X\3")
        buf.write("\2\2\2\u01c2\u01c3\7V\2\2\u01c3\u01c4\7j\2\2\u01c4\u01c5")
        buf.write("\7g\2\2\u01c5\u01c6\7p\2\2\u01c6Z\3\2\2\2\u01c7\u01c8")
        buf.write("\7X\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca\7t\2\2\u01ca\\")
        buf.write("\3\2\2\2\u01cb\u01cc\7Y\2\2\u01cc\u01cd\7j\2\2\u01cd\u01ce")
        buf.write("\7k\2\2\u01ce\u01cf\7n\2\2\u01cf\u01d0\7g\2\2\u01d0^\3")
        buf.write("\2\2\2\u01d1\u01d2\7V\2\2\u01d2\u01d3\7t\2\2\u01d3\u01d4")
        buf.write("\7w\2\2\u01d4\u01d5\7g\2\2\u01d5`\3\2\2\2\u01d6\u01d7")
        buf.write("\7H\2\2\u01d7\u01d8\7c\2\2\u01d8\u01d9\7n\2\2\u01d9\u01da")
        buf.write("\7u\2\2\u01da\u01db\7g\2\2\u01dbb\3\2\2\2\u01dc\u01dd")
        buf.write("\7G\2\2\u01dd\u01de\7p\2\2\u01de\u01df\7f\2\2\u01df\u01e0")
        buf.write("\7F\2\2\u01e0\u01e1\7q\2\2\u01e1d\3\2\2\2\u01e2\u01e3")
        buf.write("\7-\2\2\u01e3f\3\2\2\2\u01e4\u01e5\7-\2\2\u01e5\u01e6")
        buf.write("\7\60\2\2\u01e6h\3\2\2\2\u01e7\u01e8\7/\2\2\u01e8j\3\2")
        buf.write("\2\2\u01e9\u01ea\7/\2\2\u01ea\u01eb\7\60\2\2\u01ebl\3")
        buf.write("\2\2\2\u01ec\u01ed\7,\2\2\u01edn\3\2\2\2\u01ee\u01ef\7")
        buf.write(",\2\2\u01ef\u01f0\7\60\2\2\u01f0p\3\2\2\2\u01f1\u01f2")
        buf.write("\7^\2\2\u01f2r\3\2\2\2\u01f3\u01f4\7^\2\2\u01f4\u01f5")
        buf.write("\7\60\2\2\u01f5t\3\2\2\2\u01f6\u01f7\7\'\2\2\u01f7v\3")
        buf.write("\2\2\2\u01f8\u01f9\7#\2\2\u01f9x\3\2\2\2\u01fa\u01fb\7")
        buf.write("(\2\2\u01fb\u01fc\7(\2\2\u01fcz\3\2\2\2\u01fd\u01fe\7")
        buf.write("~\2\2\u01fe\u01ff\7~\2\2\u01ff|\3\2\2\2\u0200\u0201\7")
        buf.write("?\2\2\u0201\u0202\7?\2\2\u0202~\3\2\2\2\u0203\u0204\7")
        buf.write("#\2\2\u0204\u0205\7?\2\2\u0205\u0080\3\2\2\2\u0206\u0207")
        buf.write("\7>\2\2\u0207\u0082\3\2\2\2\u0208\u0209\7@\2\2\u0209\u0084")
        buf.write("\3\2\2\2\u020a\u020b\7>\2\2\u020b\u020c\7?\2\2\u020c\u0086")
        buf.write("\3\2\2\2\u020d\u020e\7@\2\2\u020e\u020f\7?\2\2\u020f\u0088")
        buf.write("\3\2\2\2\u0210\u0211\7?\2\2\u0211\u0212\7^\2\2\u0212\u0213")
        buf.write("\7?\2\2\u0213\u008a\3\2\2\2\u0214\u0215\7>\2\2\u0215\u0216")
        buf.write("\7\60\2\2\u0216\u008c\3\2\2\2\u0217\u0218\7@\2\2\u0218")
        buf.write("\u0219\7\60\2\2\u0219\u008e\3\2\2\2\u021a\u021b\7>\2\2")
        buf.write("\u021b\u021c\7?\2\2\u021c\u021d\7\60\2\2\u021d\u0090\3")
        buf.write("\2\2\2\u021e\u021f\7@\2\2\u021f\u0220\7?\2\2\u0220\u0221")
        buf.write("\7\60\2\2\u0221\u0092\3\2\2\2\u0222\u0223\7*\2\2\u0223")
        buf.write("\u0094\3\2\2\2\u0224\u0225\7+\2\2\u0225\u0096\3\2\2\2")
        buf.write("\u0226\u0227\7]\2\2\u0227\u0098\3\2\2\2\u0228\u0229\7")
        buf.write("_\2\2\u0229\u009a\3\2\2\2\u022a\u022b\7}\2\2\u022b\u009c")
        buf.write("\3\2\2\2\u022c\u022d\7\177\2\2\u022d\u009e\3\2\2\2\u022e")
        buf.write("\u022f\7<\2\2\u022f\u00a0\3\2\2\2\u0230\u0231\7\60\2\2")
        buf.write("\u0231\u00a2\3\2\2\2\u0232\u0233\7=\2\2\u0233\u00a4\3")
        buf.write("\2\2\2\u0234\u0235\7.\2\2\u0235\u00a6\3\2\2\2\u0236\u0237")
        buf.write("\7?\2\2\u0237\u00a8\3\2\2\2\36\2\u00af\u00b7\u00b9\u00c0")
        buf.write("\u00c9\u00cd\u00d7\u00e5\u00ef\u00fb\u00ff\u0104\u010a")
        buf.write("\u0110\u0114\u0117\u0125\u012f\u0134\u0139\u013f\u0144")
        buf.write("\u0147\u014c\u014f\u0155\u015b\5\3\5\2\b\2\2\3\35\3")
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
                
     


