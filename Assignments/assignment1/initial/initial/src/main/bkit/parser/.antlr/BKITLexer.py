# Generated from /home/khanh/Documents/schoolLife/201/PPL/Assignments/assignment1/initial/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u024e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\6\2\u00a9")
        buf.write("\n\2\r\2\16\2\u00aa\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00b3")
        buf.write("\n\3\f\3\16\3\u00b6\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00c8\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00cf\n\5\3\6\3\6\3\6\3\6\3\6\7\6\u00d6")
        buf.write("\n\6\f\6\16\6\u00d9\13\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\7\21\u00f1\n\21\f\21\16\21\u00f4\13\21")
        buf.write("\3\21\3\21\3\21\7\21\u00f9\n\21\f\21\16\21\u00fc\13\21")
        buf.write("\3\21\3\21\3\21\7\21\u0101\n\21\f\21\16\21\u0104\13\21")
        buf.write("\3\21\5\21\u0107\n\21\3\22\6\22\u010a\n\22\r\22\16\22")
        buf.write("\u010b\3\22\3\22\7\22\u0110\n\22\f\22\16\22\u0113\13\22")
        buf.write("\3\22\5\22\u0116\n\22\3\22\5\22\u0119\n\22\3\23\3\23\5")
        buf.write("\23\u011d\n\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\3")
        buf.write("9\39\39\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\3>\3>\3?\3?\3?\3")
        buf.write("?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\7B\u01e7\nB\fB\16B")
        buf.write("\u01ea\13B\3B\5B\u01ed\nB\3B\3B\3C\3C\7C\u01f3\nC\fC\16")
        buf.write("C\u01f6\13C\3C\3C\3C\3D\3D\3D\3D\7D\u01ff\nD\fD\16D\u0202")
        buf.write("\13D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3I\3J\5J\u0210\nJ\3")
        buf.write("K\3K\6K\u0214\nK\rK\16K\u0215\3L\3L\3L\3L\5L\u021c\nL")
        buf.write("\3M\3M\3M\3M\5M\u0222\nM\3N\3N\3N\3O\3O\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u0237\nP\3Q\3Q\3Q\3Q\5")
        buf.write("Q\u023d\nQ\3R\3R\3R\3R\5R\u0243\nR\3S\3S\7S\u0247\nS\f")
        buf.write("S\16S\u024a\13S\3S\3S\3S\4\u00b4\u0200\2T\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("A\u0081B\u0083C\u0085D\u0087E\u0089\2\u008b\2\u008d\2")
        buf.write("\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5F\3\2\21\5\2\13")
        buf.write("\f\17\17\"\"\3\2\63;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\62")
        buf.write("9\3\3\f\f\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4\2--//\t\2))^")
        buf.write("^ddhhppttvv\3\2$$\6\2\f\f$$))^^\2\u026f\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u00a5\3\2\2\2\3\u00a8")
        buf.write("\3\2\2\2\5\u00ae\3\2\2\2\7\u00c7\3\2\2\2\t\u00ce\3\2\2")
        buf.write("\2\13\u00d0\3\2\2\2\r\u00da\3\2\2\2\17\u00dc\3\2\2\2\21")
        buf.write("\u00de\3\2\2\2\23\u00e0\3\2\2\2\25\u00e2\3\2\2\2\27\u00e4")
        buf.write("\3\2\2\2\31\u00e6\3\2\2\2\33\u00e8\3\2\2\2\35\u00ea\3")
        buf.write("\2\2\2\37\u00ec\3\2\2\2!\u0106\3\2\2\2#\u0109\3\2\2\2")
        buf.write("%\u011c\3\2\2\2\'\u011e\3\2\2\2)\u0121\3\2\2\2+\u0123")
        buf.write("\3\2\2\2-\u0126\3\2\2\2/\u0128\3\2\2\2\61\u012b\3\2\2")
        buf.write("\2\63\u012d\3\2\2\2\65\u0130\3\2\2\2\67\u0132\3\2\2\2")
        buf.write("9\u0134\3\2\2\2;\u0137\3\2\2\2=\u013b\3\2\2\2?\u013f\3")
        buf.write("\2\2\2A\u0143\3\2\2\2C\u0146\3\2\2\2E\u0149\3\2\2\2G\u014c")
        buf.write("\3\2\2\2I\u014f\3\2\2\2K\u0152\3\2\2\2M\u0154\3\2\2\2")
        buf.write("O\u0156\3\2\2\2Q\u0158\3\2\2\2S\u015b\3\2\2\2U\u015e\3")
        buf.write("\2\2\2W\u0160\3\2\2\2Y\u0164\3\2\2\2[\u016d\3\2\2\2]\u0172")
        buf.write("\3\2\2\2_\u0177\3\2\2\2a\u017e\3\2\2\2c\u0181\3\2\2\2")
        buf.write("e\u0187\3\2\2\2g\u018d\3\2\2\2i\u0194\3\2\2\2k\u019d\3")
        buf.write("\2\2\2m\u01a7\3\2\2\2o\u01ad\3\2\2\2q\u01b6\3\2\2\2s\u01be")
        buf.write("\3\2\2\2u\u01c2\3\2\2\2w\u01c9\3\2\2\2y\u01ce\3\2\2\2")
        buf.write("{\u01d1\3\2\2\2}\u01d7\3\2\2\2\177\u01dc\3\2\2\2\u0081")
        buf.write("\u01e2\3\2\2\2\u0083\u01e4\3\2\2\2\u0085\u01f0\3\2\2\2")
        buf.write("\u0087\u01fa\3\2\2\2\u0089\u0203\3\2\2\2\u008b\u0205\3")
        buf.write("\2\2\2\u008d\u0207\3\2\2\2\u008f\u0209\3\2\2\2\u0091\u020b")
        buf.write("\3\2\2\2\u0093\u020f\3\2\2\2\u0095\u0211\3\2\2\2\u0097")
        buf.write("\u021b\3\2\2\2\u0099\u0221\3\2\2\2\u009b\u0223\3\2\2\2")
        buf.write("\u009d\u0226\3\2\2\2\u009f\u0236\3\2\2\2\u00a1\u023c\3")
        buf.write("\2\2\2\u00a3\u0242\3\2\2\2\u00a5\u0244\3\2\2\2\u00a7\u00a9")
        buf.write("\t\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\b\2\2\2\u00ad\4\3\2\2\2\u00ae\u00af\7,\2")
        buf.write("\2\u00af\u00b0\7,\2\2\u00b0\u00b4\3\2\2\2\u00b1\u00b3")
        buf.write("\13\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b7\u00b8\7,\2\2\u00b8\u00b9\7")
        buf.write(",\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\b\3\2\2\u00bb\6")
        buf.write("\3\2\2\2\u00bc\u00c8\59\35\2\u00bd\u00c8\5;\36\2\u00be")
        buf.write("\u00c8\5=\37\2\u00bf\u00c8\5? \2\u00c0\u00c8\5A!\2\u00c1")
        buf.write("\u00c8\5C\"\2\u00c2\u00c8\5E#\2\u00c3\u00c8\5G$\2\u00c4")
        buf.write("\u00c8\5I%\2\u00c5\u00c8\5K&\2\u00c6\u00c8\5M\'\2\u00c7")
        buf.write("\u00bc\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c7\u00be\3\2\2\2")
        buf.write("\u00c7\u00bf\3\2\2\2\u00c7\u00c0\3\2\2\2\u00c7\u00c1\3")
        buf.write("\2\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c3\3\2\2\2\u00c7\u00c4")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\b\3\2\2\2\u00c9\u00cf\5/\30\2\u00ca\u00cf\5\63\32\2\u00cb")
        buf.write("\u00cf\5\61\31\2\u00cc\u00cf\5\65\33\2\u00cd\u00cf\5\67")
        buf.write("\34\2\u00ce\u00c9\3\2\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\n\3\2\2\2\u00d0\u00d7\5\u008bF\2\u00d1\u00d6\5\u008b")
        buf.write("F\2\u00d2\u00d6\5\u008dG\2\u00d3\u00d6\5\u008fH\2\u00d4")
        buf.write("\u00d6\7a\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d2\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\f")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7}\2\2\u00db")
        buf.write("\16\3\2\2\2\u00dc\u00dd\7\177\2\2\u00dd\20\3\2\2\2\u00de")
        buf.write("\u00df\7]\2\2\u00df\22\3\2\2\2\u00e0\u00e1\7_\2\2\u00e1")
        buf.write("\24\3\2\2\2\u00e2\u00e3\7*\2\2\u00e3\26\3\2\2\2\u00e4")
        buf.write("\u00e5\7+\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\7=\2\2\u00e7")
        buf.write("\32\3\2\2\2\u00e8\u00e9\7<\2\2\u00e9\34\3\2\2\2\u00ea")
        buf.write("\u00eb\7.\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7\60\2\2\u00ed")
        buf.write(" \3\2\2\2\u00ee\u00f2\t\3\2\2\u00ef\u00f1\5\u008fH\2\u00f0")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u0107\3\2\2\2\u00f4\u00f2\3")
        buf.write("\2\2\2\u00f5\u00f6\5\u0097L\2\u00f6\u00fa\t\4\2\2\u00f7")
        buf.write("\u00f9\t\5\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u0107\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\5\u0099M\2\u00fe")
        buf.write("\u0102\t\6\2\2\u00ff\u0101\t\7\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3")
        buf.write("\2\2\2\u0103\u0107\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0107")
        buf.write("\7\62\2\2\u0106\u00ee\3\2\2\2\u0106\u00f5\3\2\2\2\u0106")
        buf.write("\u00fd\3\2\2\2\u0106\u0105\3\2\2\2\u0107\"\3\2\2\2\u0108")
        buf.write("\u010a\5\u008fH\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2")
        buf.write("\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0118")
        buf.write("\3\2\2\2\u010d\u0111\5\37\20\2\u010e\u0110\5\u008fH\2")
        buf.write("\u010f\u010e\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3")
        buf.write("\2\2\2\u0111\u0112\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0114\u0116\5\u0095K\2\u0115\u0114\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0119\5\u0095")
        buf.write("K\2\u0118\u010d\3\2\2\2\u0118\u0117\3\2\2\2\u0119$\3\2")
        buf.write("\2\2\u011a\u011d\5w<\2\u011b\u011d\5\177@\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011b\3\2\2\2\u011d&\3\2\2\2\u011e\u011f")
        buf.write("\7-\2\2\u011f\u0120\7\60\2\2\u0120(\3\2\2\2\u0121\u0122")
        buf.write("\7-\2\2\u0122*\3\2\2\2\u0123\u0124\7/\2\2\u0124\u0125")
        buf.write("\7\60\2\2\u0125,\3\2\2\2\u0126\u0127\7/\2\2\u0127.\3\2")
        buf.write("\2\2\u0128\u0129\7,\2\2\u0129\u012a\7\60\2\2\u012a\60")
        buf.write("\3\2\2\2\u012b\u012c\7,\2\2\u012c\62\3\2\2\2\u012d\u012e")
        buf.write("\7^\2\2\u012e\u012f\7\60\2\2\u012f\64\3\2\2\2\u0130\u0131")
        buf.write("\7^\2\2\u0131\66\3\2\2\2\u0132\u0133\7\'\2\2\u01338\3")
        buf.write("\2\2\2\u0134\u0135\7?\2\2\u0135\u0136\7?\2\2\u0136:\3")
        buf.write("\2\2\2\u0137\u0138\7?\2\2\u0138\u0139\7\61\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a<\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d")
        buf.write("\7?\2\2\u013d\u013e\7\60\2\2\u013e>\3\2\2\2\u013f\u0140")
        buf.write("\7@\2\2\u0140\u0141\7?\2\2\u0141\u0142\7\60\2\2\u0142")
        buf.write("@\3\2\2\2\u0143\u0144\7>\2\2\u0144\u0145\7\60\2\2\u0145")
        buf.write("B\3\2\2\2\u0146\u0147\7@\2\2\u0147\u0148\7\60\2\2\u0148")
        buf.write("D\3\2\2\2\u0149\u014a\7#\2\2\u014a\u014b\7?\2\2\u014b")
        buf.write("F\3\2\2\2\u014c\u014d\7>\2\2\u014d\u014e\7?\2\2\u014e")
        buf.write("H\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7?\2\2\u0151")
        buf.write("J\3\2\2\2\u0152\u0153\7>\2\2\u0153L\3\2\2\2\u0154\u0155")
        buf.write("\7@\2\2\u0155N\3\2\2\2\u0156\u0157\7#\2\2\u0157P\3\2\2")
        buf.write("\2\u0158\u0159\7(\2\2\u0159\u015a\7(\2\2\u015aR\3\2\2")
        buf.write("\2\u015b\u015c\7~\2\2\u015c\u015d\7~\2\2\u015dT\3\2\2")
        buf.write("\2\u015e\u015f\7?\2\2\u015fV\3\2\2\2\u0160\u0161\7X\2")
        buf.write("\2\u0161\u0162\7c\2\2\u0162\u0163\7t\2\2\u0163X\3\2\2")
        buf.write("\2\u0164\u0165\7H\2\2\u0165\u0166\7w\2\2\u0166\u0167\7")
        buf.write("p\2\2\u0167\u0168\7e\2\2\u0168\u0169\7v\2\2\u0169\u016a")
        buf.write("\7k\2\2\u016a\u016b\7q\2\2\u016b\u016c\7p\2\2\u016cZ\3")
        buf.write("\2\2\2\u016d\u016e\7D\2\2\u016e\u016f\7q\2\2\u016f\u0170")
        buf.write("\7f\2\2\u0170\u0171\7{\2\2\u0171\\\3\2\2\2\u0172\u0173")
        buf.write("\7G\2\2\u0173\u0174\7n\2\2\u0174\u0175\7u\2\2\u0175\u0176")
        buf.write("\7g\2\2\u0176^\3\2\2\2\u0177\u0178\7G\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7f\2\2\u017a\u017b\7H\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7t\2\2\u017d`\3\2\2\2\u017e\u017f")
        buf.write("\7K\2\2\u017f\u0180\7h\2\2\u0180b\3\2\2\2\u0181\u0182")
        buf.write("\7G\2\2\u0182\u0183\7p\2\2\u0183\u0184\7f\2\2\u0184\u0185")
        buf.write("\7F\2\2\u0185\u0186\7q\2\2\u0186d\3\2\2\2\u0187\u0188")
        buf.write("\7D\2\2\u0188\u0189\7t\2\2\u0189\u018a\7g\2\2\u018a\u018b")
        buf.write("\7c\2\2\u018b\u018c\7m\2\2\u018cf\3\2\2\2\u018d\u018e")
        buf.write("\7G\2\2\u018e\u018f\7n\2\2\u018f\u0190\7u\2\2\u0190\u0191")
        buf.write("\7g\2\2\u0191\u0192\7K\2\2\u0192\u0193\7h\2\2\u0193h\3")
        buf.write("\2\2\2\u0194\u0195\7G\2\2\u0195\u0196\7p\2\2\u0196\u0197")
        buf.write("\7f\2\2\u0197\u0198\7Y\2\2\u0198\u0199\7j\2\2\u0199\u019a")
        buf.write("\7k\2\2\u019a\u019b\7n\2\2\u019b\u019c\7g\2\2\u019cj\3")
        buf.write("\2\2\2\u019d\u019e\7R\2\2\u019e\u019f\7c\2\2\u019f\u01a0")
        buf.write("\7t\2\2\u01a0\u01a1\7c\2\2\u01a1\u01a2\7o\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5\7g\2\2\u01a5\u01a6")
        buf.write("\7t\2\2\u01a6l\3\2\2\2\u01a7\u01a8\7Y\2\2\u01a8\u01a9")
        buf.write("\7j\2\2\u01a9\u01aa\7k\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac")
        buf.write("\7g\2\2\u01acn\3\2\2\2\u01ad\u01ae\7E\2\2\u01ae\u01af")
        buf.write("\7q\2\2\u01af\u01b0\7p\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2")
        buf.write("\7k\2\2\u01b2\u01b3\7p\2\2\u01b3\u01b4\7w\2\2\u01b4\u01b5")
        buf.write("\7g\2\2\u01b5p\3\2\2\2\u01b6\u01b7\7G\2\2\u01b7\u01b8")
        buf.write("\7p\2\2\u01b8\u01b9\7f\2\2\u01b9\u01ba\7D\2\2\u01ba\u01bb")
        buf.write("\7q\2\2\u01bb\u01bc\7f\2\2\u01bc\u01bd\7{\2\2\u01bdr\3")
        buf.write("\2\2\2\u01be\u01bf\7H\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1")
        buf.write("\7t\2\2\u01c1t\3\2\2\2\u01c2\u01c3\7T\2\2\u01c3\u01c4")
        buf.write("\7g\2\2\u01c4\u01c5\7v\2\2\u01c5\u01c6\7w\2\2\u01c6\u01c7")
        buf.write("\7t\2\2\u01c7\u01c8\7p\2\2\u01c8v\3\2\2\2\u01c9\u01ca")
        buf.write("\7V\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc\7w\2\2\u01cc\u01cd")
        buf.write("\7g\2\2\u01cdx\3\2\2\2\u01ce\u01cf\7F\2\2\u01cf\u01d0")
        buf.write("\7q\2\2\u01d0z\3\2\2\2\u01d1\u01d2\7G\2\2\u01d2\u01d3")
        buf.write("\7p\2\2\u01d3\u01d4\7f\2\2\u01d4\u01d5\7K\2\2\u01d5\u01d6")
        buf.write("\7h\2\2\u01d6|\3\2\2\2\u01d7\u01d8\7V\2\2\u01d8\u01d9")
        buf.write("\7j\2\2\u01d9\u01da\7g\2\2\u01da\u01db\7p\2\2\u01db~\3")
        buf.write("\2\2\2\u01dc\u01dd\7H\2\2\u01dd\u01de\7c\2\2\u01de\u01df")
        buf.write("\7n\2\2\u01df\u01e0\7u\2\2\u01e0\u01e1\7g\2\2\u01e1\u0080")
        buf.write("\3\2\2\2\u01e2\u01e3\13\2\2\2\u01e3\u0082\3\2\2\2\u01e4")
        buf.write("\u01e8\5\u0089E\2\u01e5\u01e7\5\u00a3R\2\u01e6\u01e5\3")
        buf.write("\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb")
        buf.write("\u01ed\t\b\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01ef\bB\3\2\u01ef\u0084\3\2\2\2\u01f0\u01f4\7")
        buf.write("$\2\2\u01f1\u01f3\5\u00a3R\2\u01f2\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2")
        buf.write("\u01f5\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\5")
        buf.write("\u00a1Q\2\u01f8\u01f9\bC\4\2\u01f9\u0086\3\2\2\2\u01fa")
        buf.write("\u01fb\7,\2\2\u01fb\u01fc\7,\2\2\u01fc\u0200\3\2\2\2\u01fd")
        buf.write("\u01ff\13\2\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2")
        buf.write("\2\u0200\u0201\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0088")
        buf.write("\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\7$\2\2\u0204")
        buf.write("\u008a\3\2\2\2\u0205\u0206\t\t\2\2\u0206\u008c\3\2\2\2")
        buf.write("\u0207\u0208\t\n\2\2\u0208\u008e\3\2\2\2\u0209\u020a\t")
        buf.write("\13\2\2\u020a\u0090\3\2\2\2\u020b\u020c\t\f\2\2\u020c")
        buf.write("\u020d\5\u0093J\2\u020d\u0092\3\2\2\2\u020e\u0210\t\r")
        buf.write("\2\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0094")
        buf.write("\3\2\2\2\u0211\u0213\5\u0091I\2\u0212\u0214\5\u008fH\2")
        buf.write("\u0213\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0213\3")
        buf.write("\2\2\2\u0215\u0216\3\2\2\2\u0216\u0096\3\2\2\2\u0217\u0218")
        buf.write("\7\62\2\2\u0218\u021c\7z\2\2\u0219\u021a\7\62\2\2\u021a")
        buf.write("\u021c\7Z\2\2\u021b\u0217\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021c\u0098\3\2\2\2\u021d\u021e\7\62\2\2\u021e\u0222")
        buf.write("\7q\2\2\u021f\u0220\7\62\2\2\u0220\u0222\7Q\2\2\u0221")
        buf.write("\u021d\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u009a\3\2\2\2")
        buf.write("\u0223\u0224\5\u009dO\2\u0224\u0225\5\u0089E\2\u0225\u009c")
        buf.write("\3\2\2\2\u0226\u0227\7)\2\2\u0227\u009e\3\2\2\2\u0228")
        buf.write("\u0229\7^\2\2\u0229\u0237\7d\2\2\u022a\u022b\7^\2\2\u022b")
        buf.write("\u0237\7h\2\2\u022c\u022d\7^\2\2\u022d\u0237\7t\2\2\u022e")
        buf.write("\u022f\7^\2\2\u022f\u0237\7p\2\2\u0230\u0231\7^\2\2\u0231")
        buf.write("\u0237\7v\2\2\u0232\u0233\7^\2\2\u0233\u0237\7)\2\2\u0234")
        buf.write("\u0235\7^\2\2\u0235\u0237\7^\2\2\u0236\u0228\3\2\2\2\u0236")
        buf.write("\u022a\3\2\2\2\u0236\u022c\3\2\2\2\u0236\u022e\3\2\2\2")
        buf.write("\u0236\u0230\3\2\2\2\u0236\u0232\3\2\2\2\u0236\u0234\3")
        buf.write("\2\2\2\u0237\u00a0\3\2\2\2\u0238\u0239\7^\2\2\u0239\u023d")
        buf.write("\n\16\2\2\u023a\u023b\7)\2\2\u023b\u023d\n\17\2\2\u023c")
        buf.write("\u0238\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u00a2\3\2\2\2")
        buf.write("\u023e\u0243\5\u009fP\2\u023f\u0240\7)\2\2\u0240\u0243")
        buf.write("\7$\2\2\u0241\u0243\n\20\2\2\u0242\u023e\3\2\2\2\u0242")
        buf.write("\u023f\3\2\2\2\u0242\u0241\3\2\2\2\u0243\u00a4\3\2\2\2")
        buf.write("\u0244\u0248\5\u0089E\2\u0245\u0247\5\u00a3R\2\u0246\u0245")
        buf.write("\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024b\u024c\5\u0089E\2\u024c\u024d\bS\5\2\u024d\u00a6")
        buf.write("\3\2\2\2\36\2\u00aa\u00b4\u00c7\u00ce\u00d5\u00d7\u00f2")
        buf.write("\u00fa\u0102\u0106\u010b\u0111\u0115\u0118\u011c\u01e8")
        buf.write("\u01ec\u01f4\u0200\u020f\u0215\u021b\u0221\u0236\u023c")
        buf.write("\u0242\u0248\6\b\2\2\3B\2\3C\3\3S\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    RELATION_OP = 3
    MULDIV = 4
    IDENTIFIER = 5
    LB = 6
    RB = 7
    LK = 8
    RK = 9
    LP = 10
    RP = 11
    SEMI = 12
    COLON = 13
    CM = 14
    DOT = 15
    INTEGER = 16
    FLOAT = 17
    BOLEAN = 18
    FADDOP = 19
    IADDOP = 20
    FSUBOP = 21
    ISUBOP = 22
    FMULOP = 23
    IMULOP = 24
    FDIVOP = 25
    IDIVOP = 26
    IREMAIN = 27
    EQUAL = 28
    FNEQUAL = 29
    FLESSOE = 30
    FGROE = 31
    FLESS = 32
    FGR = 33
    INEQUAL = 34
    ILESSOE = 35
    IGROE = 36
    ILESS = 37
    IGR = 38
    BNEG = 39
    BAND = 40
    BOR = 41
    AS = 42
    VAR = 43
    FUNCTION = 44
    BODY = 45
    ELSE = 46
    ENDFOR = 47
    IF = 48
    ENDDO = 49
    BREAK = 50
    ELSEIF = 51
    ENDWHILE = 52
    PARAMETER = 53
    WHILE = 54
    CONTINUE = 55
    ENDBODY = 56
    FOR = 57
    RETURN = 58
    TRUE = 59
    DO = 60
    ENDIF = 61
    THEN = 62
    FALSE = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    UNTERMINATED_COMMENT = 67
    LSTRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "':'", "','", 
            "'.'", "'+.'", "'+'", "'-.'", "'-'", "'*.'", "'*'", "'\\.'", 
            "'\\'", "'%'", "'=='", "'=/='", "'<=.'", "'>=.'", "'<.'", "'>.'", 
            "'!='", "'<='", "'>='", "'<'", "'>'", "'!'", "'&&'", "'||'", 
            "'='", "'Var'", "'Function'", "'Body'", "'Else'", "'EndFor'", 
            "'If'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", 
            "'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", 
            "'Do'", "'EndIf'", "'Then'", "'False'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "RELATION_OP", "MULDIV", "IDENTIFIER", "LB", 
            "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", 
            "INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", 
            "ISUBOP", "FMULOP", "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", 
            "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", "FLESS", "FGR", "INEQUAL", 
            "ILESSOE", "IGROE", "ILESS", "IGR", "BNEG", "BAND", "BOR", "AS", 
            "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", 
            "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
            "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
            "LSTRING" ]

    ruleNames = [ "WS", "COMMENT", "RELATION_OP", "MULDIV", "IDENTIFIER", 
                  "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", 
                  "DOT", "INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", 
                  "FSUBOP", "ISUBOP", "FMULOP", "IMULOP", "FDIVOP", "IDIVOP", 
                  "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", "FLESS", 
                  "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", 
                  "BNEG", "BAND", "BOR", "AS", "VAR", "FUNCTION", "BODY", 
                  "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
                  "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", 
                  "TRUE", "DO", "ENDIF", "THEN", "FALSE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "DOUQUO", "LETTER", "UPCASE_LETTER", "NUMBER", "EXPO", 
                  "SIGN", "SCIEN", "HEX", "OCTA", "SDOUQUO", "SINGQUO", 
                  "ESCAPE_CHAR", "ILLEGAL_CHAR", "CHAR_STRING", "LSTRING" ]

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
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[81] = self.LSTRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = (self.text)[1:]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = (self.text)[1:]

     

    def LSTRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = self.text[1:-1] 
     


