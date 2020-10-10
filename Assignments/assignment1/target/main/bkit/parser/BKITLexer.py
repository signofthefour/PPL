# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u0274\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\7\2\u00be\n\2\f\2\16\2\u00c1\13\2\3\2\3\2\5")
        buf.write("\2\u00c5\n\2\3\3\3\3\3\3\3\3\3\3\7\3\u00cc\n\3\f\3\16")
        buf.write("\3\u00cf\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4\u00d8\n")
        buf.write("\4\f\4\16\4\u00db\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("\u00e4\n\5\f\5\16\5\u00e7\13\5\3\5\3\5\3\6\3\6\5\6\u00ed")
        buf.write("\n\6\3\7\3\7\5\7\u00f1\n\7\3\b\3\b\5\b\u00f5\n\b\3\t\3")
        buf.write("\t\3\t\7\t\u00fa\n\t\f\t\16\t\u00fd\13\t\3\n\3\n\7\n\u0101")
        buf.write("\n\n\f\n\16\n\u0104\13\n\3\n\3\n\3\13\3\13\7\13\u010a")
        buf.write("\n\13\f\13\16\13\u010d\13\13\3\13\5\13\u0110\n\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\7\f\u0118\n\f\f\f\16\f\u011b\13")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u0126\n\r\f")
        buf.write("\r\16\r\u0129\13\r\3\r\3\r\3\16\3\16\3\17\6\17\u0130\n")
        buf.write("\17\r\17\16\17\u0131\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\5\23\u013e\n\23\3\24\3\24\5\24\u0142\n")
        buf.write("\24\3\24\6\24\u0145\n\24\r\24\16\24\u0146\3\25\3\25\7")
        buf.write("\25\u014b\n\25\f\25\16\25\u014e\13\25\3\26\6\26\u0151")
        buf.write("\n\26\r\26\16\26\u0152\3\26\3\26\5\26\u0157\n\26\3\26")
        buf.write("\5\26\u015a\n\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\5\32\u0168\n\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\5\35\u0172\n\35\3\35\6\35\u0175")
        buf.write("\n\35\r\35\16\35\u0176\3\36\6\36\u017a\n\36\r\36\16\36")
        buf.write("\u017b\3\37\3\37\3\37\3\37\5\37\u0182\n\37\3\37\6\37\u0185")
        buf.write("\n\37\r\37\16\37\u0186\3 \3 \3 \5 \u018c\n \3!\3!\3\"")
        buf.write("\3\"\5\"\u0192\n\"\3#\3#\7#\u0196\n#\f#\16#\u0199\13#")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3>\3>\3>\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3")
        buf.write("F\3F\3G\3G\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3K\3L\3L\3")
        buf.write("L\3M\3M\3M\3N\3N\3N\3N\3O\3O\3O\3O\3P\3P\3Q\3Q\3R\3R\3")
        buf.write("S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\4\u0119")
        buf.write("\u0127\2[\3\3\5\4\7\5\t\6\13\2\r\2\17\2\21\7\23\b\25\t")
        buf.write("\27\n\31\13\33\f\35\r\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61")
        buf.write("\2\63\2\65\2\67\29\2;\2=\2?\16A\17C\20E\21G\22I\23K\24")
        buf.write("M\25O\26Q\27S\30U\31W\32Y\33[\34]\35_\36a\37c e!g\"i#")
        buf.write("k$m%o&q\'s(u)w*y+{,}-\177.\u0081/\u0083\60\u0085\61\u0087")
        buf.write("\62\u0089\63\u008b\64\u008d\65\u008f\66\u0091\67\u0093")
        buf.write("8\u00959\u0097:\u0099;\u009b<\u009d=\u009f>\u00a1?\u00a3")
        buf.write("@\u00a5A\u00a7B\u00a9C\u00abD\u00adE\u00afF\u00b1G\u00b3")
        buf.write("H\3\2\16\4\3\n\f\16\17\4\2\60\60AA\5\2\13\f\16\17\"\"")
        buf.write("\3\2c|\3\2C\\\3\2\62;\4\2GGgg\3\2\60\60\t\2))^^ddhhpp")
        buf.write("ttvv\7\2\n\f\16\17$$))^^\5\2\62;CHch\3\2\629\2\u0283\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
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
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\3\u00c4")
        buf.write("\3\2\2\2\5\u00c6\3\2\2\2\7\u00d2\3\2\2\2\t\u00de\3\2\2")
        buf.write("\2\13\u00ec\3\2\2\2\r\u00f0\3\2\2\2\17\u00f4\3\2\2\2\21")
        buf.write("\u00f6\3\2\2\2\23\u00fe\3\2\2\2\25\u0107\3\2\2\2\27\u0113")
        buf.write("\3\2\2\2\31\u0121\3\2\2\2\33\u012c\3\2\2\2\35\u012f\3")
        buf.write("\2\2\2\37\u0135\3\2\2\2!\u0137\3\2\2\2#\u0139\3\2\2\2")
        buf.write("%\u013d\3\2\2\2\'\u013f\3\2\2\2)\u0148\3\2\2\2+\u0150")
        buf.write("\3\2\2\2-\u015b\3\2\2\2/\u015e\3\2\2\2\61\u0161\3\2\2")
        buf.write("\2\63\u0167\3\2\2\2\65\u0169\3\2\2\2\67\u016b\3\2\2\2")
        buf.write("9\u0171\3\2\2\2;\u0179\3\2\2\2=\u0181\3\2\2\2?\u018b\3")
        buf.write("\2\2\2A\u018d\3\2\2\2C\u0191\3\2\2\2E\u0193\3\2\2\2G\u019d")
        buf.write("\3\2\2\2I\u01a2\3\2\2\2K\u01a8\3\2\2\2M\u01b1\3\2\2\2")
        buf.write("O\u01b4\3\2\2\2Q\u01b9\3\2\2\2S\u01c0\3\2\2\2U\u01c7\3")
        buf.write("\2\2\2W\u01cd\3\2\2\2Y\u01d4\3\2\2\2[\u01dd\3\2\2\2]\u01e1")
        buf.write("\3\2\2\2_\u01ea\3\2\2\2a\u01ed\3\2\2\2c\u01f7\3\2\2\2")
        buf.write("e\u01fe\3\2\2\2g\u0203\3\2\2\2i\u0207\3\2\2\2k\u020d\3")
        buf.write("\2\2\2m\u0212\3\2\2\2o\u0218\3\2\2\2q\u021e\3\2\2\2s\u0220")
        buf.write("\3\2\2\2u\u0223\3\2\2\2w\u0225\3\2\2\2y\u0228\3\2\2\2")
        buf.write("{\u022a\3\2\2\2}\u022d\3\2\2\2\177\u022f\3\2\2\2\u0081")
        buf.write("\u0232\3\2\2\2\u0083\u0234\3\2\2\2\u0085\u0236\3\2\2\2")
        buf.write("\u0087\u0239\3\2\2\2\u0089\u023c\3\2\2\2\u008b\u023f\3")
        buf.write("\2\2\2\u008d\u0242\3\2\2\2\u008f\u0244\3\2\2\2\u0091\u0246")
        buf.write("\3\2\2\2\u0093\u0249\3\2\2\2\u0095\u024c\3\2\2\2\u0097")
        buf.write("\u0250\3\2\2\2\u0099\u0253\3\2\2\2\u009b\u0256\3\2\2\2")
        buf.write("\u009d\u025a\3\2\2\2\u009f\u025e\3\2\2\2\u00a1\u0260\3")
        buf.write("\2\2\2\u00a3\u0262\3\2\2\2\u00a5\u0264\3\2\2\2\u00a7\u0266")
        buf.write("\3\2\2\2\u00a9\u0268\3\2\2\2\u00ab\u026a\3\2\2\2\u00ad")
        buf.write("\u026c\3\2\2\2\u00af\u026e\3\2\2\2\u00b1\u0270\3\2\2\2")
        buf.write("\u00b3\u0272\3\2\2\2\u00b5\u00c5\5\5\3\2\u00b6\u00c5\5")
        buf.write("\7\4\2\u00b7\u00c5\5\t\5\2\u00b8\u00b9\5\u00a7T\2\u00b9")
        buf.write("\u00bf\5\3\2\2\u00ba\u00bb\5\u00b1Y\2\u00bb\u00bc\5\3")
        buf.write("\2\2\u00bc\u00be\3\2\2\2\u00bd\u00ba\3\2\2\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00c2\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\5\u00a9")
        buf.write("U\2\u00c3\u00c5\3\2\2\2\u00c4\u00b5\3\2\2\2\u00c4\u00b6")
        buf.write("\3\2\2\2\u00c4\u00b7\3\2\2\2\u00c4\u00b8\3\2\2\2\u00c5")
        buf.write("\4\3\2\2\2\u00c6\u00c7\5\u00a7T\2\u00c7\u00cd\5\13\6\2")
        buf.write("\u00c8\u00c9\5\u00b1Y\2\u00c9\u00ca\5\13\6\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d1\5\u00a9U\2\u00d1\6\3")
        buf.write("\2\2\2\u00d2\u00d3\5\u00a7T\2\u00d3\u00d9\5\r\7\2\u00d4")
        buf.write("\u00d5\5\u00b1Y\2\u00d5\u00d6\5\r\7\2\u00d6\u00d8\3\2")
        buf.write("\2\2\u00d7\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00dc\u00dd\5\u00a9U\2\u00dd\b\3\2\2\2")
        buf.write("\u00de\u00df\5\u00a7T\2\u00df\u00e5\5\17\b\2\u00e0\u00e1")
        buf.write("\5\u00b1Y\2\u00e1\u00e2\5\17\b\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write("\u00e0\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5\3")
        buf.write("\2\2\2\u00e8\u00e9\5\u00a9U\2\u00e9\n\3\2\2\2\u00ea\u00ed")
        buf.write("\5? \2\u00eb\u00ed\5\21\t\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\f\3\2\2\2\u00ee\u00f1\5A!\2\u00ef")
        buf.write("\u00f1\5\21\t\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2")
        buf.write("\2\u00f1\16\3\2\2\2\u00f2\u00f5\5E#\2\u00f3\u00f5\5\21")
        buf.write("\t\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\20")
        buf.write("\3\2\2\2\u00f6\u00fb\5\37\20\2\u00f7\u00fa\5\37\20\2\u00f8")
        buf.write("\u00fa\5#\22\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\22\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0102")
        buf.write("\7$\2\2\u00ff\u0101\5\63\32\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\5")
        buf.write("-\27\2\u0106\24\3\2\2\2\u0107\u010b\7$\2\2\u0108\u010a")
        buf.write("\5\63\32\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010f\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010e\u0110\t\2\2\2\u010f\u010e\3")
        buf.write("\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\b\13\2\2\u0112")
        buf.write("\26\3\2\2\2\u0113\u0114\7,\2\2\u0114\u0115\7,\2\2\u0115")
        buf.write("\u0119\3\2\2\2\u0116\u0118\13\2\2\2\u0117\u0116\3\2\2")
        buf.write("\2\u0118\u011b\3\2\2\2\u0119\u011a\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c")
        buf.write("\u011d\7,\2\2\u011d\u011e\7,\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("\u0120\b\f\3\2\u0120\30\3\2\2\2\u0121\u0122\7,\2\2\u0122")
        buf.write("\u0123\7,\2\2\u0123\u0127\3\2\2\2\u0124\u0126\13\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012b\7\2\2\3\u012b\32\3\2\2\2\u012c\u012d")
        buf.write("\t\3\2\2\u012d\34\3\2\2\2\u012e\u0130\t\4\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\b\17\3")
        buf.write("\2\u0134\36\3\2\2\2\u0135\u0136\t\5\2\2\u0136 \3\2\2\2")
        buf.write("\u0137\u0138\t\6\2\2\u0138\"\3\2\2\2\u0139\u013a\t\7\2")
        buf.write("\2\u013a$\3\2\2\2\u013b\u013e\5\37\20\2\u013c\u013e\5")
        buf.write("!\21\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e&")
        buf.write("\3\2\2\2\u013f\u0141\t\b\2\2\u0140\u0142\5u;\2\u0141\u0140")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143")
        buf.write("\u0145\5#\22\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147(\3\2\2")
        buf.write("\2\u0148\u014c\t\t\2\2\u0149\u014b\5#\22\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d*\3\2\2\2\u014e\u014c\3\2\2\2\u014f")
        buf.write("\u0151\5#\22\2\u0150\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0159\3")
        buf.write("\2\2\2\u0154\u0156\5)\25\2\u0155\u0157\5\'\24\2\u0156")
        buf.write("\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015a\5\'\24\2\u0159\u0154\3\2\2\2\u0159\u0158")
        buf.write("\3\2\2\2\u015a,\3\2\2\2\u015b\u015c\7^\2\2\u015c\u015d")
        buf.write("\n\n\2\2\u015d.\3\2\2\2\u015e\u015f\7^\2\2\u015f\u0160")
        buf.write("\t\n\2\2\u0160\60\3\2\2\2\u0161\u0162\7)\2\2\u0162\u0163")
        buf.write("\7$\2\2\u0163\62\3\2\2\2\u0164\u0168\n\13\2\2\u0165\u0168")
        buf.write("\5/\30\2\u0166\u0168\5\61\31\2\u0167\u0164\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168\64\3\2\2\2\u0169")
        buf.write("\u016a\t\f\2\2\u016a\66\3\2\2\2\u016b\u016c\t\r\2\2\u016c")
        buf.write("8\3\2\2\2\u016d\u016e\7\62\2\2\u016e\u0172\7z\2\2\u016f")
        buf.write("\u0170\7\62\2\2\u0170\u0172\7Z\2\2\u0171\u016d\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0175\5")
        buf.write("\65\33\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177:\3\2\2\2\u0178")
        buf.write("\u017a\5#\22\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c<\3\2\2")
        buf.write("\2\u017d\u017e\7\62\2\2\u017e\u0182\7q\2\2\u017f\u0180")
        buf.write("\7\62\2\2\u0180\u0182\7Q\2\2\u0181\u017d\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0185\5\67\34")
        buf.write("\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187>\3\2\2\2\u0188\u018c")
        buf.write("\5;\36\2\u0189\u018c\59\35\2\u018a\u018c\5=\37\2\u018b")
        buf.write("\u0188\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2")
        buf.write("\u018c@\3\2\2\2\u018d\u018e\5+\26\2\u018eB\3\2\2\2\u018f")
        buf.write("\u0192\5k\66\2\u0190\u0192\5m\67\2\u0191\u018f\3\2\2\2")
        buf.write("\u0191\u0190\3\2\2\2\u0192D\3\2\2\2\u0193\u0197\7$\2\2")
        buf.write("\u0194\u0196\5\63\32\2\u0195\u0194\3\2\2\2\u0196\u0199")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u019a\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\7$\2\2")
        buf.write("\u019b\u019c\b#\4\2\u019cF\3\2\2\2\u019d\u019e\7D\2\2")
        buf.write("\u019e\u019f\7q\2\2\u019f\u01a0\7f\2\2\u01a0\u01a1\7{")
        buf.write("\2\2\u01a1H\3\2\2\2\u01a2\u01a3\7D\2\2\u01a3\u01a4\7t")
        buf.write("\2\2\u01a4\u01a5\7g\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7")
        buf.write("\7m\2\2\u01a7J\3\2\2\2\u01a8\u01a9\7E\2\2\u01a9\u01aa")
        buf.write("\7q\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad")
        buf.write("\7k\2\2\u01ad\u01ae\7p\2\2\u01ae\u01af\7w\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0L\3\2\2\2\u01b1\u01b2\7F\2\2\u01b2\u01b3")
        buf.write("\7q\2\2\u01b3N\3\2\2\2\u01b4\u01b5\7G\2\2\u01b5\u01b6")
        buf.write("\7n\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8\7g\2\2\u01b8P\3")
        buf.write("\2\2\2\u01b9\u01ba\7G\2\2\u01ba\u01bb\7n\2\2\u01bb\u01bc")
        buf.write("\7U\2\2\u01bc\u01bd\7g\2\2\u01bd\u01be\7n\2\2\u01be\u01bf")
        buf.write("\7h\2\2\u01bfR\3\2\2\2\u01c0\u01c1\7G\2\2\u01c1\u01c2")
        buf.write("\7n\2\2\u01c2\u01c3\7u\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7K\2\2\u01c5\u01c6\7h\2\2\u01c6T\3\2\2\2\u01c7\u01c8")
        buf.write("\7G\2\2\u01c8\u01c9\7p\2\2\u01c9\u01ca\7f\2\2\u01ca\u01cb")
        buf.write("\7K\2\2\u01cb\u01cc\7h\2\2\u01ccV\3\2\2\2\u01cd\u01ce")
        buf.write("\7G\2\2\u01ce\u01cf\7p\2\2\u01cf\u01d0\7f\2\2\u01d0\u01d1")
        buf.write("\7H\2\2\u01d1\u01d2\7q\2\2\u01d2\u01d3\7t\2\2\u01d3X\3")
        buf.write("\2\2\2\u01d4\u01d5\7G\2\2\u01d5\u01d6\7p\2\2\u01d6\u01d7")
        buf.write("\7f\2\2\u01d7\u01d8\7Y\2\2\u01d8\u01d9\7j\2\2\u01d9\u01da")
        buf.write("\7k\2\2\u01da\u01db\7n\2\2\u01db\u01dc\7g\2\2\u01dcZ\3")
        buf.write("\2\2\2\u01dd\u01de\7H\2\2\u01de\u01df\7q\2\2\u01df\u01e0")
        buf.write("\7t\2\2\u01e0\\\3\2\2\2\u01e1\u01e2\7H\2\2\u01e2\u01e3")
        buf.write("\7w\2\2\u01e3\u01e4\7p\2\2\u01e4\u01e5\7e\2\2\u01e5\u01e6")
        buf.write("\7v\2\2\u01e6\u01e7\7k\2\2\u01e7\u01e8\7q\2\2\u01e8\u01e9")
        buf.write("\7p\2\2\u01e9^\3\2\2\2\u01ea\u01eb\7K\2\2\u01eb\u01ec")
        buf.write("\7h\2\2\u01ec`\3\2\2\2\u01ed\u01ee\7R\2\2\u01ee\u01ef")
        buf.write("\7c\2\2\u01ef\u01f0\7t\2\2\u01f0\u01f1\7c\2\2\u01f1\u01f2")
        buf.write("\7o\2\2\u01f2\u01f3\7g\2\2\u01f3\u01f4\7v\2\2\u01f4\u01f5")
        buf.write("\7g\2\2\u01f5\u01f6\7t\2\2\u01f6b\3\2\2\2\u01f7\u01f8")
        buf.write("\7T\2\2\u01f8\u01f9\7g\2\2\u01f9\u01fa\7v\2\2\u01fa\u01fb")
        buf.write("\7w\2\2\u01fb\u01fc\7t\2\2\u01fc\u01fd\7p\2\2\u01fdd\3")
        buf.write("\2\2\2\u01fe\u01ff\7V\2\2\u01ff\u0200\7j\2\2\u0200\u0201")
        buf.write("\7g\2\2\u0201\u0202\7p\2\2\u0202f\3\2\2\2\u0203\u0204")
        buf.write("\7X\2\2\u0204\u0205\7c\2\2\u0205\u0206\7t\2\2\u0206h\3")
        buf.write("\2\2\2\u0207\u0208\7Y\2\2\u0208\u0209\7j\2\2\u0209\u020a")
        buf.write("\7k\2\2\u020a\u020b\7n\2\2\u020b\u020c\7g\2\2\u020cj\3")
        buf.write("\2\2\2\u020d\u020e\7V\2\2\u020e\u020f\7t\2\2\u020f\u0210")
        buf.write("\7w\2\2\u0210\u0211\7g\2\2\u0211l\3\2\2\2\u0212\u0213")
        buf.write("\7H\2\2\u0213\u0214\7c\2\2\u0214\u0215\7n\2\2\u0215\u0216")
        buf.write("\7u\2\2\u0216\u0217\7g\2\2\u0217n\3\2\2\2\u0218\u0219")
        buf.write("\7G\2\2\u0219\u021a\7p\2\2\u021a\u021b\7f\2\2\u021b\u021c")
        buf.write("\7F\2\2\u021c\u021d\7q\2\2\u021dp\3\2\2\2\u021e\u021f")
        buf.write("\7-\2\2\u021fr\3\2\2\2\u0220\u0221\7-\2\2\u0221\u0222")
        buf.write("\7\60\2\2\u0222t\3\2\2\2\u0223\u0224\7/\2\2\u0224v\3\2")
        buf.write("\2\2\u0225\u0226\7/\2\2\u0226\u0227\7\60\2\2\u0227x\3")
        buf.write("\2\2\2\u0228\u0229\7,\2\2\u0229z\3\2\2\2\u022a\u022b\7")
        buf.write(",\2\2\u022b\u022c\7\60\2\2\u022c|\3\2\2\2\u022d\u022e")
        buf.write("\7^\2\2\u022e~\3\2\2\2\u022f\u0230\7^\2\2\u0230\u0231")
        buf.write("\7\60\2\2\u0231\u0080\3\2\2\2\u0232\u0233\7\'\2\2\u0233")
        buf.write("\u0082\3\2\2\2\u0234\u0235\7#\2\2\u0235\u0084\3\2\2\2")
        buf.write("\u0236\u0237\7(\2\2\u0237\u0238\7(\2\2\u0238\u0086\3\2")
        buf.write("\2\2\u0239\u023a\7~\2\2\u023a\u023b\7~\2\2\u023b\u0088")
        buf.write("\3\2\2\2\u023c\u023d\7?\2\2\u023d\u023e\7?\2\2\u023e\u008a")
        buf.write("\3\2\2\2\u023f\u0240\7#\2\2\u0240\u0241\7?\2\2\u0241\u008c")
        buf.write("\3\2\2\2\u0242\u0243\7>\2\2\u0243\u008e\3\2\2\2\u0244")
        buf.write("\u0245\7@\2\2\u0245\u0090\3\2\2\2\u0246\u0247\7>\2\2\u0247")
        buf.write("\u0248\7?\2\2\u0248\u0092\3\2\2\2\u0249\u024a\7@\2\2\u024a")
        buf.write("\u024b\7?\2\2\u024b\u0094\3\2\2\2\u024c\u024d\7?\2\2\u024d")
        buf.write("\u024e\7^\2\2\u024e\u024f\7?\2\2\u024f\u0096\3\2\2\2\u0250")
        buf.write("\u0251\7>\2\2\u0251\u0252\7\60\2\2\u0252\u0098\3\2\2\2")
        buf.write("\u0253\u0254\7@\2\2\u0254\u0255\7\60\2\2\u0255\u009a\3")
        buf.write("\2\2\2\u0256\u0257\7>\2\2\u0257\u0258\7?\2\2\u0258\u0259")
        buf.write("\7\60\2\2\u0259\u009c\3\2\2\2\u025a\u025b\7@\2\2\u025b")
        buf.write("\u025c\7?\2\2\u025c\u025d\7\60\2\2\u025d\u009e\3\2\2\2")
        buf.write("\u025e\u025f\7*\2\2\u025f\u00a0\3\2\2\2\u0260\u0261\7")
        buf.write("+\2\2\u0261\u00a2\3\2\2\2\u0262\u0263\7]\2\2\u0263\u00a4")
        buf.write("\3\2\2\2\u0264\u0265\7_\2\2\u0265\u00a6\3\2\2\2\u0266")
        buf.write("\u0267\7}\2\2\u0267\u00a8\3\2\2\2\u0268\u0269\7\177\2")
        buf.write("\2\u0269\u00aa\3\2\2\2\u026a\u026b\7<\2\2\u026b\u00ac")
        buf.write("\3\2\2\2\u026c\u026d\7\60\2\2\u026d\u00ae\3\2\2\2\u026e")
        buf.write("\u026f\7=\2\2\u026f\u00b0\3\2\2\2\u0270\u0271\7.\2\2\u0271")
        buf.write("\u00b2\3\2\2\2\u0272\u0273\7?\2\2\u0273\u00b4\3\2\2\2")
        buf.write("#\2\u00bf\u00c4\u00cd\u00d9\u00e5\u00ec\u00f0\u00f4\u00f9")
        buf.write("\u00fb\u0102\u010b\u010f\u0119\u0127\u0131\u013d\u0141")
        buf.write("\u0146\u014c\u0152\u0156\u0159\u0167\u0171\u0176\u017b")
        buf.write("\u0181\u0186\u018b\u0191\u0197\5\3\13\2\b\2\2\3#\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY_LIT = 1
    INT_ARRAY = 2
    FLOAT_ARRAY = 3
    STRING_ARRAY = 4
    ID = 5
    ILLEGAL_ESCAPE = 6
    UNCLOSE_STRING = 7
    COMMENT = 8
    UNTERMINATED_COMMENT = 9
    ERROR_CHAR = 10
    WS = 11
    Integer_literal = 12
    Float_literal = 13
    Boolean_literal = 14
    String_literal = 15
    BODY = 16
    BREAK = 17
    CONTINUE = 18
    DO = 19
    ELSE = 20
    ELSELF = 21
    ELSEIF = 22
    ENDBODY = 23
    ENDFOR = 24
    ENDWHILE = 25
    FOR = 26
    FUNCTION = 27
    IF = 28
    PARAMETER = 29
    RETURN = 30
    THEN = 31
    VAR = 32
    WHILE = 33
    TRUE = 34
    FALSE = 35
    ENDDO = 36
    PLUS_INT = 37
    PLUS_FLOAT = 38
    MINUS_INT = 39
    MINUS_FLOAT = 40
    STAR_INT = 41
    STAR_FLOAT = 42
    DIV_INT = 43
    DIV_FLOAT = 44
    MOD = 45
    NOT = 46
    AND = 47
    OR = 48
    EQUAL = 49
    NOT_EQUAL_INT = 50
    LESS_INT = 51
    GREATER_INT = 52
    LESS_OR_EQUAL_INT = 53
    GREATER_OR_EQUAL_INT = 54
    NOT_EQUAL_FLOAT = 55
    LESS_FLOAT = 56
    GREATER_FLOAT = 57
    LESS_OR_EQUAL_FLOAT = 58
    GREATER_OR_EQUAL_FLOAT = 59
    LEFT_PAREN = 60
    RIGHT_PARENT = 61
    LEFT_BRACKET = 62
    RIGHT_BRACKET = 63
    LEFT_BRACE = 64
    RIGHT_BRACE = 65
    COLON = 66
    DOT = 67
    SEMI = 68
    COMMA = 69
    ASSIGN = 70

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
            "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", "ID", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR", "WS", "Integer_literal", "Float_literal", "Boolean_literal", 
            "String_literal", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSELF", "ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", 
            "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
            "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", 
            "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
            "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
            "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
            "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PARENT", "LEFT_BRACKET", 
            "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", 
            "SEMI", "COMMA", "ASSIGN" ]

    ruleNames = [ "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", 
                  "INT_ELEMENT", "FLOAT_ELEMENT", "STRING_ELEMENT", "ID", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR", "WS", "LOWERCASE_LETTER", "UPPERCASE_LETTER", 
                  "DIGIT", "LETTER", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
                  "ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_CHAR", "HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", 
                  "DECIMAL", "OCTAL", "Integer_literal", "Float_literal", 
                  "Boolean_literal", "String_literal", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSELF", "ELSEIF", "ENDBODY", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                  "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
                  "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                  "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
                  "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PARENT", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                  "COLON", "DOT", "SEMI", "COMMA", "ASSIGN" ]

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
            actions[9] = self.UNCLOSE_STRING_action 
            actions[33] = self.String_literal_action 
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

                
     


